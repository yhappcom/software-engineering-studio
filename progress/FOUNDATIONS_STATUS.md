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

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md`.

Established mutual exclusion/ordering/progress distinctions, circular-wait preconditions and lock-order alternative, plus notification-vs-durable-predicate signaling. CPython evidence is not Dart runtime evidence.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`  
Fixtures: `research/foundations/fixtures/F005_async_timeout_cancellation_model.py`, `research/foundations/fixtures/F005_async_ordering_cleanup_model.py`

Established from current Dart sources plus bounded Python 3.13.5/Linux model evidence:
- Dart isolate async work is event-loop based; Future/await does not imply generic thread creation;
- Future completion, caller waiting, timeout and cancellation are distinct semantics;
- waiter timeout can precede a later underlying side effect when work remains active;
- cancellation requires the exact API/operation contract;
- documented queue relations (for example Dart microtasks before zero-delay Future event execution) must be distinguished from incidental observed callback/timer order;
- catching an async failure does not itself perform resource cleanup;
- a bounded failure left modeled resource state open after the error was caught, while a `finally` alternative closed it and satisfied the independent cleanup oracle.

OPEN: direct Dart Future/event/microtask execution, exact Dart cancellation-capable API execution, Flutter scheduler/lifecycle interaction, streams/backpressure, cancellation-during-cleanup and native/process-death behavior.

## Remaining initial queue
- `F002` — Values, references, memory models, stack/heap and lifetime.
- `F003` — Data structures, algorithms and complexity.
- `F004` — IN STUDY / two blocks.
- `F005` — IN STUDY / two blocks.
- `F006` — OS/file/socket/network foundations.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when useful. Stage 1 remains NOT PASS.

## Dependencies / handoffs
- Mobile: direct Dart/Flutter ordering and scheduler evidence remains required; do not transfer CPython queue behavior.
- Data: D006 must separate timeout, operation terminal state and cleanup; retries can overlap active or incompletely cleaned prior work.
- Quality: Q003 should use explicit event-order traces plus state/resource terminal oracles.
- Architecture: async error/cancellation/cleanup/ordering are contracts where consumer-visible.
- Systems: abandoned resources/work are future reliability/performance boundaries.

## Next work
Use Balance Loop. F005 now has two coherent mechanism/failure blocks. Further Foundation depth should not become queue trivia without Dart execution. Strong independent next candidates are `Q003` explicit async event-order matrices using F005 vocabulary, `D006` late-completion/reorder/tombstone semantics, or `F006` networking foundations if it becomes the stronger prerequisite. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
