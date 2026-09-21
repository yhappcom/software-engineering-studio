# M003 — Android repeated-denial / USER_FIXED lifecycle

Status: **BOUNDED TRANSFER VALIDATION — API-35 EMULATOR; REPLICATION OPEN**  
Evidence date: 2026-09-22

## Problem / professional boundary
The prior user-dialog transfer validates one-time CAMERA grant and one fresh-install denial, but repeated denial is a distinct mutable-authority lifecycle. This block tests the transition from ordinary denial to a request-suppressed permanent denial state instead of treating every `DENIED` result as equivalent.

## SOURCE
Android Developers, rechecked 2026-09-21:
- `https://developer.android.com/about/versions/11/privacy/permissions` — repeated denial suppresses subsequent permission dialogs; permission flags are available for testing/diagnostics.
- `https://developer.android.com/training/permissions/requesting` — apps must check permission state at protected operations and degrade after denial/revocation; one-time permission is a separate lifecycle.
- `https://developer.android.com/guide/topics/permissions/overview` — runtime permission authority is system-managed.

## SYNTHESIS
A boolean granted/denied projection is insufficient for interaction design. `DENIED + requestable` and `DENIED + USER_FIXED/dialog-suppressed` have the same access result but different recovery behavior. Validation therefore needs independent access-state and requestability/dialog-state evidence.

## VALIDATION — successful transfer execution
Workflow: `.github/workflows/m003-android-user-permission-dialog.yml`  
Repository/ref: `yhappcom/software-engineering-studio` → `main` exact commit `5c088398f9f527b96b0da926b26e5aa77d9de000` → no product version (Studio fixture) → evidence 2026-09-22.  
Run/job: `35619492437` / `106398675688`, attempt 1.  
Target: Flutter 3.47.5 (`6a19cca56475dbfba1478ee68d7bd0c2ef891da1`), Dart 3.13.4, Android API 35 default x86_64 Pixel 6 emulator, emulator 37.1.11.0, GitHub-hosted Ubuntu 24.04 runner.

The executable oracle completed naturally and printed `M003_REPEATED_DENIAL_USER_FIXED_PASS`; the final phase file was `complete`. It observed the following sequence rather than manufacturing state with permission-flag commands:
1. initial app state `CAMERA:DENIED`;
2. real one-time system grant through `permission_allow_one_time_button`, Flutter callback/UI `CAMERA:GRANTED`, and package `granted=true` control path;
3. fresh reinstall and first user denial through `permission_deny_button`;
4. denied callback/UI plus diagnostic `USER_SET` after first denial;
5. second app-originated request exposed the state-specific Permission Controller control `permission_deny_and_dont_ask_again_button`;
6. selecting that control returned denied callback/UI and package diagnostics contained `USER_FIXED`;
7. a third app-originated request exposed neither ordinary deny nor deny-and-don't-ask-again Permission Controller controls;
8. callback/UI remained `CAMERA:DENIED`;
9. all phase classifiers and the complete-oracle gate succeeded.

## CAUSAL / ROOT-CAUSE RESULT
The earlier second-dialog discovery failure was caused by an oracle that reused the first-denial control identity (`permission_deny_button`) after the platform had transitioned to a different state-specific control (`permission_deny_and_dont_ask_again_button`). Changing only that observation/interaction identity allowed the unchanged application permission sequence to complete. This closes that harness failure cause for this bounded target; it is not a claim that the resource IDs are portable across Android versions or OEM implementations.

## TRANSFER VALIDATION
**Awarded, bounded.** The Flutter/native request path, real Permission Controller user interactions, callback/UI projection, package diagnostic flags, and post-`USER_FIXED` dialog suppression were exercised together on the stated API-35 emulator target. This is stronger than source reading or shell-manufactured permission state.

**Not REPLICATION.** There is one successful environment/run for this lifecycle. Physical devices, OEM Permission Controller variants, other Android/API versions, and a second independent green execution remain unvalidated.

## ENGINEERING JUDGMENT / PROJECT DECISION
For permission-gated product features, model at least access authority separately from requestability/recovery state. Do not promise that a repeated request will always redisplay a system dialog after permanent denial. Product code should derive recovery behavior from supported platform APIs/state rather than hard-code Permission Controller resource IDs; those IDs are test-harness observations here.

## OPEN / CHANGE WATCH
- REPLICATION: physical Android/OEM and another API/version or independent environment.
- One-time expiry/background grace and auto-reset/hibernation remain separate lifecycle classes.
- Product runtime, iOS, production and actual camera use remain OPEN.
- CHANGE WATCH: Permission Controller presentation/resource identities and repeated-denial UX can vary by platform/OEM; the resource IDs are not a product API contract.

## RELATED DOMAIN CHECK
- Foundations: OS-managed mutable authority/callback execution; no new Foundations gate claim.
- Architecture: permission access and requestability/recovery are separate externally meaningful state dimensions.
- Mobile: owning track; repeated-denial lifecycle now has bounded transfer evidence.
- Data: no durability claim.
- Quality: independent UI, package-state and phase oracles materially prevented a false platform conclusion.
- Systems: least-privilege/revocation implications noted; not complete authorization-policy evidence.
- Design Studio: downstream permission UX should distinguish ordinary denial from a state where another request does not redisplay the system dialog. No external canonical file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Design Studio: recovery UX for permanent/request-suppressed denial should differ from ordinary first denial; settings/rationale guidance may be required by the eventual product design.
- Quality: preserve access-state + package diagnostic + dialog-presence oracles; avoid presentation-string-only selectors and expose semantic phases individually.
- Architecture: represent authority and requestability/recovery separately when permission-gated features need deterministic recovery flows.
