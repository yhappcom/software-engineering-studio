# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-19

## Mission
Build language- and framework-independent understanding of how programs execute, represent data, use memory, coordinate concurrency, interact with operating systems, and communicate over networks.

## Active evidence

### F001 — Program Execution Foundations
Status: **IN STUDY — DIRECT DART JIT/AOT EXECUTION VALIDATED; FLUTTER RUNTIME TRANSFER OPEN**

Canonical: `research/foundations/F001_program_execution_foundations.md`; fixtures: `research/foundations/fixtures/F001_process_boundary.py`, `research/foundations/fixtures/F001_dart_jit_aot_boundary.dart`.

The original Linux/Python fixture established a bounded OS child-process/I/O boundary. Direct Dart transfer is now executable rather than inferred: GitHub-hosted run `35423963687`, job `105846574857`, exact workflow/source commit `ccad123b533a5aa41bed7e84d36ad852828545c8` completed successfully after `dart-lang/setup-dart@v1`; runtime identity recording, `dart run` JIT execution, `dart compile exe`, and execution of the resulting AOT executable all succeeded.

Failure→root-cause→fix evidence is retained: prior run `35421496953` reached JIT success and AOT compilation but failed AOT execution because the fixture incorrectly reused the JIT launch shape for a self-contained AOT executable. The fixture was changed so JIT spawns `dart <script> child` while AOT self-spawns `<compiled-exe> child`; the regression run then passed.

**VALIDATION:** the named direct Dart JIT/AOT gap is CLOSED for this bounded Linux hosted-runner process/I/O claim. This is not Flutter engine/embedder/mobile evidence. A Flutter framework/runtime transfer fixture and hosted workflow were added on 2026-09-19; its execution verdict remains OPEN until an actual run is observed.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY — first integrated Foundation block complete**

Canonical: `research/foundations/F002_values_references_memory_lifetime.md`; fixture: `research/foundations/fixtures/F002_aliasing_lifetime_boundary.py`. Python aliasing/lifetime evidence and Dart source model retained; direct Dart transfer for identity/alias/final-binding/resource lifetime remains OPEN.

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY — first integrated Foundation block complete**

Canonical: `research/foundations/F003_data_structures_algorithms_complexity.md`; fixture: `research/foundations/fixtures/F003_queue_structure_complexity.py`. Bounded queue/complexity evidence retained; direct Dart structures/complexity, space cost and broader product/runtime transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`. Mutual exclusion/ordering/progress, circular wait and durable-predicate signaling boundaries retained. Direct Dart concurrency transfer remains OPEN.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`. Future/wait/timeout/cancellation and ordering/error/cleanup boundaries retained. Direct Dart/Flutter async transfer remains OPEN.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F006_os_file_socket_network_foundations.md`; fixtures: `F006_stream_framing_boundary.py`, `F006_connection_termination_ambiguity.py`. Stream/framing/termination ambiguity evidence retained. Direct Dart/mobile/real-network transfer remains OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001 now has direct Dart JIT/AOT execution plus failure/root-cause/regression evidence, materially advancing the highest prerequisite. Representative Flutter framework/runtime execution is still awaiting an observed run, and the broader Stage-1 topics still need appropriate Dart/Flutter transfer where their claims require it.

## Dependencies / handoffs
- **Mobile:** consume the F001 direct Dart result as language/runtime evidence only; Flutter framework/engine/embedder and Android/iOS behavior remain separate transfer obligations.
- **Quality:** preserve the failed AOT launch-shape run as a test-fixture/oracle-design lesson; build/runtime mode must be explicit.
- **Systems:** exact workflow commit/run/job/toolchain identity belongs with executable/release evidence; direct Dart success does not establish a canonical product build.
- **Architecture/Data:** process/runtime mode is now directly transfer-tested in Dart, but product persistence/lifecycle claims remain independent.

## CHANGE WATCH / OPEN
- Flutter hosted runtime validation is OPEN until the newly added fixture/workflow actually executes and its exact SDK/engine/ref is captured.
- Direct Dart evidence is bounded to the hosted Linux runner and the tested process/I/O semantics; Android/iOS/web transfer is not implied.
- Dart/Flutter toolchain behavior is version-sensitive; preserve exact run and SDK identity in future evidence.

## Next work
First retrieve the Flutter hosted runtime fixture verdict. If it executes successfully, update F001/M001 boundaries without overclaiming Android/iOS/browser behavior. If it fails, preserve the failure, isolate root cause, and repair only when evidence supports the diagnosis. Do not repeat equivalent Dart JIT/AOT runs merely to accumulate passes.
