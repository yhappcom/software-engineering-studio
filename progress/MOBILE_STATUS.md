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
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME BACKGROUND EXPIRY + FGS-HELD AUTHORITY BOUNDED TRANSFER VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical includes `research/mobile/M003_android_user_permission_dialog_transfer.md`, `research/mobile/M003_android_repeated_denial_user_fixed_lifecycle.md`, `research/mobile/M003_one_time_permission_expiry_background_boundary.md`, `research/mobile/M003_one_time_permission_foreground_service_discriminator.md`, and `research/mobile/M003_fgs_discriminator_run2_evidence.md`.

User-driven one-time/fresh-denial transfer: exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, success.

**REPEATED-DENIAL TRANSFER VALIDATION:** exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, job `106398675688`, success. First denial produced `USER_SET`, second state-specific deny-and-don't-ask-again produced `USER_FIXED`, and a third app-originated request exposed no Permission Controller denial controls while callback/UI remained denied.

**ONE-TIME BACKGROUND EXPIRY TRANSFER VALIDATION:** exact evidence-preserving head `ae5597cc15fca07fcc63688a91f1cf8da9ac15f4`, run `35662745671`, artifact `10667827225`, digest `sha256:5f5784550773d99704067664263a46e3afd167fd9196fbfe41bc175c244b0c2f`. After real `Only this time` grant, authority remained through 55.4s after HOME; at 60.4s authority was revoked and PID absent, followed by successful re-requestability. The 60.4s value is an observation, not a portable Android timeout contract.

**FOREGROUND-SERVICE HELD-AUTHORITY TRANSFER VALIDATION:** exact head `3d948ef0c3cf63500aa840eebf0591d0df54c1bd`, run `35679723145`, job `106593845398`, artifact `10674236432`, digest `sha256:1c78cf8c7ac179fe1868477f58bb18bc2ed403c6f77d070356ef158b8705dfc5`. After real one-time CAMERA grant and a camera-type FGS started while visible, CAMERA authority, PID `2186`, and foreground-service state remained present at every 5-second observation through the 90-second HOME-background hold. The later run failure was isolated to the shell-driven explicit-stop transition; it does not invalidate the completed bounded hold subclaim and does not validate post-stop expiry.

**VALIDATION TARGET:** exact head `5eaa1eeec4e6e99d3236a3e71d9957e544636b00` replaces external shell `am stopservice` with an app-owned `stopService` path, explicit `STOP_ACCEPTED` UI acknowledgement, service-state check, HOME transition, then bounded post-stop expiry/requestability observation. Run `35687049739` was queued at the 2026-09-22 evidence check; no post-stop verdict is inferred before terminal artifact evidence.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current permission evidence is Studio-fixture evidence and makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Ordinary-background one-time expiry and the FGS-held-authority branch are now closed only at bounded API-35 emulator transfer scope. Post-FGS-stop expiry/requestability is under executable validation. Physical Android/iOS lifecycle, system-initiated process pressure, auto-reset/hibernation, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** preserve claim-scoped verdicts: a terminal-red run may still validate an earlier completed subclaim when run-bound evidence fixes the later failure boundary; never promote unexecuted downstream claims.
- **Architecture:** activity visibility, temporary permission authority, process lifetime and FGS lifetime are distinct state dimensions.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** preserve exact run/head/artifact identity and command/exception diagnostics; CI conclusion alone is not the semantic verdict.
- **Design Studio:** flows must recover from one-time authority disappearing after backgrounding and must represent continuing foreground-service access honestly. No Design canonical file edited.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- Repeated-denial, one-time-expiry and FGS-held-authority transfers are validated only at exact Studio/API-35 emulator environments; physical/OEM/other-API replication remains OPEN.
- Permission Controller resource IDs and permission-flag diagnostics are implementation/version-sensitive test observations, not product API contracts.
- Auto-reset/hibernation remains a separate OPEN lifecycle and must not be simulated by editing flags then called production-equivalent evidence.
- Post-FGS-stop expiry/requestability remains OPEN pending terminal evidence from the app-owned stop target.
- The exact root cause of run-2 shell `am stopservice` failure remains OPEN because its stderr was not preserved. Android's component-export rules make caller/access mismatch a plausible causal hypothesis, not established root cause.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Complete the exact app-owned stop validation target and inspect its run-bound semantic artifact. Do not repeat the already validated 90-second FGS hold as the primary objective. If post-stop observation is terminal and trustworthy, return to Balance Loop rather than tuning grace duration.