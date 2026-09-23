# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-23

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome + bounded macOS Safari runtime transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 permission/FGS + bounded Keystore replication; M006 Chromium PWA + macOS Safari runtime + bounded same-session origin-down offline; Safari SW lifecycle transfer REOPENED and under restart-oracle failure isolation |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q006 process-crash recovery + CI verdict-propagation failure/isolation/repair/hosted regression |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M006 / Q006 — lifecycle-valid oracle correction now reaches restart boundary
Historical Safari service-worker lifecycle run `35741047017` remains INVALID because its semantic artifact was zero bytes and its producer exit status could be masked by `tee`.

Fail-closed run `35802543585` exposed an initial-document lifecycle-invalid title oracle. Repair head `4f7e376572a6fe8c6eddea40e4d95841c4ce2033`, run `35806396805`, then produced structured run-bound evidence. Artifact `10727414954`, digest `sha256:4fd3600dd74ed8eb80e5bebc1215d9c00fbf89f3ada7427a06a743a94d40d126`, directly shows initial controller acquisition, independent V1 confirmation, explicit V2 update/controllerchange and V2 control.

The run failed only after recreating Safari WebDriver. Its restart branch repeated the same harness defect: it invoked `registerSW()` and waited directly for an application-owned V2 title even though the invocation can be destroyed by a reload while the recreated document discovers the persisted registration. Repeated `M006_SW_BOOT` therefore does not prove persistence loss.

Commit `54bbd5283920aa3d82057cc2da8a14b0db4bacbf` now polls browser-owned controller state across the restart navigation, then re-invokes the semantic V2 query in the controlled document. Regression run `35810765603` is in progress. No combined Safari SW lifecycle PASS exists yet.

### Q006 — retained CI verdict propagation evidence
Repaired Q006 exact head `bd763b301752b3adebd36b963c06d064aec94ca8`, run `35792678785`, remains bounded hosted evidence that log preservation and verdict propagation are independent controls. M006 additionally demonstrates that lifecycle validity must be checked independently at each navigation boundary, not only once per test.

## Current Balance Loop
Continue M006 through the restart-aligned regression and inspect its run-bound semantic artifact before any combined lifecycle verdict. If red, use the first structured failure observation for causal isolation; if green, restore only the bounded claim actually exercised. After closure, re-rank toward stronger evidence classes rather than equivalent Safari/harness variants.

F001 direct Dart/Flutter is not the historical blocker stated in older prompts: direct Dart JIT/AOT, Flutter framework/test binding, host→Chrome and bounded macOS Safari runtime evidence exist. Native Android/iOS/iPadOS, product and release transfer remain OPEN.

## CHANGE WATCH / OPEN
- M006 Safari SW restart-aligned regression `35810765603` pending; prior run `35741047017` remains invalid evidence.
- Q006 repository-wide semantic audit remains OPEN; complete inventory does not itself prove semantic correctness.
- M003 transfers remain bounded to exact API-35 emulator fixtures; physical Android/OEM/other API REPLICATION remains OPEN.
- Ordinary Safari relaunch/profile persistence, installed PWA and iOS/iPadOS/EFB remain OPEN.
- Physical Android/iOS and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading or workflow-green alone. Preserve exact claim/oracle/environment boundaries, subprocess verdict propagation, lifecycle-valid semantic oracles at every navigation boundary, and run-bound semantic evidence; never infer unexecuted evidence.
