# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-23

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome + bounded macOS Safari runtime transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 permission/FGS + bounded Keystore replication; M006 Chromium PWA + macOS Safari runtime + bounded same-session origin-down offline; Safari SW lifecycle transfer REOPENED after artifact audit |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q006 process-crash recovery + CI verdict-propagation failure/isolation/repair/hosted regression |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M006 / Q006 — historical false-green evidence correction
A complete workflow-directory inventory exposed that the earlier Safari service-worker lifecycle workflow still contained the same verdict-propagation hazard demonstrated by Q006: `python validate.py | tee ...` without `pipefail` or an independent semantic verdict assertion.

Direct inspection of run-bound artifact `10698973958` from prior run `35741047017`, exact head `d31cc310f7444a3b1880b1faae7901314a801a34`, found `oracle.json` was **0 bytes** while the job had been green. Therefore the prior Safari service-worker lifecycle TRANSFER VALIDATION is withdrawn as INVALID evidence. This does not erase separately evidenced Safari generic runtime or same-session origin-down offline observations.

Repair commit `6daa9781cc884aab601744a5decf7a7459d06906` adds `set -o pipefail`, non-empty oracle enforcement and explicit `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS` enforcement. Regression run `35802543585` is in progress. No Safari SW lifecycle PASS will be restored until terminal status and run-bound semantic artifact agree.

### Q006 — retained CI verdict propagation evidence
Repaired Q006 exact head `bd763b301752b3adebd36b963c06d064aec94ca8`, run `35792678785`, remains bounded hosted evidence that log preservation and verdict propagation are independent controls. The M006 historical audit is now a natural cross-workflow transfer of that mechanism, not another synthetic pipefail variant.

## Current Balance Loop
Continue the M006 evidence-correction boundary through the fail-closed regression. If it fails, preserve the semantic failure and isolate cause; if it succeeds, inspect the run-bound oracle before restoring bounded transfer. After closure, re-rank toward stronger evidence classes rather than more equivalent shell variants.

F001 direct Dart/Flutter is not the historical blocker stated in older prompts: direct Dart JIT/AOT, Flutter framework/test binding, host→Chrome and bounded macOS Safari runtime evidence exist. Native Android/iOS/iPadOS, product and release transfer remain OPEN.

## CHANGE WATCH / OPEN
- M006 Safari SW lifecycle fail-closed regression `35802543585` pending; prior run `35741047017` is invalid evidence.
- Q006 repository-wide semantic audit remains OPEN; the workflow inventory is complete but semantic review of every verdict-bearing workflow is not yet complete.
- M003 transfers remain bounded to exact API-35 emulator fixtures; physical Android/OEM/other API REPLICATION remains OPEN.
- Ordinary Safari relaunch/profile persistence, installed PWA and iOS/iPadOS/EFB remain OPEN.
- Physical Android/iOS and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading or workflow-green alone. Preserve exact claim/oracle/environment boundaries, subprocess verdict propagation and run-bound semantic evidence; never infer unexecuted evidence.
