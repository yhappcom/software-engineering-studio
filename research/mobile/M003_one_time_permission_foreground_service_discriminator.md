# M003 — One-time permission foreground-service causal discriminator

Status: **IN STUDY — executable discriminator specified; execution pending**  
Evidence date: 2026-09-22

## Problem

The ordinary-background fixture at exact head `ae5597cc15fca07fcc63688a91f1cf8da9ac15f4`, run `35662745671`, observed a real `Only this time` CAMERA grant remain granted through 55.4s after HOME and become revoked at 60.4s, followed by successful re-requestability. That 60.4s value is an observation, not an Android timeout contract.

The next professional boundary is causal rather than another timing sample: does a correctly started camera foreground service materially change the one-time-permission lifecycle when the activity becomes non-visible?

## SOURCE

Android Developers, `Request runtime permissions` / One-time permissions, checked 2026-09-22:

- a one-time location/microphone/camera permission is temporary;
- while the activity is visible, access is available;
- after ordinary backgrounding, access can continue for a short period;
- **if a foreground service is launched while the activity is visible and the user then backgrounds the app, access can continue until the foreground service stops**;
- user revocation still terminates access and the app process regardless of foreground-service use.

Android Developers, `Foreground service types`, checked 2026-09-22:

- API 34+ requires an appropriate declared foreground-service type and type-specific permission;
- a camera FGS requires `android:foregroundServiceType="camera"`, `FOREGROUND_SERVICE_CAMERA`, and a granted CAMERA runtime permission;
- camera is while-in-use restricted; a camera FGS generally must be created while the app is in a valid visible/foreground state rather than first created after backgrounding.

Android Developers, `Restrictions on starting a foreground service from the background`, checked 2026-09-22:

- for target API 34+, the OS checks required while-in-use permission eligibility when creating camera/microphone/location FGS instances;
- background creation can throw `SecurityException`; therefore the fixture must start the service while the activity is visible before HOME.

## SYNTHESIS

One-time authority, activity visibility, process liveness, and foreground-service lifetime are separate state dimensions. The prior ordinary-background observation establishes only one path through that state space. A foreground-service discriminator must preserve the same user-granted authority but intentionally alter the service-lifetime dimension.

## Executable validation contract

### CLAIM
At bounded Android API-35 emulator scope, a camera-type foreground service started while the activity is visible can retain the temporary CAMERA grant after HOME beyond the prior ordinary-background observation point; after that foreground service stops, the temporary grant becomes eligible to expire and later requestability can be re-established.

This does **not** claim a fixed Android grace duration.

### TARGET
Studio-only Flutter fixture, not MintTap or LogMate product code.

### INPUT / STATE
1. Fresh install.
2. Launch visible Flutter activity.
3. App-originated CAMERA request.
4. User/system-dialog interaction chooses `Only this time`.
5. While activity remains visible, app starts a native Android foreground service declared as type `camera`.
6. Verify service entered foreground state and CAMERA authority is granted.
7. Press HOME.
8. Observe authority + process/service state through a bounded hold interval longer than the prior 60.4s observation; this interval is a discriminator observation window, **not a platform timeout assertion**.
9. Stop the foreground service explicitly.
10. Observe bounded post-stop authority transition.
11. If expiry occurs, relaunch and verify a new app-originated request exposes the system permission dialog again.

### ORACLES
Independent observations should include:

- package CAMERA grant state from `dumpsys package`;
- PID/liveness;
- foreground-service presence from Android service/process diagnostics;
- notification/service start success;
- exact elapsed timeline;
- post-stop grant state;
- post-expiry permission-dialog requestability.

Accepted semantic verdicts:

- `FGS_HELD_THEN_EXPIRED_AND_REQUESTABLE` — grant remained while the service was running through the discriminator hold, then expired after stop and was requestable again;
- `INCONCLUSIVE_POST_STOP_WINDOW_EXHAUSTED` — FGS hold was observed but no post-stop expiry occurred within the bounded observation window;
- `CONTRADICTION_REVOKED_WHILE_FGS_ACTIVE` — authority revoked while the correctly started foreground service remained active; requires failure isolation before platform conclusion;
- `HARNESS_FAILURE:<phase>` — setup/oracle/service/dialog/tool failure.

A green CI job is not sufficient by itself; verdict + timeline + toolchain identity must be preserved as a run-bound artifact.

## FAILURE MODEL

The fixture is designed to expose:

- starting the FGS too late, after HOME;
- missing API-34+ service type or foreground-service permission;
- failure to enter actual foreground-service state;
- accidental ordinary-background execution mislabeled as FGS evidence;
- authority revocation while the service is demonstrably active;
- post-stop observation-window exhaustion;
- conflation of package permission flags with service state or actual requestability.

## ALTERNATIVE / CONTROL

The existing ordinary-background artifact is the historical matched control at the same Flutter 3.47.5 / Dart 3.13.4 / API-35 x86_64 Pixel 6 emulator family. It observed revocation at 60.4s without an FGS. The new experiment must not treat 60.4s as a normative threshold; it uses a materially different lifecycle state to test the documented causal distinction.

A stronger later replication would run ordinary-background and FGS variants in the same workflow/image and repeat across another API/OEM/physical device.

## ENGINEERING JUDGMENT

This block has higher value than repeating the already-green ordinary-background fixture because it tests a documented causal branch with direct implications for camera/microphone/location feature design, lifecycle recovery, observability, and permission UX. It also transfers to future products that use user-visible long-running capture/navigation sessions.

## OPEN / VALIDATION

- Executable FGS discriminator run pending.
- Physical Android/OEM and other API versions remain OPEN.
- Actual camera resource acquisition is not yet part of the proposed first discriminator; permission authority/service lifecycle is the bounded target.
- User revocation while FGS is active remains a separate failure path.
- Auto-reset/hibernation remains a distinct lifecycle.
- iOS permission/background semantics are not inferred.

## CHANGE WATCH

Foreground-service types, while-in-use restrictions, launch exemptions, target-SDK enforcement and Play policy are version-sensitive. Recheck current Android documentation before product guidance or release acceptance.

## RELATED DOMAIN CHECK

- **Foundations:** process lifetime and OS authority boundaries materially relevant; prior F006 warns that semantic completion and resource/process completion are distinct.
- **Architecture:** permission authority, activity visibility and service lifetime must remain separate state dimensions.
- **Mobile:** owning track; prior M003 ordinary-background artifact is the direct control evidence.
- **Data:** not materially relevant to this permission-lifecycle discriminator.
- **Quality:** three/four-valued verdict classification and run-bound semantic artifacts required; no PASS from green CI alone.
- **Systems:** FGS declaration/type/permission and exact toolchain/run provenance materially relevant.
- **Design Studio:** recovery/continuation UX may depend on whether a user-visible foreground service intentionally extends access; no Design canonical file edited.
- **Web Manager:** not materially relevant.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no product implementation claim is made; product repos not required for this Studio fixture.

## HANDOFFS

- **Quality:** treat `CONTRADICTION_REVOKED_WHILE_FGS_ACTIVE` as failure observation requiring reproduction/isolation, not immediate Android root cause.
- **Systems:** preserve service type, target SDK, manifest permissions, toolchain and run artifact identity with the verdict.
- **Design Studio:** if later product work uses one-time camera/microphone/location plus FGS, interaction semantics should communicate ongoing user-visible access and recover after authority loss; this note does not redefine Design canonical behavior.
