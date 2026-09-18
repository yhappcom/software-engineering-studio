#!/usr/bin/env python3
"""D006 bounded real TCP + process-restart ambiguous retry fixture."""
import json
import multiprocessing as mp
import os
import socket
import sqlite3
import tempfile


def server(db_path, port_q, crash_after_commit, dedup):
    con = sqlite3.connect(db_path)
    con.execute("CREATE TABLE IF NOT EXISTS counter(v INTEGER NOT NULL)")
    con.execute("INSERT INTO counter SELECT 0 WHERE NOT EXISTS(SELECT 1 FROM counter)")
    con.execute("CREATE TABLE IF NOT EXISTS ops(id TEXT PRIMARY KEY, result INTEGER NOT NULL)")
    con.commit()

    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    port_q.put(listener.getsockname()[1])

    conn, _ = listener.accept()
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    req = json.loads(data)
    op_id, delta = req["op"], req["delta"]

    prior = con.execute("SELECT result FROM ops WHERE id=?", (op_id,)).fetchone() if dedup else None
    if prior:
        result = prior[0]
    else:
        current = con.execute("SELECT v FROM counter").fetchone()[0]
        result = current + delta
        con.execute("UPDATE counter SET v=?", (result,))
        if dedup:
            con.execute("INSERT INTO ops(id,result) VALUES(?,?)", (op_id, result))
        con.commit()

    # Deliberately die after durable DB commit but before application ACK bytes.
    if crash_after_commit:
        os._exit(33)

    conn.sendall((json.dumps({"result": result}) + "\n").encode())
    conn.close()
    listener.close()
    con.close()


def attempt(db_path, crash_after_commit, dedup):
    q = mp.Queue()
    proc = mp.Process(target=server, args=(db_path, q, crash_after_commit, dedup))
    proc.start()
    port = q.get(timeout=3)
    with socket.create_connection(("127.0.0.1", port), timeout=3) as conn:
        conn.sendall(b'{"op":"op-1","delta":10}\n')
        response = conn.recv(4096)
    proc.join(3)
    return response, proc.exitcode


def read_state(db_path):
    con = sqlite3.connect(db_path)
    value = con.execute("SELECT v FROM counter").fetchone()[0]
    op_count = con.execute("SELECT COUNT(*) FROM ops").fetchone()[0]
    con.close()
    return value, op_count


def main():
    with tempfile.TemporaryDirectory() as td:
        safe_db = os.path.join(td, "safe.db")
        first, first_exit = attempt(safe_db, True, True)
        second, second_exit = attempt(safe_db, False, True)
        safe_value, safe_ops = read_state(safe_db)
        print("safe", first, first_exit, second, second_exit, safe_value, safe_ops)
        assert first == b"" and first_exit == 33
        assert json.loads(second)["result"] == 10 and second_exit == 0
        assert (safe_value, safe_ops) == (10, 1)

        unsafe_db = os.path.join(td, "unsafe.db")
        first_u, first_u_exit = attempt(unsafe_db, True, False)
        second_u, second_u_exit = attempt(unsafe_db, False, False)
        unsafe_value, _ = read_state(unsafe_db)
        print("unsafe", first_u, first_u_exit, second_u, second_u_exit, unsafe_value)
        assert first_u == b"" and first_u_exit == 33
        assert json.loads(second_u)["result"] == 20 and second_u_exit == 0
        assert unsafe_value == 20

        print("D006 real TCP ambiguous-retry restart: PASS")


if __name__ == "__main__":
    main()
