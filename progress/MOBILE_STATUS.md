# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering  
Prefix: `M###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-23

## Current evidence

### M001
**IN STUDY — DIRECT FLUTTER HOST/CHROME + BOUNDED ANDROID EMULATOR TRANSFER VALIDATED.** Exact repaired head `b6bfc4bf7e07c004c43326fb1821fd54de3986ba`, run `35507983649`, job `106070907373` terminal success. Physical Android, iOS, release-AOT, product artifacts and production remain OPEN.

### M002
**IN STUDY — BOUNDED ANDROID FORCE-STOP/FILE RECOVERY + ORDINARY HOME BACKGROUND/RESUME TRANSFERS VALIDATED.** Force-stop repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`, run `35516637659`, job `106093583857` success. Background/resume exact head `a278de3f2a9015195262b30662b1c240601f336e`, run `35529237932`, job `106126775150` success. API-35 emulator scope only.

### M003
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME ORDINARY-BACKGROUND EXPIRY + FGS HELD→APP-STOP→EXPIRY→REQUESTABILITY BOUNDED TRANSFERS VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Physical/OEM/other-API independent replication remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE/RESTART/UPDATE/COLD-START + BOUNDED macOS SAFARI RUNTIME + SAME-SESSION ORIGIN-DOWN OFFLINE TRANSFERS VALIDATED; SAFARI SERVICE-WORKER COMBINED LIFECYCLE TRANSFER REOPENED AND UNDER ORACLE FAILURE ISOLATION; FRESH SAFARIDRIVER ORIGIN-DOWN COLD START CONTRADICTORY.**

Safari runtime repaired execution remains valid at exact head `44c8be44bb53f2b67c08f40a0738f29858018bdd`, run `35727646652`, job `106745123287`, artifact `10694445918`.

Historical lifecycle run `35741047017` remains INVALID after its zero-byte semantic artifact exposed the Q006 verdict-propagation hazard. Fail-closed run `35802543585` correctly failed and exposed the initial-document lifecycle-invalid title oracle.

Repair head `4f7e376572a6fe8c6eddea40e4d95841c4ce2033`, run `35806396805`, then supplied structured evidence. Artifact `10727414954`, digest `sha256:4fd3600dd74ed8eb80e5bebc1215d9c00fbf89f3ada7427a06a743a94d40d126`, directly proves initial controller acquisition, independent V1 confirmation, explicit V2 update/controllerchange, and V2 control before restart. It failed only after recreating Safari WebDriver: the old restart oracle repeatedly observed `M006_SW_BOOT` while waiting directly for `M006_SW_READY_V2`.

**ROOT CAUSE at the harness boundary:** the recreated-session branch repeated the same lifecycle mistake as the original first-registration branch. `registerSW()` can reload an initially uncontrolled document while discovering the persisted registration; the pre-navigation invocation cannot later set the V2 title. This timeout therefore did not establish lost registration/update state.

Commit `54bbd5283920aa3d82057cc2da8a14b0db4bacbf` repairs restart validation by first polling browser-owned `navigator.serviceWorker.controller` across any reload, then re-invoking `registerSW()` in the controlled document and independently requiring V2. Regression run `35810765603` is in progress. No combined lifecycle PASS/TRANSFER VALIDATION is awarded yet.

Safari offline discriminator remains separately bounded: exact head `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`, run `35780706023`, artifact `10718495328`. Same-session unavailable-origin navigation reached the cached app with controller=true; fresh WebDriver navigation failed. Same-session origin-down offline behavior remains bounded VALIDATION; fresh-WebDriver origin-down cold-start expectation remains CONTRADICTION with lower-level cause OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current Safari fixture evidence makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Run 3 advances bounded Safari registration/control/update evidence but combined restart transfer remains OPEN pending the restart-aligned regression. Ordinary Safari relaunch/profile persistence, installed PWA, physical Android/OEM/other API, iOS/iPadOS lifecycle, broader plugin/native behavior, EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Foundations:** browser/session evidence does not infer native/iOS/iPadOS/product execution; direct Dart/Flutter is already validated and not the blocker.
- **Quality:** navigation-spanning oracle lifetime must be audited at every navigation boundary, including recreated-session branches.
- **Architecture:** registration, control, controller-change, and session persistence are distinct lifecycle contracts.
- **Data:** app-shell/service-worker evidence does not establish application-data correctness or durability.
- **Systems:** preserve exact run/head/artifact/environment and semantic artifact content; green/red metadata alone is insufficient.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical file changes required.

## CHANGE WATCH / OPEN
- Safari service-worker restart-aligned regression run `35810765603` pending.
- M003 permission/FGS transfers remain bounded to exact API-35 emulator environments; physical/OEM/other-API replication OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Ordinary Safari relaunch/profile persistence and lower-level SafariDriver fresh-session mechanism remain OPEN.
- OS-wide offline, eviction, physical-network failure diversity, iOS/iPadOS/EFB, physical device and canonical product runtime remain OPEN.

## Next work
Continue the current Safari service-worker evidence correction through run-bound semantic evidence. Do not restore combined TRANSFER VALIDATION from workflow status alone.
