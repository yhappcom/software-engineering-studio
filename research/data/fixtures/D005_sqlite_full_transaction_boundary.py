#!/usr/bin/env python3
"""D005 bounded SQLite growth-limit failure fixture.

This deliberately uses SQLite PRAGMA max_page_count to force SQLITE_FULL.
It does NOT simulate an OS/filesystem ENOSPC or power-loss event.
"""
import os
import sqlite3
import tempfile

fd, path = tempfile.mkstemp(prefix="d005-full-", suffix=".db")
os.close(fd)
try:
    db = sqlite3.connect(path)
    db.execute("PRAGMA journal_mode=DELETE")
    db.execute("PRAGMA synchronous=FULL")
    db.execute("PRAGMA page_size=512")
    db.execute("VACUUM")
    db.execute("CREATE TABLE items(id INTEGER PRIMARY KEY, payload BLOB NOT NULL)")
    db.execute("INSERT INTO items(payload) VALUES (?)", (b"a" * 100,))
    db.commit()

    baseline = db.execute(
        "SELECT count(*), sum(length(payload)) FROM items"
    ).fetchone()
    pages = db.execute("PRAGMA page_count").fetchone()[0]
    limit = db.execute(f"PRAGMA max_page_count={pages + 2}").fetchone()[0]

    observed = None
    try:
        db.execute("BEGIN IMMEDIATE")
        db.execute("INSERT INTO items(payload) VALUES (?)", (b"b" * 5000,))
        db.commit()
    except sqlite3.DatabaseError as exc:
        observed = (str(exc), getattr(exc, "sqlite_errorcode", None), getattr(exc, "sqlite_errorname", None))
        db.rollback()

    after = db.execute(
        "SELECT count(*), sum(length(payload)) FROM items"
    ).fetchone()
    integrity = db.execute("PRAGMA integrity_check").fetchone()[0]

    assert observed is not None, "expected bounded growth failure"
    assert observed[1] == sqlite3.SQLITE_FULL, observed
    assert observed[2] == "SQLITE_FULL", observed
    assert after == baseline, (baseline, after)
    assert integrity == "ok", integrity

    print("environment:", sqlite3.sqlite_version, "Python sqlite3")
    print("baseline:", baseline, "page_count:", pages, "max_page_count:", limit)
    print("failure:", observed)
    print("after rollback:", after, "integrity_check:", integrity)
    print("D005 bounded SQLITE_FULL transaction boundary: PASS")
    db.close()
finally:
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass
