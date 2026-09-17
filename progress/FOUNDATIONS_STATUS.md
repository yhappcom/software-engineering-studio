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

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY — first integrated Foundation block complete**

Canonical: `research/foundations/F003_data_structures_algorithms_complexity.md`; fixture: `research/foundations/fixtures/F003_queue_structure_complexity.py`.

Established abstract operation/invariant vs representation vs primitive cost vs workload composition vs measured resource behavior. Current CPython sources document approximately O(1) deque end removal versus O(n) list front removal. A Python 3.13.5/Linux size sweep preserved the same independently checked FIFO checksum at 5k/10k/20k/40k elements while repeated list front removal grew from 2.57x to 64.96x the observed deque drain time in this run. Timings are observations, not portable guarantees or asymptotic proof. Direct Dart structures/complexity, space cost, broader algorithms and product/runtime transfer remain OPEN.

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
- `F001` — direct Dart JIT/AOT and Flutter runtime execution OPEN.
- `F002` — IN STUDY; direct Dart identity/alias/final-binding and explicit resource-lifetime transfer OPEN.
- `F003` — IN STUDY; first queue/complexity block complete; direct Dart, space complexity, broader structures/algorithms and product transfer OPEN.
- `F004` — IN STUDY / two blocks.
- `F005` — IN STUDY / two blocks.
- `F006` — IN STUDY / two blocks.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when useful. Stage 1 remains NOT PASS.

## Dependencies / handoffs
- Architecture: A002 should use shared mutable reachability/aliasing as a concrete ownership and coupling mechanism; resource behavior can become an externally relevant contract when budgets/SLOs require it.
- Mobile: direct Dart/Flutter execution remains required; transfer-test data-structure/algorithm choices against actual frame/startup/background budgets rather than CPython timing.
- Data: use operation mix and invariants when selecting indexes/cache/import/sync structures; do not transfer CPython constants or collection guarantees.
- Quality: complexity/performance tests need semantic oracles and controlled size/workload; one timing does not prove a complexity class.
- Systems: S003 should distinguish asymptotic cost models from measured profiling/resource evidence.

## Next work
Use Balance Loop. F003 removes the last untouched Foundations Stage-1 block at a first executable level. Foundations now has at least initial evidence across F001-F006, but direct Dart/Flutter transfer remains a track-wide dependency. Strong independent candidates are `Q004` property/model-based testing for D006/Q006 state-space exploration, Architecture Foundation closure on refactoring/technical-debt boundaries, or `S002/S003` if risk/leverage outranks Quality. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
