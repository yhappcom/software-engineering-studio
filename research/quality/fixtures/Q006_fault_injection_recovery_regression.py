"""Q006 fault-injection / recovery / regression-governance fixture.

Environment validated 2026-09-17 with Python 3.13.5 on Linux 6.18.44 x86_64.

Claim under test:
A recovery test must validate semantic terminal state after each reachable failure point;
merely retrying without an operation-level invariant can duplicate an already-applied effect.

This is a deterministic single-process model, not network/backend/mobile evidence.
"""

from dataclasses import dataclass, field

FAULTS = ("before_apply", "after_apply_before_ack", "after_ack")


class InjectedFault(RuntimeError):
    pass


@dataclass
class State:
    balance: int = 100
    applied: set[str] = field(default_factory=set)
    acked: set[str] = field(default_factory=set)


def robust_apply(state: State, op_id: str, amount: int, fault: str | None = None) -> None:
    if fault == "before_apply":
        raise InjectedFault(fault)

    # Stable logical-operation identity makes replay idempotent in this bounded model.
    if op_id not in state.applied:
        state.balance += amount
        state.applied.add(op_id)

    if fault == "after_apply_before_ack":
        raise InjectedFault(fault)

    state.acked.add(op_id)

    if fault == "after_ack":
        raise InjectedFault(fault)


def mutant_apply(state: State, op_id: str, amount: int, fault: str | None = None) -> None:
    """Regression mutant: operation identity is recorded but no longer guards the effect."""
    if fault == "before_apply":
        raise InjectedFault(fault)

    state.balance += amount
    state.applied.add(op_id)

    if fault == "after_apply_before_ack":
        raise InjectedFault(fault)

    state.acked.add(op_id)

    if fault == "after_ack":
        raise InjectedFault(fault)


def run_campaign(target):
    results = []
    for fault in FAULTS:
        state = State()
        try:
            target(state, "op-1", 10, fault)
        except InjectedFault:
            pass

        # Recovery policy: caller cannot infer terminal operation state from the fault,
        # so it replays the same logical operation identity.
        target(state, "op-1", 10, None)

        oracle = (
            state.balance == 110
            and state.applied == {"op-1"}
            and state.acked == {"op-1"}
        )
        results.append((fault, state.balance, oracle))
    return results


def main() -> None:
    robust = run_campaign(robust_apply)
    mutant = run_campaign(mutant_apply)

    print("robust", robust)
    print("mutant", mutant)

    assert all(ok for _, _, ok in robust)
    assert [fault for fault, _, ok in mutant if not ok] == [
        "after_apply_before_ack",
        "after_ack",
    ]


if __name__ == "__main__":
    main()
