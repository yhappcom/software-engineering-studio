# M003 — Foreground-service discriminator run 2 evidence

Status: **BOUNDED TRANSFER VALIDATION for FGS-held authority; post-stop boundary OPEN due harness stop failure**  
Evidence date: 2026-09-22

## Scope and provenance

- repository: `yhappcom/software-engineering-studio`
- exact ref/commit: `3d948ef0c3cf63500aa840eebf0591d0df54c1bd`
- workflow: `.github/workflows/m003-one-time-fgs-discriminator.yml`
- run: `35679723145`
- job: `106593845398`
- terminal job conclusion: `failure`
- artifact: `m003-fgs-semantic-evidence`, id `10674236432`
- artifact digest: `sha256:1c78cf8c7ac179fe1868477f58bb18bc2ed403c6f77d070356ef158b8705dfc5`
- Flutter: `3.47.5`, framework revision `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`
- Dart: `3.13.4 stable`, linux_x64
- target environment: Android API-35 x86_64 Pixel 6 emulator family
- declared product version: not applicable; Studio-only fixture, not MintTap/LogMate

## VALIDATION — new semantic observation

The repaired oracle passed its new `python3 -m py_compile` preflight and executed far enough to produce a complete semantic timeline through the FGS hold.

After a real app-originated CAMERA request and user/system-dialog `Only this time` grant:

- initial app PID was `2186`;
- camera foreground service was confirmed active before HOME;
- after HOME, package CAMERA authority remained granted, PID remained `2186`, and `CameraForegroundService` remained foreground-active at every 5-second observation from 0.0s through 85.5s;
- the 90-second hold completed with `granted=True` and `service_active=True`.

The matched historical ordinary-background M003 observation in the same Flutter 3.47.5 / Dart 3.13.4 / API-35 emulator family observed authority loss and process disappearance at 60.4s after HOME without a foreground service. That 60.4s remains an observation, not a portable Android timeout contract.

## TRANSFER VALIDATION

**Awarded, bounded claim only:** in this exact API-35 emulator fixture, a camera-type foreground service started while the activity was visible preserved the one-time CAMERA authority and process/service liveness through a 90-second HOME-background hold. This materially transfers the prior ordinary-background lifecycle finding into the documented foreground-service branch and survives beyond the prior control observation point.

This does **not** establish a fixed minimum/maximum Android duration, physical-device/OEM behavior, another API level, actual camera-resource acquisition, product behavior, or production behavior. It is not independent REPLICATION.

## FAILURE / ROOT-CAUSE BOUNDARY

After the successful 90-second FGS hold, the oracle entered `stop_fgs` and produced `HARNESS_FAILURE:stop_fgs`. The final CI gate therefore correctly failed. The artifact proves that the failure occurred after the causal hold observation and before post-stop expiry observation.

The exact oracle used `adb shell am stopservice -n dev.yhapp.studio.m003_fgs/.CameraForegroundService` followed by a check that the service was no longer active. The artifact does not preserve stderr/exception text from that command, so the precise stop failure mechanism is **OPEN**. Do not label this an Android semantic contradiction or claim post-stop behavior from this run.

## CONTRADICTION

None established. Authority did not revoke while the correctly observed foreground service remained active. The run failed at the harness-controlled explicit-stop transition, not at the FGS-held authority claim.

## SYNTHESIS

A terminal-red workflow can still contain valid bounded evidence for a completed earlier subclaim when the run-bound artifact establishes the observation sequence and the later failure boundary precisely. Conversely, the later post-stop claim remains unvalidated. Verdicts must therefore be scoped to the claim boundary rather than inherited mechanically from the overall CI conclusion.

## ENGINEERING JUDGMENT

The next work should isolate the explicit-stop mechanism, not repeat the 90-second hold merely to accumulate another green run. A trustworthy repair should use an app-owned stop path with observable acknowledgement (for example, an explicit fixture control that invokes `stopService`/`stopSelf` and emits state evidence) rather than assuming shell `am stopservice` is a production-equivalent control. Preserve command stderr/return code in the next artifact before selecting the repair so root cause is not guessed.

## OPEN / VALIDATION

- exact root cause of `HARNESS_FAILURE:stop_fgs` remains OPEN because command stderr/traceback is absent from the artifact;
- explicit service-stop acknowledgement and post-stop bounded expiry remain OPEN;
- post-expiry permission-dialog requestability for the FGS branch remains OPEN;
- physical Android/OEM/other API independent REPLICATION remains OPEN;
- actual camera resource use, user revocation while FGS active, auto-reset/hibernation, iOS, and product runtime remain OPEN.

## RELATED DOMAIN CHECK

- **Foundations:** process/authority lifetime distinction remains material; PID stayed stable while FGS authority was held.
- **Architecture:** activity visibility, temporary permission authority, process lifetime, and FGS lifetime remain independent state dimensions.
- **Mobile:** owning track; this run closes only the FGS-held-authority sub-boundary.
- **Data:** not materially relevant to this permission lifecycle block.
- **Quality:** terminal workflow conclusion must not erase earlier artifact-proven subclaim evidence; later failure must not be allowed to validate an unexecuted post-stop claim.
- **Systems:** exact head/run/artifact/toolchain provenance is required; preserve stderr/return code for the next stop-path isolation.
- **Design Studio:** ongoing user-visible access semantics may depend on FGS continuation; no Design Studio canonical file edited.
- **Web Manager:** not materially relevant.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no product claim; no product repository audited in this block.

## HANDOFFS

- **Quality:** add the reusable rule that a red run may still validate a completed bounded subclaim only when artifact evidence establishes the subclaim and later failure boundary; never promote unexecuted downstream claims.
- **Systems:** next stop-path run should preserve subprocess return code/stderr plus service diagnostics before and after the stop request.
- **Mobile:** do not rerun the 90-second hold as the primary objective; isolate and repair the explicit-stop transition, then continue post-stop expiry/requestability.
