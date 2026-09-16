# Architecture Specialist Status

Track: Software Architecture & Design
Prefix: `A###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-16

## Mission
Build judgment about boundaries, ownership, dependency direction, modularity, interfaces, state, change pressure, maintainability, and architectural evolution without pattern cargo culting.

## Current evidence

### A001 — Information hiding, cohesion, coupling and change pressure
Status: **IN STUDY — first integrated source/model + executable change-locality evidence**

Canonical: `research/architecture/A001_information_hiding_change_pressure.md`
Fixture: `research/architecture/fixtures/A001_change_locality.py`

Established:
- abstraction and information hiding are related but distinct;
- useful boundaries own volatile design knowledge rather than merely increasing layer count;
- cohesion is better reasoned about through shared contract/change responsibility than superficial file similarity;
- harmful coupling includes duplicated knowledge of unstable representation/mechanism, not simply import count;
- Parnas-style decomposition starts from likely independent changes, not named patterns;
- D001 mutation/source-of-truth ownership and Q001 semantic test contracts provide concrete adjacent constraints.

Executable evidence:
- a bounded representation-change fixture preserved two semantic clients when parsing knowledge was owned behind a semantic interface;
- two leaky clients that duplicated the old representation rule both failed after the representation changed;
- deliberate failure root cause: representation knowledge was duplicated outside its owner.

Evidence limit: this validates one change-locality mechanism. It does not prove that every wrapper, repository, layer, or interface improves maintainability.

## Initial queue
- `A001` — **IN STUDY** — first integrated block complete; counterexample/transfer still open.
- `A002` — Modules, layers, boundaries, dependency direction and state ownership.
- `A003` — Interfaces/contracts, invariants and API evolution.
- `A004` — Architectural patterns: what problem each solves, costs, failure modes and misuse.
- `A005` — Refactoring, technical debt and evolutionary architecture.
- `A006` — Architecture decision records and evidence-preserving design decisions.

## Gate requirement
Foundation PASS requires comparison of materially different structures, failure/maintenance analysis, explicit boundary reasoning, and executable or product-structure validation where applicable.

A001 alone is not PASS. A counterexample to needless abstraction, interface/dependency-direction evidence, and exact-ref product transfer remain open.

## Dependencies / handoffs
- Data: D001 supplies mutation authority and SSOT; storage/sync representation should not leak without reason.
- Quality: Q001 requires semantic contracts/oracles independent of hidden implementation details.
- Mobile: platform lifecycle differences may be legitimate volatile knowledge and require explicit ownership.
- Systems: security/performance/build constraints can force or invalidate boundaries.
- Design Studio: interaction semantics remain design-owned; implementation boundaries must not silently redefine them.

## Next work
Use Balance Loop. Strong next choices are continuing A001 with a deliberate over-abstraction counterexample and exact product transfer, or advancing M001/S001 if their prerequisite/evidence leverage now exceeds Architecture.