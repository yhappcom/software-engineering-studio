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
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 hosted generation + one successful online verification, later verifier contradiction; offline/strong authorization OPEN |

No specialist has passed Foundation.

## Meaningful new evidence

### S005 — stronger authorization policy attempt reproduced hosted verifier instability
Canonical: `research/systems/S005_attestation_authorization_policy_attempt.md`; workflow: `.github/workflows/s005-attestation-authorization-policy.yml`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was available. Direct Dart/Flutter validation remains OPEN rather than simulated.

Current GitHub CLI primary documentation supports narrowing attestation verification with signer-workflow, source-ref and source-digest predicates. A hosted workflow attempted that next policy rung against the same fixed subject digest previously verified successfully.

Run `35415715727` first exposed a workflow oracle/reporting defect: `continue-on-error` allowed job-step conclusions to look successful while expression outcomes caused the final classifier to fail. The workflow was revised to fail closed.

Run `35415743203` then failed the combined exact authorization policy before negative cases. To isolate the predicate, run `35415769301` placed the previously successful repository-only verifier first. Subject reconstruction succeeded, but the repository-only baseline itself failed, so finer signer/ref/digest predicates were skipped.

**CONTRADICTION:** the same fixed subject/repository pair succeeded in prior hosted run `35409747108` but later failed the repository-only baseline in `35415769301`. This reproduces the earlier unexplained verifier-failure class. Available evidence still lacks command-level stderr, so no permission/service/CLI/attestation root cause is assigned.

**VALIDATION:** stronger workflow/ref/source authorization remains OPEN. The correct engineering response is not more flag permutations; the baseline verifier must first become diagnosable/stable or be replaced by an independent verification path. No PASS awarded.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 spans asymmetric signing, reproducibility, hosted attestation generation, one successful hosted retrieval/verification/negative identity run, failed offline input export, and now a reproduced hosted-verifier contradiction during stronger authorization-policy work; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Architecture:** evidence-critical release decisions should preserve exact workflow run/job/commit/subject, verifier policy inputs and contradictory evidence.
- **Quality:** preserve run `35415715727` as an oracle/reporting failure; do not conflate it with the later system-under-test baseline failure in `35415769301`.
- **Mobile / products:** Studio text-subject attestation is not Flutter/mobile release evidence. Product transfer requires exact product ref/version, canonical build/toolchain/lock, artifact digest, attestation, executed verification policy and delivered artifact identity.
- **Data:** bind migration/backup release evidence to exact artifact/provenance when used as a release gate.
- **Design Studio / Web Manager / Marketing Manager:** considered under cross-repo contract; not materially relevant to this bounded mechanism; no canonical files edited.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`.

Do not repeat S005 offline-export or signer/ref/digest flag variants until command-level verifier failure evidence or an independent verifier path is available. Otherwise prefer a materially different higher rung: canonical product build/attestation, independent-host reproducibility, physical/platform publication durability, natural ADR/release evidence, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability depends on OS/filesystem/device and synchronization semantics; current EIO injection is not hard-power-loss evidence.
- SQLite WAL/backup behavior depends on SQLite version, wrapper, VFS/OS/filesystem/device and synchronization mode.
- LogMate Sync and backup consistency/publication mechanisms remain OPEN product decisions.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool/version sensitive; hosted verification currently has contradictory success/failure evidence.
- OpenSSL/provider and compiler/linker behavior are toolchain sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
