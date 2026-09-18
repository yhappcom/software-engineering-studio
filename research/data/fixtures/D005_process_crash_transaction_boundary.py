"""D005: real process-crash boundary for SQLite WAL transactions.

Bounded evidence only: abrupt application-process exit on this Linux host.
Not an OS-crash, power-loss, filesystem, mobile, or Flutter validation.
"""
import os
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve()


def child(db: str, mode: str) -> None:
    con = sqlite3.connect(db)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=FULL")
    con.execute("BEGIN IMMEDIATE")
    con.execute("INSERT INTO events(id,value) VALUES(?,?)", (mode, mode))
    if mode == "committed":
        con.commit()
        os._exit(23)
    if mode == "uncommitted":
        # Deliberately bypass close()/rollback(): abrupt process termination.
        os._exit(24)
    raise AssertionError(mode)


def accepted_state(db: str):
    con = sqlite3.connect(db)
    try:
        integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        rows = con.execute("SELECT id,value FROM events ORDER BY id").fetchall()
        return integrity, rows
    finally:
        con.close()


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = str(Path(td) / "state.db")
        con = sqlite3.connect(db)
        journal_mode = con.execute("PRAGMA journal_mode=WAL").fetchone()[0]
        con.execute("PRAGMA synchronous=FULL")
        con.execute("CREATE TABLE events(id TEXT PRIMARY KEY,value TEXT NOT NULL)")
        con.execute("INSERT INTO events VALUES('baseline','baseline')")
        con.commit()
        con.close()

        baseline = accepted_state(db)
        assert baseline == ("ok", [("baseline", "baseline")])

        uncommitted = subprocess.run(
            [sys.executable, str(SCRIPT), "--child", db, "uncommitted"], check=False
        )
        after_uncommitted = accepted_state(db)
        assert uncommitted.returncode == 24
        assert after_uncommitted == baseline, after_uncommitted

        committed = subprocess.run(
            [sys.executable, str(SCRIPT), "--child", db, "committed"], check=False
        )
        after_committed = accepted_state(db)
        assert committed.returncode == 23
        assert after_committed == (
            "ok",
            [("baseline", "baseline"), ("committed", "committed")],
        ), after_committed

        print("journal_mode=", journal_mode)
        print("uncommitted_exit=", uncommitted.returncode, "rows=", after_uncommitted[1])
        print("committed_exit=", committed.returncode, "rows=", after_committed[1])
        print("D005 process-crash transaction boundary: PASS")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--child":
        child(sys.argv[2], sys.argv[3])
    else:
        main()
