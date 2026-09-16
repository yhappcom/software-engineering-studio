# F001 — Program Execution Foundations

Status: **IN STUDY — SOURCE/MODEL + FIRST EXECUTABLE BOUNDARY EVIDENCE**
Date: 2026-09-16
Lead: Computer Science & Programming Foundations

## Problem

Before reasoning about Flutter state, persistence, background work, testing, performance, or release behavior, the Studio needs a precise execution model separating:

`source/program description → translation/compilation → runtime → OS process → memory/resources → I/O/platform services`.

Framework language often collapses these boundaries and causes incorrect assumptions such as “Flutter is the runtime”, “AOT means no runtime”, or “cross-platform framework behavior is an OS guarantee”.

## SOURCE

Primary sources checked:

- Dart overview — https://dart.dev/overview
- `dart compile` — https://dart.dev/tools/dart-compile
- `dartaotruntime` — https://dart.dev/tools/dartaotruntime
- Dart SDK overview — https://dart.dev/tools/sdk
- Flutter architectural overview — https://docs.flutter.dev/resources/architectural-overview

Current Dart documentation reports SDK examples against Dart 3.13.3 as of this study date.

## First-principles model

### 1. Source code is not the running program

Source is a representation consumed by a toolchain. The execution artifact depends on target and mode.

For Dart native targets, official documentation distinguishes:

- development using a Dart VM and JIT compilation;
- production AOT compilation to native machine code;
- AOT snapshots that are executed by `dartaotruntime`;
- architecture-specific JIT/AOT artifacts.

For Dart web targets, Dart source is translated to JavaScript or WebAssembly rather than using the same native runtime path.

### 2. AOT does not mean “no runtime”

Dart documentation explicitly describes AOT-compiled native code as running inside the Dart runtime, which still provides language/runtime services including memory management and type-system support.

Therefore:

`compiled to machine code` ≠ `runtime disappears`.

This distinction matters for startup, memory behavior, FFI, garbage collection, diagnostics, and platform integration.

### 3. Flutter is a layered execution system

Official Flutter architecture separates:

- app-owned Dart code;
- Flutter framework;
- Flutter engine;
- platform embedder;
- platform runner/package;
- underlying OS.

The engine provides low-level services including a Dart runtime, graphics/text primitives, and file/network I/O support. The embedder coordinates with the OS for rendering surfaces, accessibility, input, and event-loop integration.

A useful engineering model is therefore:

`app Dart code → Flutter framework → engine/Dart runtime → platform embedder/runner → OS services`.

This is not identical on web, where Dart/Flutter code is compiled to JavaScript or Wasm and browser execution replaces the native-app runtime boundary.

### 4. A process boundary is stronger than a function/module boundary

At the operating-system level, independently executing processes have distinct process identities and communicate through explicit mechanisms such as I/O streams, files, sockets, shared memory, or platform IPC rather than ordinary in-process calls.

This matters later for isolates, background services, app process death, plugins, external helpers, testing, and synchronization design.

## EXECUTABLE VALIDATION 1 — process + I/O boundary

Fixture: `research/foundations/fixtures/F001_process_boundary.py`

Environment used for this first bounded test:

- Python 3.13.5
- Linux 6.18.44 x86_64

Observed output:

```text
parent_pid=371
child_returncode=7
captured_stdout='child_pid=386\nchild_stdout'
captured_stderr='child_stderr'
```

What this establishes:

- the child is a distinct OS process (`PID 386` vs parent `PID 371`);
- exit status crosses the process boundary explicitly (`7`);
- stdout and stderr are separate I/O channels that the parent can capture;
- the parent does not receive the child's ordinary local variables or call stack as in-process state.

What this **does not** establish:

- Dart VM process semantics;
- Dart isolate semantics;
- Flutter engine thread behavior;
- Android/iOS lifecycle/process-death behavior.

Those remain separate validation obligations.

## Failure / misconception analysis

### Misconception: “JIT is interpreted, AOT is native, therefore they are completely different programs”

The better distinction is toolchain/execution mode. Both preserve Dart language semantics while using different compilation timing and artifacts; runtime services still matter on native AOT.

### Misconception: “Flutter owns everything below the widget tree”

The Flutter architecture explicitly exposes engine, embedder, runner, and OS boundaries. Platform constraints remain real even when APIs are cross-platform.

### Misconception: “Hot reload tells us production behavior”

Development VM/JIT behavior and release AOT behavior serve different goals. A behavior that depends on development tooling, VM observability, incremental recompilation, or hot reload is not automatically evidence for release execution behavior.

## SYNTHESIS

For Studio work, every runtime-sensitive claim should identify at least these dimensions when material:

`language/toolchain mode → target platform → runtime/engine → OS process/thread context → resource/I/O boundary → build mode`.

This becomes a shared diagnostic frame for Mobile, Data, Quality, Systems, and Architecture work.

## RELATED DOMAIN CHECK

### Architecture
Execution boundaries constrain valid ownership and dependency assumptions. A module boundary is not equivalent to a process/runtime/platform boundary.

### Mobile
Flutter must be studied as framework + engine + embedder + OS integration. Android/iOS lifecycle and process-death behavior remain OPEN for `M001/M002`.

### Data
Durability cannot be inferred from an in-memory state change; persistence must survive relevant runtime/process failure boundaries. Reused by `D001`.

### Quality
Tests must identify build/runtime mode. A debug/JIT-only pass is insufficient for release/AOT claims. Reused by `Q001/Q002`.

### Systems
Runtime services, OS boundaries, build artifacts, and release mode are inseparable from performance/security/delivery reasoning. Reused by `S001`.

### Design Studio / Web Manager / Marketing Manager
No direct canonical claim changed in this block. Future runtime/performance/accessibility/instrumentation work should preserve the execution-context dimensions above.

## OPEN / VALIDATION

1. Run an equivalent Dart process/I/O fixture under an actual Dart SDK environment and record toolchain version.
2. Validate JIT vs AOT artifact/run path directly with `dart run`, `dart compile exe`, and/or AOT snapshot tooling.
3. In `M001`, validate Flutter debug/profile/release execution boundaries and current Android/iOS engine/embedder behavior.
4. Do not infer Dart isolates from OS child processes; isolate semantics require separate study.

## HANDOFFS

- Foundations → Mobile: use the layered execution model as the baseline for `M001`.
- Foundations → Quality: record build/runtime mode in executable evidence.
- Foundations → Data: distinguish memory-state success from process-surviving durability.
- Foundations → Systems: use runtime/process/artifact boundaries when analyzing performance/security/release behavior.

## Current judgment

`F001` has a defensible first-principles model and one executable OS-boundary validation, but is **not PASS** yet because Dart/Flutter executable validation remains open.
