# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-16

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

F001 is **not PASS** until sufficient Dart/runtime executable evidence exists.

## Remaining initial queue
- `F002` — Values, references, memory models, stack/heap and lifetime without oversimplified folklore.
- `F003` — Data structures, algorithms and complexity as engineering cost models.
- `F004` — Processes, threads, scheduling, synchronization and concurrency hazards.
- `F005` — Async execution, event loops, futures/promises/streams and cancellation models.
- `F006` — OS/file/socket/network foundations for application engineers.

## Gate requirement
Foundation PASS requires first-principles explanation, executable examples, representative failure cases, and transfer into at least Dart/Flutter plus one comparison context when that comparison improves understanding.

## Dependencies / handoffs
- Mobile: use F001 layered execution model in `M001`.
- Data: distinguish successful memory-state change from process-surviving durability in `D001`.
- Quality: record build/runtime mode in executable evidence.
- Systems: preserve runtime/process/artifact boundaries in security/performance/release analysis.

## Next work
First try to close the missing Dart execution evidence for `F001` when the execution environment supports it. If the required toolchain is unavailable, preserve the OPEN item rather than simulating it and let the Balance Loop advance to the highest-value independent prerequisite, likely `D001` or `M001`.
