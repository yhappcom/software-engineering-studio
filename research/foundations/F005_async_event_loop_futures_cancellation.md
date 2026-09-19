# F005 — Async Execution, Event Loops, Futures, Streams & Cancellation

Status: **IN STUDY — direct Dart transfer added**  
Evidence date: 2026-09-19

## Problem / scope
F004 established synchronization boundaries; D006 and Q003 need async vocabulary for ordering, timeout, cancellation and liveness. F005 contains three bounded blocks: (1) waiter timeout vs underlying-work cancellation, (2) queue-order assumptions plus structured cleanup/error paths, and (3) direct Dart transfer of documented ordering, timeout-source independence and concrete StreamSubscription cancellation.

## SOURCE
- Dart concurrency: an isolate processes queued events one at a time through an event loop. https://dart.dev/language/concurrency
- Dart async programming: `async` returns a Future and `await` suspends the async function. https://dart.dev/language/async
- `Future<T>` represents eventual value/error; `Future.timeout` creates a timeout future and the source future can still complete later. https://api.dart.dev/dart-async/Future/timeout.html
- `Future.microtask` schedules its computation with `scheduleMicrotask`. https://api.dart.dev/dart-async/Future/Future.microtask.html
- `Future.delayed(Duration.zero, ...)` runs no sooner than the next event-loop iteration, after microtasks have run. https://api.dart.dev/dart-async/Future/Future.delayed.html
- Stream subscription cancellation is an API-specific asynchronous cleanup contract. https://api.dart.dev/dart-async/StreamSubscription/cancel.html
- Current Dart async documentation rechecked 2026-09-19; site documentation reports Dart 3.13.3 and was updated 2026-09-14.

## SYNTHESIS — mechanism model
Keep these states distinct:

`operation start → Future/handle → caller suspension → queued continuation/event → completion(value/error) OR no completion`

and, when cancellation exists:

`cancellation request → observation/acceptance → cleanup/resource release → cancellation acknowledgement → terminal state`.

A timeout can belong to a waiter without terminating work. Queue category also matters: a documented microtask-before-next-event relation is stronger than assumptions about arbitrary callback/timer ordering. Cleanup is another independent obligation: observing/handling an async error does not itself release resources or roll back state.

## VALIDATION 1 — waiter timeout vs work cancellation model
Fixture: `research/foundations/fixtures/F005_async_timeout_cancellation_model.py`

Environment: Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41.

Observed:
```text
timeout_only ['started', 'caller_timeout', 'side_effect']
cooperative (['started', 'cancel_observed'], 'cancelled')
```

**VALIDATION:** stopping the modeled caller wait did not stop deliberately shielded underlying work; explicit cooperative cancellation was observed before the side effect.

**DEBUG / ROOT CAUSE:** semantic conflation of observer state and operation terminal state, not scheduler failure.

## VALIDATION 2 — ordering assumptions and structured cleanup model
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

## TRANSFER VALIDATION 3 — direct Dart async/runtime boundary
Fixture: `research/foundations/fixtures/F005_dart_async_timeout_ordering.dart`  
Workflow: `.github/workflows/f005-dart-async-validation.yml`  
Workflow/source commit: `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0`  
GitHub-hosted run: `35429564591`; job: `105861592799`.

