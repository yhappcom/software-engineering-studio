# A003 — Interfaces, Contracts, Invariants & API Evolution

Status: **IN STUDY — first integrated contract/evolution block complete**  
Date: 2026-09-16  
Lead: Architecture

## Problem
A source-compatible interface can still break consumers when its meaning, accepted input domain, guarantees, failure behavior, state transition, or invariant changes. Architecture therefore needs a semantic contract model, not only method signatures.

## SOURCE
Current Eiffel Design by Contract documentation was checked as a primary method source. It defines cooperation between client and supplier through precise contracts: preconditions are client obligations, postconditions are supplier guarantees when the precondition holds, and class invariants are consistency conditions maintained across exported operations. The documentation also treats assertion violations as evidence of bugs in the responsible party and distinguishes contract/interface information from implementation bodies.

Source: Eiffel.org, `ET: Design by Contract, Assertions and Exceptions`, checked 2026-09-16.

## SYNTHESIS — semantic contract model
For Studio architecture work, a useful operational contract may include:

`accepted inputs/preconditions + returned meaning/postconditions + state transition + invariants + failure semantics + observable side effects`

A type/method signature constrains only part of this space. Source compatibility, type compatibility, binary compatibility, and behavioral/semantic compatibility must not be collapsed into one claim.

## VALIDATION — same signature, broken meaning
Fixture: `research/architecture/fixtures/A003_contract_evolution.py`

### Test Evidence Contract
- **CLAIM:** preserving a method name/signature does not preserve consumer compatibility if semantic meaning changes.
- **SPEC/PROPERTY:** existing `total_minutes()` consumers expect total block time; for the fixture data the independent expected total is 150 minutes.
- **TARGET:** V1 block-time provider, same-signature provider silently changed to airborne time, and additive V2 provider.
- **INPUT:** flights with block/airborne pairs `(90,75)` and `(60,50)`.
- **ORACLE:** block total = 150; airborne total = 125, independently derived from fixture values.
- **OBSERVATION:** same-signature semantic-break provider returned 125 and failed the old consumer contract; additive V2 retained `total_minutes() == 150` and exposed `total_airborne_minutes() == 125` separately.
- **VERDICT:** syntactic sameness was insufficient; preserving the old semantic operation preserved the bounded consumer contract.
- **FAILURE MODEL:** provider changes result meaning without changing the call shape.
- **EVIDENCE LIMIT:** Python synchronous fixture only; no claim about language ABI, Dart, Flutter, HTTP versioning, persistence schema, or production compatibility.

## VALIDATION — strengthened precondition
The same fixture tests an old provider that accepts an empty collection and returns `0` against a same-signature provider that newly rejects empty input.

- **CLAIM:** strengthening a provider precondition can break an existing valid caller even when the signature is unchanged.
- **ORACLE:** the retained V1 contract accepts `[]` and returns `0`.
- **OBSERVATION:** the strengthened provider raised `ValueError` for that previously valid input.
- **ROOT CAUSE:** the provider reduced the legal input domain while callers still possessed the old contract.

This is not a rule that every API must accept empty input. The rule is that changing an already-promised legal domain is a semantic compatibility decision.

## CONTRADICTION
A common shortcut is “no breaking change because the method signature did not change.” The fixture falsifies that universal claim in two independent ways: changed result meaning and strengthened precondition.

A second shortcut is “additive API changes are always safe.” This block does **not** establish that. Additive changes can still affect overload resolution, serialization, default behavior, resource use, ordering, authorization, or exhaustive consumers depending on language/protocol. That remains OPEN for a later compatibility matrix.

## ENGINEERING JUDGMENT
When a new requirement conflicts with an established semantic contract, prefer one of:
- preserve the old operation and add a distinct semantic operation;
- explicitly version/migrate the contract;
- deliberately break the contract with identified consumers, migration evidence, and rollback/recovery where risk requires it.

Do not silently reuse an old name for a new meaning merely because the type system permits it.

## CONNECTION TO A001 / A002 / Q001
- **A001:** a boundary earns its cost by hiding volatile knowledge; A003 states what semantic promise must remain visible and stable enough for consumers.
- **A002:** dependency inversion protects policy only if the policy-owned interface has a meaningful contract; an interface whose semantics drift does not protect the policy.
- **Q001:** compatibility claims need an oracle based on the prior/public contract, not on the new implementation's own behavior.

## RELATED DOMAIN CHECK
- Foundations: type/signature compatibility must not be confused with runtime correctness; direct Dart execution remains OPEN in F001.
- Data: schema/migration compatibility is analogous but has additional persistence/recovery semantics; canonical work belongs in D003.
- Quality: retained-consumer contract tests are a direct handoff to Q002/Q006.
- Mobile: lifecycle/platform APIs can preserve Dart signatures while platform semantics differ; requires M001/M002 evidence.
- Systems: binary/build/release compatibility and rollback are separate dimensions; canonical work belongs in S004/S005/S006.
- Design Studio: not materially required for this generic semantic-contract block; interaction semantics can later serve as upstream observable contracts.
- Web Manager / Marketing Manager: not materially relevant to this block.
- Product repositories: no new product audit was required; no production claim is made.

## HANDOFFS
- **TO Data:** D003 migrations should distinguish representational/schema compatibility from semantic data invariants and retained-reader/writer contracts.
- **TO Quality:** construct compatibility tests from prior consumer expectations and invariants; do not generate the oracle from the replacement provider.
- **TO Mobile:** when platform/plugin APIs evolve, record semantic behavior and failure contracts in addition to Dart signatures.
- **TO Systems:** release/versioning evidence should state which compatibility dimension is claimed: source, binary, data/schema, protocol, or behavioral.

## OPEN / VALIDATION
- Build a provider/consumer compatibility matrix: weaker/stronger preconditions, weaker/stronger postconditions, invariant changes, failure-semantics changes.
- Test an additive change that is nevertheless breaking in a representative typed/protocol context before claiming additive safety.
- Study compatibility/versioning across API, persisted data, and distributed protocol boundaries in their owning tracks.
- Transfer-test A003 against an exact MintTap or LogMate contract when a live interface/schema evolution decision exists.

## Current conclusion
An interface is not merely its syntax. Architecture must preserve or deliberately evolve the semantic obligations on which consumers rely. Compatibility evidence therefore requires retained consumer contracts/invariants and independent oracles, not compilation success alone.
