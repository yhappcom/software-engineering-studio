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
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME BACKGROUND EXPIRY + FGS-HELD AUTHORITY BOUNDED TRANSFER VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical includes `research/mobile/M003_android_user_permission_dialog_transfer.md`, `research/mobile/M003_android_repeated_denial_user_fixed_lifecycle.md`, `research/mobile/M003_one_time_permission_expiry_background_boundary.md`, `research/mobile/M003_one_time_permission_foreground_service_discriminator.md`, `research/mobile/M003_fgs_discriminator_run2_evidence.md`, and `research/mobile/M003_fgs_discriminator_run3_ack_oracle_isolation.md`.

User-driven one-time/fresh-denial transfer: exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, success.

**REPEATED-DENIAL TRANSFER VALIDATION:** exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, job `106398675688`, success. First denial produced `USER_SET`, second state-specific deny-and-don't-ask-again produced `USER_FIXED`, and a third app-originated request exposed no Permission Controller denial controls while callback/UI remained denied.

**ONE-TIME BACKGROUND EXPIRY TRANSFER VALIDATION:** exact evidence-preserving head `ae5597cc15fca07fcc63688a91f1cf8da9ac15f4`, run `35662745671`, artifact `10667827225`, digest `sha256:5f5784550773d99704067664263a46e3afd167fd9196fbfe41bc175c244b0c2f`. After real `Only this time` grant, authority remained through 55.4s after HOME; at 60.4s authority was revoked and PID absent, followed by successful re-requestability. The 60.4s value is an observation, not a portable Android timeout contract.

**FOREGROUND-SERVICE HELD-AUTHORITY TRANSFER VALIDATION:** exact head `3d948ef0c3cf63500aa840eebf0591d0df54c1bd`, run `35679723145`, artifact `10674236432`, digest `sha256:1c78cf8c7ac179fe1868477f58bb18bc2ed403c6f77d070356ef158b8705dfc5`. After real one-time CAMERA grant and a camera-type FGS started while visible, CAMERA authority, PID `2186`, and foreground-service state remained present at every 5-second observation through the 90-second HOME-background hold. The later run failure was isolated to the shell-driven explicit-stop transition; it does not invalidate the completed bounded hold subclaim and does not validate post-stop expiry.

**RUN-3 FAILURE ISOLATION:** exact head `5eaa1eeec4e6e99d3236a3e71d9957e544636b00`, run `35687049739`, artifact `10676369995`, digest `sha256:f9441fbb5c0ab81fd8ceb64680929808cc07730783d806ab838cb86f36dbf24a`, terminal failure. The app-owned-stop target again completed the full 90-second held-authority branch (PID `2139`) and then failed at `HARNESS_FAILURE:app_owned_stop` with `AssertionError('app-owned stop was not acknowledged')`. The committed harness locates Flutter labels by Android UIAutomator `text` **or** `content-desc`, but its stop acknowledgement verifier checks only `text` and aborts before the independent Android `service_active()` postcondition. This establishes an acknowledgement-oracle coverage/ordering defect, not whether `stopService()` itself succeeded. The run did not preserve the stop UI XML, so exact stop outcome remains OPEN.

**NEXT VALIDATION TARGET:** repair acknowledgement observation to accept `text` or `content-desc`, preserve matched node/UI dump evidence, and collect Android service state independently before classifying the stop. Continue to post-stop expiry/requestability only when service state proves the FGS stopped. Do not infer PASS from the UI acknowledgement alone.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current permission evidence is Studio-fixture evidence and makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Ordinary-background one-time expiry and the FGS-held-authority branch are closed only at bounded API-35 emulator transfer scope. Post-FGS-stop expiry/requestability remains under executable validation. Physical Android/iOS lifecycle, system-initiated process pressure, auto-reset/hibernation, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** control-plane acknowledgement and underlying subsystem state are distinct oracles. Run 3 shows that a narrow UI assertion can prevent collection of the stronger platform-state postcondition.
- **Architecture:** activity visibility, temporary permission authority, process lifetime, MethodChannel/UI state and FGS lifetime are distinct state dimensions.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** preserve exact run/head/artifact identity and UI dump/node diagnostics at UI-driven failure boundaries; CI conclusion alone is not the semantic verdict.
- **Design Studio:** flows must recover from one-time authority disappearing after backgrounding and represent continuing foreground-service access honestly. No Design canonical file edited.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- Repeated-denial, one-time-expiry and FGS-held-authority transfers are validated only at exact Studio/API-35 emulator environments; physical/OEM/other-API replication remains OPEN.
- Permission Controller resource IDs and UIAutomator semantics attributes are implementation/version-sensitive test observations, not product API contracts.
- Auto-reset/hibernation remains a separate OPEN lifecycle and must not be simulated by editing flags then called production-equivalent evidence.
- Post-FGS-stop expiry/requestability remains OPEN. Run 3 does not establish whether app-owned `stopService()` succeeded because the UI acknowledgement assertion aborted before service-state observation and the stop UI dump was not preserved.
- The exact root cause of run-2 shell `am stopservice` failure remains OPEN because its stderr was not preserved.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Repair the run-3 acknowledgement oracle and diagnostic ordering, then execute the same app-owned-stop target once with run-bound UI-node/service-state evidence. If service stop is established, continue the existing post-stop expiry/requestability boundary. Do not repeat the already validated 90-second FGS hold as the primary objective or tune grace duration.