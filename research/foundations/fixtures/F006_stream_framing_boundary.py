#!/usr/bin/env python3
"""F006 bounded executable evidence: stream reads are not application-message reads."""
import platform
import socket
import sys


def main() -> None:
    left, right = socket.socketpair(type=socket.SOCK_STREAM)
    try:
        wire = b"\x00\x05HELLO"  # 2-byte big-endian length + payload
        left.sendall(wire)

        # Deliberately request less than the application header. A stream API
        # promises bytes, not completion of our application message/header.
        first = right.recv(1)
        naive_header_complete = len(first) >= 2

        # Correct bounded alternative: retain bytes and continue until the
        # protocol framing rule can be satisfied.
        buffered = bytearray(first)
        while len(buffered) < 2:
            chunk = right.recv(2 - len(buffered))
            if not chunk:
                raise AssertionError("EOF before frame header completed")
            buffered.extend(chunk)

        body_len = int.from_bytes(buffered[:2], "big")
        while len(buffered) < 2 + body_len:
            chunk = right.recv(2 + body_len - len(buffered))
            if not chunk:
                raise AssertionError("EOF before frame body completed")
            buffered.extend(chunk)

        body = bytes(buffered[2:2 + body_len])
        assert not naive_header_complete
        assert body == b"HELLO"

        print(f"python={sys.version.split()[0]}")
        print(f"platform={platform.platform()}")
        print(f"first_recv_hex={first.hex()}")
        print(f"naive_header_complete={naive_header_complete}")
        print(f"decoded_length={body_len}")
        print(f"body={body.decode()}")
        print("verdict=PASS bounded framing alternative; naive one-read assumption falsified")
    finally:
        left.close()
        right.close()


if __name__ == "__main__":
    main()
