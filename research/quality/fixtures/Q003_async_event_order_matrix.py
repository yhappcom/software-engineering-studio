"""Q003 deterministic async event-order matrix model.

Bounded model only: this is not Dart/Flutter/network runtime evidence.
Property: one logical operation may produce at most one accepted side effect.
"""
from itertools import permutations

EVENTS = ("timeout", "complete", "cancel", "retry")


def naive(order):
    applied = 0
    original_active = True
    retry_started = False
    trace = []
    for event in order:
        trace.append(event)
        if event == "complete" and original_active:
            applied += 1
            original_active = False
        elif event == "cancel" and original_active:
            original_active = False
        elif event == "retry":
            retry_started = True
    # Model the retry eventually completing after the control-event schedule.
    if retry_started:
        applied += 1
        trace.append("retry_complete")
    return applied, trace


def deduplicated(order):
    accepted_ids = set()
    original_active = True
    retry_started = False
    trace = []

    def accept(operation_id):
        accepted_ids.add(operation_id)

    for event in order:
        trace.append(event)
        if event == "complete" and original_active:
            accept("logical-op-1")
            original_active = False
        elif event == "cancel" and original_active:
            original_active = False
        elif event == "retry":
            retry_started = True
    if retry_started:
        accept("logical-op-1")
        trace.append("retry_complete")
    return len(accepted_ids), trace


def main():
    schedules = list(permutations(EVENTS))
    naive_failures = []
    dedup_failures = []
    for schedule in schedules:
        n, ntrace = naive(schedule)
        d, dtrace = deduplicated(schedule)
        if n > 1:
            naive_failures.append((schedule, n, ntrace))
        if d > 1:
            dedup_failures.append((schedule, d, dtrace))

    assert len(schedules) == 24
    assert naive_failures, "failure model did not expose duplicate accepted effects"
    assert not dedup_failures, "bounded dedup alternative violated at-most-one property"

    print(f"schedules={len(schedules)}")
    print(f"naive_duplicate_schedules={len(naive_failures)}")
    print(f"dedup_duplicate_schedules={len(dedup_failures)}")
    print("first_naive_failure=", naive_failures[0])


if __name__ == "__main__":
    main()
