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

The original Linux/Python fixture established a bounded OS child-process/I/O boundary. Direct Dart transfer is now executable rather than inferred: GitHub-hosted run `35423963687`, job `105846574857`, exact workflow/source commit `ccad123b533a5aa41bed7e84d36ad852828545c8` completed successfully; runtime identity recording, `dart run` JIT execution, `dart compile exe`, and execution of the resulting AOT executable all succeeded.

Failure→root-cause→fix evidence is retained: prior run `35421496953` reached JIT success and AOT compilation but failed AOT execution because the fixture incorrectly reused the JIT launch shape for a self-contained AOT executable. JIT now spawns `dart <script> child` while AOT self-spawns `<compiled-exe> child`; the regression run passed.

A second hosted transfer now executes Flutter framework code directly. Workflow commit `3b920ba70d315baa686a9ee931144700719bab58`, run `35426881450`, job `105854277141` completed successfully: official Flutter stable checkout installation, Flutter/Dart/engine identity recording, dependency resolution, and the widget runtime-boundary test all passed. The fixture observes `setState` dirtying state while the rebuilt observable tree advances after the next `pump`. The official stable branch observed immediately after the run was `flutter/flutter@6a19cca56475dbfba1478ee68d7bd0c2ef891da1`; that ref records engine `af7e796e161ae0bb1ff0758c71a7105418bd9ded`. Because command stdout is not exposed in the current evidence channel, that branch/ref check is corroborating identity evidence rather than a claim that the hidden log value was independently read here.

**VALIDATION:** the named direct Dart JIT/AOT gap is CLOSED for the bounded hosted Linux process/I/O claim, and the prior absence of any direct Flutter execution is CLOSED at a first framework/test-binding level. This is not Android/iOS embedder, browser/PWA, physical-device, release-mode application, or production-product evidence.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY — first integrated Foundation block complete**. Python aliasing/lifetime evidence and Dart source model retained; direct Dart identity/alias/final-binding/resource-lifetime transfer remains OPEN.

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY — first integrated Foundation block complete**. Bounded queue/complexity evidence retained; direct Dart structures/complexity, space cost and broader product/runtime transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — two integrated Foundation blocks complete**. Mutual exclusion/ordering/progress, circular wait and durable-predicate signaling boundaries retained; direct Dart concurrency transfer remains OPEN.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — two integrated Foundation blocks complete**. Future/wait/timeout/cancellation and ordering/error/cleanup boundaries retained; direct Dart/Flutter async transfer remains OPEN.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — two integrated Foundation blocks complete**. Stream/framing/termination ambiguity evidence retained; direct Dart/mobile/real-network transfer remains OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001 has materially crossed its original direct-execution blocker with Dart JIT/AOT plus first Flutter framework execution and includes failure/root-cause/regression evidence. The broader Foundations Stage-1 gate still requires appropriate transfer across memory/types, structures/complexity, concurrency, async and OS/network claims; one widget test cannot substitute for those mechanisms or for native/browser platform evidence.

## Dependencies / handoffs
- **Mobile:** M001 may consume the direct Flutter framework result, but Android/iOS/browser/embedder behavior remains separate.
- **Quality:** preserve the failed AOT launch-shape run as fixture/oracle-design evidence; build/runtime mode must be explicit.
- **Systems:** exact workflow/run/job/toolchain identity belongs with executable/release evidence; Studio hosted execution is not a canonical LogMate build.
- **Architecture/Data:** direct execution strengthens the shared model but does not alter persistence, ownership or product-behavior claims.

## CHANGE WATCH / OPEN
- Flutter/Dart toolchain behavior is version-sensitive; preserve exact ref/engine/run identity.
- Hosted Linux `flutter test` is not release-AOT native app, Android/iOS lifecycle, browser/PWA or physical-device evidence.
- F002-F006 still have direct Dart/Flutter transfer gaps where runtime semantics materially matter.

## Next work
Return to Balance Loop. Do not repeat equivalent F001 JIT/AOT/widget-test passes. Compare the remaining Foundations transfer gaps against the now-unblocked higher-leverage candidates: exact canonical LogMate Flutter build/toolchain enforcement, native/browser platform execution, or direct Dart transfer of concurrency/async/OS mechanisms. Select one coherent block by prerequisite severity, risk and cross-track leverage.
