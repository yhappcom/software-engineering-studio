# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering  
Prefix: `M###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-21

## Current evidence

### M001
**IN STUDY — DIRECT FLUTTER HOST/CHROME + BOUNDED ANDROID EMULATOR TRANSFER VALIDATED.** Exact repaired head `b6bfc4bf7e07c004c43326fb1821fd54de3986ba`, run `35507983649`, job `106070907373` terminal success. Physical Android, iOS, release-AOT, product artifacts and production remain OPEN.

### M002
**IN STUDY — BOUNDED ANDROID FORCE-STOP/FILE RECOVERY + ORDINARY HOME BACKGROUND/RESUME TRANSFERS VALIDATED.** Force-stop repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`, run `35516637659`, job `106093583857` success. Controlled force-stop is not low-memory/system-initiated kill or physical durability evidence. Background/resume exact head `a278de3f2a9015195262b30662b1c240601f336e`, run `35529237932`, job `106126775150` success; API-35 emulator scope only.

### M003
**IN STUDY — SHELL-CONTROLLED PERMISSION TRANSFER + BOUNDED KEYSTORE SEMANTIC REPLICATION; USER-DRIVEN PERMISSION DIALOG EXECUTION FAILED AND REQUIRES PHASE ISOLATION; INTERMITTENT KEYSTORE ROOT CAUSE OPEN.** Canonical: `research/mobile/M003_android_runtime_permission_revocation_transfer.md`, `M003_android_keystore_secure_storage_transfer.md`, `M003_first_launch_observation_isolation.md`, `M003_keystore_semantic_first_launch_instrumentation.md`, `M003_android_user_permission_dialog_transfer.md`.

Shell-controlled permission evidence retained: exact head `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`, run `35522782572`, job `106109634570` success for denied → granted → revoked/denied state, process replacement and natural completion.

**USER-DRIVEN DIALOG FAILURE:** exact head `63f96e010691db87fea13bc7e08866c082dfb656`, run `35564720878`, job `106224179388`, attempt 1 completed **failure**. Checkout, pinned Flutter installation/toolchain recording, fixture creation/build, oracle creation and KVM setup all passed. Failure occurred inside the combined `Execute user-driven permission oracle` step. Current job metadata does not expose whether the first failed phase was initial app UI, request interaction, one-time system choice discovery/selection, callback/UI, package-manager state, reinstall, denial interaction, or final denied state. **No PASS, TRANSFER VALIDATION, or ROOT CAUSE.** The harness observability defect must be repaired before another equivalent execution; do not rerun the opaque oracle unchanged.

Keystore evidence retained: initial complete PASS at exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528` attempt 1, job `106152447185`; second complete semantic execution at exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, job `106204067727`. This is bounded **REPLICATION** for Android 15/API-35 x86_64 emulator AndroidKeyStore AES-256/GCM, app-private ciphertext, force-stop/fresh-process recovery, external tamper and authentication rejection. Physical/hardware-backed/product claims remain OPEN. Intervening first-launch-adjacent failures are retained as CONTRADICTION; ROOT CAUSE remains OPEN.

### M004–M005
**IN STUDY.** Plugin/native and broader physical/native product transfer remain OPEN.

### M006
**IN STUDY — REAL CHROMIUM OFFLINE + RESTART + UPDATE/CONTROL + OFFLINE COLD-START TRANSFER VALIDATED.** Safari/iPadOS/EFB, physical connectivity, Flutter/LogMate artifact and production remain OPEN.

## Product transfer scope
Exact LogMate ref retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`. Default branch is not assumed production. Current M003 work is Studio-fixture evidence, not a LogMate/MintTap audit or product build.

## Gate assessment
Mobile Stage 1 remains **NOT PASS**. Physical Android/iOS lifecycle, system-initiated process death/background pressure, one-time expiry/auto-reset, broader plugin/native behavior, Safari/iPadOS/EFB, canonical product runtime and production evidence remain materially absent. User-driven permission-dialog transfer has a real failure observation but no phase/root-cause evidence yet.

## Dependencies / handoffs
- **Quality:** the dialog failure exposed insufficient failure-phase observability; repair the evidence channel before causal claims or rerun.
- **Architecture:** permission/key/storage failure states should be explicit contract states; lifecycle callbacks must not be assumed guaranteed finalization hooks.
- **Data:** process recovery does not establish physical durability or backup correctness.
- **Systems:** bounded Keystore mechanics do not establish hardware backing/StrongBox/auth policy; one-time permission is a least-privilege mechanism, not complete authorization design.
- **Design Studio:** permission rationale/denial UX remains a downstream design handoff.
- **Web Manager / Marketing Manager:** considered; no material dependency for this native Android authority-state block.

## CHANGE WATCH / OPEN
- User-driven permission run `35564720878`: terminal FAILURE; first failed semantic phase OPEN.
- One-time permission expiry/background grace, repeated-denial `USER_FIXED`, and auto-reset/hibernation OPEN.
- Keystore intermittent first-launch ROOT CAUSE OPEN; semantic REPLICATION closed only at bounded API-35 emulator scope.
- Physical Android/iOS, system-initiated lifecycle/background pressure and broader plugin-native integration OPEN.
- Hardware-backed/StrongBox, user-auth-bound key invalidation, backup/restore, reinstall/key rotation/device migration OPEN.
- Safari/iPadOS/EFB and canonical product runtime OPEN.

## Next work
Continue M003 only by making the user-dialog oracle's first failing semantic phase externally recoverable while preserving application/platform semantics. Then reproduce once and isolate before any causal claim. If that evidence channel cannot be made trustworthy, preserve the failure as OPEN and return to Balance Loop rather than simulating evidence.
