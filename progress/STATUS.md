# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + first Flutter framework execution; F004 direct Dart isolate; F005 direct Dart async; F006 direct socket harness failure/root-cause OPEN; F002/F003 transfer OPEN |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change + natural LogMate evolution transfer; A006 decision governance evidence |
| Mobile | Stage 1 IN STUDY — M001 first direct Flutter framework execution; M002-M006 professional/model boundaries; native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 exact-ref LogMate dependency/toolchain transfer; S005 hosted verification contradiction; canonical Flutter product build/strong authorization OPEN |

No specialist has passed Foundation.

## Meaningful new evidence

### F006 — direct Dart socket transfer exposed a validation-harness hang
Initial run `35434862199` reached the real Dart socket fixture and hung. The first causal hypothesis was a close/peer-EOF wait cycle. Commit `6f78f6ee8ccda32143df55d2a7f3820a117cc5c7` reordered the wait and added five-second Future timeouts, but regression run `35434895889`, job `105875778624`, again remained in the fixture step far beyond those internal deadlines.

**CONTRADICTION / FALSIFICATION:** close-order alone is not an adequate root cause. No Dart socket semantic defect is inferred. Partial running-job logs were unavailable through the current evidence channel, so the exact blocking/resource-retention phase remains OPEN.

**VALIDATION GOVERNANCE:** the workflow itself had no independent execution deadline. Commit `835104ea9dac410b4f0a4d17f748882710f5921c` adds a three-minute job timeout, one-minute fixture-step timeout and an F006 concurrency group with `cancel-in-progress` for future runs. Run `35437455712` was queued at the evidence cutoff. Application-level Future timeouts are not a substitute for an outer CI deadline; this is harness-containment evidence, not a socket PASS.

### Retained direct Dart/Flutter evidence
- F001: run `35423963687` validates direct Dart JIT/AOT execution after a fixture root-cause/fix/regression cycle.
- F001/M001: run `35426881450` validates first Flutter framework/test-binding execution.
- F004: run `35432075163` validates bounded isolate ownership/message passing and a negative sendability case.
- F005: run `35429564591` validates bounded Dart async ordering, waiter-timeout ≠ source-cancellation, and API-specific subscription cancellation.

## Retained evidence
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001 has direct framework execution; M002-M006 retain first professional/model boundaries; real native/browser/EFB transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S004 exact-ref Flutter-application dependency/toolchain transfer; S005 hosted attestation evidence plus verifier contradiction; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Quality / Systems:** F006 demonstrates that the validation harness itself needs an independent termination/resource-control boundary; target-level async timeouts can fail to bound a CI job.
- **Data / Architecture:** F006 has not yet established a Dart socket correctness result; continue to distinguish transport termination from application completion/ACK/durable effect.
- **Mobile:** `dart:io` socket evidence cannot be transferred to browser/PWA; native/browser platform behavior remains independent.
- **Systems:** hosted Studio Dart/Flutter execution is not a canonical LogMate build. S004 still requires exact product toolchain capture + committed-lock enforcement + canonical build + artifact identity.
- **Design Studio / Web Manager / Marketing Manager:** considered under the cross-repo contract; this bounded transport/harness result does not alter their canonical decisions; no files edited there.

## Current Balance Loop
First recover bounded F006 run `35437455712`. If it times out, isolate phases or use an external process deadline before another network-fixture runner cycle; do not repeat close-order variants. Because the hosted Dart/Flutter path already covers execution, isolate ownership and central async semantics, compare any further F006 debugging cost against exact canonical LogMate toolchain/lock/build/artifact transfer and F002/F003 prerequisites. Prefer a new evidence class, prerequisite closure or product transfer rather than symmetry.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref/engine identity matters.
- A moving Flutter `stable` label is not sufficient artifact identity; future runs must bind exact checkout/ref.
- Exact Flutter SDK/engine and any external CI/operator toolchain pin for inspected LogMate remain unknown from product repository evidence.
- F006 direct Dart socket root cause/verdict is OPEN; current evidence is a reproduced harness hang plus falsified hypothesis, not transport correctness.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability and SQLite WAL/backup behavior remain OS/filesystem/device/wrapper sensitive.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool-version sensitive; hosted verification has contradictory success/failure evidence.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
