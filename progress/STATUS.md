# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-23

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome + bounded macOS Safari runtime transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 permission/FGS + bounded Keystore replication; M006 Chromium PWA + macOS Safari runtime + bounded Safari SW registration/update/restart transfer + same-session origin-down offline |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q006 process-crash recovery + CI verdict-propagation failure/isolation/repair/hosted regression |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M006 / Q006 — bounded Safari service-worker lifecycle transfer restored
Historical Safari service-worker lifecycle run `35741047017` remains INVALID because its semantic artifact was zero bytes and its producer exit status could be masked by `tee`. Subsequent fail-closed runs exposed two independent lifecycle-invalid title oracles: first registration and recreated-session restart.

Exact repaired head `54bbd5283920aa3d82057cc2da8a14b0db4bacbf`, run `35810765603`, completed success. Run-bound artifact `10729767594`, digest `sha256:34bc15dbb8cb15776571ded24d38de1d38b3be87228c644844de59551740f67f`, was directly inspected. Its non-empty oracle records `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS`, initial controller acquisition, independent V1 confirmation, explicit V2 update/controllerchange, V2 control, fresh-WebDriver controller reacquisition, and independent V2 confirmation after restart.

**TRANSFER VALIDATION:** bounded macOS Safari/SafariDriver registration → control → V1→V2 update/controller replacement → fresh-WebDriver V2 registration/control recovery now PASS for the exact fixture/environment. The invalid historical run remains invalid; this verdict comes only from the repaired exact-head run and semantic artifact.

The separately observed fresh-WebDriver **origin-down offline cold-start** contradiction remains OPEN and is not resolved by this lifecycle PASS.

Canonical closure: `research/mobile/M006_safari_service_worker_lifecycle_run4_closure.md`.

### Q006 — retained CI verdict propagation evidence
Repaired Q006 exact head `bd763b301752b3adebd36b963c06d064aec94ca8`, run `35792678785`, remains bounded hosted evidence that log preservation and verdict propagation are independent controls. M006 now adds a complete natural transfer chain showing that fail-closed propagation can expose independent semantic-oracle lifetime defects at multiple navigation boundaries.

## Current Balance Loop
The repeated Safari service-worker registration/update/restart boundary is now professionally closed at the bounded fixture level. Do not spend the next block on equivalent lifecycle variants. Re-rank toward materially stronger evidence classes: physical/native Android/iOS/iPadOS/EFB, ordinary Safari profile/installed-PWA persistence, exact-product PWA build/runtime when source authorization exists, physical storage/connectivity, trustworthy complete semantic CI/release-gate audit, or natural release/ADR evidence.

F001 direct Dart/Flutter is not the historical blocker stated in older prompts: direct Dart JIT/AOT, Flutter framework/test binding, host→Chrome and bounded macOS Safari runtime evidence exist. Native Android/iOS/iPadOS, product and release transfer remain OPEN.

## CHANGE WATCH / OPEN
- M006 generic Safari SW registration/update/restart bounded transfer PASS; ordinary Safari relaunch/profile, installed PWA and fresh-SafariDriver origin-down cold-start mechanism remain OPEN.
- Q006 repository-wide semantic audit remains OPEN; complete inventory does not itself prove semantic correctness.
- M003 transfers remain bounded to exact API-35 emulator fixtures; physical Android/OEM/other API REPLICATION remains OPEN.
- Physical Android/iOS and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading or workflow-green alone. Preserve exact claim/oracle/environment boundaries, subprocess verdict propagation, lifecycle-valid semantic oracles at every navigation boundary, and run-bound semantic evidence; never infer unexecuted evidence.
