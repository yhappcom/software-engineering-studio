# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F004 first synchronization block complete |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated Foundation block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two blocks + D004 first + D005 two + D006 first block |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### F004 — scheduling, synchronization and circular-wait progress hazards
Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`  
Fixture: `research/foundations/fixtures/F004_lock_order_deadlock.py`

Executable bounded evidence (Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41):
- barrier-controlled workers each held one lock while probing the lock held by the other; both second-lock probes returned false while both first locks remained held;
- the fixture uses non-blocking probes so it exposes the circular-wait precondition without hanging the evidence runner;
- a comparison where every worker acquired A then B let both workers complete;
- root cause is inconsistent multi-lock acquisition order, not a defective lock primitive;
- mutual exclusion, ordering and progress are distinct properties: `lock present` or `no data race` does not establish global concurrency correctness;
- current Dart sources establish isolate-local memory/message-passing semantics, but the CPython shared-memory fixture is explicitly not Dart/Flutter runtime validation.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **F004:** first synchronization/progress block with circular-wait failure model and lock-order alternative.
- **D001-D006:** authority/durability through first replication/idempotency/conflict evidence retained.
- **Q001-Q003:** oracle/reproducibility, test-level boundaries, and first schedule-dependent concurrency/flakiness evidence.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context rechecked: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. F004 is a prerequisite transfer candidate for future sync/background/native-plugin work; no LogMate concurrency defect is inferred. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Foundations:** continue F004 only while signaling/liveness mechanics remain coherent; F005 async/event-loop/cancellation is the next high-leverage prerequisite.
- **Architecture:** synchronization controls must follow explicit state ownership/invariants; locks do not repair ambiguous ownership.
- **Mobile:** CPython lock evidence must not be transferred to Dart isolates; exact isolate/platform-thread/plugin boundaries require separate runtime evidence.
- **Data:** D006 should distinguish ordering, progress and convergence, and test explicit event-order matrices.
- **Quality:** Q003 should classify no-progress/deadlock separately from wrong-result races and use bounded probes/timeouts rather than indefinite hangs.
- **Systems:** runtime/build/environment identity remains part of concurrency reproduction evidence.
- **Design Studio:** recent destructive-concurrency research is adjacent at interaction-semantics level; no Design canonical files changed.
- **Web Manager:** recent PWA trust work does not alter this lock-level mechanism; browser/service-worker transfer remains separate.
- **Marketing Manager:** not materially relevant to this block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

F004 now supplies the first missing scheduling/synchronization prerequisite exposed by Q003/D006. Strong next candidates:
1. continue `F004` with condition/signaling and bounded liveness/missed-notification evidence if a deterministic mechanism-revealing fixture is available;
2. `F005` async/event-loop/futures/cancellation — highest Dart/Flutter + D006 cross-track leverage after the first F004 block;
3. continue Q003 with explicit schedule exploration/harness-vs-SUT flake isolation after Foundations vocabulary deepens;
4. D006 reordered delivery/tombstone after F004/F005 ordering discipline is stronger.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
