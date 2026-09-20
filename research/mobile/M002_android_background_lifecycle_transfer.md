# M002 — Android Background Lifecycle Transfer

Status: **BOUNDED TRANSFER VALIDATED**  
Evidence date: 2026-09-21

## Problem / scope
M002 already validates controlled `am force-stop` plus persistent-file recovery, but that does not establish ordinary foreground → background → foreground lifecycle delivery while the process remains alive. This block tests a materially different boundary: Android Activity callbacks and Flutter lifecycle observations during Home/background and return-to-foreground on an API-35 emulator.

## SOURCE
Rechecked 2026-09-21:
- Android process/lifecycle guidance states that non-visible/background processes are lower priority and may be killed; work after an Activity enters a cached state is not reliable. https://developer.android.com/guide/components/processes-and-threads and https://developer.android.com/topic/performance/memory-management
- Android Activity documentation ties killability to lifecycle state and warns that persistent data must not depend on every lifecycle callback being delivered. https://developer.android.com/reference/android/app/Activity
- Flutter `AppLifecycleState` documents Android mapping (`onPause` → inactive, `onStop` → paused), synthesized `hidden`, and explicitly warns that applications must not rely on receiving every possible notification before abrupt termination. https://api.flutter.dev/flutter/dart-ui/AppLifecycleState.html

## SYNTHESIS
Foreground/background lifecycle callbacks are useful coordination signals, not a durability or guaranteed-finalization protocol. A valid mobile architecture must tolerate skipped callbacks and process loss independently of ordinary background/resume delivery.

## EXECUTABLE VALIDATION — PASS
Workflow: `.github/workflows/m002-android-background-lifecycle-validation.yml`  
Exact Studio head: `a278de3f2a9015195262b30662b1c240601f336e`  
Run: `35529237932`  
Job: `106126775150` (`android-background-lifecycle`)  
Terminal result: **success**, 2026-09-20T18:34:52Z  
Target: GitHub-hosted Ubuntu runner + Android Emulator API 35 x86_64 / Pixel 6 profile  
Flutter target: pinned tag `3.47.5`; workflow records exact Flutter checkout and Dart identity. The retrievable job metadata confirms the identity-recording step succeeded, but does not expose its stdout, so no unobserved Dart/Flutter commit output is invented.

The fixture exposes two independent observation surfaces:
1. Flutter `WidgetsBindingObserver.didChangeAppLifecycleState` accumulates lifecycle states into visible UI.
2. Native `MainActivity` independently logs `onCreate/onStart/onResume/onPause/onStop`.

The fail-fast oracle requires:
- initial launch and non-empty PID;
- HOME background transition;
- same PID remains alive in background;
- relaunch returns with the same PID;
- Flutter UI history contains `paused` and `resumed`;
- native log contains `onPause`, `onStop`, and at least two `onResume` observations;
- natural job completion.

The workflow job metadata shows `Execute Android background lifecycle oracle` completed successfully and the job reached `Complete job` successfully. Because the oracle script is fail-fast (`set -euo pipefail`) and every predicate above precedes its PASS marker, this is executable evidence for the bounded controlled HOME/background/resume claim.

## TRANSFER VALIDATION
**PASS — bounded API-35 emulator transfer.** The same live Flutter application process crossed foreground → HOME/background → foreground while Flutter lifecycle state and native Activity callbacks independently satisfied the expected transition predicates. This transfers lifecycle-model knowledge into an Android/Flutter runtime context; it does not transfer process-retention guarantees.

## FAILURE MODEL / LIMITS
This fixture can detect missing expected callback/state propagation for the controlled Home/background path and disagreement between Flutter and native lifecycle observation. It does not simulate Android LMK/system-initiated process death, OEM-specific background policy, Doze/app standby, background services/jobs, physical device behavior, iOS, product code, release builds, persistence durability, or production behavior. Same-PID background survival is an observation for this controlled path, not a guarantee Android must keep background apps alive.

## RELATED DOMAIN CHECK
- **Foundations:** process lifetime and callbacks are distinct mechanisms; callback delivery does not guarantee process survival.
- **Architecture:** lifecycle notifications should not own durable truth or assume guaranteed finalization.
- **Mobile:** M001-M003/M006 checked; this extends M002 with ordinary background/resume rather than repeating force-stop recovery.
- **Data:** no durability claim; persistent state must remain independently protected.
- **Quality:** native callback log and Flutter UI history are separate oracles; PID continuity and natural completion are additional evidence surfaces.
- **Systems:** background process priority/resource policy is platform-controlled; no security/release claim.
- **Design Studio:** foreground/background semantics may affect interaction restoration, but no visual/content decision is needed for this mechanism test.
- **Web Manager / Marketing Manager:** not materially relevant to this native lifecycle mechanism.
- **Product source/ref:** no product repository audited; Studio fixture only.

## HANDOFFS
- **Architecture/Data:** confirmed bounded ordinary lifecycle delivery does not convert `paused`, `onStop`, or equivalent callbacks into guaranteed durable-write hooks; abrupt termination remains a separate failure class.
- **Quality:** lifecycle validation should distinguish callback observation, process identity, persistence/recovery and natural executable completion.
- **Mobile:** controlled HOME/background/resume is now validated; system-initiated process loss remains a separate OPEN class rather than being inferred from this result.

## OPEN / CHANGE WATCH
- Android system-initiated kill/LMK, OEM policy, physical device, iOS and product transfer remain OPEN.
- User-dialog/one-time/auto-reset permissions, secure storage and broader native/plugin behavior remain OPEN elsewhere in Mobile Stage 1.
- Android lifecycle policy and Flutter lifecycle mapping are version-sensitive; preserve exact SDK/OS identity for later replication.
- Replication should preserve or strengthen exact toolchain provenance; do not infer unexposed command stdout from a green identity-recording step.
