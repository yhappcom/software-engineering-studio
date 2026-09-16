# F004 — Processes, Threads, Scheduling, Synchronization & Concurrency Hazards

Status: **IN STUDY — first integrated Foundation block complete**  
Evidence date: 2026-09-17

## Problem / scope
Q003 reproduced a shared-state lost update and D006 exposed order-sensitive synchronization semantics. Before extending either study, Foundations needs a precise model for execution agents, scheduling, synchronization, mutual exclusion and deadlock. This block focuses on thread/lock mechanics and circular wait; async/event-loop semantics remain F005.

## SOURCE
- Python 3.13 `threading` docs: primitive `Lock` has locked/unlocked states; `acquire()` may block; when multiple waiters exist, which waiter proceeds is not defined; lock operations are atomic. https://docs.python.org/3.13/library/threading.html#lock-objects
- The same Python docs warn that unmatched `RLock` acquire/release pairs can lead to deadlock. https://docs.python.org/3.13/library/threading.html#rlock-objects
- Dart current concurrency documentation: Dart code runs in isolates; each isolate has its own memory and a single thread running an event loop; isolates communicate by message passing rather than shared mutable state. https://dart.dev/language/concurrency
- Dart `dart:isolate` API describes isolates as independent workers that do not share memory and communicate via messages. https://api.dart.dev/dart-isolate/

## SYNTHESIS — mechanism model
Keep these concepts distinct:

`process/execution context → schedulable execution agent → shared or isolated state → synchronization primitive/protocol → ordering/progress properties → observed result`.

- **Mutual exclusion** answers whether more than one participant may enter a protected critical region simultaneously.
- **Ordering** answers what observations/actions must precede others under the chosen synchronization protocol.
- **Progress** asks whether participants can eventually proceed. Correct exclusion does not itself prove progress.
- A race/lost update and a deadlock are different failure classes: the former can produce an incorrect state while work continues; the latter can prevent progress even though each lock individually behaves correctly.
- A scheduler choosing some runnable thread is not an application-level fairness guarantee. Python explicitly leaves lock-waiter selection undefined.

## VALIDATION — executable circular-wait boundary
Canonical fixture: `research/foundations/fixtures/F004_lock_order_deadlock.py`

Environment actually executed:
- Python 3.13.5
- Linux 6.18.44 x86_64
- glibc 2.41

### CLAIM
Two workers that each hold one lock and then require the other's lock can create a circular-wait state; imposing one global acquisition order removes that circular dependency in the bounded fixture.

### SPEC / PROPERTY
- Circular probe: while T1 holds A and T2 holds B, neither may acquire the other's lock.
- Ordered alternative: both workers must complete when both acquire A then B.

### ORACLE
The fixture uses barriers so both workers retain their first lock until both non-blocking second-lock probes have observed the state. Expected circular result is exactly `[(T1, False), (T2, False)]`. Ordered alternative must record both workers as completed.

### OBSERVATION
Executed result:

```text
python 3.13.5 platform Linux-6.18.44-x86_64-with-glibc2.41
circular_probe [('T1', False), ('T2', False)]
ordered_locking ['T1', 'T2']
PASS
```

### DEBUG / ROOT CAUSE
The failure condition is not that either lock is defective. Each lock correctly excludes the other worker. The progress hazard comes from **inconsistent multi-lock acquisition order**: T1 owns A while requesting B; T2 owns B while requesting A. Blocking indefinitely at the second acquisition would create a wait cycle. The executable uses non-blocking probes specifically to expose that state without hanging the validation runner.

### ALTERNATIVE
Both workers acquire A then B. Contention remains, but the bounded two-lock cycle is structurally absent because no worker may hold B while waiting for A.

### EVIDENCE LIMIT
This fixture does **not** prove a general deadlock detector, starvation freedom, scheduler fairness, memory-model semantics, lock-free correctness, process-shared synchronization, or Dart/Flutter behavior. The use of `time.sleep()` in the ordered alternative only widens contention; correctness is defined by lock order, not the sleep.

## CONTRADICTION / correction to simplistic rules
- `lock present → thread safe` is false as a universal rule. Multiple individually correct locks can still compose into a progress failure.
- `no data race → concurrency correct` is false. Deadlock/livelock/starvation are separate dimensions.
- `Dart uses isolates → concurrency problems disappear` is too broad. Dart's isolate model removes ordinary shared-memory data races between isolates, but message ordering, async interleavings, protocol deadlocks/liveness, duplicate/reordered distributed events and external-resource races remain separate concerns. Direct Dart runtime validation is still OPEN.

## TRANSFER VALIDATION / project boundary
Retained product context rechecked 2026-09-17:
`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 (retained prior evidence)`.

No LogMate concurrency defect is inferred. F004 is a transfer prerequisite for future sync/background/native-plugin work, especially when implementation crosses isolate, platform-thread, database, network or multi-device boundaries.

## RELATED DOMAIN CHECK
- Foundations: F001 process/runtime boundaries reused; direct Dart/Flutter execution remains OPEN.
- Architecture: synchronization cannot repair ambiguous state ownership; A002 ownership/invariant boundaries remain prerequisite context.
- Mobile: Flutter/Dart isolate and platform/native boundaries require separate runtime validation.
- Data: D006 duplicate/reorder/conflict work needs ordering/progress vocabulary from F004/F005.
- Quality: Q003 event-order tests should distinguish wrong-state races from no-progress failures.
- Systems: runtime/platform identity affects concurrency evidence; no new security/performance decision is made here.
- Design Studio: recent destructive-concurrency work is materially adjacent at interaction semantics level, but this block does not redefine its UI contracts.
- Web Manager: recent PWA trust work does not change this lock-level conclusion; browser/service-worker concurrency requires separate transfer evidence.
- Marketing Manager: not materially relevant to this mechanism block.
- Product: LogMate exact main ref rechecked; no implementation claim beyond retained version context.

## OPEN / VALIDATION
- direct Dart isolate/message execution and Flutter runtime evidence;
- F004 follow-up: condition variables/signaling, missed notification predicates, starvation/fairness boundaries, process-vs-thread isolation comparison;
- F005: event loop, futures, streams, cancellation and async liveness;
- D006: explicit duplicate/reorder/delete event matrices after ordering foundations deepen.

## HANDOFFS
- **Quality / Q003:** add no-progress/deadlock as a failure class distinct from wrong-result races; avoid tests that hang forever—use bounded probes/timeouts with preserved trace.
- **Data / D006:** model synchronization protocols as ordering + progress + state-convergence properties, not only final-state equality.
- **Mobile:** do not transfer CPython shared-memory lock behavior to Dart isolates; validate exact Flutter/Dart/native boundary when the toolchain becomes available.
