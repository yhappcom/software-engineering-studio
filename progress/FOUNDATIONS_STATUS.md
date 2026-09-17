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

Established: mutual exclusion/ordering/progress are distinct; inconsistent multi-lock order reproduced circular-wait preconditions; global order removed the bounded cycle; condition notification is not durable semantic state; predicate-based waiting correctly observed an already-true state. CPython evidence is not Dart runtime evidence.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — first integrated Foundation block complete**

Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`  
Fixture: `research/foundations/fixtures/F005_async_timeout_cancellation_model.py`

Established from current Dart sources plus bounded Python 3.13.5/Linux model evidence:
- Dart isolate async APIs operate around an event loop; `await` suspends an async function and is not generic thread creation;
- Future completion, caller waiting, timeout and cancellation are distinct semantics;
- Dart `Future.timeout` is documented as stopping waiting after a limit, while concrete APIs such as socket connection may define their own cancellation behavior;
- a bounded asyncio comparison reproduced caller timeout followed by a later underlying side effect when the task was deliberately shielded from cancellation;
- an explicit cooperative cancellation request observed by the operation exited before the modeled side effect;
- therefore `caller stopped waiting → work stopped` is not a valid universal inference, and cancellation/cleanup must be defined by the exact operation contract.

OPEN: direct Dart Future/event/microtask execution, exact Dart cancellation-capable API execution, Flutter frame/lifecycle interaction, structured cleanup/error propagation, streams/backpressure and native/process-death behavior.

## Remaining initial queue
- `F002` — Values, references, memory models, stack/heap and lifetime without oversimplified folklore.
- `F003` — Data structures, algorithms and complexity as engineering cost models.
- `F004` — **IN STUDY / two integrated blocks complete**.
- `F005` — **IN STUDY / first integrated block complete**.
- `F006` — OS/file/socket/network foundations for application engineers.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when that comparison improves understanding.

## Dependencies / handoffs
- Mobile: use F001 layered execution model; do not transfer CPython shared-memory/async behavior to Dart/Flutter runtime.
- Data: D006 should separate caller timeout/ACK loss from operation terminal state; retry may overlap still-running prior work.
- Quality: Q003 should trace timeout, late completion, cancellation request/observation and terminal state explicitly.
- Architecture: async cancellation/timeout/cleanup are behavioral contracts where consumer-visible.
- Systems: abandoned async work/resource cleanup is a future reliability/performance boundary.

## Next work
Use Balance Loop. F005 now supplies the first async timeout/cancellation boundary needed by D006 and Q003. Strong next work is either a second F005 block on event/microtask ordering plus structured error/cleanup if trustworthy executable evidence is available, or Q003/D006 transfer using explicit async event-order matrices. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
