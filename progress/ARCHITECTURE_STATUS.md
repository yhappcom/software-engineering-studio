# Architecture Specialist Status

Track: Software Architecture & Design  
Prefix: `A###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-16

## Mission
Build judgment about boundaries, ownership, dependency direction, modularity, interfaces, state, change pressure, maintainability, and architectural evolution without pattern cargo culting.

## Current evidence

### A001 — Information hiding, cohesion, coupling and change pressure
Status: **SUBSTANTIAL FOUNDATION BLOCK COMPLETE — A001 evidence mature enough to advance, Architecture Stage 1 not passed**

Canonical: `research/architecture/A001_information_hiding_change_pressure.md`

Fixtures:
- `research/architecture/fixtures/A001_change_locality.py`
- `research/architecture/fixtures/A001_abstraction_cost.py`

Established:
- abstraction and information hiding are related but distinct;
- useful boundaries own volatile design knowledge, real substitution, policy, trust/runtime or consistency concerns rather than merely increasing layer count;
- cohesion is better reasoned about through shared contract/change responsibility than superficial file similarity;
- harmful coupling includes duplicated knowledge of unstable representation/mechanism, not simply import count;
- Parnas-style decomposition starts from likely independent changes, not named patterns;
- D001 mutation/source-of-truth ownership and Q001 semantic test contracts provide concrete adjacent constraints;
- every boundary has carrying cost and must earn that cost with evidenced locality/ownership/substitution value.

## Executable evidence

### Positive change-locality case
A representation-change fixture preserved two semantic clients when parsing knowledge was owned behind a semantic interface. Two leaky clients that duplicated the old representation rule failed after the representation changed. Root cause: duplicated volatile representation knowledge outside its owner.

### Counterexample / over-abstraction case
Python 3.13.5 / Linux 6.18.44 x86_64 fixture compared one direct formatter with a Source → Repository → Service → Formatter → Presenter chain in a fixed single-source/single-policy scenario.

Observed:
- 5 valid samples produced identical behavior;
- direct fixture graph: 1 node / 0 declared dependency edges;
- layered fixture graph: 6 nodes / 9 declared dependency edges;
- invalid-input failure path exposed more fixture frames in the layered design;
- no independent volatility, substitution or locality benefit was demonstrated in that bounded scenario.

Evidence limit: node/edge/stack counts are not universal maintainability metrics. The fixture is evidence only that extra mechanism can exist without corresponding boundary benefit.

## Exact-ref product transfer — LogMate
Evidence identity:

`yhappcom/logmate → commit b551ce434ad72b1895033e0f3617c73b026d40ea → app version 1.0.0+1 → 2026-09-16`

Validated examples:
- `AirportLookup` owns bundled asset loading, positional JSON interpretation, semantic `Airport` construction and lookup/autocomplete policy while explicitly remaining separate from the open canonical FlightRecord airport representation. This is concrete representation/policy ownership.
- `AuthEngine` has both `FirebaseAuthEngine` and `PendingFirebaseAuthEngine`; screens consume/inject the `AuthEngine` contract instead of Firebase APIs. The boundary has evidenced substitution plus Firebase initialization/error-policy isolation.

Product limits:
- local ledger/persistence, canonical FlightRecord linkage, configuration persistence, Sync and Backup/Export remain not implemented at the inspected ref;
- therefore no future Repository/Service layering for those features is inferred or recommended from current mock/session structure.

## Initial queue
- `A001` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE** — positive + counterexample executable evidence and exact-ref LogMate transfer present.
- `A002` — Modules, layers, boundaries, dependency direction and state ownership.
- `A003` — Interfaces/contracts, invariants and API evolution.
- `A004` — Architectural patterns: what problem each solves, costs, failure modes and misuse.
- `A005` — Refactoring, technical debt and evolutionary architecture.
- `A006` — Architecture decision records and evidence-preserving design decisions.

## Gate requirement
Foundation PASS requires comparison of materially different structures, failure/maintenance analysis, explicit boundary reasoning, interface/dependency-direction evidence, and executable or product-structure validation where applicable.

A001 now supplies a strong first criterion, but **Architecture Stage 1 is not PASS**. A002/A003 are required before the track can claim a defensible foundation in state ownership, dependency direction, interface contracts and evolution.

## Dependencies / handoffs
- **Data:** future local-ledger/storage/sync boundaries should be justified by real durability/schema/migration/consistency ownership, not the Repository label.
- **Quality:** contract tests are valuable where a boundary owns semantics; avoid multiplying mocks around pass-through layers without an independent contract.
- **Mobile:** framework/platform lifecycle differences may be legitimate change boundaries and require explicit ownership plus M001/M002 evidence.
- **Systems:** Firebase/vendor/security/performance/build constraints can force or invalidate boundaries; an interface does not erase those risks.
- **Design Studio:** interaction semantics remain design-owned; implementation boundaries must not silently redefine them.

## Next work
Use the Balance Loop. A001's open counterexample/product-transfer obligations are now closed. Strong next candidates are:
1. `A002` because D001 + A001 now make state ownership/dependency direction directly testable;
2. `M001` because Flutter/mobile is high live-product leverage, but executable runtime claims remain toolchain-dependent;
3. `S001` because execution/data/quality/architecture prerequisites now exist.

Prefer the candidate with the strongest executable/source evidence opportunity rather than rotating mechanically.