#!/usr/bin/env python3
"""Bounded D005 fixture: validate-before-publish vs destructive restore.
Environment recorded in research note. This does NOT simulate power loss or mobile filesystems.
"""
import os
import shutil
import sqlite3
import tempfile
from pathlib import Path

EXPECTED = [("F1", 60), ("F2", 90)]


def create_db(path: Path, rows=EXPECTED, version=2):
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE flights(id TEXT PRIMARY KEY, minutes INTEGER NOT NULL CHECK(minutes>=0))")
    con.executemany("INSERT INTO flights VALUES(?,?)", rows)
    con.execute(f"PRAGMA user_version={version}")
    con.commit()
    con.close()


def accept(path: Path):
    try:
        con = sqlite3.connect(path)
        integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        version = con.execute("PRAGMA user_version").fetchone()[0]
        rows = con.execute("SELECT id,minutes FROM flights ORDER BY id").fetchall()
        con.close()
        return integrity == "ok" and version == 2 and rows == EXPECTED, (integrity, version, rows)
    except Exception as exc:
        return False, repr(exc)


def main():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        live = root / "live.db"
        known_good = root / "known_good.db"
        invalid = root / "invalid.db"
        candidate = root / "candidate.db"

        create_db(live)
        shutil.copy2(live, known_good)
        create_db(invalid, [("EVIL", 999)], version=99)

        # Failure case: publish first, validate later. Last known-good state is lost.
        shutil.copy2(invalid, live)
        print("unsafe_publish_then_validate", accept(live))

        # Alternative: preserve live, validate isolated candidate first.
        shutil.copy2(known_good, live)
        shutil.copy2(invalid, candidate)
        print("invalid_candidate", accept(candidate))
        print("live_after_candidate_rejection", accept(live))

        # Inject failure after successful candidate validation but before publication.
        shutil.copy2(known_good, candidate)
        assert accept(candidate)[0]
        try:
            raise RuntimeError("injected failure before os.replace")
        except RuntimeError:
            pass
        print("live_after_prepublication_failure", accept(live))

        # Successful same-filesystem publication in this bounded POSIX environment.
        os.replace(candidate, live)
        print("live_after_valid_publication", accept(live))


if __name__ == "__main__":
    main()
