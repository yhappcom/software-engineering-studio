# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change executable evidence; A006 decision-lifecycle + bounded executable governance evidence |
| Mobile | Stage 1 IN STUDY — M001-M006 first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real process crash + bounded `SQLITE_FULL`; D006 real transport faults + exact-ref LogMate inbound cursor/apply transfer |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search evidence; Q006 real process-crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 includes real asymmetric signing, bounded reproducible-build evidence and exact-ref LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### S005 — Exact-ref LogMate build-identity transfer
Canonical: `research/systems/S005_logmate_exact_ref_build_identity_transfer.md`.

Product evidence identity: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-18`; production identity unknown and default branch is not assumed to equal production.

The inspected ref commits `pubspec.lock` with exact hosted dependency versions/content hashes and pins Gradle 8.14, AGP 8.11.1, Google Services 4.3.15 and Kotlin 2.2.20. However, the lockfile's SDK section permits a Flutter range (`>=3.27.0`) and Android configuration obtains Flutter from `local.properties`; repository-visible evidence inspected this run does not identify one exact Flutter SDK version/ref. Current Dart documentation confirms an application lockfile controls package versions/content hashes, while current Flutter release metadata distinguishes Flutter version/ref and the SDK itself includes the Dart/framework/engine/tooling identity.

**SYNTHESIS:** source commit + application lockfile narrows build identity but does not by itself determine canonical Flutter build identity. Exact Flutter SDK/ref, relevant platform/JDK/SDK inputs, build flags/version overrides, post-build/signing transforms and final artifact identity remain separate evidence dimensions. No product build was executed because Dart/Flutter executables remain unavailable, so this is natural product configuration transfer rather than executable product PASS.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process-crash and bounded capacity evidence; D006 server death, live-process link interruption, and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 separates property/oracle strength from search strength; Q006 demonstrates structural-vs-semantic recovery-oracle discrimination under real process death.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained; S005 has real asymmetric-signature evidence, bounded compiler reproducibility and natural exact-ref product transfer.

## Cross-track handoffs
- **Mobile:** when a trustworthy SDK exists, build the exact LogMate ref under an explicitly recorded Flutter SDK/ref and lockfile policy; preserve build flags/post-build transforms, artifact hashes and package/signing identity.
- **Quality:** future LogMate reproducibility needs a byte/digest oracle plus deliberate Flutter/toolchain/input-drift negatives; source+lockfile equality is not the oracle.
- **Architecture:** evidence-critical build/release decisions should preserve exact toolchain and artifact identity, not only source/version labels.
- **Data:** migration/recovery acceptance should bind to the exact authorized release artifact, not merely a version label or a fresh rebuild of an old source ref.
- **LogMate / release engineering:** exact Flutter SDK identity should be preserved when canonical release automation is defined; no product canonical file was edited.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this build-input identity question.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck on 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available.

S005 now has three materially different evidence forms: real asymmetric signature verification, bounded compiler reproducibility with isolated failure causes, and a natural exact-ref Flutter-product configuration transfer exposing the exact-SDK identity gap. Do not repeat equivalent local signature/compiler/configuration variants. Highest-value next work remains direct Dart/Flutter/mobile first if the SDK appears. Otherwise seek a genuinely stronger boundary: real CI/attestation, independent-environment/canonical-product build, natural release/ADR evidence, or a materially different platform/storage/network failure. Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; application-process evidence must not be generalized to power loss or lower-layer ENOSPC.
- LogMate DATA-001 Sync cursor/batch/receipt semantics are OPEN product decisions, not implementation facts.
- GitHub attestation/Sigstore behavior and deployment rollback semantics are service/version sensitive.
- OpenSSL/provider and compiler/linker reproducibility behavior are version-sensitive; local evidence must not be generalized to mobile signing/package builds.
- Exact Flutter SDK/ref and release/production identity for LogMate remain release-evidence dependencies until explicitly preserved by the product/release process.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
