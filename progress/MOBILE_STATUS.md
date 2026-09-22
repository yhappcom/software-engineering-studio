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
**IN STUDY — REAL CHROMIUM OFFLINE/RESTART/UPDATE/COLD-START TRANSFER VALIDATED; SAFARI SEMANTIC TRANSFER BLOCKED AT HOSTED WEBDRIVER ENABLEMENT.**

Safari execution 3: exact workflow head `e4c68d1418eb5cda6193dbbb98b1171031053153`, run `35716201875`, job `106708178990`, `macos-15`, terminal failure. Checkout/toolchain capture/release Flutter JavaScript build succeeded; `Enable Safari WebDriver with diagnostics` failed promptly and the semantic Safari oracle was skipped. Artifact `10690100321`, digest `sha256:def6b87ba8d1bab89eb3bd749eb0cdf277a45f36a7d243291141e2edf369ef47` was preserved. The current connector cannot retrieve its payload/job logs, so exact enable stderr/return code remains OPEN. No Safari PASS/CONTRADICTION/TRANSFER VALIDATION is awarded. Canonical: `research/mobile/M006_flutter_safari_runtime_transfer.md`.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current permission/Safari-fixture evidence makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. API-35 emulator permission/FGS causal evidence is substantial, but physical Android/OEM/other API, iOS lifecycle, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent. Safari hosted validation is currently an environment/diagnostic-access dependency, not a semantic runtime verdict.

## Dependencies / handoffs
- **Foundations:** Safari semantic runtime remains OPEN; do not infer it from a successful Flutter web build.
- **Quality:** run-3 Safari prerequisite now fails closed without the prior interactive hang, but diagnostic payload retrievability is part of the validation harness contract.
- **Architecture:** lifecycle/platform/browser state dimensions remain externally meaningful boundaries.
- **Data:** process/lifecycle recovery does not establish physical durability/backup correctness.
- **Systems:** preserve exact run/head/artifact identity; hosted Safari automation enablement and artifact/log retrieval are environment capabilities.
- **Design Studio:** no new visual/interaction semantic evidence.
- **Web Manager / Marketing Manager:** considered; no canonical file changes required.

## CHANGE WATCH / OPEN
- Repeated-denial and one-time/FGS transfers remain bounded to exact API-35 emulator environments; physical/OEM/other-API replication OPEN.
- Permission Controller resource IDs and UIAutomator semantics attributes are implementation/version-sensitive observations.
- Auto-reset/hibernation, user revocation while FGS active and actual camera-resource continuation remain separate OPEN paths.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Safari run-3 exact enable stderr/return code OPEN until artifact/log payload is readable; semantic Safari WebDriver session and `M006_ASYNC_READY` remain unexecuted.
- Physical Android/iOS, hardware-backed/StrongBox, Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Do not repeat Safari privilege/flag permutations without the preserved run-3 diagnostic payload or a trustworthy environment with Safari remote automation already enabled. Return to Balance Loop and prefer a materially independent evidence class until that dependency changes: physical/native runtime, exact-product authorized build/runtime, physical storage/connectivity, natural release/ADR evidence, or another stronger Stage-1 gap.
