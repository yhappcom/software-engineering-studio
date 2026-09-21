# M003 — Android user-driven permission dialog transfer

Status: **BOUNDED TRANSFER VALIDATION — API-35 EMULATOR USER CHOICE CONTRACT PASSED**  
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

## VALIDATION — failure → isolation → intervention chain
Execution 1: exact head `63f96e010691db87fea13bc7e08866c082dfb656`, run `35564720878`, job `106224179388`, Flutter 3.47.5, Android API 35 x86_64 Pixel 6 emulator. Combined oracle failed opaquely.

Execution 2: exact head `1426e11bd7ef708dcb126579de3eab7e7ff72472`, run `35573084874`, job `106248740578`, reproduced failure and narrowed it to grouped request interaction.

Execution 3: exact head `c9328340a77c010c1b3b67a8f7ab42350f637bd8`, run `35578458429`, job `106265550190`, isolated the first failed operation to `tap_request_one_time` under a `text`-only app-button selector.

Execution 4: exact head `409075c7f208a134ad3a5910bab0db44571e0ad3`, run `35583802011`, job `106282376014`, changed only the app-button UIAutomator selector from exact `text` to exact `text` OR `content-desc`. The request-tap classifier passed and the first failure moved to `discover_one_time_choice`. This supports a harness selector/accessibility-channel cause for the earlier request-tap boundary, but the exact matched attribute was not externally recovered, so attribute-level ROOT CAUSE is not claimed.

The remaining discovery oracle searched for the English literal `Only this time`. That presentation-dependent identity was replaced by Permission Controller resource-id suffixes `permission_allow_one_time_button` and `permission_deny_button`, while application code, manifest, MethodChannel, permission sequence, callback/package-state checks, Flutter version and emulator target were retained.

## TRANSFER VALIDATION — semantic Permission Controller identity
Exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`; workflow run `35589277729`; attempt 1; job `106299744861`; completed **success** on 2026-09-21.

Environment: pinned Flutter 3.47.5; Android API 35 x86_64 Pixel 6 emulator; GitHub-hosted Ubuntu runner; Studio fixture, not a product artifact.

**ORACLE / TARGET CONTRACT:**
1. fresh install begins with CAMERA denied;
2. app invokes Android runtime CAMERA permission request;
3. actual system one-time control is discovered by Permission Controller resource identity;
4. automation selects that system control;
5. Flutter callback/UI and independent `dumpsys package` state agree on granted authority;
6. uninstall/reinstall resets authority for an independent denial path;
7. actual system denial control is selected by Permission Controller resource identity;
8. Flutter UI and package state independently agree on denial;
9. workflow requires complete oracle and natural job completion.

**OBSERVATION:** the emulator oracle step completed successfully. Every metadata-visible failure classifier (`initial install`, `initial launch or denied observation`, `one-time request tap`, `denial request tap`, `one-time choice discovery`, `system choice interaction`, `callback UI state`, `package permission state`, `fresh-install reset or relaunch`) completed without producing a failure verdict, and `Require complete user-dialog oracle` succeeded. The job and workflow both terminated success.

**VERDICT — TRANSFER VALIDATION:** the bounded API-35 emulator fixture validates an app-originated user-dialog path for one-time CAMERA grant and an independent fresh-install denial path, with system-control interaction plus callback/UI and package-manager agreement. This is materially stronger than the earlier shell-controlled permission transfer.

**CAUSAL RESULT:** replacing the English system-control label with Permission Controller resource identity advanced the exact previously failing discovery boundary through the complete contract. This supports the presentation-dependent English-label oracle as the cause of that bounded discovery failure. It does not prove resource IDs are stable across all Android/OEM/API versions; they remain a CHANGE WATCH item.

## CONTRADICTION / evidence history
Earlier failures were harness-observation failures, not evidence of Android permission-platform failure. The successful semantic-control run resolves the current user-dialog fixture contradiction at this exact environment while preserving the failure chain as evidence of oracle sensitivity.

## Evidence limits
No physical-device, OEM, older/newer Android, actual camera-use, one-time expiry/background grace, repeated-denial, auto-reset/hibernation, iOS, product, release, or production claim is made. One successful semantic-control execution is TRANSFER VALIDATION, not REPLICATION. Permission Controller internal resource identity is version-sensitive and must not be assumed universal.

## RELATED DOMAIN CHECK
- Foundations: OS-managed mutable authority; no language/runtime guarantee.
- Architecture: granted/denied are explicit feature states.
- Mobile: extends M003 beyond shell mutation with actual user/system-dialog interaction.
- Data: no material durability claim.
- Quality: failure classification and selector/control identity materially determined oracle validity; failure→isolation→causal intervention→successful regression chain is preserved.
- Systems: one-time authority is least privilege related; no complete authorization/security-policy claim.
- Design Studio: denial/rationale UX remains a handoff; no canonical design file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Quality: automation control identity is part of oracle validity. Prefer semantic platform identity over localized presentation strings when available, but preserve version scope and validate the identity.
- Design Studio: future permission request/denial UX should consume mutable-authority behavior; Engineering does not own visual/content treatment.
- Systems: one-time authority is a least-privilege mechanism, not a complete permission/security policy.

## OPEN / CHANGE WATCH / REPLICATION
- User-dialog TRANSFER VALIDATION is closed only for Flutter 3.47.5 + API-35 x86_64 Pixel 6 emulator at exact head/run above.
- Independent REPLICATION of this user-dialog semantic-control fixture is not yet claimed.
- Exact matched app accessibility attribute from the earlier selector intervention remains unrecovered and is no longer required to establish the final semantic contract.
- Permission Controller resource IDs are implementation/version-sensitive; revalidate across materially different Android/OEM/API contexts before treating them as portable automation contracts.
- One-time expiry/background grace, repeated denial / `USER_FIXED`, auto-reset/hibernation, physical/OEM/iOS, actual camera use, exact product runtime and production remain OPEN.
