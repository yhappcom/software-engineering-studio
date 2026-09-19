# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + first Flutter framework execution validated; F005 direct Dart async transfer validated; F002/F003/F004/F006 transfer OPEN |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change + natural LogMate evolution transfer; A006 decision governance evidence |
| Mobile | Stage 1 IN STUDY — M001 first direct Flutter framework execution; M002-M006 professional/model boundaries; native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 exact-ref LogMate dependency/toolchain transfer; S005 hosted verification contradiction; canonical Flutter product build/strong authorization OPEN |

No specialist has passed Foundation.

## Meaningful new evidence

### F005 — direct Dart async transfer
GitHub-hosted run `35429564591`, job `105861592799`, exact workflow/source commit `b5fc0cfaa4c79c646218326e6aae8be9121e0cf0` completed successfully on exact Dart SDK 3.13.3 / Ubuntu 24.04.5 / Linux 6.17.0-1022-azure. The fixture directly observed the documented microtask-before-zero-delay-event relation, a 10 ms timeout while the 80 ms source Future later completed its side effect/result, and `StreamSubscription.cancel()` preventing a later controller event from reaching the cancelled subscription.

**TRANSFER VALIDATION:** F005's prior Python model conclusion `waiter timeout ≠ source cancellation` now survives direct Dart execution. **EVIDENCE LIMIT:** StreamSubscription cancellation is API-specific and is not generalized to Futures, sockets, plugins or arbitrary work; arbitrary timer ordering, isolate concurrency, stream backpressure/error, Flutter scheduler/lifecycle, browser/PWA and product runtime remain OPEN.

### F001 — direct Dart JIT/AOT execution gap closed at bounded hosted Linux boundary
GitHub-hosted run `35423963687`, job `105846574857`, exact workflow/source commit `ccad123b533a5aa41bed7e84d36ad852828545c8` completed successfully. SDK setup, runtime identity recording, JIT execution, AOT compilation and AOT executable execution all passed. A prior AOT-execution failure was root-caused to a fixture launch-shape defect and the corrected regression passed.

### F001/M001 — first direct Flutter framework/test-runtime transfer
Workflow commit `3b920ba70d315baa686a9ee931144700719bab58`, run `35426881450`, job `105854277141` completed successfully. Official Flutter stable checkout installation, Flutter/Dart/engine identity recording, fixture dependency resolution and `flutter test` widget runtime execution all passed. This is framework/test-binding evidence, not Android/iOS/browser/production evidence.

## Retained evidence
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001 now has direct framework execution; M002-M006 retain first professional/model boundaries; real native/browser/EFB transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S004 exact-ref Flutter-application dependency/toolchain transfer; S005 hosted attestation evidence plus verifier contradiction; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Data / Quality / Architecture:** consume F005's direct Dart timeout/source distinction when specifying retry, cancellation and async contract oracles; caller timeout cannot stand in for operation terminal state.
- **Mobile:** consume F005 as Dart-runtime evidence only; Flutter frame scheduling, platform lifecycle and browser semantics remain independent transfer obligations.
- **Systems:** hosted Studio Dart/Flutter execution is not a canonical LogMate build. S004 still requires exact product toolchain capture + committed-lock enforcement + canonical build + artifact identity before reproducibility/provenance claims.
- **Design Studio / Web Manager / Marketing Manager:** considered under the cross-repo contract; this bounded runtime mechanism does not alter their canonical decisions; no files edited there.

## Current Balance Loop
Do not repeat equivalent F001 or F005 timing/widget passes. A trustworthy hosted Dart/Flutter execution path now exists and has transferred one central async mechanism. Next compare direct Dart transfer of F002/F003/F004/F006 against higher product leverage from an exact canonical LogMate Flutter build/toolchain-enforcement block and against native/browser platform transfer. Prefer a new evidence class, prerequisite closure or product transfer rather than symmetry.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref/engine identity matters.
- A moving Flutter `stable` label is not sufficient artifact identity; future runs must bind exact checkout/ref.
- Exact Flutter SDK/engine and any external CI/operator toolchain pin for inspected LogMate remain unknown from product repository evidence.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability and SQLite WAL/backup behavior remain OS/filesystem/device/wrapper sensitive.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool-version sensitive; hosted verification has contradictory success/failure evidence.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
