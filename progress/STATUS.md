# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated Foundation block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two blocks + D004 first + D005 two + D006 first block |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### Q003 — schedule-dependent correctness and flaky-test mechanics
Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`  
Fixture: `research/quality/fixtures/Q003_concurrency_schedule_flake.py`

Executable bounded evidence (Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41):
- two workers each performed 1,000 logical increments against a shared counter;
- deliberately split read/yield/write produced 1,000 rather than the invariant-required 2,000 in 20/20 observed runs;
- Lock-protected comparison produced 2,000 in five runs;
- root cause is lost update across a non-indivisible logical read-modify-write; injected yield widens/reproduces the schedule but is not the causal defect;
- therefore one green schedule cannot establish schedule-independent correctness, and repeated/rerun behavior must not be confused with determinism;
- D006 follow-up now has an explicit Quality requirement to exercise relevant event-order matrices and preserve event traces rather than only one happy ordering.

Current Python docs leave lock waiter selection undefined and provide explicit synchronization primitives; current pytest guidance treats ordering/shared-state/parallel effects as common flakiness sources. Evidence remains a deliberately widened CPython thread fixture, not Dart/Flutter/network/production validation.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001-D006:** authority/durability through first replication/idempotency/conflict evidence retained.
- **Q001-Q003:** oracle/reproducibility, test-level boundaries, and first schedule-dependent concurrency/flakiness evidence.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. Prior exact-ref evidence described durable ledger/configuration persistence/Sync/Backup-Export as not implemented, so D004-D006/Q003 remain transfer candidates rather than existing product defects. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Foundations:** Q003 exposes high-value F004/F005 prerequisites: scheduling/synchronization and async/event-loop mechanics should deepen before broad concurrency claims.
- **Architecture:** concurrency controls must follow explicit state ownership/invariants.
- **Mobile:** eventual lifecycle/sync validation should use controllable ordering/failure hooks rather than arbitrary sleeps where feasible.
- **Data:** D006 should test duplicate/reordered/concurrent event matrices and preserve first-failure traces.
- **Systems:** runtime/build/environment identity remains part of flake/reproduction evidence.
- **Design/Web/Marketing:** no canonical files edited; no first-block conclusion required changing their owned decisions.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

Q003 closes the previously untouched determinism/nondeterminism Foundation prerequisite at first-block depth and reveals a deeper prerequisite rather than just another Quality microtask. Strong next candidates:
1. `F004` processes/threads/scheduling/synchronization/concurrency hazards — highest prerequisite and cross-track leverage for Q003/D006;
2. `F005` async/event-loop/futures/cancellation after F004 establishes ordering/synchronization vocabulary;
3. continue Q003 with explicit schedule exploration/harness-vs-SUT flake isolation if it can be made deterministic and mechanism-revealing;
4. D006 reordered delivery/tombstone after Quality/Foundations ordering discipline is stronger.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
