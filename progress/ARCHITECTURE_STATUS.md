# Architecture Specialist Status

Track: Software Architecture & Design
Prefix: `A###`
State: **Stage 1 — READY / NOT YET PASSED**
Last sync: 2026-09-16

## Mission
Build judgment about boundaries, ownership, dependency direction, modularity, interfaces, state, change pressure, maintainability, and architectural evolution without pattern cargo culting.

## Initial queue
- `A001` — Abstraction, information hiding, cohesion, coupling and change pressure.
- `A002` — Modules, layers, boundaries, dependency direction and state ownership.
- `A003` — Interfaces/contracts, invariants and API evolution.
- `A004` — Architectural patterns: what problem each solves, costs, failure modes and misuse.
- `A005` — Refactoring, technical debt and evolutionary architecture.
- `A006` — Architecture decision records and evidence-preserving design decisions.

## Gate requirement
Foundation PASS requires comparison of materially different structures, failure/maintenance analysis, explicit boundary reasoning, and executable or product-structure validation where applicable.

## Dependencies / handoffs
- Data supplies persistence/distribution constraints.
- Mobile supplies lifecycle/platform constraints.
- Quality tests whether boundaries are observable/testable.
- Systems supplies security/performance/delivery constraints.
- Design Studio interaction semantics may constrain state ownership and flow architecture.

## Next work
`A001` follows or may pair with `F001/D001` depending on balance-loop evidence.
