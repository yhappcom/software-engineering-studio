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
**IN STUDY — SHELL-CONTROLLED PERMISSION TRANSFER + BOUNDED KEYSTORE SEMANTIC REPLICATION; USER-DRIVEN DIALOG FAILURE NOW ADVANCED FROM APP REQUEST TAP TO SYSTEM ONE-TIME CONTROL DISCOVERY.** Canonical: `research/mobile/M003_android_user_permission_dialog_transfer.md`.

Shell-controlled permission evidence retained: exact head `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`, run `35522782572`, job `106109634570` success.

**USER-DRIVEN DIALOG:** executions 1–3 progressed from opaque failure to exact `tap_request_one_time` isolation. Execution 4 exact head `409075c7f208a134ad3a5910bab0db44571e0ad3`, run `35583802011`, job `106282376014`, changed only the app-button UIAutomator selector from exact `text` to exact `text` OR `content-desc`. The request-tap classifier then passed and the first failure moved to **`discover_one_time_choice`**. This supports a harness-selector/accessibility-channel cause for the earlier request-tap boundary, but current metadata does not expose which attribute matched, so attribute-level ROOT CAUSE is not claimed. No Android permission-platform failure is inferred.

The current system-choice discovery relied on English literal `Only this time`, which is a presentation-dependent oracle. Exact head `6fda0223249e723f2b9ee636a7329a97ec64b697` preserves application/permission semantics and tests permission-controller semantic resource-id suffixes `permission_allow_one_time_button` / `permission_deny_button`. Run `35589277729` was queued at evidence capture. No PASS or TRANSFER VALIDATION yet.

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
- **Quality:** selector/control identity is part of oracle validity; the app-button intervention advanced the failure boundary and system-control identity is now under falsification.
- **Architecture:** permission/key/storage failure states remain explicit contract states.
- **Data:** process recovery does not establish physical durability/backup correctness.
- **Systems:** one-time permission is least privilege, not complete authorization design; bounded Keystore evidence is not hardware-backed policy evidence.
- **Design Studio:** permission rationale/denial UX remains downstream handoff.
- **Web Manager / Marketing Manager:** no material dependency for this block.

## CHANGE WATCH / OPEN
- User-driven dialog run `35583802011`: app request tap advanced; first failure is `discover_one_time_choice`.
- Exact matched app accessibility attribute remains unrecovered from metadata; do not overstate selector ROOT CAUSE.
- Exact head `6fda0223...`, run `35589277729`, tests semantic permission-controller resource-id discovery/tap; verdict pending.
- One-time expiry/background grace, repeated-denial `USER_FIXED`, auto-reset/hibernation OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Observe run `35589277729` once. If resource-id discovery advances, follow the next independently classified semantic boundary through callback/package-state/denial/natural completion. If it fails at discovery, reject the assumed resource identity for this environment and inspect the actual permission-controller tree via metadata-visible evidence rather than guessing another label. Do not repeat unchanged runs.
