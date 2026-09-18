#!/usr/bin/env python3
"""Bounded D006 fault injection: live TCP connection interrupted by loopback link-down.

Outer process creates fresh Linux user+network namespaces via `unshare -Urn`.
Inner process toggles only that namespace's loopback device, leaving the host network untouched.
"""
import os
import socket
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time


def ip(*args):
    subprocess.run(["ip", *args], check=True, stdout=subprocess.DEVNULL)


def init(db, safe):
    c = sqlite3.connect(db)
    c.execute("CREATE TABLE counter(v INTEGER NOT NULL)")
    c.execute("INSERT INTO counter VALUES(0)")
    if safe:
        c.execute("CREATE TABLE ops(id TEXT PRIMARY KEY,result INTEGER NOT NULL)")
    c.commit()
    c.close()


def apply(db, safe, op, delta):
    c = sqlite3.connect(db)
    c.execute("BEGIN IMMEDIATE")
    if safe:
        row = c.execute("SELECT result FROM ops WHERE id=?", (op,)).fetchone()
        if row:
            result = row[0]
        else:
            result = c.execute("SELECT v FROM counter").fetchone()[0] + delta
            c.execute("UPDATE counter SET v=?", (result,))
            c.execute("INSERT INTO ops VALUES(?,?)", (op, result))
    else:
        result = c.execute("SELECT v FROM counter").fetchone()[0] + delta
        c.execute("UPDATE counter SET v=?", (result,))
    c.commit()
    c.close()
    return result


def case(safe):
    with tempfile.TemporaryDirectory() as td:
        db = os.path.join(td, "state.db")
        init(db, safe)
        committed = threading.Event()
        ports = []

        def server():
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("127.0.0.1", 0))
            s.listen()
            ports.append(s.getsockname()[1])
            for attempt in range(2):
                conn, _ = s.accept()
                op, delta = conn.recv(100).decode().split(":")
                result = apply(db, safe, op, int(delta))
                if attempt == 0:
                    committed.set()
                    time.sleep(0.8)  # parent-side fault window after durable commit
                try:
                    conn.sendall(f"{result}\n".encode())
                except OSError:
                    pass
                conn.close()
            s.close()

        t = threading.Thread(target=server)
        t.start()
        while not ports:
            time.sleep(0.005)

        c = socket.create_connection(("127.0.0.1", ports[0]))
        c.settimeout(0.25)
        c.sendall(b"op-1:10")
        assert committed.wait(2)

        ip("link", "set", "dev", "lo", "down")
        try:
            try:
                first = c.recv(100)
                first_observation = ("bytes", first)
            except (TimeoutError, socket.timeout):
                first_observation = ("timeout", None)
        finally:
            c.close()
            ip("link", "set", "dev", "lo", "up")

        retry = socket.create_connection(("127.0.0.1", ports[0]))
        retry.settimeout(2)
        retry.sendall(b"op-1:10")
        retry_result = int(retry.recv(100).strip())
        retry.close()
        t.join(3)
        assert not t.is_alive()

        con = sqlite3.connect(db)
        final = con.execute("SELECT v FROM counter").fetchone()[0]
        ops = con.execute("SELECT count(*) FROM ops").fetchone()[0] if safe else None
        con.close()
        return first_observation, retry_result, final, ops


def inner():
    ip("link", "set", "dev", "lo", "up")
    safe = case(True)
    unsafe = case(False)
    print("safe", safe)
    print("unsafe", unsafe)
    assert safe[0][0] == "timeout" and safe[1:] == (10, 10, 1)
    assert unsafe[0][0] == "timeout" and unsafe[1] == 20 and unsafe[2] == 20
    print("D006 network-namespace link interruption: PASS")


def outer():
    p = subprocess.run(
        ["unshare", "-Urn", sys.executable, os.path.abspath(__file__), "--inner"],
        text=True,
        capture_output=True,
    )
    print(p.stdout, end="")
    print(p.stderr, end="", file=sys.stderr)
    if p.returncode:
        raise SystemExit(p.returncode)


if __name__ == "__main__":
    inner() if "--inner" in sys.argv else outer()
