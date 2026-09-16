# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-16  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution still OPEN |
| Architecture | Stage 1 IN STUDY — A001 substantial block complete; A002 first failure evidence added |
| Mobile | Stage 1 READY |
| Data | Stage 1 IN STUDY — D001 substantial first block complete |
| Quality | Stage 1 IN STUDY — Q001 substantial first block complete |
| Systems | Stage 1 READY |

No specialist has passed Foundation.

## Meaningful integrated evidence

### F001
Execution environment was checked again on 2026-09-16: no `dart` or `flutter` executable is available; Python 3.13.5 is available. Direct Dart JIT/AOT and Flutter runtime validation therefore remain OPEN. No simulated runtime evidence was substituted.

### A001
Information hiding/change pressure now has positive change-locality evidence, an over-abstraction counterexample, and exact-ref LogMate transfer. Canonical: `research/architecture/A001_information_hiding_change_pressure.md`.

### A002 — Dependency Direction, State Ownership & Derived Projections
Canonical: `research/architecture/A002_dependency_direction_state_ownership.md`  
Fixture: `research/architecture/fixtures/A002_state_ownership.py`

New evidence:
- Parnas's `uses` structure is adopted to distinguish specification-relevant dependency from mere invocation;
- call direction, data-flow direction and architectural dependency direction are explicitly separated;
- authority, mutation authority, and projection/cache ownership are treated as distinct architectural contracts;
- deliberate second-writer fixture: authoritative Flight rows totaled 150, while direct mutation of a derived projection reported 210 without changing authority;
- rebuilding from authority erased the unauthorized derived mutation and returned 150;
- routing the edit through the Ledger changed authority revision, stale projection read was rejected, and refresh restored consistent 210.

Root cause: a derived representation was allowed to act as a second mutation authority for one semantic fact. This demonstrates an ownership failure without needing concurrency, networking or persistence complexity.

Evidence limit: synchronous in-memory Python fixture only. It does not validate Flutter state-management libraries, persistence durability, process death, concurrent writers, or synchronization.

## Cross-track synthesis / handoffs
- **D001 → A002:** logical source-of-truth becomes explicit authority/mutation/projection ownership in architecture.
- **Q001 → A002:** the total oracle is independently derived from authoritative rows; stale-state failure is deliberate rather than inferred from a happy path.
- **A002 → Data:** future cache/sync/index designs must say whether copies are derived or intentional writers and define reconciliation if multi-writer.
- **A002 → Mobile:** Flutter provider/store/controller objects must not automatically be called sources of truth; their authority and lifecycle role must be established.
- **A002 → LogMate:** before local ledger implementation, classify canonical FlightRecord, totals/search, import preview and sync metadata by authority/staged/derived role. Product files were not changed.

## Product context
Prior LogMate evidence identity remains `yhappcom/logmate → b551ce434ad72b1895033e0f3617c73b026d40ea → app 1.0.0+1 → 2026-09-16`. Local ledger/persistence was not implemented at that ref, so A002 is a transferable constraint rather than a claim about current product behavior.

## Current Balance Loop
Continue **A002** rather than rotate. Its professional boundary is incomplete: next evidence should compare materially different dependency structures and interface placement, including when dependency inversion protects policy versus when it merely relocates indirection. Concurrency/event-order and intentional multi-writer sync remain deferred until F004/F005/D006 prerequisites.

`M001` remains high leverage but direct runtime evidence is still toolchain-blocked. `S001` remains the strongest independent alternative if Architecture becomes blocked.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
