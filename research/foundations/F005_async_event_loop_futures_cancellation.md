# F005 — Async Execution, Event Loops, Futures, Streams & Cancellation

Status: **IN STUDY — two integrated Foundation blocks complete**  
Evidence date: 2026-09-17

## Problem / scope
F004 established synchronization boundaries; D006 and Q003 need async vocabulary for ordering, timeout, cancellation and liveness. F005 now contains two bounded blocks: (1) waiter timeout vs underlying-work cancellation, and (2) queue-order assumptions plus structured cleanup/error paths.

## SOURCE
- Dart concurrency: an isolate processes queued events one at a time through an event loop. https://dart.dev/language/concurrency
- Dart async programming: `async` returns a Future and `await` suspends the async function. https://dart.dev/language/async
- `Future<T>` represents eventual value/error; `timeout` stops waiting after a limit. https://api.dart.dev/dart-async/Future-class.html
- `Future.microtask` schedules its computation with `scheduleMicrotask`. https://api.dart.dev/dart-async/Future/Future.microtask.html
- `Future.delayed(Duration.zero, ...)` runs no sooner than the next event-loop iteration, after microtasks have run. https://api.dart.dev/dart-async/Future/Future.delayed.html
- `Isolate` documentation states each isolate has its own event loop and an event may run smaller tasks in a nested microtask queue. https://api.dart.dev/dart-isolate/Isolate-class.html
- Stream subscriptions and cancellable socket connection tasks demonstrate that cancellation semantics belong to the concrete API contract. https://api.dart.dev/dart-async/StreamSubscription-class.html ; https://api.dart.dev/dart-io/Socket-class.html

## SYNTHESIS — mechanism model
Keep these states distinct:

`operation start → Future/handle → caller suspension → queued continuation/event → completion(value/error) OR no completion`

and, when cancellation exists:

`cancellation request → observation/acceptance → cleanup/resource release → cancellation acknowledgement → terminal state`.

A timeout can belong to a waiter without terminating work. Queue category also matters: a documented microtask-before-next-event relation is stronger than assumptions about arbitrary callback/timer ordering. Cleanup is another independent obligation: observing/handling an async error does not itself release resources or roll back state.

## VALIDATION 1 — waiter timeout vs work cancellation
Fixture: `research/foundations/fixtures/F005_async_timeout_cancellation_model.py`

Environment: Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41.

Observed:
```text
timeout_only ['started', 'caller_timeout', 'side_effect']
cooperative (['started', 'cancel_observed'], 'cancelled')
```

**VALIDATION:** stopping the modeled caller wait did not stop deliberately shielded underlying work; explicit cooperative cancellation was observed before the side effect.

**DEBUG / ROOT CAUSE:** semantic conflation of observer state and operation terminal state, not scheduler failure.

## VALIDATION 2 — ordering assumptions and structured cleanup
Fixture: `research/foundations/fixtures/F005_async_ordering_cleanup_model.py`

Environment actually executed: Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41.

Observed:
```text
ordering ['ready_callback', 'after_yield', 'timer_event']
unsafe_cleanup ({'open': True}, ['opened', 'error_observed'])
finally_cleanup ({'open': False}, ['opened', 'error_observed', 'closed'])
```

**CLAIM:** async correctness must not depend on an undocumented queue ordering, and error observation is not equivalent to cleanup completion.

**ORACLE:** the ordering subcase records rather than universalizes CPython scheduling. The cleanup subcase independently requires modeled resource state `open == False` after failure.

**FAILURE CASE:** the unsafe variant catches the modeled async failure but omits cleanup; the resource remains logically open.

**ALTERNATIVE:** the comparison uses a `finally` boundary, yielding `opened → error_observed → closed` and satisfying the cleanup oracle.

**DEBUG / ROOT CAUSE:** the defect is missing cleanup on an exceptional path. Catching the error only changes error propagation; it does not mutate the independent resource state.

**TRANSFER LIMIT:** the CPython callback/timer trace is deliberately not evidence of Dart ordering. For Dart, only documented relations such as `Future.microtask` using the microtask queue and zero-delay `Future.delayed` occurring after microtasks are promoted as SOURCE. Direct Dart execution remains OPEN.

## CONTRADICTION
- `await means another thread runs the operation` — false for Dart's documented event-loop model.
- `timeout means the operation was cancelled` — false as a universal rule.
- `Future exists → operation eventually finishes` — unjustified.
- `error caught → resources cleaned up` — false in the bounded failure fixture.
- `one observed callback/timer order → portable event-loop contract` — false; ordering claims require an explicit runtime/API guarantee.

## ENGINEERING JUDGMENT
Async APIs should document operation identity, completion/error semantics, timeout ownership, cancellation capability/acknowledgement, cleanup/resource guarantees, and any ordering relation consumers may rely on. Correctness-sensitive logic should encode state dependencies explicitly instead of depending on incidental timing.

## RELATED DOMAIN CHECK
- Foundations: F004 ordering/progress reused; F001 direct Dart/Flutter execution remains OPEN.
- Architecture: timeout/cancellation/error/cleanup/ordering are behavioral contracts when observable.
- Mobile: Flutter frame/lifecycle/plugin-native ordering requires exact runtime validation.
- Data: D006 retries after timeout may overlap prior work; cleanup failure can retain locks/resources/state that alter retry behavior.
- Quality: Q003 should use explicit event-order matrices and terminal-state/resource oracles rather than sleep-based assumptions.
- Systems: abandoned work/resources can become reliability/performance issues; no measured production claim.
- Design Studio: relevant only when UI exposes pending/cancelled/error/completed states; no files changed.
- Web Manager: browser/service-worker event-loop and cancellation are separate transfer boundaries.
- Marketing Manager: not materially relevant.
- Product: no product audit required for this mechanism block.

## OPEN / VALIDATION
- direct Dart Future/event/microtask execution;
- exact Dart cancellation-capable API execution;
- Flutter frame scheduling/lifecycle interaction;
- streams/backpressure;
- native/process-death cleanup behavior;
- cancellation during cleanup and multi-resource rollback ordering.

## HANDOFFS
- **Data / D006:** represent timeout, operation terminal state and cleanup separately; retry matrices should include late completion and retained-resource cases.
- **Quality / Q003:** assert semantic state/resource invariants and record event traces; do not make portable claims from incidental callback/timer order.
- **Architecture / A003:** cancellation, error propagation and cleanup guarantees belong in consumer-visible contracts.
- **Mobile:** validate documented Dart ordering directly when SDK becomes available, then test Flutter-specific scheduler/frame boundaries separately.
