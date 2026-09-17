#!/usr/bin/env python3
"""Q004 bounded model/property sequence generation and shrinking fixture.

Purpose: generate operation-delivery sequences for a deliberately naive replica,
compare terminal state against an independent version-aware reference model, and
shrink the first counterexample by deleting commands while preserving failure.

This file is intentionally stdlib-only so it can run without Hypothesis. It is
not evidence until an execution record captures environment, observation, and
verdict under methods/VALIDATION_STANDARD.md.
"""
from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable, Optional

SEED = 20260917
CASES = 500
MAX_STEPS = 8


@dataclass(frozen=True)
class Event:
    name: str
    kind: str
    version: int
    value: Optional[str]


EVENTS = (
    Event("update_v1", "update", 1, "A"),
    Event("update_v2", "update", 2, "B"),
    Event("delete_v3", "delete", 3, None),
)


def naive_terminal(sequence: Iterable[Event]) -> Optional[str]:
    state: Optional[str] = None
    for event in sequence:
        state = event.value if event.kind == "update" else None
    return state


def model_terminal(sequence: Iterable[Event]) -> Optional[str]:
    """Reference oracle: highest version wins; delete is a semantic state."""
    latest: Optional[Event] = None
    for event in sequence:
        if latest is None or event.version > latest.version:
            latest = event
    if latest is None or latest.kind == "delete":
        return None
    return latest.value


def violates_property(sequence: list[Event]) -> bool:
    return naive_terminal(sequence) != model_terminal(sequence)


def generate_sequences() -> Iterable[list[Event]]:
    rng = random.Random(SEED)
    for _ in range(CASES):
        length = rng.randint(1, MAX_STEPS)
        yield [rng.choice(EVENTS) for _ in range(length)]


def shrink_by_deletion(sequence: list[Event]) -> list[Event]:
    """Greedy delta-style shrink: remove commands while failure is preserved."""
    current = list(sequence)
    changed = True
    while changed:
        changed = False
        for index in range(len(current)):
            candidate = current[:index] + current[index + 1 :]
            if candidate and violates_property(candidate):
                current = candidate
                changed = True
                break
    return current


def names(sequence: Iterable[Event]) -> list[str]:
    return [event.name for event in sequence]


def main() -> None:
    first_failure: Optional[list[Event]] = None
    tested = 0
    for sequence in generate_sequences():
        tested += 1
        if violates_property(sequence):
            first_failure = sequence
            break

    if first_failure is None:
        raise AssertionError(
            f"No counterexample found in {tested} generated cases; seed={SEED}"
        )

    minimal = shrink_by_deletion(first_failure)
    assert violates_property(minimal)
    assert all(
        not violates_property(minimal[:i] + minimal[i + 1 :])
        for i in range(len(minimal))
    ), "Shrunk sequence is not 1-minimal under single-command deletion"

    print(f"seed={SEED} cases_examined={tested}")
    print(f"first_failure={names(first_failure)}")
    print(
        "first_observation="
        f"naive:{naive_terminal(first_failure)!r} "
        f"model:{model_terminal(first_failure)!r}"
    )
    print(f"shrunk_failure={names(minimal)}")
    print(
        "shrunk_observation="
        f"naive:{naive_terminal(minimal)!r} model:{model_terminal(minimal)!r}"
    )
    print("VERDICT=COUNTEREXAMPLE_FOUND_AND_1_MINIMAL_UNDER_DELETION")


if __name__ == "__main__":
    main()
