# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-19

## Mission
Build language- and framework-independent understanding of how programs execute, represent data, use memory, coordinate concurrency, interact with operating systems, and communicate over networks.

## Active evidence

### F001 — Program Execution Foundations
Status: **IN STUDY — DIRECT DART JIT/AOT + FIRST FLUTTER FRAMEWORK EXECUTION VALIDATED**

Canonical: `research/foundations/F001_program_execution_foundations.md`; fixtures: `research/foundations/fixtures/F001_process_boundary.py`, `research/foundations/fixtures/F001_dart_jit_aot_boundary.dart`, `research/foundations/fixtures/f001_flutter_runtime/`.

GitHub-hosted run `35423963687`, job `105846574857`, exact workflow/source commit `ccad123b533a5aa41bed7e84d36ad852828545c8` completed successfully; runtime identity recording, `dart run` JIT execution, `dart compile exe`, and execution of the resulting AOT executable all succeeded. Prior AOT-execution failure was root-caused to a fixture launch-shape defect and the corrected regression passed.

Workflow commit `3b920ba70d315baa686a9ee931144700719bab58`, run `35426881450`, job `105854277141` also completed official Flutter setup, identity recording, dependency resolution and a `flutter_test` widget runtime boundary. Evidence remains framework/test-binding scope, not native/browser/production runtime.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY — first integrated Foundation block complete**. Python aliasing/lifetime evidence and Dart source model retained; direct Dart identity/alias/final-binding/resource-lifetime transfer remains OPEN.

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY — first integrated Foundation block complete**. Bounded queue/complexity evidence retained; direct Dart structures/complexity, space cost and broader product/runtime transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — DIRECT DART ISOLATE TRANSFER ADDED.** Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`, `research/foundations/F004_direct_dart_isolate_transfer.md`; direct fixture: `research/foundations/fixtures/F004_dart_isolate_boundary.dart`.

GitHub-hosted run `35432075163`, job `105868357618`, exact source/workflow head `491887c4f20b2146026629984f43d25f19e949f4` succeeded with Dart SDK 3.13.3. A worker isolate exclusively owned a mutable counter; concurrent request Futures produced distinct increments and final count 3. A negative probe verified rejection of an explicitly unsendable `ReceivePort`.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — DIRECT DART TRANSFER ADDED.** Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`; direct fixture: `research/foundations/fixtures/F005_dart_async_timeout_ordering.dart`.

GitHub-hosted run `35429564591`, job `105861592799`, exact workflow/source commit `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` succeeded on Dart SDK 3.13.3 / Ubuntu 24.04.5. The oracle observed microtask-before-zero-delay-event, waiter timeout while the source Future later completed, and API-specific StreamSubscription cancellation.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — DIRECT DART SOCKET TRANSFER REPRODUCES HARNESS HANG; ROOT CAUSE OPEN.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md` plus prior F006 studies.

Initial run `35434862199` reached the Dart socket fixture and hung. A first hypothesis blamed awaiting `Socket.close()` before peer EOF observation. Commit `6f78f6ee8ccda32143df55d2a7f3820a117cc5c7` reordered that wait and added five-second Future timeouts, but regression run `35434895889`, job `105875778624`, again remained in the fixture step far beyond those internal deadlines. **CONTRADICTION / FALSIFICATION:** close-order alone is not an adequate root cause; no Dart socket defect is inferred.

The workflow itself had no independent job/step deadline. Commit `835104ea9dac410b4f0a4d17f748882710f5921c` adds `timeout-minutes` plus F006 concurrency/cancel-in-progress for future runs. Run `35437455712` was queued at evidence cutoff. This is validation-harness containment evidence, not F006 socket correctness; direct Dart socket transfer remains OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001 has direct Dart JIT/AOT plus first Flutter framework execution; F004 has direct Dart isolate/message-boundary transfer; F005 has direct Dart async transfer. F006 now adds a real Dart network-harness failure and falsified causal hypothesis, but not a successful transport verdict. F002/F003 remain selectively open and native mobile/browser/product platform evidence is separate.

## Dependencies / handoffs
- **Mobile:** consume direct Flutter framework, Dart isolate and async evidence only at their stated boundaries; F006 `dart:io` cannot transfer to browser/PWA and has no socket PASS yet.
- **Quality:** preserve F006 as failure→hypothesis→falsification; async/network harnesses require an outer deadline independent of the target's own timeout logic.
- **Data:** D006 retry/idempotency work must not infer application completion from transport termination; F006 adds no new correctness claim yet.
- **Systems:** exact workflow/run/job/toolchain identity belongs with executable evidence; bounded CI job execution is itself an evidence-pipeline control.
- **Architecture:** isolate ownership and timeout/cancellation/cleanup remain observable contract concerns where consumer-visible.

## CHANGE WATCH / OPEN
- Flutter/Dart toolchain behavior is version-sensitive; preserve exact ref/SDK/run identity.
- Hosted Linux Flutter/Dart evidence is not release-AOT native app, Android/iOS lifecycle, browser/PWA or physical-device evidence.
- F002/F003 still have direct Dart/runtime transfer gaps where runtime semantics materially matter.
- F006 direct Dart socket verdict/root cause is OPEN; exact blocking phase is not yet isolated because partial running-job logs were unavailable.
- F004 external-resource/process-failure/fairness/platform transfer and F005 backpressure/error/concrete I/O cancellation/platform transfer remain OPEN.

## Next work
First recover bounded run `35437455712`. If it times out, isolate F006 into independently bounded phases or an external process deadline before spending another runner cycle; do not repeat close-order permutations. If the harness boundary remains opaque, Balance Loop should move to exact canonical LogMate build/toolchain enforcement or another higher-leverage independent prerequisite rather than consume Actions minutes on unbounded debugging.
