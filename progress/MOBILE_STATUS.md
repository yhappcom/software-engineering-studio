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
**IN STUDY — SHELL-CONTROLLED PERMISSION TRANSFER + BOUNDED KEYSTORE SEMANTIC REPLICATION; USER-DRIVEN DIALOG FAILURE REPRODUCED AND ISOLATED TO INITIAL ONE-TIME REQUEST TAP; ROOT CAUSE OPEN.** Canonical research includes `M003_android_user_permission_dialog_transfer.md`.

Shell-controlled permission evidence retained: exact head `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`, run `35522782572`, job `106109634570` success.

**USER-DRIVEN DIALOG:** execution 1 exact head `63f96e010691db87fea13bc7e08866c082dfb656`, run `35564720878`, job `106224179388` failed opaquely. Phase-reporting execution 2 exact head `1426e11bd7ef708dcb126579de3eab7e7ff72472`, run `35573084874`, job `106248740578` reproduced failure and narrowed it to a grouped request-interaction class. Split-classifier execution 3 exact head `c9328340a77c010c1b3b67a8f7ab42350f637bd8`, run `35578458429`, job `106265550190` reproduced the failure and isolated the first failed operation to **`tap_request_one_time`**; denial-request and later classifiers did not match. No permission-platform failure, PASS, TRANSFER VALIDATION or ROOT CAUSE is inferred.

At the failing head the tap helper requires exact UIAutomator `text='REQUEST CAMERA'`, while the prior UI-presence check searches serialized XML. Current causal hypothesis: Flutter platform accessibility export may make the actionable label available through `content-desc` instead. Exact head `409075c7f208a134ad3a5910bab0db44571e0ad3` preserves application/permission semantics but allows exact `text` or `content-desc` selector matching and logs the matched channel. Execution verdict pending; this is a causal intervention, not a fix verdict.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528` attempt 1, job `106152447185`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, job `106204067727`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current M003 work is Studio-fixture evidence.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Physical Android/iOS lifecycle, system-initiated process pressure, one-time expiry/auto-reset, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** phase reporting now isolates the initial request tap; UI-automation selector/channel is part of oracle validity and is under causal test.
- **Architecture:** permission/key/storage failure states remain explicit contract states.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** one-time permission is least privilege, not complete authorization design; bounded Keystore evidence is not hardware-backed policy evidence.
- **Design Studio:** permission rationale/denial UX remains downstream handoff.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- User-driven dialog run `35578458429`: FAILURE isolated to `tap_request_one_time`; ROOT CAUSE OPEN.
- Exact head `409075c7...` tests the `text` vs `content-desc` selector hypothesis without changing permission semantics; execution evidence pending.
- One-time expiry/background grace, repeated-denial `USER_FIXED`, auto-reset/hibernation OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Observe the bounded selector-channel intervention once. If it advances the request interaction, use the logged selector channel plus downstream oracle result to judge the causal hypothesis; do not infer a platform permission defect from prior selector failure. If it fails at the same phase, reject/weaken that hypothesis and isolate readiness/bounds/activity interaction instead. Do not repeat unchanged runs.
