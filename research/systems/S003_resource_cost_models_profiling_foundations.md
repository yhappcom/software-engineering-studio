# S003 — CPU, Memory, I/O, Network Cost Models & Profiling Foundations

Status: **IN STUDY — first integrated executable Foundation block complete**  
Evidence date: 2026-09-18

## Problem / scope

Performance is not one scalar property. A program can be CPU-bound, waiting on I/O/timers, allocation-heavy, memory-retentive, network-latency-bound, throughput-limited, or constrained by a platform budget. This block establishes the minimum measurement discipline needed before optimizing or transferring asymptotic reasoning into product performance claims.

## SOURCE

- Python `time.perf_counter()` / `perf_counter_ns()` provide a high-resolution performance counter for elapsed-duration measurement; only differences between readings are meaningful. Python 3.13 uses the same monotonic clock for `perf_counter` and `monotonic` in CPython.
- Python `time.process_time()` / `_ns()` measure system + user CPU time consumed by the current process and exclude time elapsed during sleep.
- Python `tracemalloc` traces Python-managed memory allocations and can report current/peak traced allocation. Its scope is traced Python allocations, not total process RSS, native allocations, GPU memory, OS page-cache use, or platform-wide pressure.
- Linux `/proc` exposes process-specific kernel information and is a platform-specific observation surface, not a portable application contract.

## SYNTHESIS — resource model

Use this chain:

`user/system workload → operation mix → algorithm/representation → CPU work + allocation/retention + I/O waits/bytes + network waits/bytes → runtime/OS scheduling & caching → observed latency/throughput/resource use → user/product budget`

Keep these dimensions separate:

- **latency / wall time** — elapsed time seen across work and waiting;
- **CPU time** — processor time charged to the process/thread according to the selected measurement API;
- **memory allocation** — bytes/objects allocated in the observed allocator domain;
- **retained/live memory** — memory still reachable/held at an observation point;
- **peak memory** — maximum observed usage in a specified measurement domain;
- **I/O volume/waits** — bytes/operations plus time blocked or queued;
- **network latency/throughput** — transport/application path behavior, not reducible to CPU alone;
- **energy/thermal/frame/startup budgets** — platform/product constraints requiring their own instrumentation.

## ENGINEERING JUDGMENT

Optimization starts with a falsifiable bottleneck hypothesis and a measurement surface capable of observing that resource. Choosing a faster algorithm without showing that the algorithm dominates the relevant budget is not yet a performance diagnosis.

Asymptotic complexity from F003 and measured profiling are complementary. Complexity predicts growth under a model; profiling observes a particular workload, implementation, runtime and environment. Neither substitutes for the other.

## EXECUTABLE VALIDATION

Fixture: `research/systems/fixtures/S003_resource_cost_profiling.py`

Environment:
- Python 3.13.5
- Linux container environment
- evidence date 2026-09-18

### Claim
Elapsed time, CPU time and traced allocation are distinct observables; a single wall-time number cannot identify the resource bottleneck.

### Oracle
The fixture uses three deliberately different workloads:
1. CPU arithmetic;
2. an 80 ms sleep/wait;
3. approximately 5 MiB of Python-managed bytearray allocation.

Independent properties:
- wait wall time >= 70 ms;
- wait CPU time < one quarter of wait wall time;
- allocation workload traced peak > 4000 KiB;
- CPU workload CPU time > 5× wait CPU time.

### Observation
One execution produced:

| Workload | Wall ms | CPU ms | Peak traced Python KiB |
| --- | ---: | ---: | ---: |
| CPU work | 345.435 | 345.408 | 0.516 |
| wait work | 80.203 | 0.098 | 0.125 |
| memory work | 8.542 | 8.537 | 5319.660 |

All declared assertions passed.

### VALIDATION verdict
The bounded fixture supports the claim that wall duration, CPU consumption and traced Python allocation answer different questions. The wait workload had substantial elapsed time with negligible process CPU; the memory workload exposed a large traced-allocation peak despite short elapsed duration; CPU work had wall and process CPU time close in this run.

