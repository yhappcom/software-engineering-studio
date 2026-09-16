# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-16  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN |
| Architecture | Stage 1 IN STUDY — A001 substantial; A002 ownership + dependency comparison substantial |
| Mobile | Stage 1 READY |
| Data | Stage 1 IN STUDY — D001 substantial first block |
| Quality | Stage 1 IN STUDY — Q001 substantial first block |
| Systems | Stage 1 READY |

No specialist has passed Foundation.

## Meaningful new evidence

### F001 execution gap rechecked
Current execution environment again exposes Python 3.13.5 but no `dart` or `flutter`. Direct Dart JIT/AOT and Flutter runtime validation remain OPEN; no substitute evidence was fabricated.

### A002 — Dependency Direction, State Ownership & Derived Projections
Canonical: `research/architecture/A002_dependency_direction_state_ownership.md`

A002 now has two materially different executable evidence blocks:
1. **ownership failure:** writable derived projection diverged to 210 while authority remained 150; rebuild erased the unauthorized mutation; authority mutation + revision invalidation rejected stale state then restored consistent 210.
2. **dependency-structure alternative:** a block-time summary policy was tested against a settings mechanism replacement. Direct policy→concrete settings dependency required policy code to change when file/string API became remote/boolean API. A policy-owned semantic `UnitPreference` contract kept the summary policy unchanged; only the detail adapter changed. Both designs were behavior-matched by the same exact-output oracle.

Synthesis: dependency inversion is useful when a stable semantic policy must survive an independently changing detail. Dependency injection/interface presence alone is not evidence; A001's over-abstraction counterexample remains the limiting case.

Evidence limit: Python synchronous fixture only; no Flutter, persistence, concurrency, network, lifecycle or production claim.

## Cross-track handoffs
- **Data:** persistence/cache/sync interfaces should express semantic authority needs rather than vendor DTO/schema shape where possible.
- **Quality:** test a boundary with a materially different implementation/mechanism; mockability alone does not prove architectural value.
- **Mobile:** DI framework wiring must be separated from dependency inversion and state authority.
- **LogMate:** local ledger remains unimplemented at retained exact ref `b551ce434ad72b1895033e0f3617c73b026d40ea`, app `1.0.0+1`; do not prescribe generic Repository/Service layering before concrete ownership/variation exists.

## Current Balance Loop
Architecture remains high leverage because A002's professional boundary has now reached the contract question: a boundary can localize mechanism change, but its semantic obligations, invariants and compatibility under evolution are not yet established. Therefore **A003 — Interfaces, Contracts, Invariants & API Evolution** is the strongest coherent continuation.

M001 remains high product leverage but direct runtime evidence is still toolchain-blocked. S001 remains the strongest independent alternative if A003 becomes blocked. D002/Q002 remain important but do not currently exceed A003's cross-track leverage for future LogMate ledger/import/sync and MintTap calculation/data boundaries.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
