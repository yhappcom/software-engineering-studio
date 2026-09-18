#!/usr/bin/env python3
"""D005: interrupted SQLite Online Backup and publication boundary.

Environment used for canonical observation: Python 3.13.5 / SQLite 3.46.1 / Linux.
This is process-interruption evidence, not hard-power-loss evidence.
"""
from __future__ import annotations

import hashlib
import multiprocessing as mp
import os
from pathlib import Path
import sqlite3
import tempfile
import time

ROWS = 1500
PAYLOAD = b"x" * 3000


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect(path: Path):
    try:
        db = sqlite3.connect(path)
        count = db.execute("SELECT count(*) FROM ledger").fetchone()[0]
        integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
        db.close()
        return {"count": count, "integrity": integrity}
    except sqlite3.Error as exc:
        return {"error": type(exc).__name__, "message": str(exc)}


def create_source(path: Path) -> int:
    db = sqlite3.connect(path)
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("CREATE TABLE ledger(id INTEGER PRIMARY KEY, payload BLOB NOT NULL)")
    db.executemany("INSERT INTO ledger(payload) VALUES(?)", [(PAYLOAD,)] * ROWS)
    db.commit()
    pages = db.execute("PRAGMA page_count").fetchone()[0]
    db.close()
    return pages


def create_old_published(path: Path) -> None:
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE ledger(id INTEGER PRIMARY KEY, payload BLOB NOT NULL)")
    db.executemany("INSERT INTO ledger(payload) VALUES(?)", [(b"old",)] * 10)
    db.commit()
    db.close()


def backup_child(source: str, destination: str, marker: str) -> None:
    src = sqlite3.connect(source)
    dst = sqlite3.connect(destination)

    def progress(status: int, remaining: int, total: int) -> None:
        if remaining < total:
            Path(marker).write_text(f"{status},{remaining},{total}\n", encoding="utf-8")
            # Widen the deterministic parent kill window after at least one page step.
            time.sleep(0.02)

    src.backup(dst, pages=1, progress=progress, sleep=0)
    dst.close()
    src.close()


def wait_for_marker(marker: Path, timeout_s: float = 5.0) -> str:
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        if marker.exists():
            return marker.read_text(encoding="utf-8").strip()
        time.sleep(0.005)
    raise RuntimeError("backup did not reach first observable progress step")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="d005-backup-interrupt-") as td:
        root = Path(td)
        source = root / "source.db"
        unsafe_final = root / "unsafe-final.db"
        published = root / "published.db"
        candidate = root / "candidate.tmp"
        marker1 = root / "unsafe.marker"
        marker2 = root / "safe.marker"

        pages = create_source(source)

        # Failure case: a path treated as the final/public backup name exists before
        # backup completion. Kill after the first reported page of progress.
        p1 = mp.Process(target=backup_child, args=(str(source), str(unsafe_final), str(marker1)))
        p1.start()
        unsafe_progress = wait_for_marker(marker1)
        p1.kill()
        p1.join()
        unsafe = {
            "exitcode": p1.exitcode,
            "progress": unsafe_progress,
            "exists": unsafe_final.exists(),
            "size": unsafe_final.stat().st_size if unsafe_final.exists() else None,
            "inspection": inspect(unsafe_final),
        }

        # Alternative: keep the previously accepted artifact at the published path
        # and build the replacement under a private candidate path. Interruption must
        # not change the already-published artifact.
        create_old_published(published)
        published_hash_before = sha256(published)
        p2 = mp.Process(target=backup_child, args=(str(source), str(candidate), str(marker2)))
        p2.start()
        safe_progress = wait_for_marker(marker2)
        p2.kill()
        p2.join()
        published_hash_after = sha256(published)
        safe = {
            "exitcode": p2.exitcode,
            "progress": safe_progress,
            "candidate_exists": candidate.exists(),
            "candidate_size": candidate.stat().st_size if candidate.exists() else None,
            "candidate_inspection": inspect(candidate),
            "published_hash_unchanged": published_hash_before == published_hash_after,
            "published_inspection": inspect(published),
        }

        print({"sqlite": sqlite3.sqlite_version, "source_pages": pages, "unsafe": unsafe, "safe": safe})

        assert unsafe["exists"] is True
        assert unsafe["inspection"].get("count") != ROWS
        assert safe["published_hash_unchanged"] is True
        assert safe["published_inspection"] == {"count": 10, "integrity": "ok"}
        assert safe["candidate_inspection"].get("count") != ROWS


if __name__ == "__main__":
    main()
