# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering  
Prefix: `M###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-22

## Current evidence

### M001
**IN STUDY — DIRECT FLUTTER HOST/CHROME + BOUNDED ANDROID EMULATOR TRANSFER VALIDATED.** Exact repaired head `b6bfc4bf7e07c004c43326fb1821fd54de3986ba`, run `35507983649`, job `106070907373` terminal success. Physical Android, iOS, release-AOT, product artifacts and production remain OPEN.

### M002
**IN STUDY — BOUNDED ANDROID FORCE-STOP/FILE RECOVERY + ORDINARY HOME BACKGROUND/RESUME TRANSFERS VALIDATED.** Force-stop repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`, run `35516637659`, job `106093583857` success. Background/resume exact head `a278de3f2a9015195262b30662b1c240601f336e`, run `35529237932`, job `106126775150` success. API-35 emulator scope only.

### M003
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED BOUNDED TRANSFER VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION; ONE-TIME BACKGROUND EXPIRY SOURCE/MODEL ADVANCED.** Canonical: `research/mobile/M003_android_user_permission_dialog_transfer.md`, `research/mobile/M003_android_repeated_denial_user_fixed_lifecycle.md`, `research/mobile/M003_one_time_permission_expiry_background_boundary.md`.

User-driven one-time/fresh-denial transfer: exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, success.

**REPEATED-DENIAL TRANSFER VALIDATION:** exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, job `106398675688`, attempt 1, success. Flutter 3.47.5 / Dart 3.13.4 on API-35 x86_64 Pixel 6 emulator. Executed first denial (`USER_SET`), second state-specific `permission_deny_and_dont_ask_again_button`, resulting `USER_FIXED`, third app-originated request with no Permission Controller denial controls, denied callback/UI, phase `complete`, and natural successful job completion. This awards bounded TRANSFER VALIDATION, not REPLICATION. Earlier second-dialog failure is closed for this target as a harness oracle/control-identity mismatch, not an Android/Flutter semantic failure.

**ONE-TIME BACKGROUND EXPIRY:** authoritative Android guidance was rechecked 2026-09-22. The platform guarantees continued access while visible and describes only a `short period` of ordinary background grace; it does not publish a portable fixed timeout. A foreground service started while visible is an explicit discriminator because access can continue until that service stops. Validation design now requires real one-time dialog interaction, package authority, process PID/liveness, lifecycle/service state, relaunch/requestability, and a three-valued ordinary-background verdict. `still granted when bounded observation ends` is INCONCLUSIVE for expiry, not platform FAIL. No executable PASS is awarded for this block.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528` attempt 1, job `106152447185`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, job `106204067727`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current permission evidence is Studio-fixture evidence and makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Physical Android/iOS lifecycle, system-initiated process pressure, executable one-time expiry/auto-reset, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** one-time expiry needs a three-valued bounded observation verdict; do not convert an unspecified Android grace duration into a fixed-time failure oracle. Preserve independent authority/process/lifecycle/requestability oracles.
- **Architecture:** temporary permission authority, lifecycle and requestability/recovery are distinct state dimensions.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** foreground-service discriminator must use current service-type/manifest/runtime requirements; one-time/revoked permission is least privilege, not complete authorization design; bounded Keystore evidence is not hardware-backed policy evidence.
- **Design Studio:** flows must recover from one-time authority disappearing after backgrounding; ordinary denial versus dialog-suppressed permanent denial also requires distinct UX. No Design canonical file edited.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- Repeated-denial transfer is validated only at exact head/run/environment; physical/OEM/other-API replication remains OPEN.
- Permission Controller resource IDs and permission-flag diagnostics are implementation/version-sensitive test observations, not product API contracts.
- One-time expiry/background grace executable observation remains OPEN; Android documents no portable fixed grace timeout.
- Auto-reset/hibernation remains a separate OPEN lifecycle and must not be simulated by editing flags then called production-equivalent evidence.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Use Balance Loop. For M003 one-time expiry, execute only when the harness can preserve `observed expiry` versus `bounded window exhausted/inconclusive` without inventing a timeout guarantee; a matched foreground-service discriminator is stronger than arbitrary sleep-duration tuning. Otherwise prefer physical/native lifecycle/connectivity, Safari/iPadOS/EFB, authorized exact-product runtime/build, or another higher-leverage prerequisite. Do not promote Stage 1 from emulator-only evidence.