from dataclasses import dataclass

CASES = [
    ("normal", 100, 0.10, "USD 110.00"),
    ("zero", 0, 0.10, "USD 0.00"),
    ("negative", -50, 0.10, "ERROR:negative principal"),
]


def legacy_quote(principal, rate):
    if principal < 0:
        raise ValueError("negative principal")
    return f"USD {principal * (1 + rate):.2f}"


# Behavior-preserving internal restructuring.
def _amount(principal, rate):
    if principal < 0:
        raise ValueError("negative principal")
    return principal * (1 + rate)


def refactored_quote(principal, rate):
    return f"USD {_amount(principal, rate):.2f}"


# Deliberate semantic-change mutant: tidy-looking restructuring that changes
# externally observable failure behavior by clamping invalid input.
def mutant_quote(principal, rate):
    principal = max(0, principal)
    return f"USD {principal * (1 + rate):.2f}"


def observe(fn, principal, rate):
    try:
        return fn(principal, rate)
    except ValueError as exc:
        return f"ERROR:{exc}"


def run():
    legacy = [observe(legacy_quote, p, r) for _, p, r, _ in CASES]
    refactored = [observe(refactored_quote, p, r) for _, p, r, _ in CASES]
    mutant = [observe(mutant_quote, p, r) for _, p, r, _ in CASES]
    oracle = [expected for _, _, _, expected in CASES]

    assert legacy == oracle, (legacy, oracle)
    assert refactored == oracle, (refactored, oracle)
    assert mutant != oracle, (mutant, oracle)

    failing = [
        CASES[i][0]
        for i, (actual, expected) in enumerate(zip(mutant, oracle))
        if actual != expected
    ]
    print("legacy=", legacy)
    print("refactored=", refactored)
    print("mutant=", mutant)
    print("mutant_failures=", failing)
    print("verdict=behavior-preserving refactor PASS; semantic-change mutant DETECTED")


if __name__ == "__main__":
    run()
