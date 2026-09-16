#!/usr/bin/env python3
"""Q003 bounded concurrency/schedule validation fixture.

Environment observed in Studio run: Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41.
This deliberately creates a read/yield/write race. It is NOT Dart/Flutter evidence.
"""
import json
import threading
import time

ITERATIONS = 1000
RUNS = 20


def counter_run(*, locked: bool) -> int:
    state = {"value": 0}
    lock = threading.Lock()
    start = threading.Barrier(2)

    def worker() -> None:
        start.wait()
        for _ in range(ITERATIONS):
            if locked:
                with lock:
                    state["value"] += 1
            else:
                # Deliberately split read and write and yield between them.
                old = state["value"]
                time.sleep(0)
                state["value"] = old + 1

    threads = [threading.Thread(target=worker) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return state["value"]


def main() -> None:
    expected = 2 * ITERATIONS
    unsafe = [counter_run(locked=False) for _ in range(RUNS)]
    safe = [counter_run(locked=True) for _ in range(5)]
    report = {
        "claim": "A passing execution under one schedule does not establish schedule-independent correctness; shared read-modify-write requires an appropriate synchronization contract.",
        "expected": expected,
        "unsafe_runs": unsafe,
        "unsafe_failures": sum(v != expected for v in unsafe),
        "locked_runs": safe,
        "locked_failures": sum(v != expected for v in safe),
        "evidence_limit": "Deliberately widened CPython thread race only; not a probability estimate, scheduler model, Dart isolate/thread model, or proof that locks are the right architecture for every concurrent system.",
    }
    print(json.dumps(report, sort_keys=True))
    assert report["unsafe_failures"] > 0, "fixture failed to expose the deliberately widened race"
    assert report["locked_failures"] == 0, "bounded synchronized comparison violated counter invariant"


if __name__ == "__main__":
    main()
