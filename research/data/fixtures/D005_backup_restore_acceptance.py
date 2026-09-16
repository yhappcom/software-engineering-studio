"""D005 bounded backup/restore acceptance evidence.

Environment recorded by study: Python 3.13.5 / SQLite 3.46.1 / Linux.
This fixture distinguishes backup creation, physical SQLite integrity, and
application-contract acceptance. It does not simulate power loss or mobile OS
storage behavior.
"""

from __future__ import annotations

import shutil
import sqlite3
import tempfile
from pathlib import Path


def create_v2_database(path: Path) -> None:
    db = sqlite3.connect(path)
    db.executescript(
        """
        PRAGMA foreign_keys=ON;
        CREATE TABLE flights(
          id TEXT PRIMARY KEY,
          minutes INTEGER NOT NULL CHECK(minutes >= 0)
        );
        INSERT INTO flights VALUES('F1', 60), ('F2', 90);
        PRAGMA user_version=2;
        """
    )
    db.commit()
    db.close()


def application_acceptance(path: Path, expected_version: int = 2) -> tuple[bool, str]:
    try:
        db = sqlite3.connect(path)
        integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
        version = db.execute("PRAGMA user_version").fetchone()[0]
        rows = db.execute("SELECT id, minutes FROM flights ORDER BY id").fetchall()
        db.close()
    except sqlite3.DatabaseError as exc:
        return False, f"sqlite-open/read failed: {exc}"

    if integrity != "ok":
        return False, f"integrity_check={integrity}"
    if version != expected_version:
        return False, f"schema contract mismatch: user_version={version}"
    if rows != [("F1", 60), ("F2", 90)]:
        return False, f"semantic data mismatch: rows={rows}"
    return True, "integrity + schema contract + semantic rows accepted"


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        live = root / "live.db"
        backup = root / "backup.db"
        restored = root / "restored.db"
        corrupt = root / "corrupt.db"
        wrong_contract = root / "wrong_contract.db"

        create_v2_database(live)

        source = sqlite3.connect(live)
        destination = sqlite3.connect(backup)
        source.backup(destination)
        destination.close()
        source.close()

        # Destroy current live semantic data after the backup. Recovery must
        # therefore come from the backup, not from the still-healthy live DB.
        db = sqlite3.connect(live)
        db.execute("DELETE FROM flights")
        db.commit()
        db.close()

        shutil.copy2(backup, restored)
        ok, reason = application_acceptance(restored)
        print("RESTORE_ACCEPTANCE", ok, reason)
        assert ok

        # Failure case 1: a file can exist and have non-zero size yet be
        # unusable as a SQLite recovery artifact.
        shutil.copy2(backup, corrupt)
        raw = bytearray(corrupt.read_bytes())
        raw[:16] = b"X" * 16
        corrupt.write_bytes(raw)
        print("CORRUPT_BACKUP_EXISTS", corrupt.exists(), corrupt.stat().st_size)
        ok, reason = application_acceptance(corrupt)
        print("CORRUPT_ACCEPTANCE", ok, reason)
        assert not ok

        # Failure case 2: SQLite physical integrity can be OK while the artifact
        # is incompatible with the declared application/schema contract.
        shutil.copy2(backup, wrong_contract)
        db = sqlite3.connect(wrong_contract)
        db.execute("PRAGMA user_version=99")
        db.commit()
        physical = db.execute("PRAGMA integrity_check").fetchone()[0]
        db.close()
        print("WRONG_CONTRACT_PHYSICAL_INTEGRITY", physical)
        assert physical == "ok"
        ok, reason = application_acceptance(wrong_contract)
        print("WRONG_CONTRACT_ACCEPTANCE", ok, reason)
        assert not ok


if __name__ == "__main__":
    main()
