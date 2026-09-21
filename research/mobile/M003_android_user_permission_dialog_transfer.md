# M003 — Android user-driven permission dialog transfer

Status: **IN STUDY — REQUEST TAP ADVANCED; SYSTEM ONE-TIME CONTROL DISCOVERY NOW ISOLATED**  
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
Shell grant/revoke and actual user-dialog choices are different evidence classes. Authority is mutable OS state. CI observability is part of the validation contract: a failed combined oracle is insufficient when it cannot identify the first failed semantic operation. UI-automation selectors are part of the oracle/harness, not application permission semantics; selector or system-control discovery failure must be separated from platform permission failure.

## VALIDATION — executions 1–3
Execution 1: exact head `63f96e010691db87fea13bc7e08866c082dfb656`, run `35564720878`, job `106224179388`, Flutter 3.47.5, Android API 35 x86_64 Pixel 6 emulator. Combined oracle failed opaquely.

Execution 2: exact head `1426e11bd7ef708dcb126579de3eab7e7ff72472`, run `35573084874`, job `106248740578`, reproduced failure and narrowed it to grouped request interaction.

Execution 3: exact head `c9328340a77c010c1b3b67a8f7ab42350f637bd8`, run `35578458429`, job `106265550190`, reproduced and isolated the first failed operation to `tap_request_one_time` under a `text`-only app-button selector. This was reproduction/isolation, not ROOT CAUSE.

## VALIDATION — execution 4: accessibility selector intervention
Exact head `409075c7f208a134ad3a5910bab0db44571e0ad3`; run `35583802011`; job `106282376014`; attempt 1; completed **failure**.

The intervention preserved application code, manifest, MethodChannel, permission request, permission sequence, callback/package-state oracle, Flutter 3.47.5 and API-35 x86_64 Pixel 6 environment. It changed the app-button selector from exact UIAutomator `text` only to exact `text` OR `content-desc`.

**OBSERVATION:** `Fail — one-time request tap` no longer matched. The first metadata-visible failure moved forward to `Fail — one-time choice discovery`; all setup/build/emulator execution completed and the final completeness gate failed as required.

**CAUSAL INTERPRETATION:** the broadened selector falsifies the narrower claim that the request could not be activated at all. It supports a harness-selector/accessibility-channel defect as the cause of the earlier `tap_request_one_time` boundary because the only intended intervention was selector channel acceptance and the request advanced into system-dialog discovery. The exact matched channel (`text` vs `content-desc`) is not recoverable from current job metadata, so the more specific attribute-level ROOT CAUSE remains unproven. No Android permission-platform defect is inferred.

The new failure is independent: the discovery oracle searched serialized XML for the English literal `Only this time`. That is an observation contract, not a stable semantic identity for the system control.

## CAUSAL HYPOTHESIS / falsification — permission-controller semantic control
**Hypothesis:** after the app request is activated, the one-time permission control exists but the English-label discovery oracle is too presentation/localization dependent. A permission-controller resource-id identity should discriminate the semantic system control more directly than display text.

Exact head `6fda0223249e723f2b9ee636a7329a97ec64b697` preserves application and permission semantics but replaces the system-dialog English-label discovery/tap with UIAutomator resource-id suffixes `permission_allow_one_time_button` and `permission_deny_button`. App-button activation retains the prior `text`/`content-desc` selector. The oracle logs the concrete resource id if matched. Workflow run `35589277729` was queued at evidence capture; no verdict is assigned yet.

**Falsification rule:** if `discover_one_time_choice` fails again, the assumed permission-controller resource identity is absent or not observable in this environment and must not be treated as a stable oracle. If discovery advances, inspect the next independently classified phase; only complete callback/UI + package-state agreement + denial path + natural completion can support bounded TRANSFER VALIDATION.

## Target contract retained
1. fresh install starts `CAMERA:DENIED`;
2. app invokes Android runtime permission request for CAMERA;
3. actual system dialog exposes the one-time authority control;
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
- Quality: phase evidence plus causal selector intervention separated harness failure from target semantics; system-control oracle is now under falsification.
- Systems: least privilege related; no complete security-policy claim.
- Design Studio: denial/rationale UX remains a handoff; no canonical design file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Quality: selector identity is part of oracle validity. Prefer semantic/stable control identity over presentation text when the platform exposes one, but validate that identity rather than assuming it.
- Design Studio: future permission request/denial UX should consume mutable-authority behavior; Engineering does not own visual/content treatment.
- Systems: one-time authority is a least-privilege mechanism, not a complete permission/security policy.

## OPEN / CHANGE WATCH
- Earlier `tap_request_one_time` failure advanced under the broadened app-button selector at run `35583802011`; exact matched accessibility attribute is not externally recovered.
- Current first failed phase is `discover_one_time_choice` under the English-label oracle.
- Resource-id semantic-control hypothesis is under bounded test at exact head `6fda0223...`, run `35589277729`.
- User-dialog TRANSFER VALIDATION remains OPEN until the complete grant + package state + reinstall + denial contract succeeds.
- One-time expiry/background grace, repeated denial / `USER_FIXED`, auto-reset/hibernation, physical/OEM/iOS, and exact product runtime remain OPEN.
