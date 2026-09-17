"""F003 bounded queue/data-structure complexity evidence.

Environment target for recorded run: CPython 3.13.5 / Linux 6.18.44 x86_64.
This is CPython comparison evidence, not Dart/Flutter evidence.
"""
from collections import deque
from time import perf_counter

SIZES = (5_000, 10_000, 20_000, 40_000)


def drain_list(n: int):
    q = list(range(n))
    checksum = 0
    start = perf_counter()
    while q:
        checksum += q.pop(0)
    return perf_counter() - start, checksum


def drain_deque(n: int):
    q = deque(range(n))
    checksum = 0
    start = perf_counter()
    while q:
        checksum += q.popleft()
    return perf_counter() - start, checksum


def expected_checksum(n: int) -> int:
    # Independent closed-form oracle for FIFO content preservation.
    return n * (n - 1) // 2


if __name__ == "__main__":
    print("n,list_s,deque_s,ratio,semantic_oracle")
    for n in SIZES:
        list_s, list_sum = drain_list(n)
        deque_s, deque_sum = drain_deque(n)
        expected = expected_checksum(n)
        ok = list_sum == deque_sum == expected
        print(f"{n},{list_s:.9f},{deque_s:.9f},{list_s/deque_s:.2f},{ok}")
        assert ok
