# M003 — Foreground-service discriminator run 3 acknowledgement-oracle isolation

Status: **FAILURE ISOLATED TO ACKNOWLEDGEMENT ORACLE; post-stop semantic boundary remains OPEN**  
Evidence date: 2026-09-22

## Scope and provenance

- repository: `yhappcom/software-engineering-studio`
- exact ref/commit: `5eaa1eeec4e6e99d3236a3e71d9957e544636b00`
- workflow: `.github/workflows/m003-one-time-fgs-discriminator.yml`
- run: `35687049739`
- run conclusion: `failure`
- artifact: `m003-fgs-semantic-evidence`, id `10676369995`
- artifact digest: `sha256:f9441fbb5c0ab81fd8ceb64680929808cc07730783d806ab838cb86f36dbf24a`
- Flutter: `3.47.5`, framework revision `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`
- Dart: `3.13.4 stable`, linux_x64
- target: Android API-35 x86_64 Pixel 6 emulator family
- declared product version: not applicable; Studio fixture only

## VALIDATION / observation

The app-owned-stop target executed through install, real app-originated CAMERA request, real `Only this time` grant, camera foreground-service start while visible, HOME, and another complete 90-second FGS hold. PID `2139`, CAMERA authority, and foreground-service state remained present at every 5-second observation through 85.8s; the 90-second hold completed with `granted=True` and `service_active=True`.

The oracle then relaunched the Activity, confirmed authority and service state before stop, tapped the Flutter `STOP CAMERA FGS` control, and failed one second later with:

`HARNESS_FAILURE:app_owned_stop`

`AssertionError('app-owned stop was not acknowledged')`

No post-stop service-state check or post-stop expiry observation executed because the acknowledgement assertion came first.

## FAILURE ISOLATION

The committed oracle contains an asymmetric UI-semantics contract:

- `tap_label(...)` accepts either Android UIAutomator `text` **or** `content-desc` when locating Flutter controls;
- the later `text_present('SERVICE:STOP_ACCEPTED', ...)` acknowledgement oracle accepts **only** the `text` attribute.

This is a harness defect in oracle coverage: the acknowledgement verifier is narrower than the same fixture's already-used Flutter/Android label locator. Flutter exposes standard widget accessibility through a semantics tree, and platform inspection operates on that semantics representation; therefore a trustworthy acknowledgement oracle must not silently assume that this Flutter `Text` state is represented only as UIAutomator `text`.

This evidence does **not** prove that `STOP_ACCEPTED` was present as `content-desc`, because run 3 did not preserve the `stop_ack.xml` dump. It also does not prove whether `stopService()` succeeded: the oracle aborted before its independent `service_active()` postcondition. Accordingly, the exact app-owned-stop semantic outcome remains OPEN.

## ROOT CAUSE status

**ROOT CAUSE established only for the run-3 diagnostic insufficiency:** the acknowledgement oracle was structurally incapable of recognizing an otherwise matching label exposed only through `content-desc`, and it aborted before the independent service-state postcondition. This explains why the run cannot distinguish UI-representation mismatch from a real stop failure.

**OPEN:** whether this exact run's missing acknowledgement was caused by `content-desc` representation, delayed Flutter rebuild, `stopService()` returning `STOP_NOT_RUNNING`, MethodChannel failure, or another mechanism. The missing XML prevents a stronger causal claim.

## FIX / regression target

The next target should:

1. use one label-presence helper consistent with `tap_label`, accepting `text` or `content-desc`;
2. preserve the matching node attributes (or the UIAutomator dump) in the semantic timeline/artifact;
3. evaluate `service_active()` even if the UI acknowledgement is absent, so UI-state and Android-service-state become independent oracles;
4. classify outcomes separately: acknowledged+stopped, unacknowledged+stopped, acknowledged+still-active, unacknowledged+still-active;
5. continue to post-stop expiry/requestability only when Android service state establishes that the FGS actually stopped.

Do not award post-stop PASS from a UI label alone.

## SYNTHESIS

A control-plane acknowledgement and the controlled subsystem state are distinct evidence dimensions. A UI label can establish what the fixture believes happened; Android service state establishes whether the platform service actually transitioned. Conflating them or ordering the weaker UI assertion before the stronger platform-state observation can destroy diagnostic information.

## OPEN / VALIDATION

- app-owned `stopService()` outcome for run 3 remains OPEN;
- post-FGS-stop expiry/requestability remains OPEN;
- physical/OEM/other-API replication remains OPEN;
- the prior bounded FGS-held-authority TRANSFER VALIDATION remains intact; run 3 independently reproduced the 90-second held branch but is not promoted to independent REPLICATION because it uses the same fixture/environment family.

## RELATED DOMAIN CHECK

- **Foundations:** control acknowledgement and underlying OS resource/service state are separate observable states.
- **Architecture:** UI state, MethodChannel result, Android service lifecycle, permission authority, and process lifetime must remain separate dimensions.
- **Mobile:** owning track; exact post-stop lifecycle remains OPEN.
- **Data:** not materially relevant.
- **Quality:** oracle independence/order is material; a narrow UI assertion prevented collection of the stronger service-state observation.
- **Systems:** exact head/run/artifact/toolchain identity retained; future artifacts should preserve UI dump/node attributes at the failure boundary.
- **Design Studio:** no design decision is changed; Flutter accessibility semantics are used only as a test-observation boundary here.
- **Web Manager:** not materially relevant.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no MintTap/LogMate runtime claim; no product repository audited.

## HANDOFFS

- **Quality:** treat control-plane acknowledgement and subsystem-state postcondition as independent oracles; collect both before aborting where safe.
- **Systems:** preserve the exact UI dump or matched node attributes at UI-driven failure boundaries, not only the assertion message.
- **Mobile:** repair the acknowledgement oracle and classification before continuing post-stop expiry; do not tune the 90-second hold or grace window.
