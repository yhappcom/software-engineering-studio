# A003 — Interfaces, Contracts, Invariants & API Evolution

Status: **SUBSTANTIAL FOUNDATION BLOCK COMPLETE — TRACK NOT YET PASSED**  
Date: 2026-09-16  
Lead: Architecture

## Problem
A source-compatible interface can still break consumers when meaning, accepted input domain, guarantees, failure behavior, state transition, invariant, or protocol assumptions change. Architecture therefore needs semantic compatibility evidence, not signature inspection alone.

## SOURCE
Eiffel Design by Contract documentation was checked for client/supplier obligations: preconditions are client obligations, postconditions supplier guarantees, and invariants consistency conditions maintained across exported operations.

Barbara Liskov and Jeannette Wing, *A Behavioral Notion of Subtyping*, ACM TOPLAS 16(6), 1994, was checked via the CMU-hosted author paper. Its substitution criterion is specification-based: properties established for the supertype must continue to hold for the subtype. The paper explicitly reasons about preconditions, postconditions, exceptions, invariants and observable behavior/history.

## SYNTHESIS — semantic contract model
A useful operational contract may include:

`accepted inputs/preconditions + returned meaning/postconditions + state transition + invariants + failure semantics + observable side effects`

Source/type/binary/data-schema/protocol/behavioral compatibility are separate dimensions. Claims must name the dimension actually evidenced.

## VALIDATION A — same signature, broken meaning and strengthened precondition
Fixture: `research/architecture/fixtures/A003_contract_evolution.py`

Retained consumer contract expected `total_minutes()` to mean block time. Fixture data independently gives block total 150 and airborne total 125. A same-name/same-signature replacement silently returned airborne time and failed the retained oracle. An additive alternative preserved `total_minutes() == 150` and exposed airborne total separately.

A second replacement kept the signature but rejected empty input that V1 accepted as total 0. Root cause was provider-side semantic drift, not call-shape incompatibility.

## VALIDATION B — provider/consumer compatibility matrix, invariant evolution, additive break
Fixture: `research/architecture/fixtures/A003_compatibility_matrix.py`

Environment: Python 3.13.5; Linux 6.18.44 x86_64, glibc 2.41.

### Test Evidence Contract
- **CLAIM:** relative to retained consumer obligations, a replacement that accepts at least the old legal inputs and guarantees at least the old results can preserve the bounded contract; strengthening preconditions, weakening postconditions, or violating retained invariants can break it. An additive protocol field can also break a strict existing consumer.
- **SPEC/PROPERTY:** old calls use inputs `0,1,5` and require `result >= input`; account invariant requires `balance >= 0`; V1 protocol consumer accepts exactly the known `minutes` field.
- **TARGET:** four provider variants, two account implementations, and V1/V2 JSON producers against the retained V1 consumer.
- **ORACLE:** old-domain calls must remain accepted and satisfy the old postcondition; exported account operation must preserve non-negative balance; retained strict protocol consumer must successfully parse provider output.
- **OBSERVATION:** weaker precondition PASS; stronger precondition FAIL at old-legal `x=0`; stronger postcondition PASS; weaker postcondition FAIL (`x=0` returned `-1`); base account preserved invariant while replacement reached `balance=-1`; V1 JSON parsed as 90 while V2's additive `source` field was rejected as unknown.
- **VERDICT:** the bounded compatibility matrix matches behavioral-substitution reasoning. Additive syntax alone did not guarantee compatibility with an existing strict consumer.
- **FAILURE MODEL:** provider narrows legal input, weakens old guarantee, expands reachable state beyond old invariant, or expands protocol shape beyond a strict consumer's accepted language.
- **REPRODUCTION DATA:** fixture path above; deterministic fixed inputs; no network/external service.
- **EVIDENCE LIMIT:** synchronous Python/JSON example only. It does not establish Dart subtype rules, ABI compatibility, tolerant-reader best practice, HTTP/Protobuf compatibility, persisted schema migration safety, or production behavior.

