# M003 — Android one-time permission expiry / background boundary

Status: **EXECUTABLE BOUNDED TRANSFER VALIDATION — NATURAL EXPIRY + REQUESTABILITY OBSERVED**  
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
Earlier exact target `37812fccf3c52ae891f9ab13bc832557a57bd5ab`, run `35651688386`, job `106505361356` completed successfully but did not preserve a retrievable semantic payload, so it established only that the bounded observation harness could terminate correctly.

Exact evidence-preserving target: `yhappcom/software-engineering-studio → main → ae5597cc15fca07fcc63688a91f1cf8da9ac15f4 → Studio fixture (no product version) → evidence 2026-09-22`; GitHub Actions run `35662745671`, attempt 1, terminal `success`. Artifact `m003-expiry-semantic-evidence`, artifact id `10667827225`, digest `sha256:5f5784550773d99704067664263a46e3afd167fd9196fbfe41bc175c244b0c2f`, is bound to that exact run/head.

**ENVIRONMENT:** Flutter 3.47.5, framework revision `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`, engine revision `af7e796e161ae0bb1ff0758c71a7105418bd9ded`, Dart 3.13.4 linux_x64; Android API-35 x86_64 Pixel 6 emulator as defined by the fixture.

**OBSERVATION:** after real `Only this time` grant, initial app PID was `2246`. HOME transition produced `M003_ACTIVITY_AFTER_HOME=False`. Polling observed permission `granted=True` with PID `2246` from elapsed 0.0 through 55.4 seconds. At elapsed 60.4 seconds permission became `granted=False` and the PID observation became empty. The fixture then relaunched the app, made a new app-originated permission request, verified the system permission dialog was requestable, and recorded `M003_VERDICT=OBSERVED_EXPIRY_AND_REQUESTABILITY` followed by phase `complete`.

**VALIDATION / TRANSFER VALIDATION:** this closes the prior semantic-verdict retrieval gap and validates, at this exact Studio/API-35 emulator context, the documented lifecycle shape: an app-originated one-time grant can survive ordinary HOME backgrounding briefly, then be revoked with process termination, after which a new request is possible. The observed `60.4s` is **not** a portable timeout contract, SLA, or Android guarantee.

**REPLICATION:** not awarded. This is one exact emulator/API/toolchain execution. Physical devices, OEM variants, other Android API versions, independent reruns/environments, and product runtime remain OPEN.

## VALIDATION / OPEN
- Matched foreground-service discriminator remains a later alternative if causal discrimination between ordinary-background expiry and supported foreground-service continuation becomes the highest-value Mobile block.
- Physical/OEM/other-API behavior remains separate REPLICATION work.
- Auto-reset/app-hibernation is a separate lifecycle and must not be simulated by editing permission flags and called production-equivalent evidence.
- Product transfer remains OPEN; no MintTap/LogMate runtime claim follows from this Studio fixture.

## ENGINEERING JUDGMENT
Product code should treat permission authority as revocable at use time and re-check at the protected operation boundary. It should not schedule logic around the observed 60.4-second grace. If continued background access is truly required, the product must use the appropriate platform-supported execution/permission model rather than relying on incidental grace.

## CHANGE WATCH
- Android permission lifecycle and Permission Controller implementation are version/OEM sensitive.
- Foreground-service requirements and restrictions continue to evolve across Android releases.
- Permission Controller resource IDs remain test observations, not product APIs.

## RELATED DOMAIN CHECK
- Foundations: mutable OS authority and process lifetime are directly demonstrated; no new Foundations gate claim.
- Architecture: authority, lifecycle and requestability remain separate state dimensions.
- Mobile: owning track; bounded natural expiry/requestability transfer validated.
- Data: not materially relevant to the permission lease itself.
- Quality: three-valued verdict plus run-bound semantic artifact prevented a green job from being overinterpreted and now supplies the missing observation/verdict/reproduction data.
- Systems: artifact digest + exact run/head/toolchain bind the semantic payload to execution provenance.
- Design Studio: recovery UX must tolerate authority disappearing after backgrounding. No Design Studio canonical file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Quality: retain semantic verdict payload independently from job conclusion for platform lifecycle tests; elapsed observations must not silently become specifications.
- Systems: retain artifact digest and exact run/head/toolchain identity when CI evidence supports semantic claims.
- Architecture: temporary authority, process lifecycle, and requestability are independently observable dimensions.
- Design Studio: permission-gated flows should recover from authority loss after backgrounding rather than assuming a prior one-time grant remains valid.
