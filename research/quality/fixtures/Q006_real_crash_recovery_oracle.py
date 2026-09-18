import sqlite3, os, sys, tempfile, subprocess, json


def init(db):
    c = sqlite3.connect(db)
    c.executescript("""
    CREATE TABLE entity(id TEXT PRIMARY KEY,value INTEGER NOT NULL,revision INTEGER NOT NULL);
    CREATE TABLE sync_state(id INTEGER PRIMARY KEY CHECK(id=1),cursor INTEGER NOT NULL);
    INSERT INTO entity VALUES('f1',100,1);
    INSERT INTO sync_state VALUES(1,0);
    """)
    c.commit(); c.close()


def child(db, mode):
    c = sqlite3.connect(db)
    if mode == "unsafe":
        c.execute("UPDATE sync_state SET cursor=1 WHERE id=1")
        c.commit()
        os._exit(71)
    if mode == "safe":
        c.execute("BEGIN IMMEDIATE")
        c.execute("UPDATE entity SET value=120,revision=2 WHERE id='f1'")
        c.execute("UPDATE sync_state SET cursor=1 WHERE id=1")
        os._exit(72)


def observe(db):
    c = sqlite3.connect(db)
    entity = c.execute("SELECT value,revision FROM entity WHERE id='f1'").fetchone()
    cursor = c.execute("SELECT cursor FROM sync_state WHERE id=1").fetchone()[0]
    integrity = c.execute("PRAGMA integrity_check").fetchone()[0]
    c.close()
    remaining = [] if cursor >= 1 else [(1,120,2)]
    return entity,cursor,remaining,integrity


def structural_oracle(obs):
    return obs[3] == "ok"


def semantic_recovery_oracle(obs):
    entity,cursor,remaining,integrity = obs
    if integrity != "ok": return False
    if cursor >= 1 and entity != (120,2): return False
    if entity == (100,1) and not remaining: return False
    return True


if __name__ == "__main__":
    if len(sys.argv) > 2:
        child(sys.argv[1],sys.argv[2])
    out = {}
    for mode in ("unsafe","safe"):
        with tempfile.TemporaryDirectory() as td:
            db = os.path.join(td,"q.db"); init(db)
            p = subprocess.run([sys.executable,__file__,db,mode])
            obs = observe(db)
            out[mode] = {"exit":p.returncode,"entity":obs[0],"cursor":obs[1],
                         "remaining":obs[2],"integrity":obs[3],
                         "structural":structural_oracle(obs),
                         "semantic":semantic_recovery_oracle(obs)}
    print(json.dumps(out,sort_keys=True))
    assert out["unsafe"]["structural"] is True
    assert out["unsafe"]["semantic"] is False
    assert out["safe"]["structural"] is True
    assert out["safe"]["semantic"] is True
    print("Q006 real crash recovery-oracle discrimination: PASS")
