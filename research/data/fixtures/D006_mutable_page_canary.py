"""Synthetic D006 pagination/retention failure canary; no product data or network."""
import sqlite3
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    conn = sqlite3.connect(Path(tmp) / "events.sqlite")
    conn.execute("create table events(seq integer primary key, owner text, payload text)")
    def rows(sql, params=()):
        return [r[0] for r in conn.execute(sql, params)]
    def seed(values):
        conn.execute("delete from events")
        conn.executemany("insert into events values(?, 'A', 'synthetic')", [(v,) for v in values])
        conn.commit()

    seed([1, 2, 3])
    first = rows("select seq from events order by seq limit 2 offset 0")
    conn.execute("delete from events where seq=1")
    conn.commit()
    second = rows("select seq from events order by seq limit 2 offset 2")
    assert first == [1, 2] and second == [] and 3 not in first + second
    print("PASS 1: offset retention silently omits seq3")

    keyset = rows("select seq from events where seq>? order by seq limit 2", (max(first),))
    assert keyset == [3]
    print("PASS 2: keyset avoids positional retention skip")

    seed([10, 20, 30])
    first = rows("select seq from events order by seq limit 2 offset 0")
    conn.execute("insert into events values(15, 'A', 'synthetic')")
    conn.commit()
    second = rows("select seq from events order by seq limit 2 offset 2")
    assert first == [10, 20] and second == [20, 30]
    print("PASS 3: offset insertion duplicates seq20")

    second_key = rows("select seq from events where seq>? and seq<=? order by seq limit 2", (max(first), 30))
    assert second_key == [30] and set(first + second_key) == {10, 20, 30}
    print("PASS 4: bounded keyset retains original observed sequence set")

    conn.execute("insert into events values(40, 'A', 'synthetic')")
    conn.commit()
    within = rows("select seq from events where seq>? and seq<=? order by seq", (30, 30))
    later = rows("select seq from events where seq>? order by seq", (30,))
    assert within == [] and later == [40]
    print("PASS 5: later event deferred beyond fixed bound")

    seed([1, 2, 3])
    first = rows("select seq from events order by seq limit 2 offset 0")
    conn.execute("delete from events where seq=1")
    conn.commit()
    second = rows("select seq from events order by seq limit 2 offset 2")
    assert second == [] and set(first + second) != {1, 2, 3}
    print("PASS 6: empty offset page does not certify complete prefix")

    conn.execute("delete from events where seq=2")
    conn.commit()
    available = rows("select seq from events where seq>? order by seq", (0,))
    assert available == [3]
    print("PASS 7: keyset cannot prove already-GC'd history")
    conn.close()
print("D006_MUTABLE_PAGE_CANARY_PASS 7/7")
