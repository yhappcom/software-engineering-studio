"""D001 fixture: distinguish uncommitted state from committed durable state.

Bounded experiment only. It validates SQLite behavior for application-process
termination on the recorded environment; it does not simulate OS crash,
power loss, device loss, mobile filesystem behavior, or distributed sync.
"""

import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile

CHILD = r'''
import sqlite3, sys, time
path, mode = sys.argv[1], sys.argv[2]
con = sqlite3.connect(path)
con.execute("PRAGMA journal_mode=DELETE")
con.execute("PRAGMA synchronous=FULL")
if mode == "uncommitted":
    con.execute("BEGIN IMMEDIATE")
    con.execute("INSERT INTO events(label) VALUES (?)", ("uncommitted",))
    print("READY", flush=True)
    time.sleep(60)
elif mode == "committed":
    con.execute("BEGIN IMMEDIATE")
    con.execute("INSERT INTO events(label) VALUES (?)", ("committed",))
    con.commit()
    print("COMMITTED", flush=True)
else:
    raise SystemExit(2)
'''


def read_rows(db_path: str):
    con = sqlite3.connect(db_path)
    try:
        return con.execute("SELECT id, label FROM events ORDER BY id").fetchall()
    finally:
        con.close()


with tempfile.TemporaryDirectory() as temp_dir:
    db = str(Path(temp_dir) / "durability.db")

    con = sqlite3.connect(db)
    con.execute("PRAGMA journal_mode=DELETE")
    con.execute("PRAGMA synchronous=FULL")
    con.execute("CREATE TABLE events(id INTEGER PRIMARY KEY, label TEXT NOT NULL)")
    con.execute("INSERT INTO events(label) VALUES ('baseline')")
    con.commit()
    con.close()

    before = read_rows(db)

    child = subprocess.Popen(
        [sys.executable, "-c", CHILD, db, "uncommitted"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    ready = child.stdout.readline().strip()
    journal_before_kill = os.path.exists(db + "-journal")
    child.kill()
    child.wait(timeout=5)
    after_kill = read_rows(db)
    journal_after_reopen = os.path.exists(db + "-journal")

    committed = subprocess.run(
        [sys.executable, "-c", CHILD, db, "committed"],
        capture_output=True,
        text=True,
        check=True,
    )
    after_commit = read_rows(db)

    print(json.dumps({
        "python": sys.version.split()[0],
        "sqlite": sqlite3.sqlite_version,
        "platform": sys.platform,
        "before": before,
        "child_ready": ready,
        "journal_exists_before_kill": journal_before_kill,
        "killed_returncode": child.returncode,
        "after_kill_reopen": after_kill,
        "journal_exists_after_reopen": journal_after_reopen,
        "commit_child_stdout": committed.stdout.strip(),
        "after_committed_reopen": after_commit,
    }, indent=2))
