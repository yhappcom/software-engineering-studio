# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-17

## Mission
Build language- and framework-independent understanding of how programs execute, represent data, use memory, coordinate concurrency, interact with operating systems, and communicate over networks.

## Active evidence

### F001 — Program Execution Foundations
Status: **IN STUDY — SOURCE/MODEL + FIRST EXECUTABLE BOUNDARY EVIDENCE**

Canonical: `research/foundations/F001_program_execution_foundations.md`; fixture: `research/foundations/fixtures/F001_process_boundary.py`.

Established source/runtime/process/engine/embedder/OS distinctions and a Linux/Python parent-child process/I/O boundary. Direct Dart SDK JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither `dart` nor `flutter` executable is available.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY — first integrated Foundation block complete**

Canonical: `research/foundations/F002_values_references_memory_lifetime.md`; fixture: `research/foundations/fixtures/F002_aliasing_lifetime_boundary.py`.

Established variable/binding vs object/value, identity, mutation vs rebinding, aliasing, reachability and resource-lifetime distinctions. Python 3.13.5/Linux failure evidence shows direct aliasing and shallow nested copying preserve write-through mutable state, while rebinding is distinct from mutation; a bounded deep-copy comparison isolates the deliberately simple graph. Current Dart sources establish GC, identity, weak-reference/finalizer semantics, but direct Dart/Flutter execution remains OPEN. Stack/heap placement is not promoted into a language semantic guarantee.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`.

Established mutual exclusion/ordering/progress distinctions, circular-wait preconditions and lock-order alternative, plus notification-vs-durable-predicate signaling. CPython evidence is not Dart runtime evidence.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`.

Established Future/wait/timeout/cancellation distinctions plus ordering/error/cleanup boundaries from current Dart sources and bounded Python model evidence. Direct Dart/Flutter execution remains OPEN.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F006_os_file_socket_network_foundations.md`  
Fixtures: `research/foundations/fixtures/F006_stream_framing_boundary.py`, `research/foundations/fixtures/F006_connection_termination_ambiguity.py`

Established stream/application-frame separation plus graceful EOF/truncated-frame and abort/reset-after-complete-frame ambiguity in bounded Linux socket evidence. Local send, peer receive, frame completion, apply, durable commit and application ACK remain separate claims. Direct Dart/mobile/real-network transfer remains OPEN.

## Remaining initial queue
- `F002` — IN STUDY / first integrated block; direct Dart identity/alias/final-binding and explicit resource-lifetime transfer OPEN.
- `F003` — Data structures, algorithms and complexity — untouched.
- `F004` — IN STUDY / two blocks.
- `F005` — IN STUDY / two blocks.
- `F006` — IN STUDY / two blocks.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when useful. Stage 1 remains NOT PASS.

## Dependencies / handoffs
- Architecture: A002 should use shared mutable reachability/aliasing as a concrete ownership and coupling mechanism; container copying does not imply deep isolation.
- Mobile: direct Dart/Flutter execution remains required; lifecycle/GC/resource cleanup are distinct contracts.
- Data: cache/snapshot/import/backup staging must verify structural independence at every mutable level required by the invariant.
- Quality: aliasing failures need independent boundary-state oracles; avoid tests that share the same mutable expected-state graph.
- Systems: deterministic file/socket/native-resource release must not be inferred from ordinary GC/finalizer timing.

## Next work
Use Balance Loop. F002 removes the untouched values/references/aliasing gap at a first executable level, but direct Dart and deterministic resource-lifetime transfer remain OPEN. `F003` is now the only untouched Foundations Stage-1 block and is a strong independent candidate because complexity/resource reasoning feeds Data, Mobile and Systems. `Q004` property/model-based testing is also increasingly valuable for richer state-space validation. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