### Test Evidence Contract
- **CLAIM:** (a) a scheduled microtask precedes a zero-delay event in the documented relation exercised here; (b) `Future.timeout` timing out does not cancel the source future; (c) cancellation semantics must be taken from the concrete API, demonstrated with `StreamSubscription.cancel` preventing later controller events from reaching that subscription.
- **SPEC/PROPERTY:** Dart async/Future/StreamSubscription primary documentation above.
- **TARGET:** exact Studio fixture at workflow commit `b5fc0cf...`.
- **INPUT/STATE:** deterministic in-process scheduled microtask + zero-delay event; 80 ms source Future with 10 ms timeout; single-subscription StreamController receiving `1`, cancellation acknowledgement, then attempted `2` delivery.
- **ORACLE:** explicit assertions over event trace, timeout observation, independent source side effect/result, and received stream values.
- **ENVIRONMENT:** GitHub-hosted Ubuntu 24.04.5 LTS; Linux `6.17.0-1022-azure`; x86_64; exact Dart SDK `3.13.3 (stable)`; runner image `ubuntu-24.04` version `20260907.300.1`.
- **OBSERVATION:** `F005_DART_ASYNC_PASS ordering=[microtask, event] timeout=true sourceEffect=true seen=[1]`.
- **VERDICT:** **PASS for these bounded direct-Dart properties.** The previous direct Dart Future/event/microtask transfer gap is materially advanced and the timeout/source distinction is now executable in Dart rather than inferred from Python.
- **FAILURE MODEL:** catches reversal of the specified microtask/event relation, accidental assumption that timeout cancels the source, and post-cancel delivery to the tested subscription. It does not test arbitrary Timer ordering, races across isolates, socket cancellation, cancellation during cleanup, backpressure, Flutter scheduler/frame behavior, process death or platform lifecycle.
- **REPRODUCTION DATA:** fixture + workflow + exact commit/run/job above.
- **EVIDENCE LIMIT:** timing durations are only used to separate this bounded source/timeout case; this is not a latency guarantee. `StreamSubscription.cancel` does not establish cancellation semantics for Futures, sockets, plugins or arbitrary operations.

## CONTRADICTION
- `await means another thread runs the operation` — false for Dart's documented event-loop model.
- `timeout means the operation was cancelled` — directly contradicted by both Dart documentation and the new direct-Dart fixture: the source completed later and performed its effect.
- `Future exists → operation eventually finishes` — unjustified.
- `error caught → resources cleaned up` — false in the bounded failure fixture.
- `one observed callback/timer order → portable event-loop contract` — false; ordering claims require an explicit runtime/API guarantee.
- `one API's cancel semantics generalize to all async work` — false; cancellation belongs to the concrete API contract.

## ENGINEERING JUDGMENT
Async APIs should document operation identity, completion/error semantics, timeout ownership, cancellation capability/acknowledgement, cleanup/resource guarantees, and any ordering relation consumers may rely on. Correctness-sensitive logic should encode state dependencies explicitly instead of depending on incidental timing.

## RELATED DOMAIN CHECK
- Foundations: F001 direct Dart execution path enabled this transfer; F004 ordering/progress remains prerequisite context.
- Architecture: timeout/cancellation/error/cleanup/ordering are behavioral contracts when observable.
- Mobile: Flutter frame/lifecycle/plugin-native ordering requires separate exact runtime validation; this Dart CLI result does not establish it.
- Data: D006 retries after timeout may overlap prior work; the direct Dart result strengthens the requirement to separate waiter timeout from operation terminal state.
- Quality: Q003 should use explicit event-order matrices and terminal-state/resource oracles rather than sleep-based assumptions; exact runtime identity is now recorded.
- Systems: abandoned work/resources can become reliability/performance issues; no production/resource-cost claim.
- Design Studio: not materially relevant to this runtime-mechanism block except when UI exposes pending/cancelled/error/completed states; no files changed.
- Web Manager: browser/service-worker event-loop and cancellation remain separate transfer boundaries; no files changed.
- Marketing Manager: not materially relevant.
- Product: LogMate exact ref `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19` was considered for higher-leverage canonical build work. Production identity remains unknown; default branch is not assumed production. This F005 fixture is Studio evidence, not LogMate runtime evidence.

## OPEN / VALIDATION
- arbitrary/event-timer ordering beyond documented relations;
- cancellation-capable `dart:io` operation execution and cancellation during cleanup;
- streams under pause/resume/backpressure/error and multi-listener cases;
- Flutter frame scheduling/lifecycle interaction;
- isolate/message ordering and failure transfer;
- native/process-death cleanup behavior;
- product/runtime transfer to LogMate and browser/PWA.

## HANDOFFS
- **Data / D006:** represent timeout, operation terminal state and cleanup separately; retry matrices should include late completion and retained-resource cases. Direct Dart now confirms the timeout/source distinction at the product language runtime level.
- **Quality / Q003:** assert semantic state/resource invariants and record event traces; do not make portable claims from incidental callback/timer order.
- **Architecture / A003:** cancellation, error propagation and cleanup guarantees belong in consumer-visible contracts.
- **Mobile:** use this as Dart-runtime evidence only; Flutter scheduler/frame and Android/iOS/browser lifecycle remain independent transfer obligations.
