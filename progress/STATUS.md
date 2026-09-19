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
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 hosted generation + online verification; offline verification attempted but blocked at input export |

No specialist has passed Foundation.

## Meaningful new evidence

### S005 — offline attestation verification attempt exposed an input-export boundary
Canonical: `research/systems/S005_offline_attestation_verification_attempt.md`; workflow: `.github/workflows/s005-offline-attestation-verification.yml`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was available. Direct Dart/Flutter validation remains OPEN rather than simulated.

The prior S005 evidence is retained and now correctly reflected globally: exact subject digest retrieval and hosted `gh attestation verify` succeeded in run `35409747108` / job `105806806534`; wrong repository identity and mutated subject bytes were rejected. Offline verification is a distinct higher rung.

The new offline workflow attempted `online export of bundle/trusted roots → network-isolated verification`. Run `35412950674` failed at subject reconstruction because the new fixture used bytes that did not match the asserted prior digest. Comparison with the successful verification workflow established the root cause; the fixture was corrected.

After correction, runs `35412968384`, `35412983659`, and `35413003999` reconstructed the exact subject successfully but failed before offline verification at bundle/input export. The latter attempts used materially different export approaches. The available evidence channel did not expose command stderr, so no permission/service/CLI/network explanation is assigned.

**VALIDATION:** online hosted verification does not itself establish offline verification or even operational availability of the explicit bundle/root export path in the same CI context. **CONTRADICTION/DEBUG:** one failure was root-caused to a defective test fixture; later export failures remain causally OPEN. No PASS awarded.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 now spans asymmetric signing, reproducibility, real hosted attestation generation, hosted retrieval/verification/negative identity cases, and a failed higher-rung offline attempt; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Architecture:** evidence-critical decisions should preserve exact workflow run/job/commit/subject and distinguish online verification from offline-input availability.
- **Quality:** preserve defective verification fixtures as oracle failures; do not assign root cause to later bundle-export failures without command-level evidence.
- **Mobile / products:** Studio text-subject attestation is not Flutter/mobile release evidence. Product transfer requires exact product ref/version, canonical build/toolchain/lock, artifact digest, attestation, executed verification policy and delivered artifact identity.
- **Data:** bind migration/backup release evidence to exact artifact/provenance when used as a release gate.
- **Design Studio / Web Manager / Marketing Manager:** considered under cross-repo contract; not materially relevant to this bounded mechanism; no canonical files edited.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`.

Do not repeat offline bundle-export variants until command-level failure evidence is available. If that debugging channel becomes available, resume S005 at the exact input-export failure. Otherwise prefer a materially different higher rung: canonical product build/attestation, independent-host reproducibility, physical/platform publication durability, natural ADR/release evidence, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability depends on OS/filesystem/device and synchronization semantics; current EIO injection is not hard-power-loss evidence.
- SQLite WAL/backup behavior depends on SQLite version, wrapper, VFS/OS/filesystem/device and synchronization mode.
- LogMate Sync and backup consistency/publication mechanisms remain OPEN product decisions.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool/version sensitive.
- OpenSSL/provider and compiler/linker behavior are toolchain sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
