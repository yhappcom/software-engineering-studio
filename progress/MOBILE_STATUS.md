# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering  
Prefix: `M###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-21

## Current evidence

### M001
**IN STUDY — DIRECT FLUTTER HOST/CHROME + BOUNDED ANDROID EMULATOR TRANSFER VALIDATED.** Exact repaired head `b6bfc4bf7e07c004c43326fb1821fd54de3986ba`, run `35507983649`, job `106070907373` terminal success. Physical Android, iOS, release-AOT, product artifacts and production remain OPEN.

### M002
**IN STUDY — BOUNDED ANDROID FORCE-STOP/FILE RECOVERY + ORDINARY HOME BACKGROUND/RESUME TRANSFERS VALIDATED.** Force-stop repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`, run `35516637659`, job `106093583857` success. Controlled force-stop is not low-memory/system-initiated kill or physical durability evidence.

Canonical background block: `research/mobile/M002_android_background_lifecycle_transfer.md`. Exact workflow head `a278de3f2a9015195262b30662b1c240601f336e`, run `35529237932`, job `106126775150` completed success. It pins Flutter tag `3.47.5` and requires same PID across HOME/background/resume, Flutter UI history containing `paused` and `resumed`, native `onPause`/`onStop` and a second `onResume`, plus natural completion. This is bounded API-35 x86_64 emulator TRANSFER VALIDATION, not a process-retention guarantee.

### M003
**IN STUDY — BOUNDED SHELL-CONTROLLED RUNTIME-PERMISSION + KEYSTORE PROCESS/TAMPER TRANSFERS VALIDATED; KEYSTORE SEMANTIC REPLICATION ACHIEVED AT EMULATOR SCOPE; USER-DRIVEN PERMISSION DIALOG TRANSFER NOW EXECUTING; INTERMITTENT KEYSTORE ROOT CAUSE OPEN.** Canonical includes `research/mobile/M003_android_runtime_permission_revocation_transfer.md`, `M003_android_keystore_secure_storage_transfer.md`, `M003_first_launch_observation_isolation.md`, `M003_keystore_semantic_first_launch_instrumentation.md`, and `M003_android_user_permission_dialog_transfer.md`.

Permission evidence retained: exact Studio head `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`, run `35522782572`, job `106109634570` completed success for shell-controlled denied → granted → revoked/denied state, process replacement and natural completion.

**NEW VALIDATION IN PROGRESS:** Android's current primary guidance confirms `Only this time` for camera/microphone/location on Android 11+ and requires apps to tolerate denial/revocation. Exact Studio head `63f96e010691db87fea13bc7e08866c082dfb656`, workflow run `35564720878` uses pinned Flutter 3.47.5 and API-35 x86_64 emulator. The app itself calls Android's runtime permission API; the oracle locates and taps the actual system `Only this time` control, independently checks app callback/UI plus package-manager grant state, then uninstall/reinstalls and exercises an actual system-dialog `Don’t allow` choice with denied-state checks. At status capture the run is **in_progress**; **no PASS** is awarded. This intentionally does not simulate one-time expiry or auto-reset.

Initial Keystore semantic PASS: exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528`, attempt 1, job `106152447185` completed success. Environment: Android 15/API 35 x86_64 emulator; Flutter 3.47.5 revision `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`; engine `af7e796e161ae0bb1ff0758c71a7105418bd9ded`; Dart 3.13.4 stable linux_x64; Ubuntu 24.04.5. Logs show `WROTE:secure-v1:NONEXPORTABLE` → force-stop/fresh cold process → `RECOVERED:secure-v1:NONEXPORTABLE` → external ciphertext mutation → `AUTH_FAIL` → natural completion.

**CONTRADICTION retained:** same-head attempt 2, job `106160817014`, failed at first launch, and later instrumented semantic run `35554495251`, job `106195370405`, also failed without externally recoverable exact phase. These failures reproduce an intermittent first-launch-adjacent class but do not establish root cause.

**FIRST-LAUNCH ISOLATION PASS:** exact diagnostic head `282f3032a6c743fb26cb094aeff89da3b67d918e`, run `35547919604`, job `106177104878` completed success. A simplified fixture removed Keystore/AES-GCM semantics and independently required package PID, Activity `onCreate`, native completion, UI publication, `onResume`, and final `uiautomator` observation. This falsifies an infrastructure-wide/deterministic first-launch observation failure but is not Keystore replication.

**KEYSTORE SEMANTIC REPLICATION:** exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, attempt 1, job `106204067727` completed success. Original AndroidKeyStore AES-256/GCM key, app-private ciphertext, force-stop/fresh-process recovery, external tamper mutation and authentication-rejection semantics were preserved while independent phase markers and metadata-visible failure verdicts were added. Every named failure phase was skipped; explicit bounded oracle pass and natural completion succeeded. This is bounded **REPLICATION** at the same API-35 emulator class, not physical/hardware-backed/product evidence. ROOT CAUSE for intermittent failures remains OPEN.

### M004
**IN STUDY.** M002 exercises `path_provider`; M003 crosses Flutter/native Android security boundaries. Broader native/plugin/multi-engine behavior remains OPEN.

### M005
**IN STUDY.** Planned Foundation capability evidence retained; physical/native product transfer remains OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current M003 work is Studio-fixture evidence, not a LogMate/MintTap audit or product build.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Physical Android/iOS lifecycle, system-initiated process death/background pressure, one-time expiry/auto-reset, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent. Keystore repeatability is demonstrated only at bounded emulator scope. User-driven permission-dialog execution is pending and cannot yet change the gate.

## Dependencies / handoffs
- **Architecture:** permission/key/storage failure states should be explicit contract states; lifecycle callbacks must not be assumed guaranteed finalization hooks.
- **Data:** process recovery does not establish physical durability or backup correctness.
- **Quality:** distinguish actual system-dialog interaction from shell permission mutation; preserve app and package-manager oracles plus natural completion.
- **Systems:** bounded Keystore mechanics do not establish hardware backing/StrongBox/auth policy; one-time permission is a least-privilege mechanism, not complete authorization design.
- **Design Studio:** permission rationale/denial UX is a downstream design handoff; repository search found no directly relevant canonical permission research in this run.
- **Web Manager / Marketing Manager:** considered; no material dependency for this native Android authority-state block.

## CHANGE WATCH / OPEN
- User-driven permission run `35564720878` terminal result pending.
- One-time permission expiry/background grace, repeated-denial `USER_FIXED`, and auto-reset/hibernation remain OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN; semantic REPLICATION closed only at bounded API-35 emulator scope.
- Physical Android/iOS, system-initiated lifecycle/background pressure and broader plugin-native integration remain OPEN.
- Hardware-backed/StrongBox, user-auth-bound key invalidation, backup/restore, reinstall/key rotation/device migration remain OPEN.
- Safari/iPadOS/EFB and canonical product runtime remain OPEN.

## Next work
Continue the current user-driven permission-dialog block until its terminal verdict is known. If it passes, close only the actual API-35 dialog choice boundary and re-rank; do not infer one-time expiry or auto-reset. If it fails, isolate the first failing UI/callback/package-state phase before causal claims. Do not return to Keystore repetition merely to catch its intermittent failure.