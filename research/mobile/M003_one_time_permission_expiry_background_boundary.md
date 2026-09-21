# M003 — Android one-time permission expiry / background boundary

Status: **SOURCE + SYNTHESIS + EXECUTABLE BOUNDED OBSERVATION; SEMANTIC VERDICT RETRIEVAL OPEN**  
Evidence date: 2026-09-22

## Problem / professional boundary
The existing M003 fixture validates user-driven one-time CAMERA grant while the activity remains foregrounded and separately validates denial/repeated-denial behavior. It does **not** validate what happens to a one-time grant after the app leaves the foreground. This is a different lifecycle class because Android explicitly makes one-time authority depend on app visibility/background behavior and foreground-service state.

## SOURCE
Authoritative Android Developers sources rechecked 2026-09-22:

- `https://developer.android.com/training/permissions/requesting` — for camera/microphone/location one-time permissions on Android 11+, access remains while the activity is visible; after the app enters background, access can continue for a short period; if a foreground service was started while visible, access can continue until that service stops. The same guide states that revocation terminates the app process and that the next access request prompts again.
- `https://developer.android.com/about/versions/11/privacy/permissions` — Android 11 introduced one-time permissions and unused-app permission auto-reset as distinct mechanisms.
- `https://developer.android.com/topic/performance/app-hibernation` — app hibernation/unused-app reset is governed by app-usage rules and exemptions and operates on a months-scale inactivity policy; it must not be conflated with one-time background expiry.

## SYNTHESIS
One-time permission is not simply `GRANTED until explicit user denial`. It is a lease-like authority whose lifetime depends on process/activity/service lifecycle. At least three state dimensions matter: access authority now, app execution/lifecycle, and request/recovery state.

The official documentation intentionally says background access lasts a **short period** rather than publishing a portable duration. Therefore a test that asserts revocation at an arbitrary fixed second count would create a harness-defined contract not guaranteed by Android.

## CONTRADICTION PREVENTION
The already validated M003 one-time grant does not contradict later revocation; it observed the grant while the app was active. M002 HOME background/resume evidence also does not establish permission persistence because that fixture validated lifecycle/file state, not temporary permission authority.

## VALIDATION design
The executable target preserves the existing real user-dialog path and adds independent lifecycle/authority/process oracles. Ordinary background observation uses three semantic outcomes: `OBSERVED_EXPIRY_AND_REQUESTABILITY`, `INCONCLUSIVE_WINDOW_EXHAUSTED`, or `HARNESS_FAILURE:<phase>`. Window exhaustion is not platform failure.

## EXECUTABLE OBSERVATION — 2026-09-22
Exact target `yhappcom/software-engineering-studio → main → 37812fccf3c52ae891f9ab13bc832557a57bd5ab → Studio fixture (no product version) → evidence 2026-09-22` executed as GitHub Actions run `35651688386`, attempt 1, job `106505361356`.

**VALIDATION:** the job completed `success`. Fixture creation, API-35 emulator execution, `Report observation verdict`, `Classify harness failure`, and `Require trustworthy bounded observation` all completed successfully. The gate at this exact ref accepts only `OBSERVED_EXPIRY_AND_REQUESTABILITY` or `INCONCLUSIVE_WINDOW_EXHAUSTED`, requires the emulator action outcome itself to be `success`, and separately fails a `HARNESS_FAILURE:<phase>` classifier. Therefore the preceding run-level gate failure is closed as a harness/observability-gate problem for this exact target: the bounded observation can now terminate cleanly without converting window exhaustion into Android failure.

**OPEN / evidence limit:** current connected GitHub metadata exposes terminal step outcomes but not the emitted verdict-file contents or job log text, and this workflow uploaded no artifact. Consequently this run proves a trustworthy bounded observation completed, but does **not** distinguish which of the two accepted semantic outcomes occurred. It is invalid to claim that natural expiry was observed, that it was not observed within 180 seconds, or that requestability after expiry was validated from the accessible evidence alone. No PASS, TRANSFER VALIDATION, REPLICATION, or ROOT CAUSE for Android expiry semantics is awarded.

**ENGINEERING JUDGMENT:** the next useful change is evidence preservation, not a longer sleep or another semantic variant: publish the verdict and minimal authority/PID timeline as a workflow artifact or otherwise expose them through retrievable run metadata. Re-running the same target without making its semantic verdict independently retrievable has low evidence value.

## VALIDATION / OPEN
- Semantic verdict for run `35651688386` remains OPEN because verdict/log payload is not retrievable through the current evidence channel.
- Foreground-service discriminator remains a later alternative only after ordinary-background semantic evidence is preserved.
- Physical/OEM/other-API behavior remains separate REPLICATION work.
- Auto-reset/app-hibernation is a separate lifecycle and must not be simulated by editing permission flags and called production-equivalent evidence.

## ENGINEERING JUDGMENT
Product code should treat permission authority as revocable at use time and re-check at the protected operation boundary. It should not schedule logic around a presumed one-time-permission grace duration. If continued background access is truly required, the product must use the appropriate platform-supported execution/permission model rather than relying on incidental grace.

## CHANGE WATCH
- Android permission lifecycle and Permission Controller implementation are version/OEM sensitive.
- Foreground-service requirements and restrictions continue to evolve across Android releases.
- Permission Controller resource IDs remain test observations, not product APIs.

## RELATED DOMAIN CHECK
- Foundations: mutable OS authority and process lifetime are relevant; no new Foundations gate claim.
- Architecture: authority, lifecycle and requestability are separate state dimensions.
- Mobile: owning track; executable bounded observation now terminates cleanly, semantic verdict retrieval remains OPEN.
- Data: not materially relevant to the permission lease itself.
- Quality: three-valued verdict discipline worked at the gate; evidence preservation is now the limiting oracle/reproducibility issue.
- Systems: CI artifact/log provenance is materially relevant because a green gate without retrievable semantic payload cannot support the stronger platform claim.
- Design Studio: recovery UX must tolerate authority disappearing after backgrounding. No Design Studio canonical file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Quality: preserve semantic verdict payload independently from the job conclusion; a green gate is not self-interpreting evidence.
- Systems: make verdict/timeline an artifact or equivalent retrievable evidence bound to exact run/ref.
- Architecture: continue modeling temporary authority separately from lifecycle and requestability.
- Design Studio: permission-gated flows should recover from authority loss after backgrounding rather than assuming a prior one-time grant remains valid.
