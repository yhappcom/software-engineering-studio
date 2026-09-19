# F004 — Direct Dart Isolate Transfer

Status: **VALIDATED — bounded hosted Dart Native isolate/message boundary**  
Evidence date: 2026-09-19

## Problem / scope
F004 previously had executable CPython shared-memory/synchronization evidence plus a Dart isolate source model, but direct Dart isolate execution remained OPEN. This block transfer-tests the concurrency ownership boundary on the actual Dart Native runtime without pretending Dart isolates are Python threads.

## SOURCE
- Dart `dart:isolate` API: isolates are independent workers that do not share memory and communicate via messages; the library is supported on Dart Native.
- Dart `Isolate` API: Dart code executes in isolates, with inter-isolate communication through ports.
- Dart `SendPort.send`: sending is asynchronous; ordinary mutable sendable objects are copied between same-code isolates, while some objects including `ReceivePort` are explicitly unsendable.
- Dart `ReceivePort`: messages sent through its `SendPort` are dispatched to the receive port listener.

## VALIDATION
Canonical fixture: `research/foundations/fixtures/F004_dart_isolate_boundary.dart`  
Workflow: `.github/workflows/f004-dart-isolate-validation.yml`  
Exact source/workflow head: `491887c4f20b2146026629984f43d25f19e949f4`  
GitHub Actions run: `35432075163`  
Job: `105868357618`  
Toolchain requested by workflow: Dart SDK `3.13.3`  
Runner class: GitHub-hosted `ubuntu-latest`

### CLAIM
A Dart isolate can own mutable state and serialize state transitions behind a message boundary; an explicitly unsendable runtime object is rejected at that boundary rather than becoming shared mutable isolate state.

### SPEC / PROPERTY
The worker isolate exclusively owns `counter`. Three concurrent caller Futures each send one `inc` request and receive one reply. The oracle requires three distinct results in `{1,2,3}` and final worker-owned count `3`, without requiring a scheduler-specific response order. A separate negative probe attempts to send a `ReceivePort`, which the Dart API explicitly lists as unsendable.

### ORACLE
- all three increment responses must be distinct integers from 1 through 3;
- a later `get` must return exactly `3`;
- sending a `ReceivePort` must synchronously reject at the send boundary;
- orderly worker stop must report final state `3`.

### OBSERVATION / VERDICT
Run `35432075163`, job `105868357618` completed successfully. Checkout, Dart setup, environment recording, and the isolate fixture step all concluded `success`.

**VALIDATION: PASS for the bounded claim.** This closes F004's named direct-Dart-isolate execution gap at hosted Dart Native scope.

## SYNTHESIS
Dart isolate ownership changes the concurrency hazard surface rather than eliminating concurrency reasoning. The fixture does not need a shared-memory mutex for `counter`: one isolate owns the mutable state and callers cross the boundary through messages. Correctness still depends on protocol semantics—request/reply correlation, termination, timeout, duplicate/retry behavior, external resources, and any state outside that isolate remain independent concerns.

The oracle intentionally does not assert response order. Concurrency correctness here is the invariant `three accepted increments → final owned count 3`, not a scheduler-order claim.

## CONTRADICTION / correction
`Dart isolates mean concurrency is automatically safe` remains false as a general statement. The direct runtime evidence supports memory isolation/message-boundary ownership for this fixture; it does not establish distributed ordering, exactly-once effects, cancellation, fairness, external-resource serialization, or application-level protocol correctness.

## EVIDENCE LIMIT
This is Dart Native on a GitHub-hosted Linux runner. It is not Flutter frame scheduling, Android/iOS native-thread/plugin behavior, browser/web workers, shared external database/file/socket behavior, physical-device behavior, or LogMate production evidence. The negative case validates one documented unsendable type; it is not an exhaustive sendability test.

## RELATED DOMAIN CHECK
- Foundations: F001 hosted Dart execution path reused; F005 async evidence remains separate.
- Architecture: isolate ownership is a concrete state-ownership boundary, not a substitute for semantic contracts.
- Mobile: Flutter/platform plugin/native-thread transfer remains OPEN.
- Data: isolate-local ownership does not serialize external storage or distributed replicas by itself.
- Quality: invariant oracle avoids scheduler-order overfitting; negative sendability case adds failure evidence.
- Systems: exact workflow/run/job/toolchain identity retained; this is not product build/release evidence.
- Design Studio: not materially relevant to this runtime mechanism.
- Web Manager: browser workers have different runtime/platform semantics; no transfer claimed.
- Marketing Manager: not materially relevant.
- Product repositories: no product implementation was audited in this block.

## HANDOFFS
- **Architecture/A002:** use direct isolate ownership as one implementation option for state ownership, while keeping protocol invariants explicit.
- **Data/D006:** do not infer exactly-once or durable serialization from isolate-local message serialization; external side effects need their own idempotency/transaction evidence.
- **Quality/Q003:** distinguish invariant-based concurrency oracles from incidental response ordering.
- **Mobile/M004:** native/plugin callbacks can cross different thread/isolate boundaries and require platform-specific transfer.

## OPEN / CHANGE WATCH
- process-vs-isolate failure isolation and termination semantics beyond this orderly stop;
- external resource races and multi-isolate I/O;
- Flutter/native/browser transfer;
- fairness/starvation and larger protocol liveness;
- Dart isolate/sendability behavior is SDK/platform sensitive and should retain exact runtime identity in future evidence.
