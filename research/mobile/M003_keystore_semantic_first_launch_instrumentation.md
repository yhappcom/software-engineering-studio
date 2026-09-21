# M003 — Keystore semantic first-launch instrumentation

Status: **IN STUDY — causal discrimination run pending**  
Evidence date: 2026-09-21

## Problem
The original Android Keystore semantic fixture has one complete bounded PASS and two first-launch-adjacent failures. A simplified fixture subsequently proved that package PID, Activity entry, native completion, UI publication/resume, and UI-automation observation can all succeed in the available API-35 emulator environment, but it removed Keystore/AES-GCM semantics and therefore could not establish root cause.

The professional boundary is not complete while the original semantic workload remains unable to distinguish startup, native cryptographic completion, UI publication, and UI-automation observation.

## Balance Loop selection
This continuation outranks a new shallow topic because it is a bounded unresolved contradiction with direct Mobile ownership and Quality/Systems leverage. Physical Android/iOS/Safari and canonical product runtime remain stronger eventual transfer rungs but are not available in this execution context; S004 product source build remains authorization-dependent. Re-running the unchanged oracle is explicitly rejected.

## Instrumented semantic experiment
Workflow: `.github/workflows/m003-android-keystore-secure-storage-validation.yml`  
Exact instrumented head: `d6641234713784620fd6bcfe8e6c12e519b33c87`  
Triggered run: `35554495251`  
Target remains the isolated Flutter-created Android app with pinned Flutter `3.47.5`, Android API 35 x86_64 emulator, AndroidKeyStore AES-256/GCM key, app-private ciphertext, force-stop/fresh-process recovery, external ciphertext mutation, and authentication rejection.

### Preserved semantics
The key alias, AndroidKeyStore provider, AES/GCM primitive, 256-bit key request, key purposes, block mode, padding, ciphertext/IV representation, marker value, app-private file, force-stop/recovery sequence, external tamper mutation, and final `AUTH_FAIL` semantic oracle are unchanged.

### New independent signals
The application now emits independent native log markers around the original semantic path:
1. `ACTIVITY_ONCREATE_ENTER` before `super.onCreate`;
2. `FLUTTER_SUPER_ONCREATE_RETURNED` after the Flutter activity superclass returns;
3. `NATIVE_RESULT:WROTE:secure-v1:NONEXPORTABLE` only after the original Keystore/AES-GCM write path completes;
4. `UI_PUBLISHED:WROTE:secure-v1:NONEXPORTABLE` after `setContentView` publishes the result;
5. `ACTIVITY_ONRESUME` from the Activity lifecycle callback;
6. independent `uiautomator` observation of the same semantic result.

The harness separately records phases `first_launch_start`, `first_launch_pid`, `first_launch_activity`, `first_launch_native`, `first_launch_ui_publish`, `first_launch_resume`, and `first_launch_ui_observe` before proceeding to the unchanged recovery/tamper phases. It polls boundedly rather than treating a fixed three-second sleep as the only readiness criterion.

## VALIDATION contract
**CLAIM:** if the prior failure class recurs, the first absent independent signal can localize the failure boundary without changing the cryptographic/storage semantics being diagnosed.

**ORACLE:** fail-fast phase output plus native log markers and UI automation. A complete run still requires fresh-process recovery, deliberate external ciphertext mutation, `AUTH_FAIL`, and natural workflow completion.

**VERDICT:** pending. Run `35554495251` was queued when this record was written. No ROOT CAUSE, REPLICATION, or new PASS is awarded before terminal evidence is recovered.

## Failure interpretation rules
- no PID: startup/process boundary;
- PID but no Activity marker: Activity entry boundary;
- Activity entry but no expected native result: native/Keystore/AES-GCM semantic boundary;
- native result but no UI-published marker: publication boundary;
- UI published/resumed but no `uiautomator` result: observation/readiness boundary;
- complete first launch but later failure: preserve the exact recovery/tamper phase rather than relabeling it first-launch failure.

A reproduced failure phase is not automatically root cause. Causal repair still requires a hypothesis and falsification/check matched to the localized boundary.

## RELATED DOMAIN CHECK
- Foundations: direct Dart/Flutter execution exists; no new Foundations prerequisite blocks this diagnostic.
- Architecture: no application contract is changed; instrumentation is observational.
- Mobile: lead owner; Android runtime/platform boundary under test.
- Data: recovery remains logical fresh-process recovery, not physical durability/backup evidence.
- Quality: independent signals strengthen fault isolation and avoid treating final UI absence as root cause.
- Systems: cryptographic/key semantics are preserved, but this is still emulator evidence and does not establish StrongBox/hardware backing/auth policy.
- Design Studio: not materially relevant; no user interaction contract changes.
- Web Manager / Marketing Manager: not materially relevant to this native diagnostic.
- Product repositories: not inspected because this remains an isolated Studio fixture and makes no MintTap/LogMate implementation claim.

## HANDOFFS
- Mobile → Quality: use the first absent independent marker as failure localization only; do not promote it directly to causal root cause.
- Mobile → Systems: semantic security target is unchanged; instrumentation does not broaden security claims beyond the bounded emulator target.

## OPEN / CHANGE WATCH
- Run `35554495251` terminal result and exact first absent/present signals.
- Original Keystore first-launch ROOT CAUSE remains OPEN.
- Semantic REPLICATION remains OPEN until a complete repeated semantic execution succeeds under a defensible reproduction contract.
- Physical Android/iOS, hardware-backed/StrongBox, auth-bound keys, backup/restore, reinstall/migration and product transfer remain OPEN.
