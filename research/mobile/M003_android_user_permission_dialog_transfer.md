# M003 — Android user-driven permission dialog transfer

Status: **IN STUDY — EXECUTION PENDING**  
Evidence date: 2026-09-21

## Problem / professional boundary
Prior M003 permission evidence used `pm grant` / `pm revoke`. That is valuable controlled platform-state evidence but does not validate the user-facing Android permission dialog, the `Only this time` choice, or a real user denial path. This block advances to a materially different evidence class rather than repeating shell-controlled permission mutation.

## SOURCE
Android Developers, rechecked 2026-09-21:
- `https://developer.android.com/training/permissions/requesting` — dangerous runtime permissions are requested at feature need; denial must be handled; Android 11/API 30+ exposes `Only this time` for location/microphone/camera; a one-time permission is temporary and process termination/revocation semantics remain platform controlled.
- `https://developer.android.com/about/versions/11/privacy/permissions` — Android 11 introduced one-time permissions and automatic reset for unused apps; repeated denial affects future dialog visibility.
- `https://developer.android.com/topic/performance/app-hibernation` — unused-app restrictions/hibernation can reset runtime permissions and remain a separate system-managed lifecycle.

## SYNTHESIS
Shell-controlled grant/revoke and actual user-dialog choices are different evidence classes. A robust application contract must treat authority as mutable platform state and must not infer current authority merely from manifest declaration or from a previous grant. A user denial is a valid ordinary state, not an exceptional corruption state.

## ENGINEERING JUDGMENT
The highest-value executable increment available in the current environment is an API-35 emulator user-choice transfer: app requests CAMERA through the native Android permission API; automation interacts with the actual system permission UI by locating rendered text/bounds rather than mutating permission state; application state and independent package-manager state are both checked. Auto-reset and physical-device behavior are intentionally not simulated.

## VALIDATION — pending
Workflow: `.github/workflows/m003-android-user-permission-dialog.yml`  
Exact Studio head: `63f96e010691db87fea13bc7e08866c082dfb656`  
Run: `35564720878`  
State at evidence capture: **in_progress**.

Target contract:
1. pinned Flutter `3.47.5`; Android API 35 x86_64 emulator;
2. fresh install starts `CAMERA:DENIED`;
3. app invokes `ActivityCompat.requestPermissions` for CAMERA;
4. system dialog must visibly contain `Only this time`;
5. automation chooses that actual UI control by its dumped bounds;
6. app callback/UI must become `CAMERA:GRANTED` and `dumpsys package` must independently report `granted=true`;
7. uninstall/reinstall creates an independent fresh-install authority state;
8. app requests CAMERA again and automation chooses the system `Don’t allow` control;
9. app UI must remain `CAMERA:DENIED` and `dumpsys package` must independently report `granted=false`;
10. natural job completion is required.

No PASS is awarded while the run is pending.

## FAILURE MODEL
The oracle can expose: request never reaching the platform dialog; expected one-time choice absent; callback/app state disagreeing with platform state; user denial incorrectly treated as grant; or automation unable to identify the actual system choice. If the workflow fails, failure is evidence only; root cause requires isolation before any causal claim.

## Evidence limits
Even a success will not establish one-time permission expiry timing, background grace duration, system auto-reset/hibernation, repeated-denial `USER_FIXED` behavior, physical Android, OEM behavior, actual camera-device access, iOS permission semantics, product code, release builds, or production behavior. Uninstall/reinstall is used only to obtain an independent fresh user-denial path; it is not evidence about one-time expiry.

## RELATED DOMAIN CHECK
- Foundations: permission authority is OS-managed mutable state; no language/runtime guarantee.
- Architecture: denied/granted are explicit feature contract states.
- Mobile: directly extends M003 beyond prior `pm grant/revoke` evidence.
- Data: not materially relevant; no durability claim.
- Quality: app UI/callback and package-manager state are independent oracle surfaces; natural completion required.
- Systems: least-privilege/user authority is related; this does not establish complete authorization or secure-storage design.
- Design Studio: repository search for `permission denial rationale` / `permissions` found no directly relevant canonical result; denial/rationale UX remains a handoff rather than an Engineering-owned design decision.
- Web Manager: not materially relevant to this native Android block.
- Marketing Manager: not materially relevant to this native Android block.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Design Studio: future permission-request/denial UX should consume the mutable-authority and user-choice contract; Engineering does not define the visual/content treatment here.
- Quality: preserve actual system-dialog interaction separately from shell permission-state mutation.
- Systems: one-time grant is a least-privilege mechanism, not evidence of a complete permission/security policy.

## OPEN / CHANGE WATCH
- Terminal result for run `35564720878`.
- One-time expiry/background grace and process behavior.
- repeated denial / `USER_FIXED` behavior.
- auto-reset/hibernation after real inactivity.
- physical Android/OEM and iOS transfer.
- exact product/runtime transfer.
