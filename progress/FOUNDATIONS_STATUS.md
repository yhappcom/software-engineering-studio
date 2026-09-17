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
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`  
Fixtures: `research/foundations/fixtures/F004_lock_order_deadlock.py`, `research/foundations/fixtures/F004_condition_predicate_signaling.py`

Established with current Python/Dart sources plus Python 3.13.5/Linux executable evidence:
- mutual exclusion, ordering and progress are separate concurrency properties;
- barrier-controlled workers reproduced the two-lock circular-wait precondition; global A→B lock ordering removed that bounded cycle;
- root cause is inconsistent multi-lock acquisition order, not failure of either lock primitive;
- condition notification and durable application state are separate: `notify()` before a waiter existed was not retained for that future waiter, while the protected `ready=True` predicate remained true;
- a later raw `wait(timeout)` therefore timed out even though semantic readiness already held;
- `wait_for(predicate)` correctly observed the already-true predicate without requiring a new notification;
- synchronization protocols should protect and test semantic predicates/state rather than treating wakeup receipt as authority;
- current Dart docs establish isolate-local memory/message-passing semantics, but CPython lock/condition evidence is not Dart/Flutter runtime evidence.

OPEN: direct Dart isolate/message execution, starvation/fairness boundaries, process-vs-thread comparison, and F005 async/event-loop/cancellation semantics.

## Remaining initial queue
- `F002` — Values, references, memory models, stack/heap and lifetime without oversimplified folklore.
- `F003` — Data structures, algorithms and complexity as engineering cost models.
- `F004` — **IN STUDY / two integrated blocks complete**.
- `F005` — Async execution, event loops, futures/promises/streams and cancellation models.
- `F006` — OS/file/socket/network foundations for application engineers.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when that comparison improves understanding.

## Dependencies / handoffs
- Mobile: use F001 layered execution model in `M001`; do not transfer CPython shared-memory locks/conditions to Dart isolates.
- Data: D006 should separate durable operation/state from notification/ack events as well as ordering, progress and convergence.
- Quality: Q003 should classify missed signaling/state-vs-event misuse separately from races/deadlock and use bounded failure probes.
- Architecture: synchronization predicates follow explicit ownership/invariant contracts from A002/A003.
- Systems: preserve runtime/process/artifact boundaries in concurrency evidence.

## Next work
Use Balance Loop. F004 now has coherent lock-order and condition/predicate signaling evidence. Further starvation/fairness work is useful but lower leverage than `F005` async/event-loop/futures/cancellation, which directly underpins Dart/Flutter execution, D006 synchronization and Q003 ordering/flakiness. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
