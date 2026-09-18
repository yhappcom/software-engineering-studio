from dataclasses import dataclass

REQUIRED = (
    "DECISION QUESTION",
    "STATUS",
    "EVIDENCE",
    "ASSUMPTIONS",
    "VALIDATION",
    "RECONSIDERATION TRIGGER",
)
VALID_STATUS = {"PROPOSED", "ACCEPTED", "SUPERSEDED", "REJECTED"}


@dataclass(frozen=True)
class Verdict:
    ok: bool
    errors: tuple[str, ...]


def parse(text: str) -> dict[str, str]:
    out = {}
    for line in text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip().upper()] = value.strip()
    return out


def validate(text: str, known_ids: set[str]) -> Verdict:
    data = parse(text)
    errors = []
    for key in REQUIRED:
        if not data.get(key):
            errors.append(f"missing:{key}")

    status = data.get("STATUS", "").upper()
    if status and status not in VALID_STATUS:
        errors.append("invalid:STATUS")

    if status == "SUPERSEDED":
        target = data.get("SUPERSEDED BY", "")
        if not target:
            errors.append("missing:SUPERSEDED BY")
        elif target not in known_ids:
            errors.append("broken:SUPERSEDED BY")

    if data.get("EVIDENCE", "").lower() in {"ci passed", "tests passed", "docs"}:
        errors.append("unscoped:EVIDENCE")

    return Verdict(not errors, tuple(errors))


corpus = {
    "ADR-001": """ID: ADR-001
DECISION QUESTION: Which durable store owns authoritative records?
STATUS: SUPERSEDED
EVIDENCE: fixture D005 at exact repository ref abc123; Python 3.13.5/Linux; bounded restore oracle
ASSUMPTIONS: single-device local store; uninstall survival out of scope
VALIDATION: bounded executable only; mobile transfer OPEN
RECONSIDERATION TRIGGER: platform storage semantics or recovery requirements change
SUPERSEDED BY: ADR-002
""",
    "ADR-002": """ID: ADR-002
DECISION QUESTION: Which durable store owns authoritative records after sync requirement?
STATUS: ACCEPTED
EVIDENCE: exact product ref def456 plus D006 model; production ref unknown
ASSUMPTIONS: server-mediated sync required; browser transfer OPEN
VALIDATION: decision accepted; runtime acceptance OPEN
RECONSIDERATION TRIGGER: sync topology or platform target changes
""",
}

known = set(corpus)
assert all(validate(text, known).ok for text in corpus.values())

mutants = {
    "missing_evidence": corpus["ADR-002"].replace(
        "EVIDENCE: exact product ref def456 plus D006 model; production ref unknown\n", ""
    ),
    "accepted_equals_pass": corpus["ADR-002"].replace(
        "VALIDATION: decision accepted; runtime acceptance OPEN", "VALIDATION:"
    ),
    "broken_supersession": corpus["ADR-001"].replace(
        "SUPERSEDED BY: ADR-002", "SUPERSEDED BY: ADR-999"
    ),
    "unscoped_evidence": corpus["ADR-002"].replace(
        "EVIDENCE: exact product ref def456 plus D006 model; production ref unknown",
        "EVIDENCE: CI passed",
    ),
}
expected = {
    "missing_evidence": "missing:EVIDENCE",
    "accepted_equals_pass": "missing:VALIDATION",
    "broken_supersession": "broken:SUPERSEDED BY",
    "unscoped_evidence": "unscoped:EVIDENCE",
}

for name, text in mutants.items():
    verdict = validate(text, known)
    assert not verdict.ok and expected[name] in verdict.errors, (name, verdict)
    print(name, verdict.errors)

print("A006 bounded ADR governance validation: PASS")
