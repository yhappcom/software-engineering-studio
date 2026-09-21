# M003 — Android user-driven permission dialog transfer

Status: **IN STUDY — FAILURE REPRODUCED; REQUEST-INTERACTION CLASS ISOLATED**  
Evidence date: 2026-09-21

## Problem / professional boundary
Prior M003 permission evidence used `pm grant` / `pm revoke`. This block validates a materially different evidence class: an app-originated Android runtime-permission request plus actual system-dialog interaction and independent package-state observation.

## SOURCE
Android Developers, rechecked 2026-09-21:
- `https://developer.android.com/training/permissions/requesting` — dangerous permissions are requested at feature need; denial is an ordinary state; Android 11/API 30+ provides `Only this time` for camera/microphone/location.
- `https://developer.android.com/about/versions/11/privacy/permissions` — one-time permissions and unused-app reset are platform-managed lifecycle behavior.
- `https://developer.android.com/topic/performance/app-hibernation` — unused-app restrictions can reset runtime permissions and remain a separate lifecycle.

## SYNTHESIS
Shell grant/revoke and actual user-dialog choices are different evidence classes. Authority is mutable OS state. CI observability is part of the validation contract: a failed combined oracle is insufficient when it cannot identify the first failed semantic operation.

## VALIDATION — execution 1
Workflow `.github/workflows/m003-android-user-permission-dialog.yml`; exact head `63f96e010691db87fea13bc7e08866c082dfb656`; run `35564720878`; job `106224179388`; attempt 1; Flutter `3.47.5`; Android API 35 x86_64 emulator, Pixel 6 profile. Build/setup succeeded; combined emulator oracle failed. The first semantic phase was not externally recoverable. No PASS, TRANSFER VALIDATION, or ROOT CAUSE.

## VALIDATION — execution 2: phase isolation
Exact head `1426e11bd7ef708dcb126579de3eab7e7ff72472`; run `35573084874`; job `106248740578`; attempt 1; completed **failure**.

Checkout, pinned Flutter install, toolchain recording, fixture build, phase-reporting oracle creation and KVM setup all passed. The emulator wrapper returned control successfully and the metadata-visible diagnostic steps classified the saved verdict as **request interaction failure**. `Fail — request interaction` is the only semantic classifier that failed; initial install/app-state, one-time-choice discovery classifier, system-choice interaction classifier, callback/UI classifier, package-state classifier, and fresh-install classifier did not match the saved failure verdict. The final completeness gate also failed, as required.

### Interpretation
This is meaningful isolation but not ROOT CAUSE. The classifier at head `1426e11...` intentionally grouped two possible phases: `tap_request_one_time` and `tap_request_denial`. Therefore the evidence proves the failure occurred while automation attempted to tap the app's `REQUEST CAMERA` control in either the initial one-time path or the fresh-install denial path. It does **not** prove which of the two, nor whether the causal mechanism is UI publication/readiness, text-node discovery, bounds/tap automation, activity state, or another interaction-layer defect. It does not establish an Android permission-platform failure because the failing phase precedes or is separate from system-choice validation.

## VALIDATION — classifier refinement
Exact head `c9328340a77c010c1b3b67a8f7ab42350f637bd8` changes only externally visible diagnostic classification: `tap_request_one_time` and `tap_request_denial` now have separate named failure steps. Application code, manifest, MethodChannel, Android permission semantics, system-choice sequence, package-state checks, Flutter pin, API level, emulator profile, and oracle operations are unchanged. This is diagnostic instrumentation, not a semantic fix. A resulting execution may isolate the failing request tap but still cannot establish ROOT CAUSE without a causal hypothesis and falsification.

## CONTRADICTION / debugging model
Execution 1 was opaque. Execution 2 reproduced failure and narrowed it to the request-interaction class. The next evidence boundary is exact request-tap identity. Repeating the same grouped classifier has low value; splitting it is justified because it changes observability rather than target semantics.

## Target contract retained
1. fresh install starts `CAMERA:DENIED`;
2. app invokes Android runtime permission request for CAMERA;
3. actual system dialog exposes expected one-time choice;
4. automation selects the actual system control;
5. callback/UI and `dumpsys package` independently agree on grant;
6. uninstall/reinstall resets authority for an independent denial path;
7. actual system denial is selected;
8. UI and package state independently agree on denial;
9. natural completion required.

## Evidence limits
No PASS or TRANSFER VALIDATION. One-time expiry/background grace, repeated-denial behavior, auto-reset/hibernation, physical Android/OEM, actual camera access, iOS, product/release/production behavior remain OPEN.

## RELATED DOMAIN CHECK
- Foundations: OS-managed mutable authority; no language/runtime guarantee.
- Architecture: granted/denied are explicit feature states.
- Mobile: extends M003 beyond shell mutation.
- Data: no material durability claim.
- Quality: phase evidence materially improved failure isolation; classifier granularity itself was a debugging limitation.
- Systems: least privilege related; no complete security-policy claim.
- Design Studio: denial/rationale UX remains a handoff; no canonical design file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Quality: externally recoverable semantic-phase evidence and non-overbroad classifiers are part of a useful CI debugging oracle.
- Design Studio: future permission request/denial UX should consume mutable-authority behavior; Engineering does not own visual/content treatment.
- Systems: one-time authority is a least-privilege mechanism, not a complete permission/security policy.

## OPEN / CHANGE WATCH
- Exact failing request-tap phase at execution 2 remains unresolved by its grouped classifier; head `c9328340...` separates it for the next execution.
- ROOT CAUSE remains OPEN pending causal hypothesis + falsification.
- One-time expiry/background grace, repeated denial / `USER_FIXED`, auto-reset/hibernation, physical/OEM/iOS, and exact product runtime remain OPEN.
