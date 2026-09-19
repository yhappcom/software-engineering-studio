# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-19

## Mission
Build language- and framework-independent understanding of how programs execute, represent data, use memory, coordinate concurrency, interact with operating systems, and communicate over networks.

## Active evidence

### F001 — Program Execution Foundations
Status: **IN STUDY — DIRECT DART JIT/AOT + FIRST FLUTTER FRAMEWORK EXECUTION VALIDATED**. Hosted run `35423963687` validates Dart JIT, AOT compilation and AOT execution after fixture root-cause/fix/regression. Run `35426881450` validates first Flutter framework/test-binding execution. Native/browser/product runtime remains separate.

### F002 — Values, references, memory models, stack/heap and lifetime
Status: **IN STUDY**. Python aliasing/lifetime evidence and Dart source model retained; direct Dart identity/alias/final-binding/resource-lifetime transfer remains OPEN.

### F003 — Data structures, algorithms and complexity
Status: **IN STUDY**. Bounded queue/complexity evidence retained; direct Dart structures/complexity, space cost and broader product/runtime transfer remain OPEN.

### F004 — Processes, threads, scheduling, synchronization and concurrency hazards
Status: **IN STUDY — DIRECT DART ISOLATE TRANSFER ADDED.** Run `35432075163`, job `105868357618`, exact head `491887c4f20b2146026629984f43d25f19e949f4` succeeded with Dart 3.13.3, isolate-owned mutable state and a negative sendability case.

### F005 — Async execution, event loops, futures, streams and cancellation
Status: **IN STUDY — DIRECT DART TRANSFER ADDED.** Run `35429564591`, job `105861592799`, exact head `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` validates bounded async ordering, waiter-timeout ≠ source-cancellation and API-specific subscription cancellation.

### F006 — OS, file, socket and network foundations
Status: **IN STUDY — DIRECT DART SOCKET HARNESS FAILURE CONTAINED; SOCKET VERDICT/ROOT CAUSE OPEN.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md`.

Initial run `35434862199` reached the Dart socket fixture and hung. Commit `6f78f6ee8ccda32143df55d2a7f3820a117cc5c7` changed close ordering and added five-second Future timeouts, but regression run `35434895889` again remained in the fixture step. **CONTRADICTION / FALSIFICATION:** close-order alone is not an adequate root cause.

Commit `835104ea9dac410b4f0a4d17f748882710f5921c` added independent CI deadlines. **VALIDATION:** run `35437455712`, job `105882433731`, completed `failure`; setup/Dart/environment steps succeeded and the fixture step terminated as failure after roughly 73 seconds rather than remaining unbounded. This closes the harness-containment rung only. Command-level fixture output remains unavailable in the current evidence channel, so the exact blocking/resource-retention phase and socket correctness remain OPEN.

## Gate assessment
Foundation PASS is **not** awarded. F001 has direct Dart JIT/AOT plus first Flutter framework execution; F004/F005 have direct Dart transfer. F006 now has failure→hypothesis→falsification plus executable outer containment, but no transport verdict. F002/F003 remain selectively open and native mobile/browser/product platform evidence is separate.

## Dependencies / handoffs
- **Mobile:** consume direct Flutter/Dart evidence only at stated boundaries; `dart:io` cannot transfer to browser/PWA and F006 has no socket PASS.
- **Quality:** preserve F006 as failure→hypothesis→falsification→outer-containment evidence; target-level timeouts are not sufficient harness controls.
- **Data:** do not infer application completion from transport termination.
- **Systems:** exact workflow/run/job/toolchain identity belongs with executable evidence; independent CI termination is an evidence-pipeline control.
- **Architecture:** isolate ownership and timeout/cancellation/cleanup remain observable contract concerns where consumer-visible.

## CHANGE WATCH / OPEN
- Flutter/Dart toolchain behavior is version-sensitive; preserve exact ref/SDK/run identity.
- Hosted Linux evidence is not release-AOT native app, Android/iOS lifecycle, browser/PWA or physical-device evidence.
- F002/F003 still have direct Dart/runtime transfer gaps where runtime semantics materially matter.
- F006 direct Dart socket verdict/root cause is OPEN; exact blocking phase is not isolated.
- F004 external-resource/process-failure/fairness/platform transfer and F005 backpressure/error/concrete I/O cancellation/platform transfer remain OPEN.

## Next work
Do not repeat F006 close-order variants. If F006 resumes, split phases into independently observable processes/steps or use an external supervisor capable of preserving phase output before termination. Balance Loop should now prefer a higher-leverage independent evidence class—especially exact canonical LogMate toolchain + lock enforcement + build + artifact identity—or a remaining F002/F003 prerequisite if it outranks product transfer.
