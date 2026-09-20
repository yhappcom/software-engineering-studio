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
Status: **IN STUDY — DIRECT DART QUEUE/REPRESENTATION TRANSFER VALIDATED.** Canonical: `research/foundations/F003_data_structures_algorithms_complexity.md`. Run `35458320697`, job `105937470606`, exact fixture head `68d5b64c12f8a201a64e8c8332fae73c498242db` succeeded on requested Dart 3.13.3 hosted Ubuntu. The fixture validates FIFO semantic equivalence for growable `List.removeAt(0)` versus `ListQueue.removeFirst()` across a bounded size sweep using an independent closed-form checksum. Dart API source separately establishes `ListQueue` cyclic-buffer constant-time remove semantics and `ListBase.removeAt` later-element movement. Timing output is diagnostic only and is not used as a complexity oracle. Space cost, broader search/hash behavior and Flutter/product performance transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — DIRECT DART ISOLATE TRANSFER ADDED.** Run `35432075163`, job `105868357618`, exact head `491887c4f20b2146026629984f43d25f19e949f4` succeeded with Dart 3.13.3, isolate-owned mutable state and a negative sendability case.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — DIRECT DART TRANSFER ADDED.** Run `35429564591`, job `105861592799`, exact head `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` validates bounded async ordering, waiter-timeout ≠ source-cancellation and API-specific subscription cancellation.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — DIRECT DART SOCKET HARNESS FAILURE CONTAINED; SOCKET VERDICT/ROOT CAUSE OPEN.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md`. Run `35437455712`, job `105882433731`, validates independent CI containment after the first close-order hypothesis was falsified. Command-level fixture output remains unavailable; exact blocking/resource-retention phase and socket correctness remain OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001-F005 have bounded direct Dart and/or Flutter execution evidence appropriate to their current claims, and F001 now includes a successful host→Chrome test-runtime transfer. F006 has failure→hypothesis→falsification plus executable outer containment but no transport verdict. Native mobile/product transfer remains materially open, and F003 still lacks space/broader algorithm/product-resource evidence.

## Dependencies / handoffs
- **Architecture/Data:** F002 directly demonstrates binding immutability/shallow-copy ownership boundaries; F003 supplies the source-backed `operation → representation → primitive cost → workload` model for structure/index/cache choices.
- **Mobile:** F001 Chrome success establishes only a bounded Flutter/browser test-runtime transfer; it does not establish Service Worker/PWA lifecycle, Safari/iPadOS/EFB, Android/iOS, or product behavior. M006 remains the stronger browser lifecycle evidence.
- **Systems/Quality:** F001 records runtime/browser identity before comparing the same oracle across host and Chrome targets; a green host step cannot substitute for the browser verdict, and browser-test success cannot substitute for release artifact provenance.
- **Mobile:** F003 does not establish Flutter frame-budget impact; require Flutter/device/browser execution for performance claims.
- **Mobile/Systems:** F002 explicit `dart:io` close is a bounded hosted-native resource contract; do not transfer it to lifecycle cleanup, browser behavior or GC/finalizer timing.
- **Quality:** preserve F006 as failure→hypothesis→falsification→outer-containment evidence; target-level timeouts are not sufficient harness controls.
- **Data:** do not infer application completion from transport termination.

## CHANGE WATCH / OPEN
- Flutter/Dart/browser toolchains are version-sensitive; preserve exact ref/SDK/browser/run identity.
- F001 host→Chrome browser-test-runtime transfer is validated at run `35478966848`; native Android/iOS, Safari/iPadOS/EFB, PWA lifecycle, release/product runtime and physical-device evidence remain OPEN.
- The F001 workflow captured exact Flutter/Dart/Chrome/device version strings, but current connector evidence does not expose command stdout; do not fabricate those strings.
- F002 WeakReference/Finalizer timing, JIT/AOT equivalence and platform transfer remain OPEN.
- F003 space cost, broader search/hash behavior and product/platform performance transfer remain OPEN.
- F006 direct Dart socket verdict/root cause is OPEN; exact blocking phase is not isolated.
- F004 external-resource/process-failure/fairness/platform transfer and F005 backpressure/error/concrete I/O cancellation/platform transfer remain OPEN.

## Next work
Return to Balance Loop. Do not repeat the same F001 host/Chrome oracle now that the named transfer is closed. Prefer a materially stronger evidence class: native Android/iOS or Safari/iPadOS/EFB execution, canonical product runtime/build when exact-ref access exists, storage/physical-connectivity boundary, natural release/ADR lifecycle, or F006 root cause only when a phase-isolating harness is available. Resume S004 exact LogMate source build immediately if authorized exact-ref source acquisition becomes available.