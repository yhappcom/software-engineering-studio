# M003 — Android Runtime Permission Grant/Revocation Transfer

Status: **IN STUDY — executable Android Emulator transfer pending**  
Evidence date: 2026-09-21

## Problem / scope

M003's storage-property model already distinguishes sandbox access from runtime authority, but representative Android runtime-permission execution remained OPEN. This block tests whether an application-observed dangerous-permission state tracks platform grant/revocation state across process replacement, without treating a manifest declaration as authority.

## SOURCE

Android Developers, rechecked 2026-09-21, states that dangerous permissions on Android 6.0/API 23+ require runtime authorization, that applications must check authorization when performing protected operations, and that denial/revocation must be handled rather than assumed away. Android's permission testing guidance explicitly recommends exercising granted and revoked combinations and documents `adb shell pm grant|revoke` for test control.

Primary sources:
- https://developer.android.com/training/permissions/requesting
- https://developer.android.com/training/permissions/usage-notes
- https://developer.android.com/guide/topics/permissions/overview

## SYNTHESIS

A manifest declaration is capability eligibility, not proof of current runtime authority. Permission state is mutable platform state. A correct boundary therefore needs an observation at the point of use and must survive the transition `declared+denied → granted → revoked` rather than validating only the initially granted happy path.

## EXECUTABLE VALIDATION — pending

Workflow: `.github/workflows/m003-android-runtime-permission-validation.yml`  
Initial exact Studio head: `17d7e16dd1f25268f5d0f929cc106dabe56e6b48`.

Fixture shape:
- generate an isolated Flutter Android application;
- declare `android.permission.CAMERA` in the manifest;
- expose native Android `ContextCompat.checkSelfPermission` through a Flutter `MethodChannel`;
- render `CAMERA:DENIED` or `CAMERA:GRANTED` from the native result;
- install on an API 35 x86_64 Android Emulator;
- require initial denied state in both app UI and `dumpsys package`;
- grant CAMERA with `pm grant`, relaunch, and require app UI + platform state to report granted;
- revoke CAMERA with `pm revoke` while the granted-state process is live;
- test process disappearance, relaunch, fresh PID, and app UI + platform state returning to denied;
- require natural workflow completion.

### Claim / oracle

**CLAIM:** at this bounded Android target, current dangerous-permission authority is mutable platform state observed through the native boundary; grant and revoke transitions must change the app-observed state, and revocation behavior must not be modeled as a static manifest property.

**ORACLE:** two independent observation surfaces are required at each state: application UI populated through `checkSelfPermission`, plus Android package-manager state from `dumpsys package`. PID observations distinguish a continued process from a fresh post-revocation process.

**VERDICT:** OPEN. The workflow was committed, but no terminal execution evidence existed at note creation. No PASS or TRANSFER VALIDATION is awarded until the run completes and the exact environment/result are recovered.

## FAILURE MODEL

The fixture can expose:
- assuming a declared dangerous permission is already granted;
- stale application permission state after platform grant/revoke;
- failure to re-evaluate authority after process replacement;
- CI/oracle errors that confuse platform state with application state.

It does not exercise the user-facing permission dialog, rationale UI, one-time grant timing, actual camera access, permission-group behavior, auto-reset/hibernation, physical-device behavior, iOS, or product code.

## RELATED DOMAIN CHECK

- **Foundations:** F001/F002 execution and state boundaries checked; runtime authority is platform state, not a language guarantee.
- **Architecture:** A003 contracts checked; permission-dependent features need explicit denied/granted behavior rather than hidden environmental preconditions.
- **Mobile:** M001/M002 and M003 base research checked. This is a materially different authority-state transfer, not another file-sentinel variant.
- **Data:** no durability claim is made; permission state is not application persistence evidence.
- **Quality:** independent app/platform oracles and failure-first denied/grant/revoke sequence are used.
- **Systems:** S002 least-privilege boundary is consumed; this fixture does not establish secure-storage or threat-model completeness.
- **Design Studio:** permission rationale/denial UX is materially related but no design contract is changed by this engineering fixture.
- **Web Manager / Marketing Manager:** not materially relevant to this native runtime-authority mechanism.
- **Product source/ref:** no product repository is audited; this is a Studio fixture only.

## HANDOFFS

- **Quality:** preserve permission-state transition and fresh-process observations as separate oracles; a successful `pm` command alone is not application behavior evidence.
- **Architecture:** permission-dependent APIs should make denial/revocation an explicit contract state.
- **Systems:** use this as runtime least-privilege mechanics only; it does not validate secure storage or broader authorization policy.
- **Design Studio:** future product permission UX should consume the platform rule that denial/revocation is normal mutable state; no canonical design files edited.

## OPEN / CHANGE WATCH

- Terminal execution result and exact Flutter/Dart/Android/emulator identity are OPEN.
- User-driven dialog denial, one-time permissions, auto-reset, physical Android and product transfer remain OPEN.
- Android permission behavior and Flutter/native integration are version-sensitive; preserve exact environment identity.
