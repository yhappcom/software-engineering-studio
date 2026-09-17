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
- documented queue relations must be distinguished from incidental observed callback/timer order;
- catching an async failure does not itself perform resource cleanup.

OPEN: direct Dart Future/event/microtask execution, exact Dart cancellation-capable API execution, Flutter scheduler/lifecycle interaction, streams/backpressure, cancellation-during-cleanup and native/process-death behavior.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — first integrated Foundation block complete**

Canonical: `research/foundations/F006_os_file_socket_network_foundations.md`  
Fixture: `research/foundations/fixtures/F006_stream_framing_boundary.py`

Established from RFC 9293, POSIX/Python socket semantics and bounded Python 3.13.5/Linux socket execution:
- stream transport bytes and application message/frame boundaries are distinct;
- a one-byte receive left a two-byte application header incomplete; a buffered length-prefixed parser reconstructed the frame correctly;
- local send completion, peer receipt, parse, application apply, durable commit and application acknowledgement are distinct claims;
- framing failure must not be misdiagnosed as transport data loss merely because one receive call returned less than an application frame;
- the result is local `SOCK_STREAM` evidence, not Dart Socket, real TCP partition, mobile network or production evidence.

OPEN: direct Dart/Flutter socket execution, TCP/reset/half-close/timeout/partition experiments, DNS/IP/routing/UDP contrast, mobile connectivity/background behavior, TLS/security and resource/performance boundaries.

## Remaining initial queue
- `F002` — Values, references, memory models, stack/heap and lifetime.
- `F003` — Data structures, algorithms and complexity.
- `F004` — IN STUDY / two blocks.
- `F005` — IN STUDY / two blocks.
- `F006` — IN STUDY / first socket-framing block.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when useful. Stage 1 remains NOT PASS.

## Dependencies / handoffs
- Mobile: direct Dart/Flutter execution and exact mobile networking/background evidence remain required; do not transfer CPython socket behavior as Dart runtime proof.
- Data: D006 should place logical operation identity/retry above transport framing and distinguish write/receive/parse/apply/durable commit/ACK.
- Quality: Q005/Q006 should isolate truncated frame, EOF, timeout/reset, late ACK and retry as distinct failure classes.
- Architecture: framing, timeout, acknowledgement and cancellation are contracts where consumer-visible.
- Systems: TLS/authentication, socket/resource exhaustion and network performance remain separate security/performance concerns.

## Next work
Use Balance Loop. F006 removed the untouched networking prerequisite at a bounded stream/framing level. The strongest continuation is a second F006 block on connection termination/timeout/partial-delivery ambiguity if it can add executable failure evidence; otherwise Q006 fault injection/recovery governance or M002 lifecycle/process-death evidence may outrank it. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
