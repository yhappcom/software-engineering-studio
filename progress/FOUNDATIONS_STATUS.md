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

The original Linux/Python fixture established a bounded OS child-process/I/O boundary. Direct Dart transfer is executable: GitHub-hosted run `35423963687`, job `105846574857`, exact workflow/source commit `ccad123b533a5aa41bed7e84d36ad852828545c8` completed successfully; runtime identity recording, `dart run` JIT execution, `dart compile exe`, and execution of the resulting AOT executable all succeeded.

Failure→root-cause→fix evidence is retained: prior run `35421496953` reached JIT success and AOT compilation but failed AOT execution because the fixture incorrectly reused the JIT launch shape for a self-contained AOT executable. JIT now spawns `dart <script> child` while AOT self-spawns `<compiled-exe> child`; the regression run passed.

A second hosted transfer executes Flutter framework code directly. Workflow commit `3b920ba70d315baa686a9ee931144700719bab58`, run `35426881450`, job `105854277141` completed successfully: official Flutter stable checkout installation, Flutter/Dart/engine identity recording, dependency resolution, and the widget runtime-boundary test all passed. Evidence remains bounded to framework/test-binding execution, not native/browser/production runtime.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY — first integrated Foundation block complete**. Python aliasing/lifetime evidence and Dart source model retained; direct Dart identity/alias/final-binding/resource-lifetime transfer remains OPEN.

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY — first integrated Foundation block complete**. Bounded queue/complexity evidence retained; direct Dart structures/complexity, space cost and broader product/runtime transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — DIRECT DART ISOLATE TRANSFER ADDED.** Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`, `research/foundations/F004_direct_dart_isolate_transfer.md`; direct fixture: `research/foundations/fixtures/F004_dart_isolate_boundary.dart`.

Prior CPython evidence retains mutual exclusion/ordering/progress, circular-wait and durable-predicate signaling boundaries. GitHub-hosted run `35432075163`, job `105868357618`, exact source/workflow head `491887c4f20b2146026629984f43d25f19e949f4` succeeded with workflow-requested Dart SDK 3.13.3. A worker isolate exclusively owned a mutable counter; three concurrent request Futures produced three distinct increments and final count 3 without a scheduler-order oracle. A negative probe verified that sending an explicitly unsendable `ReceivePort` is rejected at the message boundary.

**TRANSFER VALIDATION:** F004's source/model claim that Dart isolate concurrency uses memory isolation + message passing now has direct Dart Native execution evidence. This does not establish fairness, exactly-once protocol effects, external-resource serialization, Flutter/native-thread/plugin behavior, browser workers, or product concurrency correctness.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — DIRECT DART TRANSFER ADDED.** Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`; direct fixture: `research/foundations/fixtures/F005_dart_async_timeout_ordering.dart`.

GitHub-hosted run `35429564591`, job `105861592799`, exact workflow/source commit `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` succeeded on exact Dart SDK 3.13.3 / Ubuntu 24.04.5 / Linux 6.17.0-1022-azure. The executable oracle observed `ordering=[microtask, event]`, a timeout at 10 ms while the 80 ms source Future later completed its side effect/result, and a StreamSubscription that received `[1]` but not the post-cancel `2` after awaiting `cancel()`.

**TRANSFER VALIDATION:** the prior Python model's central waiter-timeout ≠ source-cancellation distinction now survives direct Dart execution, and the documented microtask-before-zero-delay-event relation is directly exercised. Cancellation remains API-specific: the StreamSubscription result must not be generalized to Futures, sockets, plugins or arbitrary work. Flutter scheduler/frame, isolate concurrency, stream backpressure/error, `dart:io` cancellation and product/browser transfer remain OPEN.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — two integrated Foundation blocks complete**. Stream/framing/termination ambiguity evidence retained; direct Dart/mobile/real-network transfer remains OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001 has direct Dart JIT/AOT plus first Flutter framework execution with failure/root-cause/regression evidence; F004 now has direct Dart Native isolate/message-boundary transfer with a negative sendability case; F005 has direct Dart async transfer. The broader Stage-1 gate still needs appropriate transfer across memory/types, structures/complexity and OS/network claims; hosted Dart Native evidence cannot substitute for native mobile/browser/product platform evidence.

## Dependencies / handoffs
- **Mobile:** consume direct Flutter framework, Dart isolate and async evidence only at their stated runtime boundaries; Flutter scheduler/frame, native plugin threads and Android/iOS/browser behavior remain separate.
- **Quality:** preserve exact runtime identity and semantic oracles; concurrency tests should assert invariants rather than incidental scheduler order.
- **Data:** D006 retry/idempotency work should model late source completion after caller timeout and must not infer durable/exactly-once effects from isolate-local serialization.
- **Systems:** exact workflow/run/job/toolchain identity belongs with executable/release evidence; Studio hosted execution is not a canonical LogMate build.
- **Architecture:** isolate ownership is a concrete state-ownership option; timeout/cancellation/cleanup and request/reply semantics remain consumer-visible contracts where observable.

## CHANGE WATCH / OPEN
- Flutter/Dart toolchain behavior is version-sensitive; preserve exact ref/SDK/run identity.
- Hosted Linux `flutter test` and Dart Native isolate execution are not release-AOT native app, Android/iOS lifecycle, browser/PWA or physical-device evidence.
- F002/F003/F006 still have direct Dart/runtime transfer gaps where runtime semantics materially matter.
- F004 still needs external-resource/process-failure/fairness/platform transfer; F005 still needs stream backpressure/error, concrete I/O cancellation, Flutter scheduler/lifecycle and product/browser transfer.

## Next work
Return to Balance Loop. Do not repeat equivalent F001/F004/F005 happy-path variants. The trustworthy hosted Dart/Flutter path has now transferred execution, isolate ownership and a central async mechanism. Recompare F002/F003/F006 against exact canonical LogMate build/toolchain enforcement and native/browser execution; prefer a coherent block that changes evidence class, closes a remaining prerequisite, or creates product transfer rather than another timing/order permutation.
