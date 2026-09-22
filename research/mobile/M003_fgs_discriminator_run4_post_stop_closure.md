# M003 — Foreground-service discriminator run 4 post-stop closure

Status: **BOUNDED TRANSFER VALIDATION — app-owned stop → expiry → requestability observed**  
Evidence date: 2026-09-22

## Scope and provenance

- repository: `yhappcom/software-engineering-studio`
- exact ref/commit: `07b389dfbbe3abf9440a00e7f80668a367b556f3`
- workflow: `.github/workflows/m003-one-time-fgs-discriminator.yml`
- run: `35695122004`
- run conclusion: `success`
- artifact: `m003-fgs-semantic-evidence`, id `10680900102`
- artifact digest: `sha256:fe3ab7cbe28ec5a210c210cb27444d41da349787fe6e46d812451f603447ad0c`
- Flutter: `3.47.5`, framework revision `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`
- Dart: `3.13.4 stable`, linux_x64
- target: Android API-35 x86_64 Pixel 6 emulator family
- declared product version: not applicable; Studio fixture only

## CLAIM

At this bounded Android emulator target, a one-time CAMERA grant can remain available while a camera foreground service that was started while visible remains active after HOME; once the app explicitly stops that FGS and backgrounds again, the temporary grant can expire, after which an app-originated permission request is requestable again.

This is not a fixed-timeout claim and is not physical-device/OEM/iOS/product evidence.

## VALIDATION

Run 4 completed terminal success and preserved a run-bound semantic artifact. The verdict is:

`FGS_HELD_THEN_APP_STOPPED_EXPIRED_AND_REQUESTABLE`

Observed timeline:

- fresh app flow obtained the real one-time CAMERA authority; initial PID `2031`;
- camera FGS was active before HOME;
- during the 90-second HOME-background discriminator hold, every 5-second observation from 0.0s through 86.2s retained `granted=True`, PID `2031`, and `service_active=True`;
- at hold completion, permission remained granted and service active;
- Activity was relaunched and the app-owned stop control was exercised;
- the repaired acknowledgement oracle matched `SERVICE:STOP_ACCEPTED` specifically through UIAutomator `content-desc` with empty `text`, directly confirming the run-3 coverage hypothesis for this new execution;
- the independent Android service-state oracle simultaneously observed `service_active=False`;
- after HOME again, permission remained granted through 55.9s with the service absent;
- at 60.9s, permission was revoked, PID was absent, and service remained absent;
- after relaunch, a new app-originated permission request exposed the system dialog again;
- semantic verdict was written and the workflow completed success.

## ROOT CAUSE / regression result for run-3 harness defect

Run 3 established that the acknowledgement verifier was narrower than the fixture's control locator and aborted before service-state collection. Run 4 is the regression evidence for that harness defect:

- `STOP_ACCEPTED` was in fact represented in this execution as `content-desc`, not `text`;
- the repaired `text OR content-desc` oracle recognized it;
- the stronger independent service-state postcondition was collected and showed the FGS absent.

This closes the named run-3 acknowledgement-oracle coverage/ordering defect for this fixture. It does not retroactively prove what happened in run 3 because run 3 did not preserve its stop XML.

## SYNTHESIS

The full bounded causal sequence is now executable evidence rather than documentation-only reasoning:

`one-time authority + visible-started camera FGS → HOME with authority retained through 90s → app-owned FGS stop → HOME without FGS → temporary authority expiry → requestability restored`.

The ordinary-background control previously expired at 60.4s; this run's post-stop branch expired at 60.9s. These are observations in one emulator family, not Android grace-duration contracts. The meaningful result is the state-dependent lifecycle distinction, not the near-equal elapsed samples.

## EVIDENCE LEVEL

**TRANSFER VALIDATION** is awarded to the bounded stop→expiry→requestability subclaim because the prior source/model claim has now survived direct Flutter/Android emulator execution with independent permission, PID, service-state, UI-semantics, and requestability observations.

**REPLICATION is not awarded.** Runs 2–4 use the same Studio fixture/environment family and progressively repaired the same causal path rather than independently reproducing it in a materially different environment.

Mobile Stage 1 remains **NOT PASS**.

## OPEN / VALIDATION

- physical Android/OEM/other API-level replication remains OPEN;
- actual camera resource acquisition/continued capture is outside this permission-authority fixture;
- user revocation while FGS is active remains a separate failure path;
- auto-reset/hibernation remains separate;
- iOS permission/background semantics are not inferred;
- canonical MintTap/LogMate runtime and production evidence are not inferred.

## CHANGE WATCH

Foreground-service types, while-in-use restrictions, permission lifecycle, target-SDK enforcement and Play policy are version-sensitive. Recheck current Android primary documentation before product/release guidance.

## RELATED DOMAIN CHECK

- **Foundations:** process/PID, OS authority and resource-lifetime boundaries materially relevant; semantic state and process/service lifetime remain separate observations.
- **Architecture:** activity visibility, permission authority, UI acknowledgement, process lifetime and FGS lifetime are distinct state dimensions.
- **Mobile:** owning track; this closes the named bounded post-FGS-stop lifecycle boundary.
- **Data:** not materially relevant.
- **Quality:** run 4 provides regression evidence that the repaired oracle can recognize `content-desc` and collect the independent service-state postcondition before semantic classification.
- **Systems:** exact head/run/artifact digest/toolchain identity bind the evidence; CI success is supplementary to the semantic artifact, not its substitute.
- **Design Studio:** no canonical design decision changed. The result supports honest recovery/continuation UX if a future product uses one-time camera/microphone/location plus FGS.
- **Web Manager:** not materially relevant.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no product repository audited; no MintTap/LogMate implementation claim made.

## HANDOFFS

- **Quality:** the run-3 diagnostic defect now has fix/regression evidence: UI acknowledgement appeared via `content-desc`, while independent service state established the actual stop. Preserve control-plane and subsystem-state oracles separately.
- **Systems:** retain artifact `10680900102` and digest as the provenance anchor for the closed bounded lifecycle.
- **Mobile:** do not continue timing permutations on this API-35 emulator family. Return to Balance Loop and prefer a materially different evidence class such as physical/native Android/iOS, Safari/iPadOS/EFB, exact-product runtime/build, or physical storage/connectivity.
