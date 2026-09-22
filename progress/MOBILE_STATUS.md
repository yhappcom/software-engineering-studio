# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering  
Prefix: `M###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-23

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
**IN STUDY — REAL CHROMIUM OFFLINE/RESTART/UPDATE/COLD-START + BOUNDED macOS SAFARI RUNTIME + SAFARI SERVICE-WORKER LIFECYCLE + SAME-SESSION ORIGIN-DOWN OFFLINE TRANSFERS VALIDATED; FRESH SAFARIDRIVER COLD START CONTRADICTORY.**

Safari runtime repaired execution: exact head `44c8be44bb53f2b67c08f40a0738f29858018bdd`, run `35727646652`, job `106745123287`, runner `macos-15`, terminal success. Artifact `10694445918`, digest `sha256:f1274228bdbfaf29b6eca507a6e490385dbf3756777ce7e130007ecbb75bdf35`.

Safari service-worker lifecycle transfer: exact head `d31cc310f7444a3b1880b1faae7901314a801a34`, run `35741047017`, job `106790579808`, terminal success. V1 registration/control → byte-different V2 update → `controllerchange` → V2 control → V2 registration/control after WebDriver recreation is bounded **TRANSFER VALIDATION**.

Safari offline discriminator: exact head `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`, run `35780706023`, terminal failure; artifact `10718495328`, digest `sha256:ec95755ab0c98a8b9e8f6ead62bc3d190c3edeedd6e4b0a0f78b6e7d2113c563`, directly inspected. Environment: macOS 15.7.9 build 24G830, Safari/safaridriver 26.6.1. Online execution/control and cache precondition passed; independent probe proved `origin-down=true`. With the **same Safari WebDriver session**, unavailable-origin navigation still reached `M006_APP_READY` with controller=true. After quitting/recreating WebDriver, unavailable-origin navigation repeatedly returned `Failed to open page` and timed out.

**VALIDATION:** bounded macOS Safari origin-down offline fetch/cache/app-shell execution is positively established for the surviving browsing session. **CONTRADICTION:** fresh-WebDriver cold-start expectation fails. **ROOT CAUSE remains OPEN** below the isolated session-recreation/state-identity boundary; do not equate SafariDriver recreation with ordinary Safari relaunch or installed PWA restart.

Canonical: `research/mobile/M006_flutter_safari_runtime_transfer.md`, `research/mobile/M006_safari_service_worker_lifecycle_transfer.md`, `research/mobile/M006_safari_offline_cold_start_transfer.md`, `research/mobile/M006_safari_offline_cold_start_failure_isolation.md`.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current Safari fixture evidence makes no product-runtime claim.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Same-session macOS Safari origin-down offline app-shell behavior is now bounded executable evidence, but ordinary Safari relaunch/profile persistence, installed PWA, physical Android/OEM/other API, iOS/iPadOS lifecycle, broader plugin/native behavior, EFB, canonical product runtime and production evidence remain materially absent.

## Dependencies / handoffs
- **Foundations:** bounded Safari evidence is browser/session evidence; do not infer native/iOS/iPadOS/product execution.
- **Quality:** recovery/restart harnesses must preserve or explicitly vary the state identity named by the claim; a later restart failure must not erase a preceding positive offline-fetch observation.
- **Architecture:** browser/profile/session identity can be externally meaningful to offline boot and must be explicit in validation boundaries.
- **Data:** app-shell CacheStorage success does not establish application-data correctness or durable persistence.
- **Systems:** preserve exact run/head/artifact/environment and browser/profile/storage identity; product transfer still requires product-owned build provenance.
- **Design Studio:** no visual/interaction semantic evidence.
- **Web Manager / Marketing Manager:** considered; no canonical file changes required.

## CHANGE WATCH / OPEN
- M003 permission/FGS transfers remain bounded to exact API-35 emulator environments; physical/OEM/other-API replication OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN.
- Safari same-session origin-down offline transfer is bounded to the Studio fixture/environment.
- Ordinary Safari relaunch/profile persistence and lower-level SafariDriver fresh-session mechanism remain OPEN.
- OS-wide offline, eviction, physical-network failure diversity, iOS/iPadOS/EFB, physical device and canonical product runtime remain OPEN.
- Hardware-backed/StrongBox and canonical product runtime remain OPEN.

## Next work
Do not repeat equivalent same-session/fresh-WebDriver variants. Return to Balance Loop and prefer a materially stronger evidence class: ordinary browser/profile relaunch if a trustworthy mechanism exists, installed/physical iOS/iPadOS/EFB, physical Android/OEM, exact product PWA build/runtime, physical storage/connectivity, or another track's stronger Stage-1 gap.
