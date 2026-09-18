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

The first block established architecture-description distinction, observer-scoped refactoring evidence and contingent future-change debt. The second block closes the named bounded repeated-change gap: across R1 rate-only → R2 cap → R3 minimum requirements, complete duplicated and single-owner implementations both satisfied an independent policy oracle, while a deliberate partial R2 migration across duplicated semantic owners produced `(120, '200.00', True)` instead of `(120, '120.00', True)` for principal 2000. Root cause was incomplete propagation of one semantic decision, not formatting. This supports `change pressure → semantic ownership → coordination obligation → partial-change risk`; it does not prove duplication is always debt or centralization universally superior.

Exact Dart/Flutter and exact-ref product evolution/debt transfer remain OPEN.

### A006 — Evidence-preserving architecture decisions and ADR lifecycle
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/architecture/A006_evidence_preserving_architecture_decisions.md`.

Established that ADRs preserve architecturally significant context/rationale/consequences/status but are not architecture or correctness proof; accepted decisions should be superseded rather than silently rewritten; Studio evidence-critical decisions preserve evidence/ref, assumptions, validation status and reconsideration triggers where applicable. Executable ADR-corpus governance validation and exact-ref product decision transfer remain OPEN.

## Queue
- `A001` — substantial Foundation block complete.
- `A002` — substantial Foundation block complete; concurrency intentionally deferred.
- `A003` — substantial Foundation block complete; product transfer deferred until a real evolution decision exists.
- `A004` — patterns and misuse; useful but not required as a pattern catalog for Foundation closure.
- `A005` — **IN STUDY / two executable blocks**; named repeated-change model gap closed; Dart/Flutter and exact-ref product evolution transfer OPEN.
- `A006` — IN STUDY / first integrated decision-evidence block complete; executable governance check and exact-ref product decision transfer OPEN.

## Gate assessment
Architecture Stage 1 remains **NOT PASS**. A001-A003/A005/A006 cover the roadmap's principal Foundation concepts and now include repeated-change failure evidence rather than only a one-step refactoring example. Broader product/runtime transfer and A006 executable governance evidence remain open; no PASS is awarded from model evidence alone.

## HANDOFFS
- **Data:** persisted schema/data evolution is not ordinary internal refactoring; duplicated reader/writer policy is a candidate transfer context for the A005 coordination-obligation model.
- **Quality:** evolutionary refactoring tests should inject partial migrations across duplicated semantic owners; current green tests alone do not establish low future-change risk.
- **Mobile:** lifecycle/plugin/platform behavior can be externally relevant; volatile platform facts used in decisions require versioned evidence and revalidation triggers.
- **Systems:** performance/security/artifact properties belong in observer sets when contractual/risk-significant; build/release evidence referenced by decisions must retain exact identity.
- **Product teams:** debt records should identify a plausible future coordinated-change scenario and observer-visible consequence rather than label duplication/smell alone.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter transfer remains blocked: environment rechecked 2026-09-18; neither `dart` nor `flutter` executable is available, Python 3.13.5 is available.
- A005 exact-ref product evolution/debt transfer remains OPEN; future stronger evidence should use real commit history or controlled multi-version product evidence without edit count as the sole oracle.
- A006 executable ADR-corpus governance validation and exact-ref product decision transfer remain OPEN.
- AWS/Microsoft ADR guidance checked 2026-09-18; recheck when operational guidance changes.
- ISO/IEC/IEEE 42010:2022 remains current from prior check; DIS 42024 remains CHANGE WATCH.

## Next work
Return to Balance Loop. The explicit A005 repeated-change/evolution model gap is now closed at bounded executable level. Do not deepen A005 merely for continuity. The strongest independent candidate is `A006` executable ADR-corpus governance validation because it can strengthen evidence-preserving decisions across all tracks without pretending unavailable Flutter/device evidence. Targeted real product/platform transfer outranks it whenever trustworthy exact runtime/device infrastructure becomes available. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK environment becomes available.
