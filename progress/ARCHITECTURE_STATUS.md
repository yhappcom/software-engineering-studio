# Architecture Specialist Status

Track: Software Architecture & Design  
Prefix: `A###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-18

## Current evidence

### A001 — Information hiding, cohesion, coupling and change pressure
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Positive change-locality evidence, over-abstraction counterexample, and exact-ref LogMate transfer are preserved in `research/architecture/A001_information_hiding_change_pressure.md`.

### A002 — Dependency direction, state ownership and derived projections
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Ownership failure + materially different dependency-structure comparison are preserved in `research/architecture/A002_dependency_direction_state_ownership.md` and its fixtures.

### A003 — Interfaces, contracts, invariants and API evolution
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Canonical: `research/architecture/A003_interfaces_contracts_api_evolution.md`. Established semantic compatibility, retained-consumer oracles, stronger/weaker pre/postcondition effects and additive-shape compatibility failure in bounded executable evidence.

### A005 — Architecture/design/implementation, refactoring, technical debt and evolutionary change pressure
**IN STUDY — two integrated executable Foundation blocks complete.**  
Canonical: `research/architecture/A005_refactoring_technical_debt_evolutionary_boundaries.md`, `research/architecture/A005_repeated_change_evolution_evidence.md`.  
Fixtures: `research/architecture/fixtures/A005_refactoring_behavior_boundary.py`, `research/architecture/fixtures/A005_repeated_change_pressure.py`.

Observer-scoped refactoring, contingent future-change debt, and repeated-change/partial-migration failure evidence are established. Exact Dart/Flutter and exact-ref product evolution/debt transfer remain OPEN.

### A006 — Evidence-preserving architecture decisions and ADR lifecycle
**IN STUDY — two integrated Foundation blocks complete; bounded executable governance sensitivity added.**  
Canonical: `research/architecture/A006_evidence_preserving_architecture_decisions.md`; fixture: `research/architecture/fixtures/A006_adr_governance_validator.py`.

The first block established that ADRs preserve architecturally significant context/rationale/consequences/status but are not architecture or correctness proof; accepted decisions should be superseded rather than silently rewritten; Studio evidence-critical decisions preserve evidence/ref, assumptions, validation status and reconsideration triggers where applicable.

The second block adds Python 3.13.5/Linux executable governance evidence over a two-record synthetic ADR corpus. Four deliberate mutations—missing evidence, Accepted with blank validation, broken supersession target, and unscoped `CI passed` evidence—were each rejected for the intended structural reason. This closes the named bounded executable-governance gap, but not substantive architecture correctness: the validator cannot establish truth/relevance of evidence, rationale quality, architectural significance or production behavior. Natural-corpus and exact-ref product transfer remain OPEN.

## Queue
- `A001` — substantial Foundation block complete.
- `A002` — substantial Foundation block complete; concurrency intentionally deferred.
- `A003` — substantial Foundation block complete; product transfer deferred until a real evolution decision exists.
- `A004` — patterns and misuse; useful but not required as a pattern catalog for Foundation closure.
- `A005` — two executable blocks; named repeated-change model gap closed; Dart/Flutter and exact-ref product evolution transfer OPEN.
- `A006` — **two integrated blocks**; named bounded executable governance gap closed; natural ADR corpus and exact-ref product decision transfer OPEN.

## Gate assessment
Architecture Stage 1 remains **NOT PASS**. A001-A003/A005/A006 cover the roadmap's principal Foundation concepts and now include repeated-change failure evidence plus executable decision-governance sensitivity. Broader product/runtime transfer and naturally occurring decision-corpus validation remain open; no PASS is awarded from synthetic/model evidence alone.

## HANDOFFS
- **Data:** persisted schema/data evolution is not ordinary internal refactoring; migration/sync/recovery ADRs should preserve compatibility/failure assumptions and validation dependencies.
- **Quality:** evolutionary refactoring tests should inject partial migrations; governance linters can use deliberate mutants but a passing linter is not a decision-correctness oracle.
- **Mobile:** lifecycle/plugin/platform behavior can be externally relevant; volatile platform facts used in decisions require versioned evidence and revalidation triggers.
- **Systems:** performance/security/artifact properties belong in observer sets when contractual/risk-significant; vague evidence labels such as `CI passed` are insufficient for evidence-critical decisions.
- **Product teams:** debt records should identify coordinated-change obligations; significant decisions should preserve exact evidence/ref and supersession history.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter transfer remains blocked: environment rechecked 2026-09-18; neither `dart` nor `flutter` executable is available, Python 3.13.5 is available.
- A005 exact-ref product evolution/debt transfer remains OPEN.
- A006 natural ADR-corpus validation and exact-ref product decision transfer remain OPEN.
- AWS/Microsoft ADR guidance checked 2026-09-18; recheck when operational guidance changes.
- ISO/IEC/IEEE 42010:2022 remains current from prior check; DIS 42024 remains CHANGE WATCH.

## Next work
Return to Balance Loop. A006's named bounded executable-governance gap is now closed, so do not deepen synthetic ADR linting merely for continuity. Highest-value next work should seek stronger real transfer/evidence rather than another model-only Architecture block: direct Dart/Flutter execution first if a trustworthy SDK appears; otherwise prioritize a tractable real crash/restart/durable/network or exact-ref product evidence block that materially advances a Foundation gate.
