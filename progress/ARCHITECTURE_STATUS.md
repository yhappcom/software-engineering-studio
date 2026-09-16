# Architecture Specialist Status

Track: Software Architecture & Design  
Prefix: `A###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-16

## Mission
Build judgment about boundaries, ownership, dependency direction, modularity, interfaces, state, change pressure, maintainability, and architectural evolution without pattern cargo culting.

## Current evidence

### A001 — Information hiding, cohesion, coupling and change pressure
Status: **SUBSTANTIAL FOUNDATION BLOCK COMPLETE**

Canonical: `research/architecture/A001_information_hiding_change_pressure.md`
Fixtures:
- `research/architecture/fixtures/A001_change_locality.py`
- `research/architecture/fixtures/A001_abstraction_cost.py`

A001 established both positive change-locality evidence and a deliberate over-abstraction counterexample, plus exact-ref LogMate transfer. Core rule: a boundary must earn indirection by owning volatile knowledge, policy, substitution, trust/runtime or consistency concerns.

### A002 — Dependency direction, state ownership and derived projections
Status: **IN STUDY — first integrated source/model + executable failure evidence**

Canonical: `research/architecture/A002_dependency_direction_state_ownership.md`
Fixture: `research/architecture/fixtures/A002_state_ownership.py`

Established:
- call direction, data-flow direction and architectural dependency/uses relationships must not be collapsed into one concept;
- state architecture must name authority, mutation authority, and projection/cache ownership separately;
- a derived copy can be legitimate without being an independent writer;
- multiple writers require explicit reconciliation semantics or they create accidental inconsistency;
- dependency direction should protect semantic policy/invariants without forcing volatile UI/storage/vendor representation to become co-owner of domain state.

Executable evidence (Python 3.13.5 / Linux):
- authoritative flights A=60 and B=90 produced total 150;
- a deliberate UI-style direct mutation of the derived projection changed displayed total to 210 while authority remained 150;
- rebuilding from authority erased that unauthorized mutation and restored 150;
- routing A→120 through the Ledger incremented authority revision, stale projection read was rejected, refresh then produced 210 consistently in both authority-derived calculation and projection.

Root cause: the bad path created a second mutation authority for one semantic fact. This failure required no database, network or concurrency, demonstrating that ownership errors precede distributed-system complexity.

Evidence limit: synchronous in-memory fixture only; no Flutter state library, persistence durability, concurrency, process death or sync behavior is inferred.

## Exact-ref product context — LogMate
Prior evidence identity retained:
`yhappcom/logmate → commit b551ce434ad72b1895033e0f3617c73b026d40ea → app version 1.0.0+1 → 2026-09-16`.

At that ref local ledger/persistence and canonical FlightRecord/calculation linkage were not implemented. A002 therefore supplies a future design constraint, not a claim about current implementation: canonical flight mutation authority should be named before totals/search/import-preview/sync projections are introduced.

## Initial queue
- `A001` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE**.
- `A002` — **IN STUDY** — ownership/second-writer failure evidence complete; materially different dependency-structure comparison still open.
- `A003` — Interfaces/contracts, invariants and API evolution.
- `A004` — Architectural patterns: what problem each solves, costs, failure modes and misuse.
- `A005` — Refactoring, technical debt and evolutionary architecture.
- `A006` — Architecture decision records and evidence-preserving design decisions.

## Gate requirement
Foundation PASS requires comparison of materially different structures, failure/maintenance analysis, explicit boundary reasoning, interface/dependency-direction evidence, and executable or product-structure validation where applicable.

Architecture Stage 1 remains **NOT PASS**. A002 still needs a dependency-structure alternative comparison; A003 remains required for interface/contract evolution.

## Dependencies / handoffs
- **Data:** D001 authority semantics are now architecture-visible; D002–D006 should preserve mutation authority versus derived-copy distinction.
- **Quality:** test bypassed mutation authority deliberately and used an independently derived total oracle; future state tests should include stale/rebuild paths.
- **Mobile:** Flutter state containers must be classified by authority/lifecycle role rather than automatically called sources of truth.
- **Systems:** trust/security boundaries may further restrict mutation authority; not yet validated.
- **Design Studio:** saved/synced/recovery presentation states may be projections of distinct engineering authorities and must not be collapsed for implementation convenience.

## Next work
Continue A002 while its professional boundary is incomplete: compare materially different dependency structures and dependency inversion/interface placement without pattern-first assumptions. Do not add concurrency/multi-writer sync experiments until Foundations/Data prerequisites support those claims.
