# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change + natural LogMate evolution transfer; A006 decision governance evidence |
| Mobile | Stage 1 IN STUDY — M001-M006 first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 now includes real hosted GitHub Actions attestation generation; S006 directory-sync publication failure evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### S005 — real hosted CI + GitHub artifact-attestation generation
Canonical: `research/systems/S005_real_github_actions_attestation.md`; workflow: `.github/workflows/s005-attestation-boundary.yml`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was found; direct Dart/Flutter validation remains OPEN rather than simulated.

The Studio itself now supplies a real hosted-CI evidence rung. Exact commit `ab6dbf4307078fc82ddc056029f686dd61eae3a7` triggered GitHub Actions run `35405920497`, job `105795544174` on `ubuntu-latest`. Checkout, deterministic exact-commit subject creation and `actions/attest@v4` each concluded `success`. The subject reconstructs to SHA-256 `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`.

**VALIDATION:** real GitHub-hosted CI and artifact-attestation generation are now demonstrated for this bounded Studio artifact/context. This supersedes the prior evidence limit that there was no real CI/attestation execution.

**EVIDENCE LIMIT:** generation success is not independent attestation verification, signer/workflow authorization policy, release acceptance, Flutter/mobile build evidence, deployment or production evidence. Current GitHub documentation explicitly requires verification/policy use for security benefit.

**CONTRADICTION / OPEN DEBUG:** immediately prior run `35405881832` at `eab2972843130b0e997203d5ba5b8c108cb67dde` failed specifically at the attestation step after checkout/subject generation succeeded. The available evidence channel did not expose the failed action log, so root cause is not assigned. The subsequent successful attestation disproves categorical unavailability in this repository context.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 asymmetric signing/reproducibility/product identity plus real hosted attestation generation; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Architecture:** evidence-critical decisions should preserve exact workflow run/job/commit/subject identity; `CI passed` remains insufficient.
- **Quality:** distinguish overall workflow green from exact attestation-generation and independent verification-policy predicates; negative wrong-identity verification remains required.
- **Mobile / products:** Studio text-subject attestation is not Flutter/mobile release evidence. Product transfer requires exact product ref/version, canonical build/toolchain/lock, artifact digest, attestation, verification policy and delivered artifact identity.
- **Data:** bind migration/backup release evidence to exact artifact/provenance when used as a release gate.
- **Design Studio / Web Manager / Marketing Manager:** considered under cross-repo contract; no canonical files edited and no owned decision changed.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux are available.

S005's named real CI/attestation-generation gap is now materially advanced. Do not repeat green-workflow variants. If Dart/Flutter remains unavailable, prefer a higher/different rung: independent attestation retrieval/verification + identity-policy negative cases, canonical product build/attestation, independent-host reproducibility, physical/platform publication durability, natural ADR/release evidence, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability depends on OS/filesystem/device and synchronization semantics; current EIO injection is not hard-power-loss evidence.
- SQLite WAL/backup behavior depends on SQLite version, wrapper, VFS/OS/filesystem/device and synchronization mode.
- LogMate Sync and backup consistency/publication mechanisms remain OPEN product decisions.
- GitHub Actions/`actions/attest`/OIDC/private-repository availability and verification semantics are service/version/plan sensitive.
- OpenSSL/provider and compiler/linker behavior are toolchain sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
