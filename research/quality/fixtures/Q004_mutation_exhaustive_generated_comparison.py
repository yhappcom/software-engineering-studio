#!/usr/bin/env python3
"""Q004 mutation sensitivity and bounded exhaustive-vs-generated comparison."""
from itertools import product
import random
from dataclasses import dataclass
from typing import Optional

SEED = 20260919
SAMPLE_CASES = 3
MAX_STEPS = 4

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

def model_terminal(sequence):
    latest = None
    for event in sequence:
        if latest is None or event.version > latest.version:
            latest = event
    return None if latest is None or latest.kind == "delete" else latest.value

def mutant_arrival_order(sequence):
    state = None
    for event in sequence:
        state = event.value if event.kind == "update" else None
    return state

def mutant_ignore_delete(sequence):
    latest = None
    for event in sequence:
        if event.kind == "delete":
            continue
        if latest is None or event.version > latest.version:
            latest = event
    return None if latest is None else latest.value

def exhaustive_sequences():
    for length in range(1, MAX_STEPS + 1):
        yield from (list(items) for items in product(EVENTS, repeat=length))

def sampled_sequences():
    rng = random.Random(SEED)
    for _ in range(SAMPLE_CASES):
        yield [rng.choice(EVENTS) for _ in range(rng.randint(1, MAX_STEPS))]

def killed_by(mutant, sequences):
    return [sequence for sequence in sequences if mutant(sequence) != model_terminal(sequence)]

def names(sequence):
    return [event.name for event in sequence]

def main():
    exhaustive = list(exhaustive_sequences())
    sampled = list(sampled_sequences())
    exhaustive_arrival = killed_by(mutant_arrival_order, exhaustive)
    exhaustive_delete = killed_by(mutant_ignore_delete, exhaustive)
    sampled_arrival = killed_by(mutant_arrival_order, sampled)
    sampled_delete = killed_by(mutant_ignore_delete, sampled)
    deterministic_regression = [EVENTS[2], EVENTS[1]]

    assert len(exhaustive) == 120
    assert len(exhaustive_arrival) == 61
    assert len(exhaustive_delete) == 86
    assert len(sampled_arrival) == 0
    assert len(sampled_delete) == 1
    assert mutant_arrival_order(deterministic_regression) != model_terminal(deterministic_regression)

    print("exhaustive_cases=120 arrival_mutant_killed=61 ignore_delete_mutant_killed=86")
    print(f"seed={SEED} sampled_cases={list(map(names, sampled))}")
    print(f"sampled_arrival_kills={len(sampled_arrival)} sampled_ignore_delete_kills={len(sampled_delete)}")
    print(f"deterministic_regression={names(deterministic_regression)} arrival_mutant_killed=True")
    print("VERDICT=BOUNDED_EXHAUSTIVE_KILLS_BOTH_MUTANTS_SAMPLED_CAMPAIGN_MISSES_ONE")

if __name__ == "__main__":
    main()
