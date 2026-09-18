import sqlite3, os, sys, tempfile, subprocess, json


def init(db):
    c = sqlite3.connect(db)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS entity(id TEXT PRIMARY KEY, value INTEGER NOT NULL, revision INTEGER NOT NULL);
    CREATE TABLE IF NOT EXISTS sync_state(id INTEGER PRIMARY KEY CHECK(id=1), cursor INTEGER NOT NULL);
    INSERT OR IGNORE INTO entity VALUES('f1',100,1);
    INSERT OR IGNORE INTO sync_state VALUES(1,0);
    """)
    c.commit(); c.close()


def child(db, mode):
    c = sqlite3.connect(db)
    if mode == "unsafe":
        c.execute("UPDATE sync_state SET cursor=1 WHERE id=1")
        c.commit()
        os._exit(77)  # crash after cursor publication, before entity apply
    if mode == "safe":
        c.execute("BEGIN IMMEDIATE")
        c.execute("UPDATE entity SET value=120, revision=2 WHERE id='f1'")
        c.execute("UPDATE sync_state SET cursor=1 WHERE id=1")
        os._exit(78)  # crash before transaction commit


def recover(db):
    c = sqlite3.connect(db)
    row = c.execute("SELECT value,revision FROM entity WHERE id='f1'").fetchone()
    cursor = c.execute("SELECT cursor FROM sync_state WHERE id=1").fetchone()[0]
    integrity = c.execute("PRAGMA integrity_check").fetchone()[0]
    c.close()
    # Bounded server model: cursor 1 means change 1 will not be returned again.
    remaining = [] if cursor >= 1 else [(1, 120, 2)]
    return row, cursor, remaining, integrity


if __name__ == "__main__":
    if len(sys.argv) > 2:
        child(sys.argv[1], sys.argv[2])

    out = {}
    for mode in ("unsafe", "safe"):
        with tempfile.TemporaryDirectory() as td:
            db = os.path.join(td, "x.db")
            init(db)
            p = subprocess.run([sys.executable, __file__, db, mode])
            row, cursor, remaining, integrity = recover(db)
            out[mode] = {
                "exit": p.returncode,
                "entity": row,
                "cursor": cursor,
                "server_remaining": remaining,
                "integrity": integrity,
            }

    print(json.dumps(out, sort_keys=True))
    assert out["unsafe"]["entity"] == (100, 1)
    assert out["unsafe"]["cursor"] == 1
    assert out["unsafe"]["server_remaining"] == []
    assert out["safe"]["entity"] == (100, 1)
    assert out["safe"]["cursor"] == 0
    assert len(out["safe"]["server_remaining"]) == 1
    print("D006 inbound cursor/apply crash boundary: PASS")
