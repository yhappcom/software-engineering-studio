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

### A005 — Architecture/design/implementation, refactoring and technical-debt boundaries
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/architecture/A005_refactoring_technical_debt_evolutionary_boundaries.md`. Architecture-description distinction, observer-scoped refactoring evidence and contingent future-change debt model established.

### A006 — Evidence-preserving architecture decisions and ADR lifecycle
**IN STUDY — first integrated Foundation block complete.**  
Canonical: `research/architecture/A006_evidence_preserving_architecture_decisions.md`

Established from current AWS Prescriptive Guidance and Microsoft Azure Well-Architected guidance plus prior Studio validation evidence:
- ADRs preserve architecturally significant decision context/rationale/consequences/status; they are not architecture itself or proof of correctness;
- accepted decision history should be superseded rather than silently rewritten when new evidence changes the decision;
- Studio evidence-critical ADRs should preserve decision question, constraints, options, criteria, evidence/ref, assumptions/uncertainty, decision, consequences, validation status and supersession trigger/history where applicable;
- `ADR Accepted` and `validation PASS` are separate verdicts;
- volatile platform/build/security facts need source/version/ref and CHANGE WATCH/TRANSFER VALIDATION rather than timeless rationale;
- document-level adversarial review checks whether a future reviewer can reconstruct the original rationale, evidence limits, rejected alternatives, current/superseded status and reconsideration trigger.

Evidence limit: document/governance synthesis and adversarial review model only; no product ADR transfer or repository-level executable governance checker yet.

## Queue
- `A001` — substantial Foundation block complete.
- `A002` — substantial Foundation block complete; concurrency intentionally deferred.
- `A003` — substantial Foundation block complete; product transfer deferred until a real evolution decision exists.
- `A004` — patterns and misuse; useful but not required as a pattern catalog for Foundation closure.
- `A005` — IN STUDY; repeated-change/evolution and Dart/Flutter/product transfer OPEN.
- `A006` — **IN STUDY / first integrated decision-evidence block complete**; executable governance check and exact-ref product decision transfer OPEN.

## Gate assessment
Architecture Stage 1 remains **NOT PASS**. A001-A003/A005/A006 now cover the roadmap's principal Foundation concepts plus evidence-preserving decision lifecycle. Reading alone did not close the track: earlier blocks include executable ownership/contract/refactoring failures, while A006 adds a document-level adversarial oracle. Broader evolutionary/product transfer and an executable ADR-governance check remain open.

## HANDOFFS
- **Data:** persisted schema/data evolution is not ordinary internal refactoring; migration/sync/recovery decisions should preserve compatibility/failure assumptions and validation dependencies.
- **Quality:** refactoring validation should declare observer sets; ADR Accepted must never be used as a correctness verdict.
- **Mobile:** lifecycle/plugin/platform behavior can be externally relevant; volatile platform facts used in decisions require versioned evidence and revalidation triggers.
- **Systems:** performance/security/artifact properties belong in observer sets when contractual/risk-significant; build/release evidence referenced by decisions must retain exact identity.
- **Product teams:** supersede significant decisions rather than silently rewriting accepted rationale; technical-debt items should identify concrete future-change liability.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter transfer remains blocked: environment rechecked 2026-09-18; neither `dart` nor `flutter` executable is available, Python 3.13.5 is available.
- A005 repeated-change/evolution evidence and exact-ref product debt transfer remain OPEN.
- A006 executable ADR-corpus governance validation and exact-ref product decision transfer remain OPEN.
- AWS/Microsoft ADR guidance checked 2026-09-18; recheck when operational guidance changes.
- ISO/IEC/IEEE 42010:2022 remains current from prior check; DIS 42024 remains CHANGE WATCH.

## Next work
Return to Balance Loop. A006 removes the main untouched Architecture decision-governance boundary at first professional level. Do not deepen Architecture merely for symmetry. Strong independent candidates are `M005` cross-platform portability/divergence, `Q004` mutation sensitivity/search-strength comparison, or an A006 executable governance checker only if its cross-track leverage outranks those gaps. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK environment becomes available.
