# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering  
Prefix: `M###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-21

## Current evidence

### M001
**IN STUDY — DIRECT FLUTTER HOST/CHROME + BOUNDED ANDROID EMULATOR TRANSFER VALIDATED.** Exact repaired head `b6bfc4bf7e07c004c43326fb1821fd54de3986ba`, run `35507983649`, job `106070907373` terminal success. Physical Android, iOS, release-AOT, product artifacts and production remain OPEN.

### M002
**IN STUDY — BOUNDED ANDROID FORCE-STOP/FILE RECOVERY + ORDINARY HOME BACKGROUND/RESUME TRANSFERS VALIDATED.** Force-stop repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`, run `35516637659`, job `106093583857` success. Background/resume exact head `a278de3f2a9015195262b30662b1c240601f336e`, run `35529237932`, job `106126775150` success. API-35 emulator scope only.

### M003
**IN STUDY — USER-DIALOG TRANSFER VALIDATED; REPEATED-DENIAL / USER_FIXED FAILURE ISOLATED TO SECOND-DENIAL CLASS; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical: `research/mobile/M003_android_user_permission_dialog_transfer.md`, `research/mobile/M003_android_repeated_denial_user_fixed_lifecycle.md`.

Shell-controlled permission evidence retained: exact head `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`, run `35522782572`, job `106109634570` success.

**USER-DRIVEN DIALOG TRANSFER VALIDATION:** exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, completed success. The API-35 emulator fixture validates app-originated one-time CAMERA grant plus independent fresh-install denial with callback/UI and package-state agreement. Scope remains Flutter 3.47.5 + API-35 x86_64 Pixel 6 emulator only.

**REPEATED-DENIAL FAILURE:** exact head `bab16cc993d72d1ca98f3c9f2aa2bf4a4bbf8aa4`, run `35599908037`, job `106333291875`, completed failure. Setup/build/oracle/emulator wrapper succeeded. Baseline one-time and first-denial classifiers did not match failure; the metadata-visible `second denial and USER_FIXED transition` classifier failed and the complete-oracle gate failed. The current classifier groups `tap_request_denial_second`, `discover_second_denial_dialog`, `select_dont_allow_second`, `observe_denied_callback_second`, and `verify_user_fixed`, so ROOT CAUSE remains OPEN. No repeated-denial PASS/TRANSFER VALIDATION/REPLICATION is awarded. Next step is finer phase isolation and one reproduction before causal attribution.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528` attempt 1, job `106152447185`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, job `106204067727`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current repeated-denial work is Studio-fixture evidence and makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Physical Android/iOS lifecycle, system-initiated process pressure, one-time expiry/auto-reset, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** permission access state and requestability/dialog state need independent oracles; current grouped second-denial classifier must be split before root-cause attribution.
- **Architecture:** `DENIED + requestable` and `DENIED + USER_FIXED` are distinct interaction states despite equal access authority.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** one-time/revoked permission is least privilege, not complete authorization design; bounded Keystore evidence is not hardware-backed policy evidence.
- **Design Studio:** ordinary denial versus dialog-suppressed permanent denial can require different recovery/rationale/settings UX; repeated-denial behavior is not yet validated and no Design canonical file was edited.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- Repeated-denial run `35599908037` failed in the grouped second-denial/USER_FIXED transition; exact operation and ROOT CAUSE OPEN.
- User-driven dialog transfer is validated only at its exact head/run/environment; independent replication remains OPEN.
- Permission Controller resource IDs and permission-flag diagnostics are implementation/version-sensitive and require revalidation across materially different Android/OEM/API contexts.
- One-time expiry/background grace and auto-reset/hibernation remain OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Continue the current repeated-denial professional boundary. Split the second-denial classifier into metadata-visible semantic operations and reproduce once without changing application/platform semantics. Use the first exact failed phase to form/falsify a causal hypothesis; do not attribute the failure to Android or Flutter from the grouped failure alone.
