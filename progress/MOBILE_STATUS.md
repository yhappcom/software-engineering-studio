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
**IN STUDY — BOUNDED RUNTIME-PERMISSION + KEYSTORE PROCESS/TAMPER TRANSFERS VALIDATED; KEYSTORE SEMANTIC REPLICATION NOW ACHIEVED AT EMULATOR SCOPE; INTERMITTENT ROOT CAUSE OPEN.** Canonical: `research/mobile/M003_android_runtime_permission_revocation_transfer.md`, `research/mobile/M003_android_keystore_secure_storage_transfer.md`, `research/mobile/M003_first_launch_observation_isolation.md`, `research/mobile/M003_keystore_semantic_first_launch_instrumentation.md`.

Permission evidence: exact Studio head `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`, run `35522782572`, job `106109634570` completed success for denied → granted → revoked/denied state, process replacement and natural completion.

Initial Keystore semantic PASS: exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528`, attempt 1, job `106152447185` completed success. Environment: Android 15/API 35 x86_64 emulator; Flutter 3.47.5 revision `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`; engine `af7e796e161ae0bb1ff0758c71a7105418bd9ded`; Dart 3.13.4 stable linux_x64; Ubuntu 24.04.5. Logs show `WROTE:secure-v1:NONEXPORTABLE` → force-stop/fresh cold process → `RECOVERED:secure-v1:NONEXPORTABLE` → external ciphertext mutation → `AUTH_FAIL` → natural completion.

**CONTRADICTION retained:** same-head attempt 2, job `106160817014`, failed at first launch, and later instrumented semantic run `35554495251`, job `106195370405`, also failed without externally recoverable exact phase. These failures reproduce an intermittent first-launch-adjacent class but do not establish root cause.

**FIRST-LAUNCH ISOLATION PASS:** exact diagnostic head `282f3032a6c743fb26cb094aeff89da3b67d918e`, run `35547919604`, job `106177104878` completed success. A simplified fixture removed Keystore/AES-GCM semantics and independently required package PID, Activity `onCreate`, native completion, UI publication, `onResume`, and final `uiautomator` observation. This falsifies an infrastructure-wide/deterministic first-launch observation failure but is not Keystore replication.

**KEYSTORE SEMANTIC REPLICATION:** exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, attempt 1, job `106204067727` completed success. The original AndroidKeyStore AES-256/GCM key, app-private ciphertext, force-stop/fresh-process recovery, external tamper mutation and authentication-rejection semantics were preserved while independent phase markers and metadata-visible failure verdicts were added. Emulator execution completed; every named failure phase was skipped; explicit `M003 bounded Keystore oracle passed` and natural job completion succeeded. A second complete semantic execution is therefore recorded as bounded **REPLICATION** at the same API-35 emulator class. This does not explain the intermittent failures; ROOT CAUSE remains OPEN.

### M004
**IN STUDY.** M002 exercises `path_provider`; M003 crosses Flutter/native Android security boundaries. Broader native/plugin/multi-engine behavior remains OPEN.

### M005
**IN STUDY.** Planned Foundation capability evidence retained; physical/native product transfer remains OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current M003 Keystore/startup work is Studio-fixture evidence, not a LogMate/MintTap audit or product build.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Physical Android/iOS lifecycle, system-initiated process death/background pressure, user-driven/one-time/auto-reset permissions, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent. Keystore repeatability is now demonstrated at bounded emulator scope, but intermittent first-launch failures remain unexplained and no physical/hardware-backed security claim is supported.

## Dependencies / handoffs
- **Architecture:** permission/key/storage failure states should be explicit contract states; lifecycle callbacks must not be assumed guaranteed finalization hooks.
- **Data:** process recovery does not establish physical durability or backup correctness; Keystore ciphertext recovery is a distinct property.
- **Quality:** phase-observable instrumentation now coexists with the semantic target. If the intermittent failure recurs in a materially useful experiment, use the first named absent phase before forming a causal hypothesis.
- **Systems:** bounded Keystore process/tamper mechanics now have repeated semantic success at emulator scope; do not infer hardware backing, StrongBox, auth policy, root resistance or complete secret management.
- **Design Studio:** user-auth/recovery UX becomes related for auth-bound keys; current fixture has no product interaction contract.
- **Web Manager / Marketing Manager:** considered; no material dependency for this native storage/startup mechanism.

## CHANGE WATCH / OPEN
- Keystore intermittent first-launch ROOT CAUSE OPEN; semantic REPLICATION is closed only at bounded API-35 emulator scope.
- Physical Android/iOS, system-initiated lifecycle/background pressure, user-dialog/one-time/auto-reset permissions and broader plugin-native integration remain OPEN.
- Hardware-backed/StrongBox, user-auth-bound key invalidation, backup/restore, reinstall/key rotation/device migration remain OPEN.
- Same-PID HOME survival must not be generalized to Android process-retention guarantees.
- Safari/iPadOS/EFB and canonical product runtime remain OPEN.

## Next work
The M003 semantic replication boundary is now complete enough to leave this loop. Do not spend runs merely trying to catch the intermittent first-launch failure. Preserve ROOT CAUSE as OPEN unless a future failure can discriminate a causal hypothesis. Return to Balance Loop and prefer a materially different high-value evidence class: physical/native lifecycle or storage/connectivity, Safari/iPadOS/EFB, user-driven permission lifecycle, authorized exact-product runtime/build, or another track's stronger Stage-1 gap.
