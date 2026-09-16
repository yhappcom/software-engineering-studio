#!/usr/bin/env python3
import threading
import time
import platform
import sys


def circular_wait_probe():
    """Expose circular-wait preconditions without hanging the test process forever."""
    a, b = threading.Lock(), threading.Lock()
    ready = threading.Barrier(2)
    probed = threading.Barrier(2)
    results = []

    def worker(first, second, name):
        first.acquire()
        try:
            ready.wait(timeout=1)
            # Probe while both workers still hold their first lock. If this were a
            # blocking acquire, both workers would now wait on a resource held by
            # the other. The second barrier prevents one worker from releasing its
            # first lock before both probes have observed the state.
            got = second.acquire(blocking=False)
            results.append((name, got))
            probed.wait(timeout=1)
            if got:
                second.release()
        finally:
            first.release()

    t1 = threading.Thread(target=worker, args=(a, b, "T1"))
    t2 = threading.Thread(target=worker, args=(b, a, "T2"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return sorted(results)


def ordered_locking():
    """Alternative: all workers acquire shared locks in one global order."""
    a, b = threading.Lock(), threading.Lock()
    results = []

    def worker(name):
        with a:
            time.sleep(0.01)
            with b:
                results.append(name)

    t1 = threading.Thread(target=worker, args=("T1",))
    t2 = threading.Thread(target=worker, args=("T2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return sorted(results)


def main():
    circular = circular_wait_probe()
    ordered = ordered_locking()
    print("python", sys.version.split()[0], "platform", platform.platform())
    print("circular_probe", circular)
    print("ordered_locking", ordered)
    assert circular == [("T1", False), ("T2", False)], circular
    assert ordered == ["T1", "T2"], ordered
    print("PASS")


if __name__ == "__main__":
    main()
