#!/usr/bin/env python3
"""Bounded F006 transport-termination fixture.

Shows two distinct stream outcomes:
1) graceful peer write-close after a truncated application frame -> EOF with partial frame;
2) abortive close (SO_LINGER=0) after a complete frame -> receiver can obtain the
   complete application bytes and only then observe ConnectionResetError.

This is local Python/Linux socket evidence, not a Dart/Flutter or real-network proof.
"""

import socket
import struct

FRAME = struct.pack("!H", 5) + b"HELLO"


def graceful_truncation():
    sender, receiver = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sender.sendall(FRAME[:4])  # header + only 2/5 payload bytes
        sender.shutdown(socket.SHUT_WR)
        chunks = []
        while True:
            chunk = receiver.recv(1024)
            if chunk == b"":
                break
            chunks.append(chunk)
        observed = b"".join(chunks)
        declared = struct.unpack("!H", observed[:2])[0]
        body = observed[2:]
        assert declared == 5
        assert body == b"HE"
        assert len(body) < declared
        return {"terminal": "eof", "wire_hex": observed.hex(), "declared": declared, "body": body.decode()}
    finally:
        sender.close()
        receiver.close()


def abort_after_complete_frame():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(listener.getsockname())
        server, _ = listener.accept()
        try:
            server.sendall(FRAME)
            # Abortive close: discard graceful FIN path and request RST on close.
            server.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1, 0))
            server.close()

            received = bytearray()
            terminal = None
            while True:
                try:
                    chunk = client.recv(1024)
                    if chunk == b"":
                        terminal = "eof"
                        break
                    received.extend(chunk)
                except ConnectionResetError:
                    terminal = "reset"
                    break

            declared = struct.unpack("!H", received[:2])[0]
            body = bytes(received[2:])
            assert declared == 5
            assert body == b"HELLO"
            assert terminal == "reset"
            return {"terminal": terminal, "wire_hex": bytes(received).hex(), "declared": declared, "body": body.decode()}
        finally:
            try:
                server.close()
            except OSError:
                pass
    finally:
        client.close()
        listener.close()


if __name__ == "__main__":
    graceful = graceful_truncation()
    abortive = abort_after_complete_frame()
    print("graceful_truncation=", graceful)
    print("abort_after_complete_frame=", abortive)
    print("PASS: connection termination and application-frame completion are distinct observations")
