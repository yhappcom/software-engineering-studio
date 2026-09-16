from __future__ import annotations
from dataclasses import dataclass
import json, platform, sys

@dataclass(frozen=True)
class ContractResult:
    name: str
    compatible: bool
    observation: str

# Base contract: accepts x >= 0; guarantees result >= x.
def weaker_pre(x: int) -> int:
    return x + 1

def stronger_pre(x: int) -> int:
    if x <= 0:
        raise ValueError("x must be positive")
    return x + 1

def stronger_post(x: int) -> int:
    assert x >= 0
    return x + 2

def weaker_post(x: int) -> int:
    assert x >= 0
    return x - 1

def check_old_consumers(fn):
    for x in [0, 1, 5]:
        try:
            y = fn(x)
        except Exception as error:
            return False, f"x={x}: raised {type(error).__name__}"
        if y < x:
            return False, f"x={x}: postcondition result>=x violated by {y}"
    return True, "all retained old-domain calls satisfy old postcondition"

class BaseAccount:
    def __init__(self, balance: int): self.balance = balance
    def withdraw(self, amount: int):
        if amount < 0 or amount > self.balance: raise ValueError
        self.balance -= amount

class BrokenInvariantAccount(BaseAccount):
    def withdraw(self, amount: int):
        if amount < 0: raise ValueError
        self.balance -= amount

def strict_v1_consumer(payload: str) -> int:
    obj = json.loads(payload)
    if set(obj) != {"minutes"}:
        raise ValueError(f"unknown fields: {sorted(set(obj) - {'minutes'})}")
    return int(obj["minutes"])

def provider_v1() -> str:
    return json.dumps({"minutes": 90}, sort_keys=True)

def provider_v2_additive() -> str:
    return json.dumps({"minutes": 90, "source": "import"}, sort_keys=True)

def main() -> None:
    results = []
    for name, fn in [
        ("weaker_precondition", weaker_pre),
        ("stronger_precondition", stronger_pre),
        ("stronger_postcondition", stronger_post),
        ("weaker_postcondition", weaker_post),
    ]:
        ok, obs = check_old_consumers(fn)
        results.append(ContractResult(name, ok, obs))

    base = BaseAccount(10); base.withdraw(10)
    replacement = BrokenInvariantAccount(10); replacement.withdraw(11)
    invariant_base = base.balance >= 0
    invariant_replacement = replacement.balance >= 0

    additive_v1 = strict_v1_consumer(provider_v1())
    try:
        strict_v1_consumer(provider_v2_additive())
        additive = "unexpected pass"
    except ValueError as error:
        additive = f"break reproduced: {error}"

    print(f"python_version={sys.version.split()[0]}")
    print(f"platform={platform.platform()}")
    for result in results:
        print(f"{result.name}: compatible={result.compatible}; {result.observation}")
    print(f"base_invariant_preserved={invariant_base}; replacement_invariant_preserved={invariant_replacement}; replacement_balance={replacement.balance}")
    print(f"additive_v1_baseline={additive_v1}; additive_change={additive}")

    assert results[0].compatible
    assert not results[1].compatible
    assert results[2].compatible
    assert not results[3].compatible
    assert invariant_base and not invariant_replacement
    assert "break reproduced" in additive

if __name__ == "__main__":
    main()
