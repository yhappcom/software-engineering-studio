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
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 includes real asymmetric signing plus bounded reproducible-build evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### S005 — Bounded compiler reproducibility and failure isolation
Canonical: `research/systems/S005_reproducible_build_boundary.md`; fixture: `research/systems/fixtures/S005_reproducible_build_boundary.py`.

GCC 14.2.0/GNU ld 2.44/Linux evidence closes the previously named reproducible-build comparison gap only for a bounded same-host compiler target. Identical C source was built in different absolute directories and at different wall-clock times. Naive builds differed. Fixed `SOURCE_DATE_EPOCH` alone still differed, and `-ffile-prefix-map` alone still differed. Combining fixed time with normalized build paths produced byte-identical executables with SHA-256 `69c2e47764cc2a982a4a4cc1a535eb06e3a032a6450aee63875ac1fc12395dba`.

The single-control failures isolate two concrete nondeterminism inputs and falsify the claim that either normalization alone was sufficient. The pass does not establish hermeticity, cross-host/toolchain reproducibility, Flutter/mobile package reproducibility, CI provenance, signing authorization or production equivalence.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process-crash and bounded capacity evidence; D006 server death, live-process link interruption, and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 separates property/oracle strength from search strength; Q006 demonstrates structural-vs-semantic recovery-oracle discrimination under real process death.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained; S005 has both real asymmetric-signature evidence and bounded compiler reproducibility evidence.

## Cross-track handoffs
- **Mobile:** reproduce the canonical Flutter/product build twice with exact source ref, lock/toolchain, flags, post-build transforms and artifact hashes; separate unsigned build reproducibility from platform signing/package identity.
- **Quality:** reproducibility requires its own byte-identity oracle and deliberate input-drift negatives; byte equality does not establish functional correctness.
- **Architecture:** evidence-critical build/release decisions should preserve toolchain, flags, normalized inputs and artifact identity.
- **Data:** migration/recovery acceptance should bind to the exact authorized release artifact, not merely a version label or a fresh rebuild of an old source ref.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this bounded build mechanism.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck on 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5, OpenSSL 3.5.5, GCC 14.2.0 and GNU ld 2.44 are available.

S005 now has two materially different real mechanism rungs: asymmetric signature verification and bounded compiler reproducibility with isolated failure causes. Do not repeat equivalent local signature/compiler variants. Highest-value next work remains direct Dart/Flutter/mobile first if the SDK appears. Otherwise seek a genuinely stronger boundary: real CI/attestation, independent-environment/canonical-product rebuild, natural exact-ref product/ADR transfer, or a materially different platform/storage/network failure. Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; application-process evidence must not be generalized to power loss or lower-layer ENOSPC.
- LogMate DATA-001 Sync cursor/batch/receipt semantics are OPEN product decisions, not implementation facts.
- GitHub attestation/Sigstore behavior and deployment rollback semantics are service/version sensitive.
- OpenSSL/provider and compiler/linker reproducibility behavior are version-sensitive; local evidence must not be generalized to mobile signing/package builds.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
