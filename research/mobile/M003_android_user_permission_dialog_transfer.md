# M003 — Android user-driven permission dialog transfer

Status: **IN STUDY — FAILURE REPRODUCED; ONE-TIME REQUEST TAP ISOLATED; CAUSAL SELECTOR TEST STARTED**  
Evidence date: 2026-09-21

## Problem / professional boundary
Prior M003 permission evidence used `pm grant` / `pm revoke`. This block validates a materially different evidence class: an app-originated Android runtime-permission request plus actual system-dialog interaction and independent package-state observation.

## SOURCE
Android Developers, rechecked 2026-09-21:
- `https://developer.android.com/training/permissions/requesting` — dangerous permissions are requested at feature need; denial is an ordinary state; Android 11/API 30+ provides `Only this time` for camera/microphone/location.
- `https://developer.android.com/about/versions/11/privacy/permissions` — one-time permissions and unused-app reset are platform-managed lifecycle behavior.
- `https://developer.android.com/topic/performance/app-hibernation` — unused-app restrictions can reset runtime permissions and remain a separate lifecycle.
- Flutter accessibility/testing docs, rechecked 2026-09-21: Flutter exposes widget semantics to platform accessibility APIs and recommends inspecting/testing that semantics layer. This supports treating platform accessibility labels as a distinct observation/automation channel rather than assuming visible Flutter labels necessarily occupy Android UIAutomator's `text` attribute.

## SYNTHESIS
Shell grant/revoke and actual user-dialog choices are different evidence classes. Authority is mutable OS state. CI observability is part of the validation contract: a failed combined oracle is insufficient when it cannot identify the first failed semantic operation. A UI-automation selector is also part of the oracle/harness, not the application permission semantics; selector failure must be separated from platform permission failure.

## VALIDATION — execution 1
Workflow `.github/workflows/m003-android-user-permission-dialog.yml`; exact head `63f96e010691db87fea13bc7e08866c082dfb656`; run `35564720878`; job `106224179388`; attempt 1; Flutter `3.47.5`; Android API 35 x86_64 emulator, Pixel 6 profile. Build/setup succeeded; combined emulator oracle failed. The first semantic phase was not externally recoverable. No PASS, TRANSFER VALIDATION, or ROOT CAUSE.

## VALIDATION — execution 2: phase isolation
Exact head `1426e11bd7ef708dcb126579de3eab7e7ff72472`; run `35573084874`; job `106248740578`; attempt 1; completed **failure**.

Checkout, pinned Flutter install, toolchain recording, fixture build, phase-reporting oracle creation and KVM setup all passed. The emulator wrapper returned control successfully and the metadata-visible diagnostic steps classified the saved verdict as **request interaction failure**. `Fail — request interaction` was the matching semantic classifier. That classifier grouped `tap_request_one_time` and `tap_request_denial`, so exact request-tap identity remained unresolved.

## VALIDATION — execution 3: split request classifier
Exact head `c9328340a77c010c1b3b67a8f7ab42350f637bd8`; run `35578458429`; job `106265550190`; attempt 1; completed **failure**.

Checkout, Flutter installation/toolchain capture, fixture build, phase-reporting oracle generation, KVM setup and emulator wrapper execution all completed. The split metadata classifiers now identify the first failed semantic operation as **`tap_request_one_time`**: `Fail — one-time request tap` failed, while `Fail — denial request tap` and all later classifiers did not match the saved verdict. The final completeness gate failed as required.

### Interpretation
This is reproduction plus isolation, not ROOT CAUSE. The failure occurs before discovery/selection of Android's one-time permission choice. It therefore does not establish a permission-platform defect. At this head the tap helper searches only UIAutomator nodes whose `text` attribute exactly equals `REQUEST CAMERA`; the preceding `require_ui` merely searches serialized XML and can succeed when a label is exported through a different accessibility attribute. Flutter's platform semantics export makes an accessibility-label channel a plausible harness-level causal hypothesis.

## CAUSAL HYPOTHESIS / falsification — selector channel
**Hypothesis:** the app button is present and observable, but Flutter exports its actionable label through Android accessibility semantics such that the UIAutomator node is addressable by `content-desc` rather than the harness's exact `text`-only selector. If true, the prior request-tap failure is a harness selector defect, not Android permission behavior.

Exact head `409075c7f208a134ad3a5910bab0db44571e0ad3` changes only the UI-automation selector: it accepts an exact match in either `text` or `content-desc` and logs which channel matched. Application code, manifest, MethodChannel, Android permission request, user-choice sequence, callback/package-state oracles, Flutter 3.47.5 pin, API-35 x86_64 emulator and Pixel 6 profile remain unchanged. This is a bounded causal intervention. At evidence capture, workflow execution had not yet appeared in the Actions run listing; therefore no verdict is assigned.

**Falsification rule:** if the broadened selector still fails at `tap_request_one_time`, the accessibility-attribute hypothesis is weakened/rejected for that run and investigation must inspect another interaction/readiness mechanism. If the request tap advances and the complete permission oracle succeeds, the intervention supports the selector-channel cause; the logged channel is needed before naming the exact attribute mechanism. A later failure can still isolate an independent downstream defect.

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
No PASS or TRANSFER VALIDATION yet for the user-driven dialog block. One-time expiry/background grace, repeated-denial behavior, auto-reset/hibernation, physical Android/OEM, actual camera access, iOS, product/release/production behavior remain OPEN.

## RELATED DOMAIN CHECK
- Foundations: OS-managed mutable authority; no language/runtime guarantee.
- Architecture: granted/denied are explicit feature states.
- Mobile: extends M003 beyond shell mutation.
- Data: no material durability claim.
- Quality: phase evidence converted opaque failure to exact request-tap isolation; selector implementation is now under causal test.
- Systems: least privilege related; no complete security-policy claim.
- Design Studio: denial/rationale UX remains a handoff; no canonical design file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Quality: automation selectors are part of oracle validity. Preserve the accessibility attribute/channel used to locate a control rather than conflating selector failure with target failure.
- Design Studio: future permission request/denial UX should consume mutable-authority behavior; Engineering does not own visual/content treatment.
- Systems: one-time authority is a least-privilege mechanism, not a complete permission/security policy.

## OPEN / CHANGE WATCH
- Exact request tap is isolated to `tap_request_one_time` at run `35578458429`.
- Accessibility `text` vs `content-desc` selector hypothesis is under bounded causal test at head `409075c7...`; execution verdict pending.
- ROOT CAUSE remains OPEN until the intervention is executed and the selector channel/result is observed.
- One-time expiry/background grace, repeated denial / `USER_FIXED`, auto-reset/hibernation, physical/OEM/iOS, and exact product runtime remain OPEN.
