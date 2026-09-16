from __future__ import annotations

import hashlib
import json
import random
import sys

SPEC = "ledger_total(entries) returns the arithmetic sum of every signed integer entry."
SEED = 20260916
GENERATED_CASES = 100


def ledger_total_correct(entries: list[int]) -> int:
    return sum(entries)


def ledger_total_mutant(entries: list[int]) -> int:
    """Deliberate defect: silently drops negative entries."""
    return sum(x for x in entries if x >= 0)


def weak_oracle(fn) -> bool:
    """Intentionally weak: one coarse property over positive-only data."""
    return fn([10, 20, 5]) >= 0


def exact_oracle(fn) -> list[dict]:
    cases = [
        ([10, 20, 5], 35),
        ([10, -7, 2], 5),
        ([-5, -2], -7),
        ([], 0),
    ]
    failures = []
    for entries, expected in cases:
        observed = fn(entries)
        if observed != expected:
            failures.append(
                {"entries": entries, "expected": expected, "observed": observed}
            )
    return failures


def signed_symmetry_oracle(fn) -> bool:
    """For arithmetic sum, sum(-x_i) must equal -sum(x_i)."""
    data = [4, -3, 10, -8]
    return fn([-x for x in data]) == -fn(data)


def generated_oracle(fn, seed: int = SEED, count: int = GENERATED_CASES):
    rng = random.Random(seed)
    cases = [
        [rng.randint(-20, 20) for _ in range(rng.randint(0, 8))]
        for _ in range(count)
    ]
    encoded = json.dumps(cases, separators=(",", ":"), sort_keys=True).encode()
    case_hash = hashlib.sha256(encoded).hexdigest()

    failures = []
    for index, entries in enumerate(cases):
        # Executable oracle derived independently from the stated arithmetic-sum spec.
        expected = sum(entries)
        observed = fn(entries)
        if observed != expected:
            failures.append(
                {
                    "index": index,
                    "entries": entries,
                    "expected": expected,
                    "observed": observed,
                }
            )
    return case_hash, failures


def report(name: str, fn) -> dict:
    case_hash, generated_failures = generated_oracle(fn)
    return {
        "implementation": name,
        "weak_oracle_pass": weak_oracle(fn),
        "exact_failure_count": len(exact_oracle(fn)),
        "symmetry_oracle_pass": signed_symmetry_oracle(fn),
        "generated_seed": SEED,
        "generated_case_hash": case_hash,
        "generated_failure_count": len(generated_failures),
        "first_generated_failure": generated_failures[0] if generated_failures else None,
    }


def main() -> None:
    correct = report("correct", ledger_total_correct)
    mutant = report("mutant", ledger_total_mutant)

    # The fixture itself fails if the intended demonstration stops being true.
    assert correct["weak_oracle_pass"] is True
    assert correct["exact_failure_count"] == 0
    assert correct["symmetry_oracle_pass"] is True
    assert correct["generated_failure_count"] == 0

    # Critical lesson: a defective implementation can pass a weak test.
    assert mutant["weak_oracle_pass"] is True
    assert mutant["exact_failure_count"] > 0
    assert mutant["symmetry_oracle_pass"] is False
    assert mutant["generated_failure_count"] > 0
    assert mutant["generated_case_hash"] == correct["generated_case_hash"]

    print(f"python={sys.version.split()[0]}")
    print(f"spec={SPEC}")
    print(json.dumps(correct, sort_keys=True))
    print(json.dumps(mutant, sort_keys=True))


if __name__ == "__main__":
    main()
