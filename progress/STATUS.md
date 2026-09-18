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
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 now includes real asymmetric public-key signing/verification evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### S005 — Real asymmetric signature verification boundary
Canonical: `research/systems/S005_ci_signing_versioning_release_evidence.md`; fixture: `research/systems/fixtures/S005_real_public_key_signature_boundary.py`.

OpenSSL 3.5.5/Linux evidence moved S005 beyond its prior synthetic release-identity model. An ephemeral RSA-2048 private key signed exact artifact bytes; verification under the corresponding public key succeeded. Appending `TAMPER` to the artifact caused verification failure, and verification under an independently generated unrelated public key also failed. This closes the prior "no real signature" gap only for the bounded public-key signature mechanism.

The evidence deliberately does not equate a valid signature with release authorization, provenance, CI identity or mobile package signing. Key selection/trust policy, custody/revocation, certificate chains, CI/OIDC/attestation, Android/iOS signing, store delivery and production deployment remain separate OPEN claims.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process-crash and bounded capacity evidence; D006 server death, live-process link interruption, and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 separates property/oracle strength from search strength; Q006 demonstrates structural-vs-semantic recovery-oracle discrimination under real process death.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained; S005 now transfer-tests S001's authenticity/integrity distinction with an actual asymmetric mechanism.

## Cross-track handoffs
- **Mobile:** reproduce release identity/signing on the exact Flutter/Android/iOS package toolchain; OpenSSL verification is not mobile code-signing evidence.
- **Quality:** release signature negative tests should include changed artifact and wrong verification-key cases; signature success is not an authorization oracle.
- **Architecture:** signer/trust-policy/artifact identity is evidence-critical decision state where release governance depends on it.
- **Data:** migration/recovery acceptance should bind to the exact authorized release artifact, not merely version labels.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this bounded cryptographic mechanism.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck on 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 and OpenSSL 3.5.5 are available.

S005 now has a materially stronger real asymmetric-signature rung, so do not repeat equivalent local cryptographic variants. Highest-value next work remains direct Dart/Flutter/mobile first if the SDK appears. Otherwise seek a genuinely stronger boundary: real CI/attestation/reproducible-build evidence if accessible, natural exact-ref product/ADR transfer, or a materially different platform/storage/network failure. Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; application-process evidence must not be generalized to power loss or lower-layer ENOSPC.
- LogMate DATA-001 Sync cursor/batch/receipt semantics are OPEN product decisions, not implementation facts.
- GitHub attestation/Sigstore behavior and deployment rollback semantics are service/version sensitive.
- OpenSSL/provider behavior is version-sensitive; local signature evidence must not be generalized to platform package signing.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
