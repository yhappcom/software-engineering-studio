# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F004 two synchronization blocks complete |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated Foundation block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two blocks + D004 first + D005 two + D006 first block |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### F004 — condition predicate vs notification semantics
Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`  
Fixture: `research/foundations/fixtures/F004_condition_predicate_signaling.py`

Executable bounded evidence (Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41):
- producer set `ready=True` and called `Condition.notify()` before any waiter existed;
- a later raw `wait(timeout)` returned false even though `ready` remained true, reproducing the failure caused by treating notification receipt as durable application state;
- the comparison using `wait_for(lambda: ready)` returned true immediately because the protected predicate was already satisfied;
- root cause is state/event conflation: notification is a coordination event, while the application predicate is the semantic condition;
- Python's current Condition documentation explicitly states `notify()` is a no-op when no threads are waiting and documents predicate rechecking/`wait_for` as the normal protocol;
- this CPython evidence is not transferred to Dart/Flutter runtime behavior.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **F004:** lock-order/circular-wait block plus condition predicate/signaling block.
- **D001-D006:** authority/durability through first replication/idempotency/conflict evidence retained.
- **Q001-Q003:** oracle/reproducibility, test-level boundaries, and first schedule-dependent concurrency/flakiness evidence.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. F004 is a prerequisite transfer candidate for future sync/background/native-plugin work; no LogMate concurrency defect is inferred. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Foundations:** F004 has coherent lock-order and signaling/predicate evidence; F005 async/event-loop/futures/cancellation now has higher cross-track leverage than extending F004 into fairness detail.
- **Architecture:** synchronization predicates require explicit state ownership/invariants; notification mechanisms must not become accidental authority.
- **Mobile:** CPython Condition evidence must not be transferred to Dart isolates/event loops; exact async/platform primitive requires separate runtime evidence.
- **Data:** D006 should distinguish durable operation/confirmed/pending/conflicted state from ACK/notification/wakeup events.
- **Quality:** Q003 should add missed-signal/state-vs-event misuse and preserve predicate state plus event trace; bounded timeout is an observation tool, not root cause.
- **Systems:** runtime/build/environment identity remains part of concurrency reproduction evidence.
- **Design Studio:** future interaction semantics may need durable pending/confirmed/conflicted state rather than transient event receipt; no Design canonical files changed.
- **Web Manager:** browser/service-worker event delivery is a separate transfer boundary.
- **Marketing Manager:** not materially relevant to this block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

F004 now covers two high-value shared-memory synchronization boundaries: lock ordering/progress and predicate/signaling semantics. Strong next candidates:
1. `F005` async/event-loop/futures/cancellation — highest Dart/Flutter + D006 + Q003 prerequisite leverage;
2. continue Q003 with explicit schedule/event-order exploration after F005 supplies async vocabulary;
3. D006 reordered delivery/tombstone after F005 ordering/cancellation discipline;
4. F004 starvation/fairness/process-vs-thread only when a stronger executable boundary justifies returning.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
