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
**IN STUDY — USER-DIALOG + REPEATED-DENIAL/USER_FIXED + ONE-TIME ORDINARY-BACKGROUND EXPIRY + FGS HELD→APP-STOP→EXPIRY→REQUESTABILITY BOUNDED TRANSFERS VALIDATED; BOUNDED KEYSTORE SEMANTIC REPLICATION.** Canonical research retains the full run/failure-isolation chain.

Repeated-denial transfer exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, success. Ordinary one-time expiry exact head `ae5597cc15fca07fcc63688a91f1cf8da9ac15f4`, run `35662745671`, artifact `10667827225`, observed revocation at 60.4s; observation is not a portable timeout contract.

Foreground-service full bounded causal transfer exact repaired head `07b389dfbbe3abf9440a00e7f80668a367b556f3`, run `35695122004`, artifact `10680900102`, digest `sha256:fe3ab7cbe28ec5a210c210cb27444d41da349787fe6e46d812451f603447ad0c`. A real one-time CAMERA grant plus camera FGS retained authority/PID/service through 90 seconds HOME; app-owned stop was independently acknowledged and service state became false; after HOME without FGS authority expired at observed 60.9s and requestability returned. Run-3 acknowledgement-oracle regression is closed by run 4.

Keystore bounded REPLICATION retained at API-35 x86_64 emulator scope; intermittent first-launch ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE/RESTART/UPDATE/COLD-START TRANSFER + BOUNDED macOS SAFARI RUNTIME TRANSFER VALIDATED.**

Safari repaired execution: exact workflow head `44c8be44bb53f2b67c08f40a0738f29858018bdd`, run `35727646652`, job `106745123287`, runner `macos-15`, terminal success. The release JavaScript build, noninteractive Safari WebDriver enablement, isolated Selenium provisioning, and fail-closed Safari semantic oracle all completed successfully. Artifact `10694445918`, digest `sha256:f1274228bdbfaf29b6eca507a6e490385dbf3756777ce7e130007ecbb75bdf35` is bound to the exact head/run. The committed oracle creates `webdriver.Safari`, loads the release artifact, polls browser-owned `driver.title`, and fails unless it observes `M006_ASYNC_READY`; therefore this is bounded executable **TRANSFER VALIDATION** beyond Chromium. The artifact ZIP payload was not downloadable through the current connector, so per-poll observations/capability payload are not invented.

The failure chain is retained: interactive WebDriver enablement probe defect → noninteractive repair; then PEP 668 system-Python Selenium provisioning defect → isolated venv repair → green semantic regression. Canonical: `research/mobile/M006_flutter_safari_runtime_transfer.md`.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current permission/Safari-fixture evidence makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Browser-engine transfer is stronger now, but physical Android/OEM/other API, iOS/iPadOS lifecycle, broader plugin/native behavior, Safari PWA offline/update semantics, EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Foundations:** bounded macOS Safari runtime transfer is now executable evidence; do not infer native/iOS/iPadOS/product execution.
- **Quality:** Safari chain supplies setup failure→root cause→repair→semantic regression evidence; preserve the fail-closed oracle contract.
- **Architecture:** lifecycle/platform/browser state dimensions remain externally meaningful boundaries.
- **Data:** browser execution does not establish persistence/durability semantics.
- **Systems:** preserve exact run/head/artifact identity; product transfer still requires product-owned build provenance.
- **Design Studio:** no visual/interaction semantic evidence.
- **Web Manager / Marketing Manager:** considered; no canonical file changes required.

## CHANGE WATCH / OPEN
- Repeated-denial and one-time/FGS transfers remain bounded to exact API-35 emulator environments; physical/OEM/other-API replication OPEN.
- Permission Controller resource IDs and UIAutomator semantics attributes are implementation/version-sensitive observations.
- Auto-reset/hibernation, user revocation while FGS active and actual camera-resource continuation remain separate OPEN paths.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- macOS Safari runtime is validated only for the bounded fixture; Safari service-worker/offline/update, iOS/iPadOS/EFB and physical device remain OPEN.
- Hardware-backed/StrongBox and canonical product runtime remain OPEN.

## Next work
Do not repeat the same macOS Safari async-title fixture. Return to Balance Loop and prefer a materially independent evidence class: physical/native runtime, Safari PWA lifecycle, exact-product authorized build/runtime, physical storage/connectivity, natural release/ADR evidence, or another stronger Stage-1 gap.
