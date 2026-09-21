# M003 — Android user-driven permission dialog transfer

Status: **IN STUDY — FIRST EXECUTION FAILED; PHASE ISOLATION REQUIRED**  
Evidence date: 2026-09-21

## Problem / professional boundary
Prior M003 permission evidence used `pm grant` / `pm revoke`. That is valuable controlled platform-state evidence but does not validate the user-facing Android permission dialog, the `Only this time` choice, or a real user denial path. This block advances to a materially different evidence class rather than repeating shell-controlled permission mutation.

## SOURCE
Android Developers, rechecked 2026-09-21:
- `https://developer.android.com/training/permissions/requesting` — dangerous runtime permissions are requested at feature need; denial must be handled; Android 11/API 30+ exposes `Only this time` for location/microphone/camera; one-time authority is temporary and platform controlled.
- `https://developer.android.com/about/versions/11/privacy/permissions` — Android 11 introduced one-time permissions and automatic reset for unused apps; repeated denial affects future dialog behavior.
- `https://developer.android.com/topic/performance/app-hibernation` — unused-app restrictions/hibernation can reset runtime permissions and remain a separate system-managed lifecycle.

## SYNTHESIS
Shell-controlled grant/revoke and actual user-dialog choices are different evidence classes. A robust application contract must treat authority as mutable platform state and must not infer current authority merely from manifest declaration or from a previous grant. A user denial is a valid ordinary state, not an exceptional corruption state.

## ENGINEERING JUDGMENT
The highest-value executable increment available in the current environment remains an API-35 emulator user-choice transfer: app requests CAMERA through the native Android permission API; automation interacts with the actual system permission UI rather than mutating permission state; application state and independent package-manager state are both checked. Auto-reset and physical-device behavior are intentionally not simulated.

## VALIDATION — execution 1 failed
Workflow: `.github/workflows/m003-android-user-permission-dialog.yml`  
Exact Studio head: `63f96e010691db87fea13bc7e08866c082dfb656`  
Run: `35564720878`; job: `106224179388`; attempt: 1.  
Environment contract: pinned Flutter `3.47.5`; Android API 35 x86_64 emulator; Pixel 6 profile.

Observed job evidence:
- checkout: PASS;
- pinned Flutter install: PASS;
- toolchain identity: PASS;
- isolated fixture creation/build: PASS;
- user-choice oracle creation: PASS;
- KVM enablement: PASS;
- `Execute user-driven permission oracle`: **FAIL** after emulator execution began;
- natural workflow verdict: **FAIL**.

The current externally recoverable Actions job metadata does not reveal whether the first failing semantic phase was initial app observation, request-button interaction, presence/text of `Only this time`, grant callback/UI, package-manager grant state, reinstall, `Don’t allow` interaction, denial callback/UI, or package-manager denied state. Therefore the failure is a `VALIDATION` failure observation only. It is **not** ROOT CAUSE and does not justify claims that Android 15 lacks the documented choice, that Flutter permission bridging failed, or that UI automation is the cause.

## CONTRADICTION / diagnostic defect
The workflow's oracle has useful internal assertions but collapses all semantic phases into one `android-emulator-runner` job step. That is insufficient observability for the Studio failure→isolation→causal-hypothesis standard. The next execution must preserve the application/platform semantics while exporting the first failed phase into metadata-visible evidence (for example, capture a phase verdict file while allowing the emulator wrapper to return, then use named conditional steps to expose the phase). Merely rerunning the same opaque oracle has low evidence value.

## Target contract retained
1. fresh install starts `CAMERA:DENIED`;
2. app invokes Android runtime permission request for CAMERA;
3. actual system dialog exposes the one-time choice expected for this API/environment;
4. automation selects the actual system control;
5. app callback/UI and `dumpsys package` independently agree on granted state;
6. uninstall/reinstall creates an independent fresh-install authority state;
7. actual system denial is selected;
8. app UI and package-manager state independently agree on denied state;
9. natural completion is required.

No PASS or TRANSFER VALIDATION is awarded from execution 1.

## FAILURE MODEL
The oracle can expose: request never reaching the platform dialog; expected one-time choice absent; callback/app state disagreeing with platform state; user denial incorrectly treated as grant; package-manager disagreement; or automation unable to identify the actual system choice. A reproduced failing phase still requires causal isolation before ROOT CAUSE.

## Evidence limits
A future success will still not establish one-time permission expiry timing, background grace duration, system auto-reset/hibernation, repeated-denial `USER_FIXED` behavior, physical Android, OEM behavior, actual camera-device access, iOS permission semantics, product code, release builds, or production behavior. Uninstall/reinstall is used only to obtain an independent fresh user-denial path; it is not evidence about one-time expiry.

## RELATED DOMAIN CHECK
- Foundations: permission authority is OS-managed mutable state; no language/runtime guarantee.
- Architecture: denied/granted are explicit feature contract states.
- Mobile: directly extends M003 beyond prior `pm grant/revoke` evidence.
- Data: not materially relevant; no durability claim.
- Quality: the failed execution exposed an observability defect in the test harness; first-failed-phase evidence is required before causal claims.
- Systems: least-privilege/user authority is related; this does not establish complete authorization or secure-storage design.
- Design Studio: prior repository check found no directly relevant canonical permission research; denial/rationale UX remains a handoff rather than an Engineering-owned design decision.
- Web Manager: not materially relevant to this native Android block.
- Marketing Manager: not materially relevant to this native Android block.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Quality: preserve actual system-dialog interaction separately from shell permission mutation; make semantic phase verdicts externally recoverable before another run.
- Design Studio: future permission-request/denial UX should consume the mutable-authority and user-choice contract; Engineering does not define visual/content treatment here.
- Systems: one-time grant is a least-privilege mechanism, not evidence of a complete permission/security policy.

## OPEN / CHANGE WATCH
- First failing phase of run `35564720878` remains unknown from current metadata.
- One-time expiry/background grace and process behavior.
- repeated denial / `USER_FIXED` behavior.
- auto-reset/hibernation after real inactivity.
- physical Android/OEM and iOS transfer.
- exact product/runtime transfer.
