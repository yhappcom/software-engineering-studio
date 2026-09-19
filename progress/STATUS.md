# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + first Flutter framework execution validated; F002-F006 initiated |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change + natural LogMate evolution transfer; A006 decision governance evidence |
| Mobile | Stage 1 IN STUDY — M001 first direct Flutter framework execution; M002-M006 professional/model boundaries; native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 exact-ref LogMate dependency/toolchain transfer; S005 hosted verification contradiction; canonical Flutter product build/strong authorization OPEN |

No specialist has passed Foundation.

## Meaningful new evidence

### F001 — direct Dart JIT/AOT execution gap closed at bounded hosted Linux boundary
GitHub-hosted run `35423963687`, job `105846574857`, exact workflow/source commit `ccad123b533a5aa41bed7e84d36ad852828545c8` completed successfully. SDK setup, runtime identity recording, JIT execution, AOT compilation and AOT executable execution all passed.

A prior run `35421496953` had passed JIT and AOT compilation but failed AOT execution. Root cause was a fixture launch-shape defect: JIT requires `dart <script> child`, while the self-contained compiled executable must self-spawn as `<exe> child`. The corrected regression passed. The failure is retained as FAILURE → DEBUG/ROOT CAUSE → FIX → REGRESSION evidence.

### F001/M001 — first direct Flutter framework/test-runtime transfer
Workflow commit `3b920ba70d315baa686a9ee931144700719bab58`, run `35426881450`, job `105854277141` completed successfully. Official Flutter stable checkout installation, Flutter/Dart/engine identity recording, fixture dependency resolution and `flutter test` widget runtime execution all passed. The test observes a state transition across the framework test binding's pump boundary rather than merely parsing or compiling Flutter source.

The official `flutter/flutter` stable branch observed immediately after the run was commit `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`; that exact ref records engine `af7e796e161ae0bb1ff0758c71a7105418bd9ded`. The workflow itself records checkout identity, but current connector evidence does not expose command stdout, so the post-run branch/ref observation is corroborating identity evidence, not a fabricated hidden-log value.

**VALIDATION:** the original F001 direct Dart JIT/AOT gap is CLOSED for the bounded hosted Linux claim, and the absence of any direct Flutter execution is CLOSED at a first framework/test-binding level. **EVIDENCE LIMIT:** this does not establish Android/iOS embedder/lifecycle behavior, physical-device behavior, release-AOT Flutter application behavior, browser/PWA behavior, canonical LogMate build correctness or production behavior.

## Retained evidence
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001 now has direct framework execution; M002-M006 retain first professional/model boundaries; real native/browser/EFB transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S004 exact-ref Flutter-application dependency/toolchain transfer; S005 hosted attestation evidence plus verifier contradiction; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Mobile:** consume the new Flutter result as framework/test-runtime evidence only. Android/iOS/browser/embedder and product runtime semantics remain independent transfer obligations.
- **Quality:** preserve the failed AOT run and corrected regression as evidence that fixtures can encode execution-mode defects; runtime/build identity belongs in the oracle contract.
- **Systems:** hosted Studio Flutter execution is not a canonical LogMate build. S004 still requires exact product toolchain capture + committed-lock enforcement + canonical build + artifact identity before reproducibility/provenance claims.
- **Architecture/Data:** direct Dart/Flutter execution strengthens the shared execution model but does not change persistence, ownership or product behavior claims.
- **Design Studio / Web Manager / Marketing Manager:** considered under the cross-repo contract; this bounded runtime mechanism does not alter their canonical decisions; no files edited there.

## Current Balance Loop
Do not repeat equivalent F001 JIT/AOT/widget-test passes. The prerequisite picture has materially changed: a trustworthy hosted Dart/Flutter execution path now exists. Next compare direct Dart transfer of F002-F006 against higher product leverage from an exact canonical LogMate Flutter build/toolchain-enforcement block and against native/browser platform transfer. Select one coherent block by risk, cross-track leverage and evidence maturity rather than deepening F001 for symmetry.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref/engine identity matters.
- A moving `stable` label is not sufficient artifact identity; future runs must bind exact checkout/ref.
- Exact Flutter SDK/engine and any external CI/operator toolchain pin for inspected LogMate remain unknown from product repository evidence.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability and SQLite WAL/backup behavior remain OS/filesystem/device/wrapper sensitive.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool-version sensitive; hosted verification has contradictory success/failure evidence.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
