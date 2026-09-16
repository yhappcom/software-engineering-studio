# Architecture Specialist Status

Track: Software Architecture & Design  
Prefix: `A###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-16

## Current evidence

### A001 — Information hiding, cohesion, coupling and change pressure
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Positive change-locality evidence, over-abstraction counterexample, and exact-ref LogMate transfer are preserved in `research/architecture/A001_information_hiding_change_pressure.md`.

### A002 — Dependency direction, state ownership and derived projections
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Ownership failure + materially different dependency-structure comparison are preserved in `research/architecture/A002_dependency_direction_state_ownership.md` and its two fixtures.

### A003 — Interfaces, contracts, invariants and API evolution
**IN STUDY — first semantic compatibility/failure block complete.**

Canonical: `research/architecture/A003_interfaces_contracts_api_evolution.md`  
Fixture: `research/architecture/fixtures/A003_contract_evolution.py`

Established:
- interface syntax/signature is only part of a contract;
- operational semantic contract includes accepted inputs/preconditions, returned meaning/postconditions, state transition, invariants, failure semantics and observable side effects where relevant;
- same method name/signature was executable-tested with a silent meaning change from block time to airborne time: old consumer oracle expected 150, replacement returned 125;
- a same-signature strengthened precondition rejected empty input that the prior contract accepted as total 0;
- additive alternative preserved the old `total_minutes` semantic contract and exposed airborne time under a distinct operation;
- root cause in both failures was provider-side semantic contract drift relative to retained consumer expectations, not call-shape incompatibility.

Primary method source checked: current Eiffel Design by Contract documentation, 2026-09-16.

Evidence limit: Python synchronous fixture. No Dart/Flutter, ABI, persisted-schema, network-protocol, mobile, or production compatibility claim.

## Queue
- `A001` — substantial Foundation block complete.
- `A002` — substantial Foundation block complete; concurrency intentionally deferred.
- `A003` — **IN STUDY** — semantic break + strengthened-precondition failures complete; compatibility matrix/invariant evolution/additive-breaking counterexample remain OPEN.
- `A004` — patterns and misuse.
- `A005` — refactoring/technical debt/evolutionary architecture.
- `A006` — ADRs/evidence-preserving decisions.

## Gate requirement
Architecture Stage 1 remains **NOT PASS**. A001/A002 establish change pressure, ownership, failure, alternative structure and dependency direction. A003 now establishes that syntactic compatibility is not semantic compatibility, but its professional boundary still needs provider/consumer compatibility reasoning across pre/postconditions/invariants and a counterexample to naive additive-safety claims.

## HANDOFFS
- **Data:** D003 should distinguish schema/representation compatibility from semantic invariants and retained reader/writer contracts.
- **Quality:** compatibility tests should retain prior consumer expectations as independent oracles; compilation success is insufficient.
- **Mobile:** plugin/platform evolution must preserve or explicitly revise behavior/failure semantics, not only Dart signatures.
- **Systems:** release/versioning evidence should name the compatibility dimension claimed: source, binary, data/schema, protocol, or behavioral.

## Next work
Continue A003 while its professional boundary is incomplete. Build the provider/consumer compatibility matrix and executable invariant/additive-change counterexamples. If trustworthy Dart/Flutter execution becomes available first, F001/M001 may preempt under the Balance Loop.
