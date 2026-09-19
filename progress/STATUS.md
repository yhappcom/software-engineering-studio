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
| Systems | Stage 1 IN STUDY — S004 exact-ref LogMate dependency/toolchain transfer; S005 hosted verification contradiction; direct Flutter build/strong authorization OPEN |

No specialist has passed Foundation.

## Meaningful new evidence

### S004 — exact-ref LogMate lockfile/toolchain identity transfer
Canonical: `research/systems/S004_logmate_lockfile_toolchain_transfer.md`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was available. Direct Dart/Flutter validation remains OPEN rather than simulated.

Product evidence: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19`; production identity unknown and default branch is not assumed production.

At that exact ref, `pubspec.yaml` declares Dart `^3.10.7` and ranged hosted dependencies while committed `pubspec.lock` records exact selected hosted versions and SHA-256 content hashes. Concrete examples: `cloud_functions ^6.0.0 → 6.4.0` and `cupertino_icons ^1.0.8 → 1.0.9`. The lockfile records Dart `>=3.10.7 <4.0.0` and Flutter `>=3.27.0`, but does not identify one exact Flutter SDK/engine revision. Repository search found no `flutter-version` or `fvm` pin and `.github/workflows` was absent at the exact ref through the contents API; external CI/operator configuration remains unknown.

**SYNTHESIS:** `manifest constraints != resolved package graph/content != exact SDK/toolchain != build artifact`. The committed lockfile materially strengthens package reproducibility, but it is not sufficient evidence for exact Flutter build reproducibility/provenance.

**VALIDATION:** no Flutter/Dart executable was available, so lockfile enforcement, package-content retrieval, canonical LogMate build, independent-host comparison and artifact digest/signing/attestation remain OPEN. No PASS awarded.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S004 now has exact-ref Flutter-application dependency/toolchain transfer. S005 retains hosted attestation generation, one successful retrieval/verification/negative identity run and later verifier contradiction; S006 retains directory-sync publication failure evidence.

## Cross-track handoffs
- **Architecture:** build/toolchain identity becomes an externally relevant contract when reproducibility/provenance is required; evidence-critical release decisions should preserve exact artifact/toolchain/provenance identity.
- **Quality:** future product reproducibility validation should inject toolchain drift separately from lockfile/content-hash drift.
- **Mobile / LogMate:** when canonical build tooling becomes available, capture exact Flutter SDK/engine, enforce the committed lockfile, execute the canonical build, then bind artifact digest/signing/attestation. Current static source evidence does not establish a reproducible mobile artifact.
- **Data:** bind migration/backup release evidence to exact artifact/provenance when used as a release gate.
- **Design Studio / Web Manager / Marketing Manager:** considered under cross-repo contract; not materially relevant to this bounded mechanism; no canonical files edited.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`.

The S004 static product-transfer boundary is now explicit; do not repeat manifest/lockfile audits. The next product rung is executable lockfile enforcement + exact toolchain capture + canonical build. Do not repeat S005 offline-export or signer/ref/digest flag variants until command-level verifier failure evidence or an independent verifier path is available. Otherwise prefer a materially different higher rung: independent-host reproducibility, physical/platform publication durability, natural ADR/release evidence, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build and pub lockfile behavior are version-sensitive; exact SDK/ref matters.
- Exact Flutter SDK/engine and any external CI/operator toolchain pin for inspected LogMate remain unknown.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability depends on OS/filesystem/device and synchronization semantics; current EIO injection is not hard-power-loss evidence.
- SQLite WAL/backup behavior depends on SQLite version, wrapper, VFS/OS/filesystem/device and synchronization mode.
- LogMate Sync and backup consistency/publication mechanisms remain OPEN product decisions.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool/version sensitive; hosted verification currently has contradictory success/failure evidence.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
