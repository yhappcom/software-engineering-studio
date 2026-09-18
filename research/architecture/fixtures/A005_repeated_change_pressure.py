from dataclasses import dataclass

@dataclass(frozen=True)
class Policy:
    rate: float
    cap: float | None = None
    minimum: float = 0.0

# Independent specification/oracle for each evolutionary requirement.
def oracle(principal: float, policy: Policy) -> float:
    if principal < 0:
        raise ValueError("negative principal")
    value = principal * policy.rate
    if policy.cap is not None:
        value = min(value, policy.cap)
    return max(value, policy.minimum)

# Coupled design: policy semantics duplicated across three consumers.
def coupled_quote(p, policy):
    if p < 0:
        raise ValueError("negative principal")
    x = p * policy.rate
    if policy.cap is not None:
        x = min(x, policy.cap)
    return max(x, policy.minimum)

def coupled_export(p, policy):
    return f"{coupled_quote(p, policy):.2f}"

def coupled_alert(p, policy):
    return coupled_quote(p, policy) >= 100.0

# Encapsulated design: one policy owner, consumers depend on its result.
def evaluate(p, policy):
    return oracle(p, policy)

def encapsulated_quote(p, policy):
    return evaluate(p, policy)

def encapsulated_export(p, policy):
    return f"{evaluate(p, policy):.2f}"

def encapsulated_alert(p, policy):
    return evaluate(p, policy) >= 100.0

# Deliberate evolution mutant: new cap added only to quote path; export/alert retain old semantics.
def partial_quote(p, policy):
    return coupled_quote(p, policy)

def partial_export(p, policy):
    legacy = Policy(rate=policy.rate, cap=None, minimum=policy.minimum)
    return f"{coupled_quote(p, legacy):.2f}"

def partial_alert(p, policy):
    legacy = Policy(rate=policy.rate, cap=None, minimum=policy.minimum)
    return coupled_quote(p, legacy) >= 100.0

requirements = [
    ("R1 rate only", Policy(.10), [0, 500, 2000]),
    ("R2 add cap", Policy(.10, cap=120), [0, 500, 2000]),
    ("R3 add minimum", Policy(.10, cap=120, minimum=5), [0, 10, 2000]),
]

def expected(p, pol):
    v = oracle(p, pol)
    return (v, f"{v:.2f}", v >= 100)

def observe(q, e, a, p, pol):
    return (q(p, pol), e(p, pol), a(p, pol))

for _, pol, inputs in requirements:
    for p in inputs:
        exp = expected(p, pol)
        assert observe(encapsulated_quote, encapsulated_export, encapsulated_alert, p, pol) == exp
        assert observe(coupled_quote, coupled_export, coupled_alert, p, pol) == exp

# Partial migration is indistinguishable under R1 but fails when R2's cap matters.
assert observe(partial_quote, partial_export, partial_alert, 500, requirements[0][1]) == expected(500, requirements[0][1])
obs = observe(partial_quote, partial_export, partial_alert, 2000, requirements[1][1])
exp = expected(2000, requirements[1][1])
assert obs != exp
assert obs == (120.0, "200.00", True)
assert exp == (120.0, "120.00", True)

# Negative-input failure policy remains part of the observer set throughout evolution.
for funcs in [
    (coupled_quote, coupled_export, coupled_alert),
    (encapsulated_quote, encapsulated_export, encapsulated_alert),
]:
    for f in funcs:
        try:
            f(-1, requirements[-1][1])
        except ValueError:
            pass
        else:
            raise AssertionError("negative-input contract lost")

print("A005 repeated-change fixture: PASS")
print("partial migration R2 observed=", obs, "expected=", exp)
print("requirements_checked=", len(requirements), "consumer_contracts=3")
