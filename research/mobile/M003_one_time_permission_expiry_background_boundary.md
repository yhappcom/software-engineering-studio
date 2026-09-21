# M003 — Android one-time permission expiry / background boundary

Status: **SOURCE + SYNTHESIS + VALIDATION DESIGN; EXECUTION OPEN**  
Evidence date: 2026-09-22

## Problem / professional boundary
The existing M003 fixture validates user-driven one-time CAMERA grant while the activity remains foregrounded and separately validates denial/repeated-denial behavior. It does **not** validate what happens to a one-time grant after the app leaves the foreground. This is a different lifecycle class because Android explicitly makes one-time authority depend on app visibility/background behavior and foreground-service state.

## SOURCE
Authoritative Android Developers sources rechecked 2026-09-22:

- `https://developer.android.com/training/permissions/requesting` — for camera/microphone/location one-time permissions on Android 11+, access remains while the activity is visible; after the app enters background, access can continue for a short period; if a foreground service was started while visible, access can continue until that service stops. The same guide states that revocation terminates the app process and that the next access request prompts again.
- `https://developer.android.com/about/versions/11/privacy/permissions` — Android 11 introduced one-time permissions and unused-app permission auto-reset as distinct mechanisms.
- `https://developer.android.com/topic/performance/app-hibernation` — app hibernation/unused-app reset is governed by app-usage rules and exemptions and operates on a months-scale inactivity policy; it must not be conflated with one-time background expiry.

## SYNTHESIS
One-time permission is not simply `GRANTED until explicit user denial`. It is a lease-like authority whose lifetime depends on process/activity/service lifecycle. At least three state dimensions matter:

1. access authority now (`GRANTED` / `DENIED`);
2. app execution/lifecycle (`visible`, ordinary background/cached, process terminated, foreground service active);
3. request/recovery state (whether a subsequent app-originated request can show a permission dialog).

The official documentation intentionally says background access lasts a **short period** rather than publishing a portable duration. Therefore a test that asserts revocation at an arbitrary fixed second count would create a harness-defined contract not guaranteed by Android.

## CONTRADICTION PREVENTION
The already validated M003 one-time grant does not contradict later revocation; it observed the grant while the app was active. M002 HOME background/resume evidence also does not establish permission persistence because that fixture validated lifecycle/file state, not temporary permission authority. Reusing either PASS as proof of one-time background behavior would violate the evidence boundary.

## VALIDATION design
A trustworthy executable transfer should preserve the existing real user-dialog path and add independent lifecycle/authority/process oracles.

### Candidate A — ordinary background grace observation
1. fresh install and launch;
2. request CAMERA from the app and select the real `Only this time` system control;
3. independently verify callback/UI plus package permission grant;
4. send HOME without force-stop;
5. poll package permission authority and process identity/liveness over a bounded observation window;
6. if the platform revokes during that window, record elapsed observation only as an **observation**, not a portable timeout contract;
7. verify whether process identity changes/terminates as authority is revoked;
8. relaunch and issue a fresh app-originated request, observing whether the system dialog is available again.

A timeout without revocation is **INCONCLUSIVE for expiry**, not FAIL, because Android does not specify a maximum portable grace duration.

### Candidate B — foreground-service discriminator
Use a matched fixture where a correctly declared foreground service is started while the activity is visible before backgrounding. Compare authority/process behavior with Candidate A. This is a materially different lifecycle control because the official contract explicitly states that one-time access can continue until that foreground service stops.

### Candidate C — process/revocation boundary
Observe a system-driven or platform-supported revocation transition and verify process termination/relaunch semantics. Do not manufacture the claimed lifecycle solely with `pm revoke` and then relabel it as natural one-time expiry; shell revocation may be useful only as a control path.

## ORACLE requirements
- real Permission Controller interaction for the initial one-time choice;
- independent package permission state, not Flutter UI alone;
- app process PID/liveness before and after background/revocation;
- activity/background state evidence;
- foreground-service state for the discriminator variant;
- callback/UI projection after relaunch;
- permission-dialog presence/requestability after expiry;
- natural job completion and named phase reporting.

## VALIDATION / OPEN
No PASS, TRANSFER VALIDATION, REPLICATION, or ROOT CAUSE is awarded by this note. The current execution environment has proven capable of API-35 emulator user-dialog work, but the platform does not publish a fixed ordinary-background grace timeout. A bounded CI run can therefore observe a transition but cannot truthfully fail the platform for not expiring within an arbitrary harness deadline.

Execution remains OPEN until the harness can distinguish `observed expiry` from `observation window exhausted` without inventing a platform guarantee. Physical/OEM/other-API behavior remains separate REPLICATION work even after an emulator observation succeeds.

Auto-reset/app-hibernation is a separate lifecycle and should receive its own validation method; months-scale production policy must not be simulated by simply editing permission flags and calling that production-equivalent evidence.

## ENGINEERING JUDGMENT
Product code should treat permission authority as revocable at use time and re-check at the protected operation boundary. It should not schedule logic around a presumed one-time-permission grace duration. If continued background access is truly required, the product must use the appropriate platform-supported execution/permission model rather than relying on incidental grace.

## CHANGE WATCH
- Android permission lifecycle and Permission Controller implementation are version/OEM sensitive.
- Foreground-service requirements and restrictions continue to evolve across Android releases.
- Permission Controller resource IDs remain test observations, not product APIs.

## RELATED DOMAIN CHECK
- Foundations: mutable OS authority and process lifetime are relevant; no new Foundations gate claim.
- Architecture: authority, lifecycle and requestability are separate state dimensions; permission checks belong at protected-operation boundaries.
- Mobile: owning track; this closes a source/model ambiguity but not executable validation.
- Data: not materially relevant to the permission lease itself.
- Quality: fixed-time assertions would be invalid without a specified timeout; `not observed within bounded window` must remain inconclusive.
- Systems: least privilege and foreground-service execution policy are relevant; this is not complete authorization/security evidence.
- Design Studio: recovery UX must tolerate authority disappearing after backgrounding and a later request being needed. No Design Studio canonical file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture/model only.

## HANDOFFS
- Quality: preserve a three-valued verdict for ordinary background observation — observed expiry / still granted at window end (inconclusive for expiry) / harness failure — rather than inventing a timeout contract.
- Architecture: model temporary authority separately from activity/process/service lifecycle and requestability.
- Design Studio: permission-gated flows should recover from authority loss after backgrounding instead of assuming a prior one-time grant remains valid.
- Systems: any foreground-service discriminator must use current service-type/manifest/runtime requirements and record exact API/target SDK.