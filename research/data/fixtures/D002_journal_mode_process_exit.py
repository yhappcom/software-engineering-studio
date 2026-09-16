"""D002 bounded SQLite journal-mode/process-exit validation.

Claim boundary: application-process abrupt exit after an uncommitted vs committed
transaction. This does NOT simulate OS crash, power loss, fsync failure, torn
writes, Android/iOS storage, or benchmark performance.
"""
import json
import os
import sqlite3
import subprocess
import sys
import tempfile


def setup(path: str, mode: str) -> None:
    con = sqlite3.connect(path)
    actual = con.execute(f"PRAGMA journal_mode={mode}").fetchone()[0]
    assert actual.lower() == mode.lower()
    con.execute("PRAGMA synchronous=FULL")
    con.execute("CREATE TABLE flights(id TEXT PRIMARY KEY, minutes INTEGER NOT NULL)")
    con.execute("INSERT INTO flights VALUES('A', 60)")
    con.commit()
    con.close()


def abrupt_child(path: str, mode: str, commit: bool) -> int:
    child = r'''
import os, sqlite3, sys
path, mode, commit = sys.argv[1], sys.argv[2], sys.argv[3] == "1"
con = sqlite3.connect(path)
assert con.execute(f"PRAGMA journal_mode={mode}").fetchone()[0].lower() == mode.lower()
con.execute("PRAGMA synchronous=FULL")
con.execute("BEGIN IMMEDIATE")
con.execute("INSERT INTO flights VALUES('B', 90)")
if commit:
    con.commit()
os._exit(99)
'''
    return subprocess.run(
        [sys.executable, "-c", child, path, mode, "1" if commit else "0"],
        check=False,
    ).returncode


def observe(path: str):
    con = sqlite3.connect(path)
    rows = con.execute("SELECT id, minutes FROM flights ORDER BY id").fetchall()
    integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
    con.close()
    return rows, integrity


def main() -> None:
    observations = []
    with tempfile.TemporaryDirectory() as directory:
        for mode in ("DELETE", "WAL"):
            for committed in (False, True):
                path = os.path.join(directory, f"{mode}_{committed}.db")
                setup(path, mode)
                rc = abrupt_child(path, mode, committed)
                rows, integrity = observe(path)
                expected = [("A", 60), ("B", 90)] if committed else [("A", 60)]
                assert rc == 99
                assert rows == expected
                assert integrity == "ok"
                observations.append(
                    {
                        "journal_mode": mode,
                        "committed_before_exit": committed,
                        "child_exit": rc,
                        "rows_after_reopen": rows,
                        "integrity_check": integrity,
                    }
                )
    print(json.dumps(observations, indent=2))


if __name__ == "__main__":
    main()
