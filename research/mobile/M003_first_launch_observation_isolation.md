# M003 — first-launch observation isolation

Status: **IN STUDY — diagnostic execution pending**  
Evidence date: 2026-09-21

## Problem
The Keystore semantic fixture has one complete bounded PASS but two first-launch-adjacent observation failures. Same-head replication therefore failed, and current evidence cannot distinguish process/activity startup, native completion, UI publication, UI-automation readiness, or emulator timing. Re-running the same combined oracle has low evidence value.

## Balance Loop selection
Mobile remains the highest-value coherent block because this unresolved contradiction is already inside an active professional boundary and has direct Quality debugging/reproducibility leverage. Foundations has bounded direct Dart/Flutter evidence; Architecture, Data and Quality have substantial Stage-1 executable boundaries; Systems S004 is source-authorization dependent. Physical Android/iOS/Safari/product-runtime evidence would be stronger but is not available in this execution context.

## Diagnostic design
Workflow: `.github/workflows/m003-first-launch-isolation.yml`  
Exact diagnostic head: `282f3032a6c743fb26cb094aeff89da3b67d918e`  
Run: `35547919604` (queued at evidence capture)

The diagnostic intentionally removes Keystore/AES-GCM semantics and isolates only the disputed observation chain. It uses pinned Flutter 3.47.5, Android API 35 x86_64 emulator, and five ordered signals:

1. `am start -W` start request/result;
2. independent package PID existence;
3. native Activity/logcat markers for `onCreate`, native-work completion, UI publication, and `onResume`;
4. only after those signals, `uiautomator dump` observes the published text;
5. failure verdict names the first absent signal.

The native result is deliberately trivial. This is a diagnostic discriminator, not a replacement semantic secure-storage test.

## VALIDATION contract
**CLAIM:** the prior first-launch contradiction can be narrowed by observing process/activity/native/UI-publication/UI-automation boundaries independently.

**ORACLE:** a PASS requires process existence, all independent native log markers, and final UI-hierarchy observation. A failure is classified at the first missing signal and must not be called a Keystore failure.

**FAILURE MODEL:** app process absence, Activity/native completion absence, UI publication absence, or UI-automation observation absence. Emulator boot failure and install failure remain separately identifiable infrastructure phases.

**VERDICT:** OPEN until run `35547919604` reaches terminal state. No ROOT CAUSE, REPLICATION, or new semantic PASS is awarded from creating the diagnostic.

## RELATED DOMAIN CHECK
- Foundations: direct Dart/Flutter execution already exists; exact runtime identity remains required.
- Architecture: not materially changed; this is observation-boundary isolation rather than contract redesign.
- Mobile: owns the Android startup/runtime boundary.
- Data: no durability claim is tested here.
- Quality: directly supports symptom → isolation → causal-hypothesis discipline and independent oracles.
- Systems: Keystore semantics are intentionally removed; no security claim is advanced by this diagnostic.
- Design Studio: no user interaction contract is being evaluated.
- Web Manager / Marketing Manager: not materially relevant to this native startup diagnostic.
- Product repositories: not used; no MintTap/LogMate behavior is claimed.

## HANDOFFS
- Mobile → Quality: use the first absent independent signal, not the final UI symptom, as the next causal-isolation boundary.
- Mobile → Systems: this diagnostic does not weaken or strengthen the existing bounded Keystore semantic PASS; it only investigates observation repeatability.

## OPEN / CHANGE WATCH
- Await terminal run evidence.
- If native completion/UI publication are present but UI automation is absent, isolate automation/readiness without changing Keystore semantics.
- If an earlier signal is absent, investigate that earlier boundary first.
- If the diagnostic itself cannot discriminate reliably, preserve ROOT CAUSE and REPLICATION as OPEN and return to Balance Loop.
