# M003 — first-launch observation isolation

Status: **BOUNDED DIAGNOSTIC PASS — prior Keystore first-launch ROOT CAUSE remains OPEN**  
Evidence date: 2026-09-21

## Problem
The Keystore semantic fixture has one complete bounded PASS but two first-launch-adjacent observation failures. Same-head replication therefore failed, and prior evidence could not distinguish process/activity startup, native completion, UI publication, UI-automation readiness, or emulator timing. Re-running the same combined oracle had low evidence value.

## Balance Loop selection
Mobile remained the highest-value coherent block because this unresolved contradiction was already inside an active professional boundary and had direct Quality debugging/reproducibility leverage. Foundations has bounded direct Dart/Flutter evidence; Architecture, Data and Quality have substantial Stage-1 executable boundaries; Systems S004 is source-authorization dependent. Physical Android/iOS/Safari/product-runtime evidence would be stronger but is not available in this execution context.

## Diagnostic design
Workflow: `.github/workflows/m003-first-launch-isolation.yml`  
Exact diagnostic head: `282f3032a6c743fb26cb094aeff89da3b67d918e`  
Run: `35547919604`, attempt 1  
Job: `106177104878`  
Environment family: pinned Flutter 3.47.5; Android API 35 x86_64 emulator; Ubuntu GitHub-hosted runner.

The diagnostic intentionally removes Keystore/AES-GCM semantics and isolates only the disputed observation chain. It uses five ordered signals:

1. `am start -W` start request/result;
2. independent package PID existence;
3. native Activity/logcat markers for `onCreate`, native-work completion, UI publication, and `onResume`;
4. only after those signals, `uiautomator dump` observes the published text;
5. failure verdict names the first absent signal.

The native result is deliberately trivial. This is a diagnostic discriminator, not a replacement semantic secure-storage test.

## VALIDATION contract and result
**CLAIM:** the prior first-launch contradiction can be narrowed by observing process/activity/native/UI-publication/UI-automation boundaries independently.

**ORACLE:** a PASS requires process existence, all independent native log markers, and final UI-hierarchy observation. A failure is classified at the first missing signal and must not be called a Keystore failure.

**OBSERVATION:** run `35547919604`, job `106177104878` completed success. The `Execute first-launch isolation oracle` step succeeded and the job reached natural completion. Because the script is fail-fast, success requires package PID observation, `ACTIVITY_ONCREATE_ENTER`, `NATIVE_COMPLETE:m003-first-launch`, `UI_PUBLISHED`, `ACTIVITY_ONRESUME`, and final UI hierarchy observation of `NATIVE_COMPLETE:m003-first-launch`.

**VALIDATION VERDICT:** bounded diagnostic PASS. In this simplified matched environment, process startup, Activity entry, native completion, UI publication, resume, and UI-automation observation can all succeed in one cold first launch.

**CONTRADICTION / ROOT CAUSE:** this result falsifies a deterministic claim that the API-35 emulator/UI-automation path necessarily fails at first launch. It does **not** establish why the Keystore fixture failed twice near first launch. The removed Keystore/AES-GCM work, timing/load interactions, fixture-specific publication behavior, emulator nondeterminism, or another unmeasured interaction remain possible. ROOT CAUSE remains OPEN.

**REPLICATION:** not awarded for the Keystore semantic fixture. This diagnostic is a different simplified target and cannot repair the failed same-head semantic replication.

## FAILURE MODEL / evidence limit
This diagnostic can discriminate app-process absence, Activity/native completion absence, UI publication absence, and UI-automation observation absence when they occur in this simplified fixture. It does not reproduce the Keystore workload, ciphertext state, force-stop/recovery/tamper sequence, physical-device behavior, product runtime, or production conditions. A successful simplified startup path is therefore not evidence that the original Keystore first launch is deterministic.

## SYNTHESIS
Independent startup/native/UI signals are executable in the available CI environment, so the previous broad first-launch symptom should not be treated as an infrastructure-wide inability to observe Android startup. Any further M003 root-cause work must preserve the Keystore semantics while adding equivalent independent markers to the original semantic fixture; otherwise it changes the target and cannot establish causality.

## RELATED DOMAIN CHECK
- Foundations: direct Dart/Flutter execution already exists; exact runtime identity remains required.
- Architecture: not materially changed; this is observation-boundary isolation rather than contract redesign.
- Mobile: owns the Android startup/runtime boundary.
- Data: no durability claim is tested here.
- Quality: directly advances symptom → isolation → falsification discipline and independent oracles.
- Systems: Keystore semantics are intentionally removed; no security claim is advanced by this diagnostic.
- Design Studio: no user interaction contract is being evaluated.
- Web Manager / Marketing Manager: not materially relevant to this native startup diagnostic.
- Product repositories: not used; no MintTap/LogMate behavior is claimed.

## HANDOFFS
- Mobile → Quality: the simplified independent-signal chain is viable. If M003 root-cause work resumes, instrument the original semantic target with these markers rather than infer cause from final UI absence.
- Mobile → Systems: this diagnostic neither weakens nor strengthens the existing bounded Keystore semantic PASS; security semantics were removed intentionally. Keystore REPLICATION remains absent.

## OPEN / CHANGE WATCH
- Keystore first-launch ROOT CAUSE remains OPEN; same-head semantic REPLICATION remains OPEN.
- Do not call the simplified diagnostic a Keystore replication.
- A stronger next causal experiment would add the independent markers to the original Keystore target without changing crypto/key/ciphertext semantics, then compare success/failure at the first absent signal.
- If that instrumentation cannot be executed or yields no discriminating failure, preserve ROOT CAUSE/REPLICATION as OPEN and return to Balance Loop rather than repeat identical runs.