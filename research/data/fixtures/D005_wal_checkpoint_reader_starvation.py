import os
import sqlite3
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as td:
    db = Path(td) / "checkpoint.db"
    writer = sqlite3.connect(db, isolation_level=None)
    assert writer.execute("PRAGMA journal_mode=WAL").fetchone()[0] == "wal"
    writer.execute("PRAGMA wal_autocheckpoint=0")
    writer.execute("CREATE TABLE ledger(value INTEGER PRIMARY KEY)")
    writer.execute("INSERT INTO ledger VALUES(100)")
    assert writer.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone() == (0, 0, 0)

    reader = sqlite3.connect(db, isolation_level=None)
    reader.execute("BEGIN")
    assert reader.execute("SELECT value FROM ledger ORDER BY value").fetchall() == [(100,)]

    writer.execute("INSERT INTO ledger VALUES(200)")
    writer.execute("INSERT INTO ledger VALUES(300)")
    wal = Path(str(db) + "-wal")
    before = wal.stat().st_size

    checkpointer = sqlite3.connect(db, isolation_level=None)
    checkpointer.execute("PRAGMA busy_timeout=0")
    passive = checkpointer.execute("PRAGMA wal_checkpoint(PASSIVE)").fetchone()
    blocked = checkpointer.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    during = wal.stat().st_size

    assert reader.execute("SELECT value FROM ledger ORDER BY value").fetchall() == [(100,)]
    assert passive[0] == 0 and passive[1] > passive[2]
    assert blocked[0] == 1 and during > 0

    reader.execute("COMMIT")
    completed = checkpointer.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    after = wal.stat().st_size
    assert completed == (0, 0, 0) and after == 0
    assert checkpointer.execute("SELECT value FROM ledger ORDER BY value").fetchall() == [(100,), (200,), (300,)]
    assert checkpointer.execute("PRAGMA integrity_check").fetchone()[0] == "ok"

    print({"sqlite": sqlite3.sqlite_version, "wal_before": before,
           "passive": passive, "truncate_blocked": blocked,
           "wal_during": during, "truncate_after_reader": completed,
           "wal_after": after})
