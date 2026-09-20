# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-20

## Mission
Build language- and framework-independent understanding of how programs execute, represent data, use memory, coordinate concurrency, interact with operating systems, and communicate over networks.

## Active evidence

### F001 — Program Execution Foundations
Status: **IN STUDY — DIRECT DART JIT/AOT + FLUTTER HOST→CHROME RUNTIME TRANSFER VALIDATED.** Hosted run `35423963687` validates Dart JIT, AOT compilation and AOT execution after fixture root-cause/fix/regression. Run `35426881450` validates first Flutter framework/test-binding execution. Exact workflow head `b547c5d564731521eaf49380492fd10b5a980df9`, run `35478966848`, job `105993130270` completed success: identity capture, dependency resolution, the existing host Flutter widget oracle, and the same oracle under `flutter test --platform chrome` all succeeded. Canonical transfer record: `research/foundations/F001_flutter_chrome_runtime_transfer.md`. This is bounded hosted browser-test-runtime evidence, not PWA/Safari/native/product/release evidence.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY — DIRECT DART IDENTITY/ALIAS/FINAL-BINDING + EXPLICIT RESOURCE-CLOSE TRANSFER VALIDATED.** Canonical base: `research/foundations/F002_values_references_memory_lifetime.md`; direct transfer: `research/foundations/F002_direct_dart_identity_resource_lifetime_transfer.md`. Run `35455279567`, job `105929339080`, exact head `d6bc8629f18b2ec8b7f8fb86849e7682f7ff36c2` succeeded on requested Dart 3.13.3 hosted Ubuntu. GC/finalizer timing, JIT/AOT equivalence, native mobile/browser and product transfer remain OPEN.

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY — DIRECT DART QUEUE/REPRESENTATION TRANSFER VALIDATED.** Canonical: `research/foundations/F003_data_structures_algorithms_complexity.md`. Run `35458320697`, job `105937470606`, exact fixture head `68d5b64c12f8a201a64e8c8332fae73c498242db` succeeded on requested Dart 3.13.3 hosted Ubuntu. The fixture validates FIFO semantic equivalence for growable `List.removeAt(0)` versus `ListQueue.removeFirst()` across a bounded size sweep using an independent closed-form checksum. Timing output is diagnostic only and is not used as a complexity oracle. Space cost, broader search/hash behavior and Flutter/product performance transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — DIRECT DART ISOLATE TRANSFER ADDED.** Run `35432075163`, job `105868357618`, exact head `491887c4f20b2146026629984f43d25f19e949f4` succeeded with Dart 3.13.3, isolate-owned mutable state and a negative sendability case.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — DIRECT DART TRANSFER ADDED.** Run `35429564591`, job `105861592799`, exact head `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` validates bounded async ordering, waiter-timeout ≠ source-cancellation and API-specific subscription cancellation.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — TRANSPORT SEMANTIC ORACLES PASS; COMBINED NATURAL PROCESS EXIT FAILS; ONE-SHOT LISTENER HYPOTHESIS FALSIFIED; ROOT CAUSE OPEN.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md`, `research/foundations/F006_process_liveness_phase_isolation.md`.

Recovered decoded logs for exact head `835104ea9dac410b4f0a4d17f748882710f5921c`, run `35437455712`, job `105882433731` show Dart 3.13.3 emitted the semantic PASS marker and then remained alive until the independent one-minute deadline.

The structurally different alternative at exact head `3904ca9806d8e48bb90b5f6019acbdffc60feffb`, run `35484021836`, job `106006913686` also failed natural exit. Its decoded log completed every phase through `F006_DART_SOCKET_PASS` and `natural_process_exit_expected` before timing out. Replacing open-ended `ServerSocket.listen` with `server.first`, awaiting server close and bounding endpoint operations therefore did not fix liveness. The listener-ownership hypothesis is falsified at this target; no specific retained resource is yet established.

A four-way phase-isolated A/B fixture now separates server-only close, accepted connection close, truncated EOF and refused-connect cases. Exact workflow head `75ba5067f8b173cc2ce8e7fdf7a7effb2e9dcefe`, run `35486660067` is pending. Do not award root cause or regression PASS before per-case terminal evidence.

## Gate assessment
Foundation PASS is **not** awarded. F001-F005 have bounded direct Dart and/or Flutter execution evidence appropriate to their current claims. F006 has positive bounded transport-semantic evidence plus reproducible post-oracle process-liveness failure across two combined fixture structures. The first listener-lifecycle causal hypothesis is now falsified; retained-resource root cause and successful natural-exit regression remain OPEN. Native mobile/product transfer remains materially open, and F003 still lacks space/broader algorithm/product-resource evidence.

## Dependencies / handoffs
- **Architecture/Data:** F002 directly demonstrates binding immutability/shallow-copy ownership boundaries; F003 supplies the source-backed `operation → representation → primitive cost → workload` model for structure/index/cache choices.
- **Mobile:** F001 Chrome success establishes only a bounded Flutter/browser test-runtime transfer; it does not establish Service Worker/PWA lifecycle, Safari/iPadOS/EFB, Android/iOS, or product behavior. M006 remains the stronger browser lifecycle evidence.
- **Systems/Quality:** F001 records runtime/browser identity before comparing the same oracle across host and Chrome targets; a green host step cannot substitute for the browser verdict, and browser-test success cannot substitute for release artifact provenance.
- **Mobile:** F003 does not establish Flutter frame-budget impact; require Flutter/device/browser execution for performance claims.
- **Mobile/Systems:** F002 explicit `dart:io` close is a bounded hosted-native resource contract; do not transfer it to lifecycle cleanup, browser behavior or GC/finalizer timing.
- **Quality/Systems:** both F006 combined runs are semantic-oracle PASS + executable-process-liveness FAIL. Preserve independent CI deadlines and treat the falsified listener hypothesis as debugging evidence rather than hiding it.
- **Data:** do not infer application durable completion from transport termination.

## CHANGE WATCH / OPEN
- Flutter/Dart/browser toolchains are version-sensitive; preserve exact ref/SDK/browser/run identity.
- F001 host→Chrome browser-test-runtime transfer is validated at run `35478966848`; native Android/iOS, Safari/iPadOS/EFB, PWA lifecycle, release/product runtime and physical-device evidence remain OPEN.
- The F001 workflow captured exact Flutter/Dart/Chrome/device version strings, but current connector evidence does not expose command stdout; do not fabricate those strings.
- F002 WeakReference/Finalizer timing, JIT/AOT equivalence and platform transfer remain OPEN.
- F003 space cost, broader search/hash behavior and product/platform performance transfer remain OPEN.
- F006 transport semantics are positive, but combined natural process exit fails under both original and one-shot-listener structures; exact retained-resource root cause remains OPEN.
- F006 A/B run `35486660067` is pending; use its per-case liveness outcomes to select the next causal test.
- F004 external-resource/process-failure/fairness/platform transfer and F005 backpressure/error/concrete I/O cancellation/platform transfer remain OPEN.

## Next work
Recover run `35486660067` first. If an isolated case hangs, use that smallest case for causal investigation. If all isolated cases exit, build the smallest composition that reproduces the combined hang. Do not return to blind close-order/listener permutations. After this professional boundary is resolved or genuinely blocked, return to Balance Loop for native/platform/product evidence or S004 when authorized source acquisition becomes available.
