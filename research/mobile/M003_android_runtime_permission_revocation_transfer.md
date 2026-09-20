# M003 — Android Runtime Permission Grant/Revocation Transfer

Status: **BOUNDED ANDROID EMULATOR TRANSFER VALIDATED**  
Evidence date: 2026-09-21

## Problem / scope
M003's storage-property model distinguished sandbox access from runtime authority, but representative Android runtime-permission execution remained OPEN. This block tests whether application-observed dangerous-permission state tracks platform grant/revocation state across process replacement.

## SOURCE
Android Developers, rechecked 2026-09-21, states that dangerous permissions require runtime authorization on supported Android versions, applications must check authorization when performing protected operations, and denial/revocation must be handled. Android permission testing guidance recommends granted/revoked combinations and documents `adb shell pm grant|revoke` for test control.

Primary sources:
- https://developer.android.com/training/permissions/requesting
- https://developer.android.com/training/permissions/usage-notes
- https://developer.android.com/guide/topics/permissions/overview

## SYNTHESIS
A manifest declaration is capability eligibility, not current runtime authority. Permission state is mutable platform state; the application boundary must tolerate `declared+denied → granted → revoked` rather than validating only a granted happy path.

## TRANSFER VALIDATION — PASS
Workflow: `.github/workflows/m003-android-runtime-permission-validation.yml`  
Exact Studio head: `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`  
Run: `35522782572`  
Job: `106109634570`  
Target: GitHub-hosted Ubuntu runner + Android Emulator API 35 x86_64, Pixel 6 profile  
Terminal result: **success**, 2026-09-20T16:32:58Z.

The exact workflow generated an isolated Flutter Android application, declared CAMERA, exposed native `ContextCompat.checkSelfPermission` through a Flutter MethodChannel, built a debug APK, and executed a fail-fast Android oracle. The oracle required:
1. first launch UI `CAMERA:DENIED` plus package-manager `granted=false`;
2. force-stop, `pm grant`, relaunch, UI `CAMERA:GRANTED` plus `granted=true`;
3. capture a live granted-state PID;
4. `pm revoke` while live, then require process disappearance;
5. relaunch, UI `CAMERA:DENIED` plus `granted=false`;
6. require a non-empty PID different from the pre-revocation PID;
7. natural job completion.

GitHub reports the emulator oracle step and complete job successful. Therefore all fail-fast conditions above passed at this bounded target.

### Claim / oracle / verdict
**CLAIM:** at this bounded Android target, dangerous-permission authority is mutable platform state observed through the native boundary; grant and revoke transitions change app-observed state, and revocation must not be modeled as a static manifest property.

**ORACLE:** application UI populated from native `checkSelfPermission` plus independent Android package-manager state from `dumpsys package`; PID observations distinguish the granted process from the fresh post-revocation process.

**VERDICT:** **TRANSFER VALIDATION PASS** for the named API-35 emulator boundary.

### Environment evidence limit
The workflow recorded `flutter --version --machine`, Flutter checkout HEAD, and `dart --version`, but the currently retrievable run/job metadata does not expose those command outputs. Do not invent or infer the exact Flutter/Dart versions. The workflow itself cloned the then-current `stable` branch, so framework identity is weaker than a pinned SDK despite the exact Studio workflow ref. Android target identity is explicit in the workflow: API 35 / x86_64 emulator.

## FAILURE MODEL / LIMITS
This evidence exposes static-manifest assumptions, stale app permission state across grant/revoke, and failure to re-evaluate authority after process replacement. It does **not** validate user-facing permission dialog/rationale UX, one-time permission timing, auto-reset/hibernation, actual camera access, permission groups, physical Android, iOS, secure storage, product code, release builds, or production behavior. `pm revoke` is a controlled test mechanism and must not be generalized to every user/system revocation path.

## RELATED DOMAIN CHECK
- **Foundations:** runtime authority is platform state, not a language guarantee.
- **Architecture:** permission-dependent features need explicit denied/granted behavior rather than hidden environmental preconditions.
- **Mobile:** M001/M002 checked; this is a materially different authority-state transfer.
- **Data:** no durability claim is made.
- **Quality:** independent app/platform oracles plus fresh-process evidence and natural completion are required.
- **Systems:** least-privilege mechanics are exercised; secure-storage/threat-model completeness is not established.
- **Design Studio:** permission rationale/denial UX remains a related downstream concern; no design canonical file edited.
- **Web Manager / Marketing Manager:** not materially relevant to this native runtime-authority mechanism.
- **Product source/ref:** no product repository audited; Studio fixture only.

## HANDOFFS
- **Quality:** retain app-observed state, package-manager state, process replacement and natural completion as separate evidence surfaces.
- **Architecture:** model denial/revocation as explicit runtime contract states.
- **Systems:** bounded least-privilege transfer only; secure storage and authorization-policy completeness remain OPEN.
- **Design Studio:** denial/rationale UX should consume the mutable-authority rule; no canonical design files edited.

## OPEN / CHANGE WATCH
- Exact Flutter/Dart command-output identity for this historical run is not presently recoverable from available metadata; do not fabricate it.
- User-driven dialog denial, one-time permission, auto-reset, physical Android, iOS, secure storage and product transfer remain OPEN.
- Android permission behavior and Flutter/native integration are version-sensitive; future replication should pin SDK identity in the workflow itself rather than cloning an unpinned stable branch.
