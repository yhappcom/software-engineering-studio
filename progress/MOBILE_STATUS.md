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
**IN STUDY — SHELL-CONTROLLED PERMISSION TRANSFER + BOUNDED USER-DRIVEN DIALOG TRANSFER VALIDATION + BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical: `research/mobile/M003_android_user_permission_dialog_transfer.md`.

Shell-controlled permission evidence retained: exact head `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`, run `35522782572`, job `106109634570` success.

**USER-DRIVEN DIALOG TRANSFER VALIDATION:** after a four-execution failure/isolation chain, exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, completed success. The fixture preserves app-originated CAMERA request semantics and replaces presentation-dependent English system-control lookup with Permission Controller resource-id identities. Actual one-time grant and independent fresh-install denial paths completed; Flutter callback/UI and independent package-manager state agreed; every phase classifier and the complete-oracle gate succeeded. Scope is Flutter 3.47.5 + API-35 x86_64 Pixel 6 emulator only. This is TRANSFER VALIDATION, not independent REPLICATION, physical-device, OEM, product or production evidence.

The failure chain matters: a text-only app selector first failed at request tap; text/content-desc advanced to system-control discovery; the English `Only this time` oracle then failed; semantic Permission Controller control identity advanced through the complete contract. Selector/control identity is therefore part of oracle validity. Exact app accessibility attribute remains unrecovered and Permission Controller resource IDs remain version-sensitive CHANGE WATCH.

Keystore evidence retained: complete PASS exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528` attempt 1, job `106152447185`; second complete execution exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, job `106204067727`. Bounded **REPLICATION** only for API-35 x86_64 emulator scope. Intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current M003 user-dialog work is Studio-fixture evidence and makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Physical Android/iOS lifecycle, system-initiated process pressure, one-time expiry/auto-reset, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Quality:** selector/control identity is part of oracle validity; preserve the failure→isolation→causal intervention chain and avoid localized presentation strings when a validated semantic identity is available.
- **Architecture:** permission/key/storage failure states remain explicit contract states.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** one-time permission is least privilege, not complete authorization design; bounded Keystore evidence is not hardware-backed policy evidence.
- **Design Studio:** permission rationale/denial UX remains downstream handoff.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- User-driven dialog transfer is validated only at exact head/run/environment above; independent replication remains OPEN.
- Permission Controller resource IDs are implementation/version-sensitive and require revalidation across materially different Android/OEM/API contexts.
- Exact matched app accessibility attribute from the earlier selector intervention remains unrecovered; do not overstate attribute-level ROOT CAUSE.
- One-time expiry/background grace, repeated-denial `USER_FIXED`, auto-reset/hibernation OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Return to Balance Loop rather than repeating the successful emulator dialog fixture. Prefer a materially different high-leverage evidence class: one-time expiry/auto-reset lifecycle if it can be executed without simulation, physical/native lifecycle/storage/connectivity, Safari/iPadOS/EFB, authorized exact-product runtime/build, or another track's stronger Stage-1 gap.