## COMPATIBILITY MATRIX — bounded reasoning rule
For an established consumer contract:

| Provider evolution | Bounded expectation | Executable result |
| --- | --- | --- |
| Weaken precondition / accept more | can preserve old callers | PASS |
| Strengthen precondition / accept less | may reject old-valid caller | FAIL reproduced |
| Strengthen postcondition / guarantee more while retaining old guarantee | can preserve old expectation | PASS |
| Weaken postcondition | may violate old expectation | FAIL reproduced |
| Permit state violating retained invariant | breaks behavioral substitutability | FAIL reproduced |
| Add protocol member | not inherently safe; depends on consumer acceptance rules | strict-consumer FAIL reproduced |

This is not a universal versioning algorithm. Compatibility is relational: **provider change × actual consumer assumptions × compatibility dimension**.

## CONTRADICTION
Two shortcuts are now executable-falsified:
1. “same signature means non-breaking”; and
2. “additive change means non-breaking”.

The additive JSON example is deliberately strict. It does not imply consumers should always reject unknown fields. It proves only that additive provider changes are not intrinsically safe independent of the consumer contract.

## ENGINEERING JUDGMENT
When a new requirement conflicts with an established semantic contract, prefer preserving the old semantic operation and adding a distinct one, explicit version/migration, or a deliberate breaking change with identified consumers and migration/rollback evidence proportional to risk.

Do not weaken a public guarantee or expand reachable invalid state merely because compilation succeeds. Do not label an additive change safe until the relevant consumer acceptance rule is known.

## CONNECTION TO A001 / A002 / Q001
- **A001:** boundaries hide volatile knowledge; A003 defines the visible promise that must remain stable or deliberately evolve.
- **A002:** dependency inversion protects policy only when the policy-owned interface preserves meaningful semantics and invariants.
- **Q001:** prior consumer expectations/invariants are independent compatibility oracles; replacement behavior cannot define its own correctness.

## RELATED DOMAIN CHECK
- Foundations: type/signature compatibility must not be confused with runtime correctness; direct Dart execution remains OPEN in F001.
- Data: schema/migration compatibility adds persistence, old/new reader-writer, rollback and recovery semantics; canonical work belongs in D003.
- Quality: retained-consumer contract suites transfer directly to Q002/Q006.
- Mobile: Dart/plugin/platform evolution requires exact framework/platform evidence; M001/M004 remain open.
- Systems: binary/build/release compatibility and rollback are separate dimensions; S004-S006 own them.
- Design Studio: not materially required for this generic block; interaction semantics can later be upstream observable contracts.
- Web Manager / Marketing Manager: not materially relevant to this bounded study.
- Product repositories: no live product evolution decision was required, so no new product claim was made.

## HANDOFFS
- **TO Data:** D003 should build explicit old-reader/new-writer/new-reader/old-writer matrices and preserve semantic invariants separately from schema shape.
- **TO Quality:** compatibility suites should retain prior consumer contracts as independent oracles and include failure semantics/invariants, not only return values.
- **TO Mobile:** plugin/platform upgrades require behavioral and failure-contract checks in addition to Dart source compatibility.
- **TO Systems:** release/versioning evidence must name source, binary, protocol, data, or behavioral compatibility and validate rollback where relevant.

## OPEN / VALIDATION
- Transfer-test A003 against an exact MintTap or LogMate contract when a real interface/schema evolution decision exists.
- Persisted-schema/protocol compatibility matrices belong in D003/S005 rather than being inferred from the JSON fixture.
- Dart/Flutter behavioral transfer remains blocked by missing trustworthy execution environment.

## Current conclusion
An interface is not merely syntax. Compatibility is a relationship between an evolved provider and retained consumer properties. A replacement must continue to accept the old legal calls, preserve the guarantees and invariants those callers rely on, and respect the consumer's accepted protocol/state language—or explicitly version/migrate the contract. “Same signature” and “additive” are classifications of change shape, not compatibility proofs.
