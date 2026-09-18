#!/usr/bin/env python3
"""D005: SQLite Online Backup API under live WAL writes.

Environment used for canonical observation: Python 3.13.5, SQLite 3.46.1, Linux.
The fixture deliberately writes from a second source connection during an
incremental backup. It checks that the completed destination is structurally
valid and contains the concurrently committed row, while progress shows the
backup restarting (remaining pages increase after the external write).
"""
from __future__ import annotations

import os
import sqlite3
import tempfile
from pathlib import Path


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="d005-backup-") as td:
        root = Path(td)
        source_path = root / "source.db"
        backup_path = root / "backup.db"

        source = sqlite3.connect(source_path)
        mode = source.execute("PRAGMA journal_mode=WAL").fetchone()[0]
        source.execute("PRAGMA wal_autocheckpoint=0")
        source.execute("CREATE TABLE ledger(id INTEGER PRIMARY KEY, payload BLOB NOT NULL)")
        payload = b"x" * 3000
        source.executemany("INSERT INTO ledger(payload) VALUES(?)", [(payload,)] * 500)
        source.commit()

        writer = sqlite3.connect(source_path)
        destination = sqlite3.connect(backup_path)
        progress: list[tuple[int, int, int]] = []
        injected = False

        def on_progress(status: int, remaining: int, total: int) -> None:
            nonlocal injected
            progress.append((status, remaining, total))
            if not injected and len(progress) >= 2:
                writer.execute("INSERT INTO ledger(payload) VALUES(?)", (b"CONCURRENT",))
                writer.commit()
                injected = True

        source.backup(destination, pages=5, progress=on_progress, sleep=0.001)

        source_count = source.execute("SELECT count(*) FROM ledger").fetchone()[0]
        backup_count = destination.execute("SELECT count(*) FROM ledger").fetchone()[0]
        concurrent_rows = destination.execute(
            "SELECT count(*) FROM ledger WHERE payload=?", (b"CONCURRENT",)
        ).fetchone()[0]
        integrity = destination.execute("PRAGMA integrity_check").fetchone()[0]

        # External modification causes backup restart on a later step. In this
        # deterministic fixture the first two steps reduce remaining pages,
        # then the injected commit causes remaining pages to jump upward.
        restart_observed = any(
            progress[i][1] > progress[i - 1][1] for i in range(1, len(progress))
        )

        assert mode == "wal"
        assert injected
        assert restart_observed
        assert source_count == 501
        assert backup_count == 501
        assert concurrent_rows == 1
        assert integrity == "ok"
        assert progress[-1][0] == sqlite3.SQLITE_DONE
        assert progress[-1][1] == 0

        print(f"python={os.sys.version.split()[0]} sqlite={sqlite3.sqlite_version} journal={mode}")
        print(f"progress_first={progress[:5]}")
        print(f"progress_last={progress[-3:]}")
        print(f"restart_observed={restart_observed}")
        print(f"source_count={source_count} backup_count={backup_count}")
        print(f"concurrent_rows={concurrent_rows} integrity_check={integrity}")

        destination.close()
        writer.close()
        source.close()


if __name__ == "__main__":
    main()
