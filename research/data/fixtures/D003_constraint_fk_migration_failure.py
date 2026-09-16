import sqlite3
import tempfile
import os
import json


def setup(path):
    c = sqlite3.connect(path)
    c.execute("PRAGMA foreign_keys=ON")
    c.executescript("""
    CREATE TABLE pilots(id TEXT PRIMARY KEY);
    CREATE TABLE flights(
      id TEXT PRIMARY KEY,
      pilot_id TEXT NOT NULL,
      minutes INTEGER NOT NULL,
      FOREIGN KEY(pilot_id) REFERENCES pilots(id)
    );
    INSERT INTO pilots VALUES('P1');
    INSERT INTO flights VALUES('F1','P1',60);
    PRAGMA user_version=1;
    """)
    c.commit()
    c.close()


def failed_transform(weak):
    path = tempfile.mktemp(suffix=".db")
    setup(path)
    c = sqlite3.connect(path)
    c.execute("PRAGMA foreign_keys=ON")
    error = None
    try:
        c.execute("BEGIN")
        c.execute("""CREATE TABLE flights_v2(
          id TEXT PRIMARY KEY,
          pilot_id TEXT NOT NULL,
          seconds INTEGER NOT NULL CHECK(seconds>=0),
          FOREIGN KEY(pilot_id) REFERENCES pilots(id)
        )""")
        # Legacy state that the proposed V2 invariant cannot represent.
        c.execute("INSERT INTO flights VALUES('BAD','P1',-5)")
        try:
            c.execute("INSERT INTO flights_v2 SELECT id,pilot_id,minutes*60 FROM flights")
        except sqlite3.IntegrityError as exc:
            error = str(exc)
            if not weak:
                raise
        # Weak protocol incorrectly publishes V2 after the failed transform.
        c.execute("PRAGMA user_version=2")
        c.commit()
    except sqlite3.IntegrityError:
        # Strong protocol treats transform failure as migration failure.
        c.rollback()

    tables = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )]
    out = {
        "weak": weak,
        "transform_error": error,
        "user_version": c.execute("PRAGMA user_version").fetchone()[0],
        "tables": tables,
        "v2_rows": c.execute("SELECT count(*) FROM flights_v2").fetchone()[0]
        if "flights_v2" in tables else None,
        "old_rows": c.execute("SELECT count(*) FROM flights").fetchone()[0],
    }
    c.close()
    os.remove(path)
    return out


def fk_validation():
    path = tempfile.mktemp(suffix=".db")
    setup(path)
    c = sqlite3.connect(path)
    c.execute("PRAGMA foreign_keys=OFF")
    c.execute("INSERT INTO flights VALUES('ORPHAN','MISSING',30)")
    c.commit()
    c.execute("PRAGMA foreign_keys=ON")
    out = {
        "foreign_keys_enabled": c.execute("PRAGMA foreign_keys").fetchone()[0],
        "foreign_key_check": c.execute("PRAGMA foreign_key_check").fetchall(),
    }
    c.close()
    os.remove(path)
    return out


if __name__ == "__main__":
    print(json.dumps({
        "weak_transform_protocol": failed_transform(True),
        "atomic_transform_protocol": failed_transform(False),
        "fk_validation": fk_validation(),
    }, indent=2))
