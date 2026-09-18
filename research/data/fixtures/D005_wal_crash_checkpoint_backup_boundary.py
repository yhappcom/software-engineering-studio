#!/usr/bin/env python3
"""D005 executable evidence: WAL commit/crash/checkpoint/main-file-copy boundary.

Environment recorded by the research note. This fixture deliberately disables
WAL auto-checkpointing, commits in a child process, exits without sqlite close,
and compares the authoritative WAL-mode database with a copy of the main file
alone before and after an explicit checkpoint.
"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile

EXPECTED_BASELINE = [(100,)]
EXPECTED_COMMITTED = [(100,), (200,)]


def rows(path: Path):
    con = sqlite3.connect(path)
    try:
        result = con.execute("SELECT amount FROM ledger ORDER BY id").fetchall()
        integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        return result, integrity
    finally:
        con.close()


def main() -> None:
    root = Path(tempfile.mkdtemp(prefix="d005-wal-"))
    db = root / "ledger.db"

    con = sqlite3.connect(db)
    assert con.execute("PRAGMA journal_mode=WAL").fetchone()[0] == "wal"
    con.execute("PRAGMA wal_autocheckpoint=0")
    con.execute("CREATE TABLE ledger(id INTEGER PRIMARY KEY, amount INTEGER NOT NULL)")
    con.execute("INSERT INTO ledger(amount) VALUES (100)")
    con.commit()
    con.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchall()
    con.close()

    child = root / "writer.py"
    child.write_text(
        "import os, sqlite3\n"
        f"db={str(db)!r}\n"
        "c=sqlite3.connect(db)\n"
        "c.execute('PRAGMA journal_mode=WAL')\n"
        "c.execute('PRAGMA wal_autocheckpoint=0')\n"
        "c.execute('INSERT INTO ledger(amount) VALUES (200)')\n"
        "c.commit()\n"
        "os._exit(77)\n",
        encoding="utf-8",
    )
    proc = subprocess.run([sys.executable, str(child)], check=False)
    assert proc.returncode == 77

    wal = Path(str(db) + "-wal")
    assert wal.exists() and wal.stat().st_size > 0

    # Copy only the main DB before any normal reopen can recover/checkpoint WAL.
    main_only = root / "main_only.db"
    shutil.copy2(db, main_only)
    main_rows, main_integrity = rows(main_only)
    assert main_integrity == "ok"
    assert main_rows == EXPECTED_BASELINE

    # Normal reopen of the original DB observes the committed WAL transaction.
    con = sqlite3.connect(db)
    try:
        authoritative_rows = con.execute(
            "SELECT amount FROM ledger ORDER BY id"
        ).fetchall()
        authoritative_integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        assert authoritative_integrity == "ok"
        assert authoritative_rows == EXPECTED_COMMITTED

        # Explicit checkpoint transfers committed WAL state to the main DB.
        checkpoint = con.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchall()
    finally:
        con.close()

    post_checkpoint = root / "post_checkpoint.db"
    shutil.copy2(db, post_checkpoint)
    post_rows, post_integrity = rows(post_checkpoint)
    assert post_integrity == "ok"
    assert post_rows == EXPECTED_COMMITTED

    print(f"python={sys.version.split()[0]} sqlite={sqlite3.sqlite_version}")
    print(f"child_exit={proc.returncode} wal_bytes_before_reopen={wal.stat().st_size if wal.exists() else 0}")
    print(f"main_only_before_checkpoint={main_rows} integrity={main_integrity}")
    print(f"authoritative_reopen={authoritative_rows} integrity={authoritative_integrity}")
    print(f"checkpoint={checkpoint}")
    print(f"main_only_after_checkpoint={post_rows} integrity={post_integrity}")
    print("VERDICT=PASS bounded WAL crash/checkpoint/main-file-copy oracle")


if __name__ == "__main__":
    main()
