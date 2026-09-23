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
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME ORDINARY-BACKGROUND EXPIRY + FGS HELD→APP-STOP→EXPIRY→REQUESTABILITY BOUNDED TRANSFERS VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical research retains the full run/failure-isolation chain. Physical/OEM/other-API independent replication remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE/RESTART/UPDATE/COLD-START + BOUNDED macOS SAFARI RUNTIME + SAME-SESSION ORIGIN-DOWN OFFLINE TRANSFERS VALIDATED; SAFARI SERVICE-WORKER LIFECYCLE TRANSFER REOPENED AND UNDER FAILURE ISOLATION; FRESH SAFARIDRIVER COLD START CONTRADICTORY.**

Safari runtime repaired execution remains valid at exact head `44c8be44bb53f2b67c08f40a0738f29858018bdd`, run `35727646652`, job `106745123287`, artifact `10694445918`.

Historical lifecycle run `35741047017` remains INVALID after its zero-byte semantic artifact exposed the Q006 verdict-propagation hazard. Fail-closed repair head `6daa9781cc884aab601744a5decf7a7459d06906` converted that false-green path into a trustworthy red gate: run `35802543585`, job `106995919837`, terminal failure. Artifact `10726377605`, digest `sha256:67483e7b00559f54792f606f5f906ed55b82b8703c2ce63cc6c22326ca63cdcd`, preserved `ENABLE_RC=0`, an empty stdout oracle, and initial page/worker requests.

**ROOT CAUSE at the harness boundary:** the fixture's first `registerSW()` reloads an initially uncontrolled document. The validator then waited for `M006_SW_READY_V1`, a title that the pre-navigation invocation cannot produce after it is destroyed by reload. Commit `4f7e376572a6fe8c6eddea40e4d95841c4ce2033` repairs this by polling browser-owned `navigator.serviceWorker.controller`, then re-invoking the V1 semantic query in the controlled document, while retaining V2 update/controllerchange/restart checks and adding structured failure output. Regression run `35806396805` is in progress. No lifecycle PASS/TRANSFER VALIDATION is awarded yet.

Safari offline discriminator remains separately bounded: exact head `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`, run `35780706023`, artifact `10718495328`. Online control/cache and origin-down proof passed; same-session unavailable-origin navigation reached `M006_APP_READY` with controller=true; fresh WebDriver navigation failed. Same-session origin-down offline behavior remains bounded VALIDATION; fresh-WebDriver cold-start expectation remains CONTRADICTION with lower-level cause OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current Safari fixture evidence makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Safari service-worker lifecycle transfer is reopened pending lifecycle-aligned fail-closed regression. Ordinary Safari relaunch/profile persistence, installed PWA, physical Android/OEM/other API, iOS/iPadOS lifecycle, broader plugin/native behavior, EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Foundations:** browser/session evidence does not infer native/iOS/iPadOS/product execution.
- **Quality:** subprocess verdict propagation and navigation-spanning oracle lifetime are independent correctness properties; document-owned presentation state cannot be assumed to survive reload.
- **Architecture:** browser/profile/session identity and registration/control/controller-change are distinct lifecycle contracts.
- **Data:** app-shell CacheStorage success does not establish application-data correctness or durable persistence.
- **Systems:** preserve exact run/head/artifact/environment and verify semantic artifact content; green metadata alone is insufficient.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical file changes required.

## CHANGE WATCH / OPEN
- Safari service-worker lifecycle repaired regression run `35806396805` pending.
- M003 permission/FGS transfers remain bounded to exact API-35 emulator environments; physical/OEM/other-API replication OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Ordinary Safari relaunch/profile persistence and lower-level SafariDriver fresh-session mechanism remain OPEN.
- OS-wide offline, eviction, physical-network failure diversity, iOS/iPadOS/EFB, physical device and canonical product runtime remain OPEN.

## Next work
Continue the current Safari service-worker evidence correction through run-bound semantic evidence. Do not restore TRANSFER VALIDATION from workflow status alone.
