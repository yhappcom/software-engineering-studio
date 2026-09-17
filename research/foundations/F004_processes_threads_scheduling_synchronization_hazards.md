# F004 — Processes, Threads, Scheduling, Synchronization & Concurrency Hazards

Status: **IN STUDY — two integrated Foundation blocks complete**  
Evidence date: 2026-09-17

## Problem / scope
Q003 reproduced a shared-state lost update and D006 exposed order-sensitive synchronization semantics. Foundations therefore needs a precise model for execution agents, scheduling, synchronization, mutual exclusion, signaling and liveness. This study now covers lock-order/circular-wait mechanics plus condition-variable predicate/signaling semantics; async/event-loop semantics remain F005.

## SOURCE
- Python 3.13 `threading` docs: primitive `Lock` has locked/unlocked states; `acquire()` may block; when multiple waiters exist, which waiter proceeds is not defined; lock operations are atomic. https://docs.python.org/3.13/library/threading.html#lock-objects
- Python 3.13 `Condition` docs: a condition is associated with a lock; `wait()` releases the lock and later reacquires it; `notify()` is a no-op if nobody is waiting; the normal pattern is to protect shared state and repeatedly test the application predicate; `wait_for(predicate)` automates that loop. https://docs.python.org/3.13/library/threading.html#condition-objects
- Dart current concurrency documentation: Dart code runs in isolates; each isolate has its own memory and a single thread running an event loop; isolates communicate by message passing rather than shared mutable state. https://dart.dev/language/concurrency
- Dart `dart:isolate` API describes isolates as independent workers that do not share memory and communicate via messages. https://api.dart.dev/dart-isolate/

## SYNTHESIS — mechanism model
Keep these concepts distinct:

`process/execution context → schedulable execution agent → shared or isolated state → synchronization primitive/protocol → predicate/state transition → notification/wakeup → ordering/progress properties → observed result`.

- **Mutual exclusion** answers whether more than one participant may enter a protected critical region simultaneously.
- **Ordering** answers what observations/actions must precede others under the chosen synchronization protocol.
- **Progress** asks whether participants can eventually proceed. Correct exclusion does not itself prove progress.
- **Predicate/state** is the semantic condition the application cares about; **notification** is only a coordination event that may cause a waiter to re-check that state.
- A race/lost update and a deadlock are different failure classes: the former can produce an incorrect state while work continues; the latter can prevent progress even though each lock individually behaves correctly.
- A scheduler choosing some runnable thread is not an application-level fairness guarantee. Python explicitly leaves lock-waiter selection undefined.

## VALIDATION 1 — executable circular-wait boundary
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

### ORACLE / OBSERVATION
Expected circular result is exactly `[(T1, False), (T2, False)]`; ordered alternative must record both workers. Observed:

```text
python 3.13.5 platform Linux-6.18.44-x86_64-with-glibc2.41
circular_probe [('T1', False), ('T2', False)]
ordered_locking ['T1', 'T2']
PASS
```

### DEBUG / ROOT CAUSE
The locks are not defective. The progress hazard is inconsistent multi-lock acquisition order: T1 owns A while requesting B; T2 owns B while requesting A. Blocking indefinitely at the second acquisition would create a wait cycle. Non-blocking probes expose that state without hanging the validation runner.

### ALTERNATIVE
Both workers acquire A then B. Contention remains, but the bounded two-lock cycle is structurally absent.

## VALIDATION 2 — notification is not durable state
Canonical fixture: `research/foundations/fixtures/F004_condition_predicate_signaling.py`

Environment actually executed:
- Python 3.13.5
- Linux 6.18.44 x86_64
- glibc 2.41

### CLAIM
A condition notification that occurs before a waiter exists is not a durable record that the application predicate became true; correctness must be based on protected shared state/predicate rather than assuming a past notification will be delivered to a future waiter.

### SPEC / PROPERTY
The producer sets `ready=True` while holding the condition lock and calls `notify()` before the consumer starts. The failure variant treats later `wait()` return as the evidence of readiness. The alternative calls `wait_for(lambda: ready)` so the already-true predicate can satisfy immediately.

### ORACLE
- Failure variant must show `notified=False` after the bounded timeout while `ready_after_timeout=True`.
- Predicate alternative must show `predicate_satisfied=True` and `ready=True`.

