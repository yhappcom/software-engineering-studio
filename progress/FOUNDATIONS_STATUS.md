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

Canonical study: `research/foundations/F001_program_execution_foundations.md`
Fixture: `research/foundations/fixtures/F001_process_boundary.py`

Established so far:
- source representation, compilation/translation mode, runtime, process, engine/embedder and OS boundaries must be kept distinct;
- official Dart evidence distinguishes native JIT, native AOT and web JS/Wasm paths;
- AOT machine code still executes with Dart runtime services on native targets;
- official Flutter architecture separates app/framework/engine/embedder/runner/OS responsibilities;
- an executable Linux/Python fixture reproduced a real parent/child process boundary, independent PIDs, explicit exit status, and stdout/stderr channels.

OPEN:
- equivalent direct Dart SDK execution validation;
- JIT vs AOT artifact/run-path execution evidence;
- Flutter debug/profile/release and Android/iOS runtime validation belongs partly to `M001/M002`;
- isolate semantics must not be inferred from the OS child-process fixture.

F001 is **not PASS** until sufficient Dart/runtime executable evidence exists. Environment rechecked 2026-09-17: neither `dart` nor `flutter` executable is available.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — first integrated Foundation block complete**

Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`  
Fixture: `research/foundations/fixtures/F004_lock_order_deadlock.py`

Established with current Python/Dart sources plus Python 3.13.5/Linux executable evidence:
- mutual exclusion, ordering and progress are separate concurrency properties;
- two workers each holding one lock while requiring the other's lock reproduced the circular-wait precondition under barrier-controlled non-blocking probes;
- the probe intentionally avoids hanging the test runner while preserving both held resources until both observations are made;
- imposing one global A→B acquisition order let both workers complete in the bounded alternative;
- root cause is inconsistent multi-lock acquisition order, not failure of either lock primitive;
- `lock present` and `no data race` are insufficient global correctness claims because deadlock/livelock/starvation are separate failure classes;
- current Dart docs establish isolate-local memory/message-passing semantics, but CPython lock evidence is not Dart/Flutter runtime evidence.

OPEN: direct Dart isolate/message execution, condition/signaling hazards, starvation/fairness boundaries, process-vs-thread comparison, and F005 async/event-loop/cancellation semantics.

## Remaining initial queue
- `F002` — Values, references, memory models, stack/heap and lifetime without oversimplified folklore.
- `F003` — Data structures, algorithms and complexity as engineering cost models.
- `F004` — **IN STUDY / first integrated block complete**.
- `F005` — Async execution, event loops, futures/promises/streams and cancellation models.
- `F006` — OS/file/socket/network foundations for application engineers.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when that comparison improves understanding.

## Dependencies / handoffs
- Mobile: use F001 layered execution model in `M001`; do not transfer CPython shared-memory locks to Dart isolates.
- Data: distinguish successful memory-state change from process-surviving durability in `D001`; D006 should separate ordering, progress and convergence properties.
- Quality: record build/runtime mode in executable evidence; Q003 should treat no-progress/deadlock separately from wrong-state races and use bounded failure probes.
- Architecture: synchronization follows explicit ownership/invariant contracts from A002.
- Systems: preserve runtime/process/artifact boundaries in security/performance/release analysis.

## Next work
Use Balance Loop. F004 now closes the first scheduling/synchronization prerequisite block exposed by Q003/D006. Strong next candidates are to continue F004 with condition/signaling and bounded liveness failures if the professional boundary remains productive, or move to `F005` async/event-loop/futures/cancellation because Dart/Flutter and D006 depend heavily on those semantics. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
