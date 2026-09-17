# F005 — Async Execution, Event Loops, Futures, Streams & Cancellation

Status: **IN STUDY — first integrated Foundation block complete**  
Evidence date: 2026-09-17

## Problem / scope
F004 established shared-memory synchronization and state-vs-notification boundaries; D006 and Q003 now need async vocabulary for ordering, timeout, cancellation and liveness. This first block focuses on event-loop/Future semantics and the professional boundary between **stopping a wait** and **stopping underlying work**.

## SOURCE
- Current Dart concurrency documentation: an isolate processes queued events one at a time through an event loop; Futures, Streams and async/await are built around that model. https://dart.dev/language/concurrency
- Current Dart asynchronous-programming documentation: an `async` function returns a Future; `await` suspends that function until the awaited Future completes while other asynchronous work can continue. https://dart.dev/language/async
- Current `Future<T>` API: a Future represents the eventual result/error of an asynchronous computation; `timeout` is described as stopping **waiting for this future** after the time limit. The API also warns that a Future may fail to ever complete. https://api.dart.dev/dart-async/Future-class.html
- Current `Future.delayed`: zero/non-positive delay completes no sooner than the next event-loop iteration, after microtasks have run. https://api.dart.dev/dart-async/Future/Future.delayed.html
- Current Stream/StreamSubscription APIs expose explicit subscription cancellation; cancellation semantics therefore belong to the operation/API contract rather than being inferred from `await`. https://api.dart.dev/dart-async/Stream-class.html
- `Socket.startConnect` returns a cancellable `ConnectionTask`, while `Socket.connect(timeout: ...)` explicitly specifies cancellation of ongoing connection attempts on its own timeout. This is evidence that cancellation is API-specific. https://api.dart.dev/dart-io/Socket-class.html

## SYNTHESIS — mechanism model
Keep these states distinct:

`operation start → Future/handle returned → caller waiting/suspended → event-loop progress → completion(value/error) OR no completion`

and, when cancellation exists:

`cancellation request → operation observes/accepts request → cleanup/rollback/resource release → cancellation completion/acknowledgement → caller-visible terminal state`.

A timeout can be a property of a **waiter** without proving termination of the underlying operation. Conversely, some concrete APIs define timeout as cancellation of their underlying activity. Therefore `timeout`, `Future completion`, `cancellation request`, `work stopped`, and `cleanup completed` are separate claims unless the exact API contract binds them together.

`await` is suspension of the async function, not automatic execution on another thread and not a generic cancellation primitive.

## VALIDATION — bounded waiter-timeout vs work-cancellation model
Canonical fixture: `research/foundations/fixtures/F005_async_timeout_cancellation_model.py`

Environment actually executed:
- Python 3.13.5
- Linux 6.18.44 x86_64
- glibc 2.41

### CLAIM
Stopping a caller's wait does not logically imply that the underlying operation stopped; cancellation needs a separate protocol/primitive when the operation contract requires it.

### SPEC / PROPERTY
Failure variant deliberately shields an underlying asyncio task from waiter timeout. Oracle requires the trace to contain `caller_timeout` followed later by `side_effect`. Alternative uses an explicit cancellation-request state observed by the operation before its side effect.

### OBSERVATION
```text
python 3.13.5 platform Linux-6.18.44-x86_64-with-glibc2.41
timeout_only ['started', 'caller_timeout', 'side_effect']
cooperative (['started', 'cancel_observed'], 'cancelled')
```

### DEBUG / ROOT CAUSE
The failure is semantic conflation, not scheduler failure: the first policy stops one observer from waiting but deliberately leaves the task alive. The later side effect proves that caller timeout was not an operation terminal state. The alternative has a distinct cancellation request and an observation point inside the operation, so the operation exits before the modeled side effect.

### ALTERNATIVE
Use an operation-specific cancellation mechanism and define what acknowledgement/cleanup means. A cooperative token is one model; Dart APIs may instead expose subscription cancellation, cancellable connection tasks, resource close/dispose, isolate termination, or no cancellation at all. Do not invent a universal token abstraction from this fixture.

### EVIDENCE LIMIT
This is CPython asyncio model evidence only. It does not establish Dart Future scheduling, microtask ordering, Flutter frame scheduling, Dart cancellation behavior, native I/O cancellation, cleanup durability, process death, or production behavior. The direct Dart/Flutter toolchain remains unavailable in the current execution environment.

## CONTRADICTION
- `await means another thread runs the operation` — false for Dart's documented event-loop model.
- `timeout means the operation was cancelled` — false as a universal rule; exact API semantics decide.
- `Future exists → operation will eventually finish` — false; Dart documents that a Future may never complete.
- `cancellation requested → cleanup finished` — unjustified without acknowledgement/terminal-state evidence.

## ENGINEERING JUDGMENT
Async APIs should document at least: operation identity, completion result/error, timeout ownership, whether cancellation exists, cancellation observation/acknowledgement, side effects that may outlive the caller, and cleanup/resource guarantees. This becomes especially important for sync retries: retrying after a local timeout while the first operation is still active can create duplicate concurrent work even when the caller thinks attempt 1 is over.

## RELATED DOMAIN CHECK
- Foundations: F004 ordering/progress and predicate-vs-event distinctions reused; F001 direct Dart/Flutter execution remains OPEN.
- Architecture: async completion/cancellation are semantic contracts, not merely implementation syntax.
- Mobile: Flutter frame/lifecycle/background and plugin-native async behavior require separate exact-runtime validation.
- Data: D006 lost-ACK/retry logic must distinguish caller timeout from underlying operation terminal state.
- Quality: Q003 should capture async event order plus cancellation request/observation/terminal traces rather than relying on sleep/rerun alone.
- Systems: leaked work/resources after abandoned waits can become performance/reliability concerns; no measured production claim here.
- Design Studio: materially relevant only when UI exposes cancel/pending/completed states; no design canonical files changed.
- Web Manager: browser/service-worker cancellation and lifecycle are separate transfer boundaries.
- Marketing Manager: not materially relevant.
- Product: no new product implementation audit was required for this Foundation mechanism block.

## OPEN / VALIDATION
- direct Dart execution of Future/event/microtask ordering;
- direct Dart cancellation-capable API comparison;
- Flutter frame scheduling and lifecycle interaction;
- structured cancellation/cleanup/error propagation alternatives;
- streams/backpressure and cancellation in a later coherent block;
- process death/native resource behavior.

## HANDOFFS
- **Data / D006:** model timeout/ACK loss separately from operation terminal state; retries need operation identity/idempotency when prior work may still be active.
- **Quality / Q003:** event-order matrices should include timeout-before-completion, cancellation-request-before/after side effect, late completion, and duplicate retry traces.
- **Architecture / A003:** cancellation/timeout/cleanup belong in behavioral contracts when observable to consumers.
- **Mobile:** validate exact Flutter/plugin/native APIs rather than assuming generic Future cancellation.
