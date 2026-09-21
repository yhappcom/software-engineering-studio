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
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME BACKGROUND EXPIRY BOUNDED TRANSFER VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical: `research/mobile/M003_android_user_permission_dialog_transfer.md`, `research/mobile/M003_android_repeated_denial_user_fixed_lifecycle.md`, `research/mobile/M003_one_time_permission_expiry_background_boundary.md`.

User-driven one-time/fresh-denial transfer: exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, success.

**REPEATED-DENIAL TRANSFER VALIDATION:** exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, job `106398675688`, success. First denial produced `USER_SET`, second state-specific deny-and-don't-ask-again produced `USER_FIXED`, and a third app-originated request exposed no Permission Controller denial controls while callback/UI remained denied. Earlier second-dialog failure is closed for this target as a harness oracle/control-identity mismatch.

**ONE-TIME BACKGROUND EXPIRY TRANSFER VALIDATION:** exact evidence-preserving head `ae5597cc15fca07fcc63688a91f1cf8da9ac15f4`, run `35662745671`, success. Run-bound artifact id `10667827225`, digest `sha256:5f5784550773d99704067664263a46e3afd167fd9196fbfe41bc175c244b0c2f`, records Flutter 3.47.5 / Dart 3.13.4 and the semantic timeline. After real `Only this time` grant, PID `2246` remained alive and authority remained granted through 55.4s after HOME; at 60.4s authority was revoked and PID was absent. Relaunch + a new app-originated request exposed the permission dialog again. Verdict: `OBSERVED_EXPIRY_AND_REQUESTABILITY`. The 60.4s value is an observation, not a portable Android timeout contract. Physical/OEM/other-API independent REPLICATION remains OPEN.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current permission evidence is Studio-fixture evidence and makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. The ordinary-background one-time-permission semantic boundary is now closed at bounded API-35 emulator transfer scope, but physical Android/iOS lifecycle, system-initiated process pressure, auto-reset/hibernation, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** preserve three-valued observation semantics and run-bound verdict/timeline evidence; do not convert the observed 60.4s into a fixed-time oracle.
- **Architecture:** temporary permission authority, lifecycle and requestability/recovery are distinct state dimensions.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** CI semantic evidence is bound to exact run/head/artifact digest; a future foreground-service discriminator must use current service-type/manifest/runtime requirements.
- **Design Studio:** flows must recover from one-time authority disappearing after backgrounding; ordinary denial versus dialog-suppressed permanent denial also requires distinct UX. No Design canonical file edited.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- Repeated-denial and one-time-expiry transfers are validated only at exact Studio/API-35 emulator environments; physical/OEM/other-API replication remains OPEN.
- Permission Controller resource IDs and permission-flag diagnostics are implementation/version-sensitive test observations, not product API contracts.
- Auto-reset/hibernation remains a separate OPEN lifecycle and must not be simulated by editing flags then called production-equivalent evidence.
- Foreground-service continuation is not yet compared against the ordinary-background expiry observation.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Return to Balance Loop. Do not repeat the ordinary-background expiry fixture merely to accumulate green runs or tune the observed expiry time. Prefer a materially different evidence class: a correctly specified foreground-service discriminator if it has sufficient cross-track leverage, physical/native Android/iOS evidence, Safari/iPadOS/EFB, exact-product runtime/build, physical storage/connectivity, or another track's stronger Stage-1 gap. Do not promote Stage 1 from emulator-only evidence.