# Architecture Specialist Status

Track: Software Architecture & Design  
Prefix: `A###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-17

## Current evidence

### A001 — Information hiding, cohesion, coupling and change pressure
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Positive change-locality evidence, over-abstraction counterexample, and exact-ref LogMate transfer are preserved in `research/architecture/A001_information_hiding_change_pressure.md`.

### A002 — Dependency direction, state ownership and derived projections
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Ownership failure + materially different dependency-structure comparison are preserved in `research/architecture/A002_dependency_direction_state_ownership.md` and its fixtures.

### A003 — Interfaces, contracts, invariants and API evolution
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Canonical: `research/architecture/A003_interfaces_contracts_api_evolution.md`. Established semantic compatibility, retained-consumer oracles, stronger/weaker pre/postcondition effects and additive-shape compatibility failure in bounded executable evidence.

### A005 — Architecture/design/implementation, refactoring and technical-debt boundaries
**IN STUDY — first integrated Foundation block complete.**  
Canonical: `research/architecture/A005_refactoring_technical_debt_evolutionary_boundaries.md`  
Fixture: `research/architecture/fixtures/A005_refactoring_behavior_boundary.py`

Established:
- architecture is the significant structures/relations/properties/decisions needed to reason about system qualities; an architecture description is not the architecture itself;
- architecture/design/implementation are reasoning scopes, not labels mechanically assigned by file/class size;
- refactoring is behavior-preserving restructuring relative to an explicit observer set, not arbitrary cleanup/rewrite;
- Python 3.13.5/Linux executable evidence preserved all three declared behaviors across an internal split refactoring, while a deliberate clamp mutant changed negative-input failure semantics and was detected;
- technical debt is modeled as a concrete contingent future-change liability, not a synonym for bug, smell, old code or aesthetic dislike;
- debt claims should name artifact/decision, short-term context/benefit, plausible future change, extra cost/risk, remediation and uncertainty.

Current primary sources: ISO/IEC/IEEE 42010:2022, CMU SEI architecture/technical-debt material, and Fowler's precise refactoring definition. ISO/IEC/IEEE DIS 42024 remains under development and is CHANGE WATCH rather than adopted authority.

## Queue
- `A001` — substantial Foundation block complete.
- `A002` — substantial Foundation block complete; concurrency intentionally deferred.
- `A003` — substantial Foundation block complete; product transfer deferred until a real evolution decision exists.
- `A004` — patterns and misuse; useful but not required as a pattern catalog for Foundation closure.
- `A005` — **IN STUDY / first integrated Foundation block complete**; repeated-change/evolution and Dart/Flutter/product transfer OPEN.
- `A006` — ADRs/evidence-preserving decisions.

## Gate assessment
Architecture Stage 1 remains **NOT PASS**. A001-A003 plus A005 now cover the roadmap's principal Foundation concepts: information hiding/change pressure, ownership/dependency direction, contracts/invariants, architecture-vs-design-vs-implementation, and refactoring/technical-debt fundamentals. Reading alone did not close the gap: A005 includes a behavior-preservation oracle and deliberate semantic-change mutant. Broader evolutionary evidence, transfer, and remaining A004/A006 professional boundaries remain open.

## HANDOFFS
- **Data:** persisted schema/data evolution is not ordinary internal refactoring when old readers/writers/data are observers.
- **Quality:** refactoring validation should declare observer sets and use independent contract oracles; green tests alone do not prove preservation.
- **Mobile:** lifecycle/plugin/platform behavior can be externally relevant even when Dart-facing structure looks internal.
- **Systems:** performance/security/artifact properties belong in the observer set when contractual/risk-significant; debt can exist in build/release infrastructure too.
- **Product teams:** technical-debt backlog items should identify a concrete future-change liability and consequence rather than generic cleanup.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter transfer remains blocked by unavailable `dart`/`flutter` executables.
- ISO/IEC/IEEE 42010:2022 is current as checked 2026-09-17; DIS 42024 is under development.
- A005 repeated-change/evolution evidence and exact-ref product debt transfer remain OPEN.

## Next work
Return to Balance Loop. The principal Architecture Foundation conceptual gap is now materially closed at first executable level, so do not extend A005 merely for continuity. Untouched `S002` threat modeling/least privilege/secrets now has stronger risk/reuse leverage; `S003` performance/profiling and Mobile M003 remain strong candidates. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK environment becomes available.