### OBSERVATION
```text
python 3.13.5 platform Linux-6.18.44-x86_64-with-glibc2.41
notification_as_state {'notified': False, 'ready_after_timeout': True}
predicate_state {'predicate_satisfied': True, 'ready': True}
PASS
```

### DEBUG / ROOT CAUSE
`notify()` does not queue a durable future entitlement for a thread that is not yet waiting. In the failure variant the semantic state transition happened successfully, but the consumer incorrectly used a later wakeup event as the source of truth. The timeout exposes the liveness symptom; it does not cause the defect. The alternative couples predicate inspection and waiting under the same condition lock, matching the documented condition-variable protocol.

### ALTERNATIVE
Protect the state transition and predicate inspection with the condition's lock, and wait on the predicate (`while not predicate: wait()` or `wait_for`) rather than interpreting notification itself as state.

### EVIDENCE LIMIT
This is a bounded CPython condition-variable fixture. It does not prove scheduler fairness, starvation freedom, general happens-before/memory-model rules, process-shared synchronization, Dart/Flutter behavior, distributed message durability, or that every notification loss is a bug. Some event APIs intentionally define edge-triggered semantics; the application contract decides whether state or event semantics are required.

## CONTRADICTION / correction to simplistic rules
- `lock present → thread safe` is false as a universal rule. Multiple individually correct locks can still compose into a progress failure.
- `no data race → concurrency correct` is false. Deadlock/livelock/starvation are separate dimensions.
- `notify happened → future waiter will observe it` is false for Python `Condition`; notification is not persisted for absent waiters.
- `wakeup → predicate is true` is unsafe as a general condition-variable rule; the documented pattern re-checks the predicate.
- `Dart uses isolates → concurrency problems disappear` is too broad. Dart's isolate model removes ordinary shared-memory data races between isolates, but message ordering, async interleavings, protocol liveness, duplicate/reordered distributed events and external-resource races remain separate concerns. Direct Dart runtime validation is still OPEN.

## TRANSFER VALIDATION / project boundary
Retained product context: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`.

No LogMate concurrency defect is inferred. F004 is a transfer prerequisite for future sync/background/native-plugin work. In particular, a sync/UI protocol should not confuse an ephemeral wakeup/event with the durable pending/confirmed/conflicted state it is meant to signal.

## RELATED DOMAIN CHECK
- Foundations: F001 process/runtime boundaries reused; direct Dart/Flutter execution remains OPEN.
- Architecture: synchronization cannot repair ambiguous state ownership; predicates must derive from an owned invariant/state contract.
- Mobile: Flutter/Dart isolate, event-loop and native-thread boundaries require separate runtime validation.
- Data: D006 duplicate/reorder/conflict work should distinguish durable operation/state from notification/ack/wakeup events.
- Quality: Q003 event-order tests should distinguish wrong-state races, missed signaling and no-progress failures; bounded timeouts are evidence instruments, not root causes.
- Systems: runtime/platform identity affects concurrency evidence; no new security/performance decision is made here.
- Design Studio: interaction state may need to expose durable pending/confirmed/conflicted semantics rather than transient event receipt; no Design canonical files changed.
- Web Manager: browser/service-worker event delivery has different semantics and requires separate transfer evidence.
- Marketing Manager: not materially relevant to this mechanism block.
- Product: retained LogMate exact-ref context only; no current implementation claim is made.

## OPEN / VALIDATION
- direct Dart isolate/message execution and Flutter runtime evidence;
- F004: starvation/fairness boundaries and process-vs-thread isolation comparison remain open;
- F005: event loop, futures, streams, cancellation and async liveness;
- D006: explicit duplicate/reorder/delete event matrices after ordering/async foundations deepen.

## HANDOFFS
- **Quality / Q003:** add missed-signal/state-vs-event misuse as a failure class; preserve predicate/state and event trace separately.
- **Data / D006:** do not model ACK/notification as durable operation state; define which state survives delayed, duplicated, absent or reordered signaling.
- **Architecture / A002-A003:** synchronization predicate belongs to an explicit state owner and semantic contract; notification mechanism must not silently become authority.
- **Mobile:** do not transfer CPython condition behavior to Dart isolates/event loops; validate the exact async/native primitive used by the product.
