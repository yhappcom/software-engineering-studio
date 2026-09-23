# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-23

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome + bounded macOS Safari runtime transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 permission/FGS + bounded Keystore replication; M006 Chromium PWA + macOS Safari runtime + bounded same-session origin-down offline; Safari SW lifecycle transfer REOPENED and under oracle failure isolation |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q006 process-crash recovery + CI verdict-propagation failure/isolation/repair/hosted regression |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M006 / Q006 — false-green correction exposed a second oracle defect
Historical Safari service-worker lifecycle run `35741047017` remains INVALID because its semantic artifact was zero bytes and its producer exit status could be masked by `tee`.

Fail-closed repair head `6daa9781cc884aab601744a5decf7a7459d06906` converted that path into a trustworthy failure: run `35802543585`, job `106995919837`, terminal failure. Artifact `10726377605`, digest `sha256:67483e7b00559f54792f606f5f906ed55b82b8703c2ce63cc6c22326ca63cdcd`, records successful WebDriver enablement, an empty stdout oracle, and initial page/service-worker requests.

Exact fixture inspection isolates the next defect at the harness boundary. Initial `registerSW()` reloads an uncontrolled document, terminating that JavaScript invocation; the old validator nevertheless waited for a V1 title only that destroyed invocation could later emit. Commit `4f7e376572a6fe8c6eddea40e4d95841c4ce2033` now polls browser-owned `navigator.serviceWorker.controller` across the possible reload, re-invokes the V1 semantic query in the controlled document, retains V2/controllerchange/restart checks, and emits structured failure observations. Regression run `35806396805` is in progress. No Safari SW lifecycle PASS exists yet.

### Q006 — retained CI verdict propagation evidence
Repaired Q006 exact head `bd763b301752b3adebd36b963c06d064aec94ca8`, run `35792678785`, remains bounded hosted evidence that log preservation and verdict propagation are independent controls. M006 now shows why fail-closed propagation matters: it exposed a distinct lifecycle-invalid oracle that the earlier false green concealed.

## Current Balance Loop
Continue M006 through the lifecycle-aligned regression and inspect its run-bound semantic artifact before any verdict. If red, use the structured first-failure observation for causal isolation; if green, restore only the bounded claim actually exercised. After closure, re-rank toward stronger evidence classes rather than equivalent Safari/harness variants.

F001 direct Dart/Flutter is not the historical blocker stated in older prompts: direct Dart JIT/AOT, Flutter framework/test binding, host→Chrome and bounded macOS Safari runtime evidence exist. Native Android/iOS/iPadOS, product and release transfer remain OPEN.

## CHANGE WATCH / OPEN
- M006 Safari SW lifecycle repaired regression `35806396805` pending; prior run `35741047017` remains invalid evidence.
- Q006 repository-wide semantic audit remains OPEN; complete inventory does not itself prove semantic correctness.
- M003 transfers remain bounded to exact API-35 emulator fixtures; physical Android/OEM/other API REPLICATION remains OPEN.
- Ordinary Safari relaunch/profile persistence, installed PWA and iOS/iPadOS/EFB remain OPEN.
- Physical Android/iOS and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading or workflow-green alone. Preserve exact claim/oracle/environment boundaries, subprocess verdict propagation, lifecycle-valid semantic oracles and run-bound semantic evidence; never infer unexecuted evidence.
