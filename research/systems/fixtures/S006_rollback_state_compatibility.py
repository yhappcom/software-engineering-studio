from dataclasses import dataclass


@dataclass(frozen=True)
class Artifact:
    name: str
    schema_max: int


def run(artifact: Artifact, state_schema: int) -> str:
    if state_schema > artifact.schema_max:
        raise RuntimeError(f"{artifact.name} cannot read schema {state_schema}")
    return "healthy"


v1 = Artifact("v1-known-good", 1)
v2 = Artifact("v2-bad-release", 2)

# The new release has already advanced durable state before its runtime defect is detected.
state_schema = 2
naive_rollback_ok = True
try:
    run(v1, state_schema)
except RuntimeError as exc:
    naive_rollback_ok = False
    print("naive rollback:", exc)

# Alternative: restore a separately validated compatible state snapshot before routing to
# the exact previously accepted v1 artifact. This is a bounded model, not a universal
# recommendation to reverse database migrations in place.
restored_state = 1
print("coordinated rollback:", run(v1, restored_state))

assert not naive_rollback_ok
assert run(v1, restored_state) == "healthy"
print("PASS")