## FAILURE / ROOT-CAUSE BOUNDARY

A deliberately invalid shortcut would diagnose the 80 ms wait as "80 ms of CPU work" from wall time alone. The CPU-time observation falsifies that explanation for this fixture. Conversely, low CPU time does not by itself prove disk/network I/O; this fixture knows the causal intervention was `sleep`, but a production observation would need additional I/O/network evidence before assigning root cause.

Likewise, `tracemalloc` peak is not process RSS. Treating it as total memory consumption would exceed the tool's measurement domain.

## ALTERNATIVES / TRADE-OFFS

- Wall-clock timers answer end-to-end elapsed-duration questions but conflate computation and waiting.
- Process/thread CPU clocks isolate charged CPU time but omit waiting and do not identify which code path consumed it without a profiler.
- Allocation tracing can locate allocator-domain pressure but adds overhead and can miss native/external memory.
- Sampling profilers reduce instrumentation burden and locate hot stacks statistically, but require sampling-rate/overhead interpretation.
- Event tracing and OS/platform profilers can connect scheduling, I/O, rendering and native work, but evidence is platform/tool/version specific.

## Invalid shortcuts

Do not equate:
- one benchmark run with performance truth;
- wall time with CPU time;
- low CPU with proof of network/disk bottleneck;
- allocation bytes with retained memory;
- traced Python memory with total RSS;
- average latency with tail latency;
- microbenchmark improvement with user-visible/product improvement;
- simulator/container behavior with mobile-device production behavior;
- asymptotic complexity with measured constant-factor performance.

## RELATED DOMAIN CHECK

- **Foundations:** F003 complexity directly reused; F005/F006 explain waiting/async/network boundaries.
- **Architecture:** performance becomes architectural when budgets/SLOs depend on cross-boundary structure or resource ownership.
- **Mobile:** frame, startup, background, thermal and memory-pressure transfer requires Flutter/Android/iOS tooling; currently OPEN.
- **Data:** indexes, serialization, transactions, cache and sync can shift CPU/memory/I/O/network costs; no Data canonical conclusion changed.
- **Quality:** performance evidence needs workload, environment, oracle/budget and reproducibility; regression thresholds need noise discipline.
- **Systems:** canonical owner of profiling/resource measurement.
- **Design Studio:** not materially relevant to this bounded mechanism block; user-perceived responsiveness transfer is future work.
- **Web Manager:** not materially relevant; browser/PWA performance transfer is future work.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no product implementation was audited; no MintTap/LogMate performance claim is made.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** direct Dart/Flutter profiling; `dart` and `flutter` executables remain unavailable on 2026-09-18.
- **OPEN:** sampling profiler vs instrumentation comparison; process RSS/native allocation; disk and real-network measurements; tail latency and throughput distributions.
- **OPEN:** Android/iOS physical-device CPU/memory/frame/startup/thermal evidence and Flutter DevTools transfer.
- **VALIDATION:** repeat controlled runs and quantify variance before defining any regression threshold.
- **TRANSFER VALIDATION:** reproduce resource separation and bottleneck diagnosis using Dart/Flutter plus exact mobile/web product artifacts when environments become available.
- **CHANGE WATCH:** profiler/tool/runtime measurement semantics and platform performance tooling are version-sensitive.

## HANDOFFS

- **Foundations/F003 → Systems/S003:** preserve complexity as predictive model; do not promote benchmark timings into complexity proofs.
- **Quality:** future performance regression tests should bind exact artifact/environment/workload, use a product budget as oracle, preserve distributions/noise, and verify deliberate performance regressions where feasible.
- **Mobile:** when Flutter/Android/iOS tooling is available, transfer-test CPU vs elapsed wait, allocation/retention, frame/startup and platform memory-pressure observations rather than importing Python constants.
- **Data:** when evaluating index/cache/sync alternatives, record which resource dimension moved; a latency win can trade memory, writes or network bytes.
