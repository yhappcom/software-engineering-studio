# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-20

## Mission
Build language- and framework-independent understanding of how programs execute, represent data, use memory, coordinate concurrency, interact with operating systems, and communicate over networks.

## Active evidence

### F001 — Program Execution Foundations
Status: **IN STUDY — DIRECT DART JIT/AOT + FIRST FLUTTER FRAMEWORK EXECUTION VALIDATED**. Hosted run `35423963687` validates Dart JIT, AOT compilation and AOT execution after fixture root-cause/fix/regression. Run `35426881450` validates first Flutter framework/test-binding execution. Native/browser/product runtime remains separate.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY — DIRECT DART IDENTITY/ALIAS/FINAL-BINDING + EXPLICIT RESOURCE-CLOSE TRANSFER VALIDATED.** Canonical base: `research/foundations/F002_values_references_memory_lifetime.md`; direct transfer: `research/foundations/F002_direct_dart_identity_resource_lifetime_transfer.md`. Run `35455279567`, job `105929339080`, exact head `d6bc8629f18b2ec8b7f8fb86849e7682f7ff36c2` succeeded on requested Dart 3.13.3 hosted Ubuntu. The fixture validates direct alias identity/mutation, `final` binding versus mutable object, shallow outer-copy/nested-alias failure, explicit bounded nested-copy isolation, and explicit `dart:io` file-handle close followed by rejected use. GC/finalizer timing, JIT/AOT equivalence, native mobile/browser and product transfer remain OPEN.

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY**. Bounded queue/complexity evidence retained; direct Dart structures/complexity, space cost and broader product/runtime transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — DIRECT DART ISOLATE TRANSFER ADDED.** Run `35432075163`, job `105868357618`, exact head `491887c4f20b2146026629984f43d25f19e949f4` succeeded with Dart 3.13.3, isolate-owned mutable state and a negative sendability case.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — DIRECT DART TRANSFER ADDED.** Run `35429564591`, job `105861592799`, exact head `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` validates bounded async ordering, waiter-timeout ≠ source-cancellation and API-specific subscription cancellation.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — DIRECT DART SOCKET HARNESS FAILURE CONTAINED; SOCKET VERDICT/ROOT CAUSE OPEN.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md`. Run `35437455712`, job `105882433731`, validates independent CI containment after the first close-order hypothesis was falsified. Command-level fixture output remains unavailable; exact blocking/resource-retention phase and socket correctness remain OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001 has direct Dart JIT/AOT plus first Flutter framework execution; F002 now has direct Dart identity/alias/final-binding/explicit-close transfer; F004/F005 have direct Dart transfer. F006 has failure→hypothesis→falsification plus executable outer containment but no transport verdict. F003 direct Dart/runtime transfer and native mobile/browser/product evidence remain open.

## Dependencies / handoffs
- **Architecture/Data:** F002 now directly demonstrates in Dart that binding immutability and shallow outer copying do not establish deep ownership isolation.
- **Mobile/Systems:** F002 explicit `dart:io` close is a bounded hosted-native resource contract; do not transfer it to lifecycle cleanup, browser behavior or GC/finalizer timing.
- **Mobile:** consume direct Flutter/Dart evidence only at stated boundaries; `dart:io` cannot transfer to browser/PWA and F006 has no socket PASS.
- **Quality:** preserve F006 as failure→hypothesis→falsification→outer-containment evidence; target-level timeouts are not sufficient harness controls.
- **Data:** do not infer application completion from transport termination.
- **Systems:** exact workflow/run/job/toolchain identity belongs with executable evidence; independent CI termination is an evidence-pipeline control.

## CHANGE WATCH / OPEN
- Flutter/Dart toolchain behavior is version-sensitive; preserve exact ref/SDK/run identity.
- Hosted Linux evidence is not release-AOT native app, Android/iOS lifecycle, browser/PWA or physical-device evidence.
- F002 WeakReference/Finalizer timing, JIT/AOT equivalence and platform transfer remain OPEN; do not use nondeterministic GC timing as a PASS oracle.
- F003 still has direct Dart/runtime transfer gaps where runtime semantics materially matter.
- F006 direct Dart socket verdict/root cause is OPEN; exact blocking phase is not isolated.
- F004 external-resource/process-failure/fairness/platform transfer and F005 backpressure/error/concrete I/O cancellation/platform transfer remain OPEN.

## Next work
Do not repeat the F002 alias/final/shallow-copy fixture merely to accumulate passes. S004 exact LogMate source build remains blocked by cross-private-repository source acquisition in the Studio runner; do not repeat unauthenticated clone attempts. Balance Loop should compare F003 direct Dart structures/complexity against materially stronger native/browser/product transfer and resume S004 immediately if an authorized exact-ref execution path becomes available.
