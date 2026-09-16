"""D003 executable fixture: schema compatibility and migration transaction boundaries.

Environment used for canonical run 2026-09-17:
Python 3.13.5 / SQLite 3.46.1 / Linux.

This fixture deliberately distinguishes:
- old/new reader-writer compatibility,
- schema shape from application user_version metadata,
- transactional migration rollback from split publication,
- expand/contract evolution from destructive compatibility breaks.
"""
import sqlite3
import tempfile
from pathlib import Path


def init_v1(path: Path) -> None:
    c = sqlite3.connect(path)
    c.execute("CREATE TABLE flights(id TEXT PRIMARY KEY, minutes INTEGER NOT NULL)")
    c.execute("INSERT INTO flights VALUES('A',60)")
    c.execute("PRAGMA user_version=1")
    c.commit()
    c.close()


def old_read(c):
    return c.execute("SELECT id, minutes FROM flights ORDER BY id").fetchall()


def old_write(c, flight_id, minutes):
    c.execute("INSERT INTO flights(id, minutes) VALUES(?,?)", (flight_id, minutes))


def new_read(c):
    return c.execute(
        "SELECT id, COALESCE(duration_seconds, minutes*60) FROM flights ORDER BY id"
    ).fetchall()


def new_write_dual(c, flight_id, seconds):
    c.execute(
        "INSERT INTO flights(id, minutes, duration_seconds) VALUES(?,?,?)",
        (flight_id, seconds // 60, seconds),
    )


def migrate_v2(c):
    c.execute("BEGIN IMMEDIATE")
    c.execute("ALTER TABLE flights ADD COLUMN duration_seconds INTEGER")
    c.execute(
        "UPDATE flights SET duration_seconds=minutes*60 WHERE duration_seconds IS NULL"
    )
    c.execute("PRAGMA user_version=2")
    c.commit()


def main():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)

        # Expand phase: old and new consumers coexist when new code tolerates old writes
        # and new code dual-writes the retained old representation.
        p = root / "v2.sqlite"
        init_v1(p)
        c = sqlite3.connect(p)
        migrate_v2(c)
        old_write(c, "B", 90)
        new_write_dual(c, "C", 7200)
        c.commit()
        print("v2 old reader", old_read(c))
        print("v2 new reader", new_read(c))
        print("version", c.execute("PRAGMA user_version").fetchone()[0])
        c.close()

        # Failure: schema publication and application version metadata are split across
        # commits. A crash/interruption between them leaves a truthful schema with stale
        # application migration metadata.
        q = root / "bad_split.sqlite"
        init_v1(q)
        c = sqlite3.connect(q)
        c.execute("ALTER TABLE flights ADD COLUMN duration_seconds INTEGER")
        c.commit()
        c.close()  # interruption before user_version update
        c = sqlite3.connect(q)
        print(
            "bad split version",
            c.execute("PRAGMA user_version").fetchone()[0],
            "columns",
            [r[1] for r in c.execute("PRAGMA table_info(flights)")],
        )
        c.close()

        # Alternative: schema + data + version metadata share one transaction. Injected
        # failure before COMMIT rolls the whole migration back to the v1 contract.
        r = root / "transactional.sqlite"
        init_v1(r)
        c = sqlite3.connect(r)
        try:
            c.execute("BEGIN IMMEDIATE")
            c.execute("ALTER TABLE flights ADD COLUMN duration_seconds INTEGER")
            c.execute("UPDATE flights SET duration_seconds=minutes*60")
            c.execute("PRAGMA user_version=2")
            raise RuntimeError("injected migration failure")
        except RuntimeError:
            c.rollback()
        print(
            "rollback version",
            c.execute("PRAGMA user_version").fetchone()[0],
            "columns",
            [x[1] for x in c.execute("PRAGMA table_info(flights)")],
            "rows",
            old_read(c),
        )
        c.close()

        # Contract phase: removing the retained representation is a deliberate
        # compatibility break. The old reader fails even though the migrated data is valid.
        s = root / "v3.sqlite"
        init_v1(s)
        c = sqlite3.connect(s)
        migrate_v2(c)
        c.execute("BEGIN")
        c.execute(
            "CREATE TABLE flights_new(id TEXT PRIMARY KEY, duration_seconds INTEGER NOT NULL)"
        )
        c.execute("INSERT INTO flights_new SELECT id,duration_seconds FROM flights")
        c.execute("DROP TABLE flights")
        c.execute("ALTER TABLE flights_new RENAME TO flights")
        c.execute("PRAGMA user_version=3")
        c.commit()
        try:
            old_read(c)
        except sqlite3.OperationalError as exc:
            print("v3 old reader FAIL", exc)
        print("v3 new rows", c.execute("SELECT * FROM flights").fetchall())
        c.close()


if __name__ == "__main__":
    main()
