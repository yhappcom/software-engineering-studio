# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering  
Prefix: `M###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-23

## Current evidence

### M001
**IN STUDY — DIRECT FLUTTER HOST/CHROME + BOUNDED ANDROID EMULATOR TRANSFER VALIDATED.** Exact repaired head `b6bfc4bf7e07c004c43326fb1821fd54de3986ba`, run `35507983649`, job `106070907373` terminal success. Physical Android, iOS, release-AOT, product artifacts and production remain OPEN.

### M002
**IN STUDY — BOUNDED ANDROID FORCE-STOP/FILE RECOVERY + ORDINARY HOME BACKGROUND/RESUME TRANSFERS VALIDATED.** Force-stop repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`, run `35516637659`; background/resume exact head `a278de3f2a9015195262b30662b1c240601f336e`, run `35529237932`. API-35 emulator scope only.

### M003
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME ORDINARY-BACKGROUND EXPIRY + FGS HELD→APP-STOP→EXPIRY→REQUESTABILITY BOUNDED TRANSFERS VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Physical/OEM/other-API independent replication remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE/RESTART/UPDATE/COLD-START + BOUNDED macOS SAFARI RUNTIME + BOUNDED SAFARI SERVICE-WORKER REGISTRATION/UPDATE/RESTART + SAME-SESSION ORIGIN-DOWN OFFLINE TRANSFERS VALIDATED; FRESH SAFARIDRIVER ORIGIN-DOWN COLD START CONTRADICTORY.**

Safari runtime remains valid at exact head `44c8be44bb53f2b67c08f40a0738f29858018bdd`, run `35727646652`, artifact `10694445918`.

Historical lifecycle run `35741047017` remains INVALID after its zero-byte semantic artifact exposed the Q006 verdict-propagation hazard. Fail-closed execution then exposed two harness defects: application-owned title state was incorrectly expected from JavaScript invocations destroyed by navigation during initial control and again during recreated-session restart.

**TRANSFER VALIDATION:** exact repaired head `54bbd5283920aa3d82057cc2da8a14b0db4bacbf`, run `35810765603`, completed success. Run-bound artifact `10729767594`, digest `sha256:34bc15dbb8cb15776571ded24d38de1d38b3be87228c644844de59551740f67f`, was directly inspected. Its non-empty oracle verdict is `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS`; observations show initial controller `false→true`, independent V1 confirmation, explicit V2 update with `controllerchange`, V2 control, fresh-WebDriver restart controller `false→true`, and independent V2 confirmation. Canonical closure: `research/mobile/M006_safari_service_worker_lifecycle_run4_closure.md`.

Safari offline discriminator remains separately bounded: exact head `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`, run `35780706023`, artifact `10718495328`. Same-session unavailable-origin navigation reached the cached app with controller=true; fresh WebDriver navigation failed. The latter contradiction and lower-level cause remain OPEN; the lifecycle PASS does not resolve it.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current Safari fixture evidence makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. The generic macOS Safari registration/control/update/restart fixture boundary is now professionally closed, but ordinary Safari profile relaunch/installed-PWA persistence, physical Android/OEM/other API, iOS/iPadOS lifecycle, broader plugin/native behavior, EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Foundations:** direct Dart/Flutter is already validated and not the blocker; browser/session evidence does not infer native/iOS/iPadOS/product execution.
- **Quality:** retain the complete false-green → fail-closed red → lifecycle-oracle isolation → repaired regression chain; oracle owner/lifetime must be rechecked at every navigation boundary.
- **Architecture:** registration, control, controller-change and session persistence are distinct lifecycle contracts.
- **Data:** app-shell/service-worker evidence does not establish application-data correctness or durability.
- **Systems:** exact run/head/artifact/environment plus semantic artifact content are required; workflow green alone is insufficient.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical file changes required.

## CHANGE WATCH / OPEN
- Ordinary Safari relaunch/profile persistence, installed PWA and lower-level SafariDriver fresh-session origin-down mechanism remain OPEN.
- M003 permission/FGS transfers remain bounded to exact API-35 emulator environments; physical/OEM/other-API replication OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- OS-wide offline, eviction, physical-network failure diversity, iOS/iPadOS/EFB, physical device and canonical product runtime remain OPEN.

## Next work
Return to Balance Loop. Do not repeat equivalent Safari registration/update/restart variants. Prefer a materially stronger evidence class: physical/native runtime, ordinary installed-PWA/profile persistence, exact-product PWA build/runtime when authorization exists, physical storage/connectivity, or another track's stronger Stage-1 gap.
