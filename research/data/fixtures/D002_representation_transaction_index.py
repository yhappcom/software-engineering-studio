"""D002 bounded validation: representation, transaction, and index semantics.

This fixture compares three distinct mechanisms:
1. destructive whole-file JSON overwrite interrupted mid-write;
2. staging a replacement file but interrupting before publication;
3. SQLite transaction rollback plus query-plan change from an index.

It does not model power loss, fsync guarantees, mobile filesystems, or benchmark speed.
"""

from __future__ import annotations

import json
import pathlib
import platform
import sqlite3
import sys
import tempfile


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = pathlib.Path(directory)
        target = root / "ledger.json"
        baseline = [{"id": "A", "minutes": 60}]
        updated = baseline + [{"id": "B", "minutes": 90}]
        payload = json.dumps(updated)

        # Failure A: destructive publication and serialization are coupled.
        target.write_text(json.dumps(baseline), encoding="utf-8")
        with target.open("w", encoding="utf-8") as stream:
            stream.write(payload[: len(payload) // 2])
            stream.flush()

        try:
            json.loads(target.read_text(encoding="utf-8"))
            destructive_result = "unexpected-valid-json"
        except json.JSONDecodeError:
            destructive_result = "invalid-json-after-interruption"

        # Alternative: stage bytes separately. Interruption before publication
        # leaves the old canonical file intact in this process-level model.
        target.write_text(json.dumps(baseline), encoding="utf-8")
        staging = root / "ledger.tmp"
        staging.write_text(payload[: len(payload) // 2], encoding="utf-8")
        staged_old_state_preserved = (
            json.loads(target.read_text(encoding="utf-8")) == baseline
        )

        # Transaction failure: B is executed but rolled back before commit.
        database = root / "ledger.db"
        connection = sqlite3.connect(database)
        connection.execute("PRAGMA journal_mode=DELETE")
        connection.execute(
            "CREATE TABLE flights(id TEXT PRIMARY KEY, minutes INTEGER NOT NULL)"
        )
        connection.execute("INSERT INTO flights VALUES('A', 60)")
        connection.commit()

        try:
            connection.execute("BEGIN")
            connection.execute("INSERT INTO flights VALUES('B', 90)")
            raise RuntimeError("simulated failure before commit")
        except RuntimeError:
            connection.rollback()

        rows_after_rollback = connection.execute(
            "SELECT id, minutes FROM flights ORDER BY id"
        ).fetchall()

        # Index experiment: same semantic query/result, different access plan.
        connection.executemany(
            "INSERT INTO flights VALUES(?, ?)",
            [(f"X{i}", i % 120) for i in range(1000)],
        )
        connection.commit()
        plan_without_index = connection.execute(
            "EXPLAIN QUERY PLAN SELECT id FROM flights WHERE minutes=90"
        ).fetchall()
        count_without_index = connection.execute(
            "SELECT count(*) FROM flights WHERE minutes=90"
        ).fetchone()[0]

        connection.execute("CREATE INDEX idx_flights_minutes ON flights(minutes)")
        plan_with_index = connection.execute(
            "EXPLAIN QUERY PLAN SELECT id FROM flights WHERE minutes=90"
        ).fetchall()
        count_with_index = connection.execute(
            "SELECT count(*) FROM flights WHERE minutes=90"
        ).fetchone()[0]
        connection.close()

        assert destructive_result == "invalid-json-after-interruption"
        assert staged_old_state_preserved is True
        assert rows_after_rollback == [("A", 60)]
        assert count_without_index == count_with_index
        assert any("SCAN flights" in row[3] for row in plan_without_index)
        assert any("USING INDEX idx_flights_minutes" in row[3] for row in plan_with_index)

        print(f"python_version={sys.version.split()[0]}")
        print(f"sqlite_version={sqlite3.sqlite_version}")
        print(f"platform={platform.platform()}")
        print(f"destructive_json={destructive_result}")
        print(f"staged_old_state_preserved={staged_old_state_preserved}")
        print(f"rows_after_rollback={rows_after_rollback}")
        print(f"plan_without_index={plan_without_index}")
        print(f"plan_with_index={plan_with_index}")
        print(f"semantic_count_equal={count_without_index == count_with_index}")


if __name__ == "__main__":
    main()
