# Architecture Specialist Status

Track: Software Architecture & Design  
Prefix: `A###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-16

## Current evidence

### A001 — Information hiding, cohesion, coupling and change pressure
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Positive change-locality evidence, over-abstraction counterexample, and exact-ref LogMate transfer are preserved in `research/architecture/A001_information_hiding_change_pressure.md`.

### A002 — Dependency direction, state ownership and derived projections
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Ownership failure + materially different dependency-structure comparison are preserved in `research/architecture/A002_dependency_direction_state_ownership.md` and its fixtures.

### A003 — Interfaces, contracts, invariants and API evolution
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.**

Canonical: `research/architecture/A003_interfaces_contracts_api_evolution.md`  
Fixtures: `research/architecture/fixtures/A003_contract_evolution.py`, `research/architecture/fixtures/A003_compatibility_matrix.py`

Established with executable failure/alternative evidence:
- same method signature can break retained consumers through changed meaning or strengthened precondition;
- provider/consumer compatibility is relational, not a property of change syntax alone;
- weaker precondition and stronger postcondition variants preserved the bounded old consumer contract;
- stronger precondition and weaker postcondition variants broke it;
- a replacement that expanded reachable state to negative balance violated a retained invariant;
- an additive JSON field broke a strict retained consumer, falsifying the universal claim that additive changes are inherently non-breaking;
- prior consumer expectations/invariants provide the compatibility oracle; replacement behavior does not define its own correctness.

Primary sources checked: Eiffel Design by Contract documentation and Liskov/Wing 1994 behavioral-subtyping paper. Evidence limit remains synchronous Python/JSON; no Dart/Flutter, ABI, persisted-schema, network-protocol, or production compatibility claim.

## Queue
- `A001` — substantial Foundation block complete.
- `A002` — substantial Foundation block complete; concurrency intentionally deferred.
- `A003` — substantial Foundation block complete; product transfer deferred until a real evolution decision exists.
- `A004` — patterns and misuse.
- `A005` — refactoring/technical debt/evolutionary architecture.
- `A006` — ADRs/evidence-preserving decisions.

## Gate assessment
Architecture Stage 1 remains **NOT PASS**. A001-A003 now cover change pressure/information hiding, ownership/dependency direction, semantic contracts/invariants, failures, alternatives, and exact-ref transfer in A001. The remaining Foundation roadmap gap is architecture-vs-design-vs-implementation plus refactoring/technical-debt fundamentals; A004 pattern catalog depth is not itself a Foundation prerequisite and should not be used to delay more urgent cross-track work.

## HANDOFFS
- **Data:** D003 should distinguish schema shape from semantic compatibility and build old/new reader-writer matrices.
- **Quality:** retain prior consumer contracts as independent compatibility oracles; include invariants/failure semantics.
- **Mobile:** plugin/platform evolution requires behavior/failure evidence in addition to Dart signatures.
- **Systems:** release/versioning evidence must name compatibility dimension and rollback expectations.

## Next work
Return to Balance Loop rather than extending A003. F001 direct Dart/Flutter execution remains toolchain-blocked. Strong independent candidates are `M001` using official source/model evidence without pretending runtime validation, `S001` trust/resource/build boundaries, or Architecture Foundation closure work on architecture-vs-design/refactoring if its prerequisite leverage wins the comparison.
