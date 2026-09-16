"""D006 bounded model: retry/idempotency and LWW conflict loss.
Environment used for Studio validation: Python 3.13.5, Linux, 2026-09-17.
This is a deterministic model, not a network/Firestore runtime test.
"""


class CounterServer:
    def __init__(self):
        self.total = 0
        self.seen = {}

    def unsafe_add(self, delta):
        self.total += delta
        return self.total

    def keyed_add(self, operation_id, delta):
        if operation_id in self.seen:
            return self.seen[operation_id]
        self.total += delta
        self.seen[operation_id] = self.total
        return self.total


def retry_after_lost_ack():
    unsafe = CounterServer()
    first = unsafe.unsafe_add(10)  # applied, but modeled response is lost
    second = unsafe.unsafe_add(10)  # client retries same intent
    assert first == 10 and second == 20 and unsafe.total == 20

    keyed = CounterServer()
    first_keyed = keyed.keyed_add("op-1", 10)  # applied, response lost
    second_keyed = keyed.keyed_add("op-1", 10)  # retry same operation identity
    assert first_keyed == second_keyed == 10 and keyed.total == 10
    return unsafe.total, keyed.total


def concurrent_lww_loss():
    base = {"night": 10, "ifr": 20}
    writer_a = {"night": 15, "ifr": 20, "ts": 2}
    writer_b = {"night": 10, "ifr": 25, "ts": 3}

    lww = max((writer_a, writer_b), key=lambda x: x["ts"])
    independent_field_merge = {"night": writer_a["night"], "ifr": writer_b["ifr"]}

    assert lww["night"] == base["night"]  # A's night update disappeared
    assert lww["ifr"] == 25
    assert independent_field_merge == {"night": 15, "ifr": 25}
    return lww, independent_field_merge


if __name__ == "__main__":
    unsafe_total, keyed_total = retry_after_lost_ack()
    lww, merged = concurrent_lww_loss()
    print(f"unsafe_retry_total={unsafe_total} keyed_retry_total={keyed_total}")
    print(f"lww={lww} independent_field_merge={merged}")
    print("VERDICT=PASS")
