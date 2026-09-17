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

Canonical: `research/foundations/F005_async_event_loop_futures_cancellation.md`.

Established Future/wait/timeout/cancellation distinctions plus ordering/error/cleanup boundaries from current Dart sources and bounded Python model evidence. Direct Dart/Flutter execution remains OPEN.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — two integrated Foundation blocks complete**

Canonical: `research/foundations/F006_os_file_socket_network_foundations.md`  
Fixtures: `research/foundations/fixtures/F006_stream_framing_boundary.py`, `research/foundations/fixtures/F006_connection_termination_ambiguity.py`

Established from RFC 9293, socket semantics and bounded Python 3.13.5/Linux execution:
- stream transport bytes and application frame boundaries are distinct;
- buffered framing is required when protocol messages need explicit boundaries;
- graceful EOF after `00 05 HE` left a declared five-byte payload incomplete and must not publish a valid frame;
- an abortive loopback TCP close delivered the complete `00 05 HELLO` frame to the receiver before `ConnectionResetError` in the bounded environment;
- therefore reset does not prove that zero application bytes were received, and neither reset nor EOF establishes business-operation apply/durable-commit state;
- local send, peer receive, frame completion, apply, durable commit and application ACK remain separate claims.

Evidence limit: local Linux sockets only; abortive-close sequencing is OS/socket-stack dependent. No Dart Socket/Flutter, real network partition, cross-OS/mobile/TLS/multi-device or production claim.

## Remaining initial queue
- `F002` — Values, references, memory models, stack/heap and lifetime.
- `F003` — Data structures, algorithms and complexity.
- `F004` — IN STUDY / two blocks.
- `F005` — IN STUDY / two blocks.
- `F006` — IN STUDY / two blocks.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when useful. Stage 1 remains NOT PASS.

## Dependencies / handoffs
- Mobile: direct Dart/Flutter execution and exact mobile networking/background evidence remain required; do not transfer Linux socket behavior as Dart/mobile runtime proof.
- Data: D006 should keep logical operation identity and explicit application ACK/durable state above ambiguous connection failures.
- Quality: Q005/Q006 should isolate EOF-before-frame, reset-after-complete-frame, timeout and late ACK as distinct failure classes.
- Architecture: framing, terminal state, timeout and acknowledgement are contracts where consumer-visible.
- Systems: TLS/authentication, socket/resource exhaustion and network performance remain separate security/performance concerns.

## Next work
Use Balance Loop. F006 now covers framing plus graceful/abortive termination ambiguity at a bounded executable level. Further local socket elaboration has diminishing Foundation value until Dart/mobile or real-network transfer is available. Strong independent candidates are `Q006` fault injection/recovery/regression governance, `M002` lifecycle/process-death/background execution with authoritative platform evidence, or untouched `F002/F003` if their prerequisite leverage wins. Direct Dart/Flutter execution remains the first attempt whenever a trustworthy SDK environment becomes available.
