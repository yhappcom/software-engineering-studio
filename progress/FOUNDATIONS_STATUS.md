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
Status: **IN STUDY — two integrated Foundation blocks complete**. Mutual exclusion/ordering/progress, circular wait and durable-predicate signaling boundaries retained; direct Dart isolate/concurrency transfer remains OPEN.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — DIRECT DART TRANSFER ADDED.** Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`; direct fixture: `research/foundations/fixtures/F005_dart_async_timeout_ordering.dart`.

GitHub-hosted run `35429564591`, job `105861592799`, exact workflow/source commit `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` succeeded on exact Dart SDK 3.13.3 / Ubuntu 24.04.5 / Linux 6.17.0-1022-azure. The executable oracle observed `ordering=[microtask, event]`, a timeout at 10 ms while the 80 ms source Future later completed its side effect/result, and a StreamSubscription that received `[1]` but not the post-cancel `2` after awaiting `cancel()`.

**TRANSFER VALIDATION:** the prior Python model's central waiter-timeout ≠ source-cancellation distinction now survives direct Dart execution, and the documented microtask-before-zero-delay-event relation is directly exercised. Cancellation remains API-specific: the StreamSubscription result must not be generalized to Futures, sockets, plugins or arbitrary work. Flutter scheduler/frame, isolate concurrency, stream backpressure/error, `dart:io` cancellation and product/browser transfer remain OPEN.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — two integrated Foundation blocks complete**. Stream/framing/termination ambiguity evidence retained; direct Dart/mobile/real-network transfer remains OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001 has crossed its original direct-execution blocker with Dart JIT/AOT plus first Flutter framework execution and includes failure/root-cause/regression evidence. F005 now adds direct Dart async transfer rather than reading/model evidence alone. The broader Foundations Stage-1 gate still needs appropriate transfer across memory/types, structures/complexity, concurrency and OS/network claims; one async fixture cannot substitute for those mechanisms or for native/browser platform evidence.

## Dependencies / handoffs
- **Mobile:** M001 may consume direct Flutter framework evidence and F005 direct Dart async semantics, but Flutter scheduler/frame and Android/iOS/browser behavior remain separate.
- **Quality:** preserve exact runtime identity and semantic oracles; timeout tests must observe source terminal state independently of waiter state.
- **Data:** D006 retry/idempotency work should model late source completion after caller timeout explicitly.
- **Systems:** exact workflow/run/job/toolchain identity belongs with executable/release evidence; Studio hosted execution is not a canonical LogMate build.
- **Architecture:** timeout/cancellation/cleanup semantics are consumer-visible contracts where observable.

## CHANGE WATCH / OPEN
- Flutter/Dart toolchain behavior is version-sensitive; preserve exact ref/SDK/run identity.
- Hosted Linux `flutter test` is not release-AOT native app, Android/iOS lifecycle, browser/PWA or physical-device evidence.
- F002/F003/F004/F006 still have direct Dart/Flutter transfer gaps where runtime semantics materially matter.
- F005 still needs isolate, stream backpressure/error, concrete I/O cancellation, Flutter scheduler/lifecycle and product/browser transfer.

## Next work
Return to Balance Loop. Do not repeat equivalent F001 or F005 happy-path variants. The trustworthy hosted Dart/Flutter path now supports direct transfer of remaining Foundations mechanisms. Recompare F002/F003/F004/F006 against exact canonical LogMate build/toolchain enforcement and native/browser execution; prefer a coherent block that changes evidence class or closes a prerequisite, not another timing permutation.
