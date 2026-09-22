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
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME ORDINARY-BACKGROUND EXPIRY + FGS HELD→APP-STOP→EXPIRY→REQUESTABILITY BOUNDED TRANSFERS VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical includes `research/mobile/M003_android_user_permission_dialog_transfer.md`, `research/mobile/M003_android_repeated_denial_user_fixed_lifecycle.md`, `research/mobile/M003_one_time_permission_expiry_background_boundary.md`, `research/mobile/M003_one_time_permission_foreground_service_discriminator.md`, `research/mobile/M003_fgs_discriminator_run2_evidence.md`, `research/mobile/M003_fgs_discriminator_run3_ack_oracle_isolation.md`, and `research/mobile/M003_fgs_discriminator_run4_post_stop_closure.md`.

User-driven one-time/fresh-denial transfer: exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, success.

**REPEATED-DENIAL TRANSFER VALIDATION:** exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, job `106398675688`, success. First denial produced `USER_SET`, second state-specific deny-and-don't-ask-again produced `USER_FIXED`, and a third app-originated request exposed no Permission Controller denial controls while callback/UI remained denied.

**ONE-TIME ORDINARY-BACKGROUND EXPIRY TRANSFER VALIDATION:** exact head `ae5597cc15fca07fcc63688a91f1cf8da9ac15f4`, run `35662745671`, artifact `10667827225`, digest `sha256:5f5784550773d99704067664263a46e3afd167fd9196fbfe41bc175c244b0c2f`. After real `Only this time` grant, authority remained through 55.4s after HOME; at 60.4s authority was revoked and PID absent, followed by successful re-requestability. The 60.4s value is an observation, not a portable Android timeout contract.

**FOREGROUND-SERVICE FULL BOUNDED CAUSAL TRANSFER:** exact repaired head `07b389dfbbe3abf9440a00e7f80668a367b556f3`, run `35695122004`, artifact `10680900102`, digest `sha256:fe3ab7cbe28ec5a210c210cb27444d41da349787fe6e46d812451f603447ad0c`, Flutter 3.47.5 / Dart 3.13.4 / Android API-35 x86_64 Pixel 6 emulator family. A real one-time CAMERA grant plus camera FGS started while visible retained authority, PID `2031`, and service state through the full 90-second HOME hold. The app-owned stop acknowledgement was observed as UIAutomator `content-desc='SERVICE:STOP_ACCEPTED'` with empty `text`, and the independent Android service-state oracle observed `service_active=False`. After HOME without the FGS, authority remained through 55.9s and was revoked with PID absent at 60.9s; relaunch made the permission dialog requestable again. Semantic verdict: `FGS_HELD_THEN_APP_STOPPED_EXPIRED_AND_REQUESTABLE`.

**RUN-3 HARNESS REGRESSION CLOSED:** run 3 had established an acknowledgement-oracle coverage/ordering defect but could not establish its exact UI representation. Run 4 directly validates the repair: the acknowledgement was represented through `content-desc`, the broadened oracle recognized it, and independent service-state evidence was collected. This closes the named fixture defect; it does not retroactively establish run-3 platform state.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current permission evidence is Studio-fixture evidence and makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. The named API-35 emulator one-time-permission FGS causal boundary is now closed through app-owned stop, post-stop expiry, and requestability. This is bounded TRANSFER VALIDATION, not independent REPLICATION and not a timing contract. Physical Android/OEM/other API, iOS lifecycle, system-initiated process pressure, auto-reset/hibernation, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** run 4 closes the run-3 oracle regression: control-plane acknowledgement and underlying service state were collected independently; `content-desc` was the actual acknowledgement representation in this execution.
- **Architecture:** activity visibility, temporary permission authority, process lifetime, MethodChannel/UI state and FGS lifetime remain distinct state dimensions.
- **Data:** process/lifecycle recovery does not establish physical durability/backup correctness.
- **Systems:** preserve exact run/head/artifact identity and semantic payload; CI conclusion alone is not the semantic verdict.
- **Design Studio:** flows using one-time authority plus FGS must represent ongoing access honestly and recover after authority loss. No Design canonical file edited.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- Repeated-denial and one-time/FGS transfers are validated only at exact Studio/API-35 emulator environments; physical/OEM/other-API replication remains OPEN.
- 60.4s ordinary-background and 60.9s post-stop expiry are observations, not portable Android grace-duration contracts.
- Permission Controller resource IDs and UIAutomator semantics attributes are implementation/version-sensitive test observations, not product API contracts.
- Auto-reset/hibernation remains a separate OPEN lifecycle and must not be simulated by editing flags then called production-equivalent evidence.
- User revocation while an FGS is active and actual camera-resource continuation remain separate OPEN paths.
- The exact root cause of run-2 shell `am stopservice` failure remains OPEN because its stderr was not preserved; it no longer blocks the app-owned lifecycle boundary.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Return to Balance Loop. Do not continue timing permutations on the same API-35 emulator fixture. Prefer a materially different evidence class with higher Stage-1 leverage: physical/native Android/iOS, Safari/iPadOS/EFB, exact-product runtime/build, physical storage/connectivity, or another track's stronger prerequisite gap.