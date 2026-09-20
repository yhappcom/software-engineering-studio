# M002 — Android Background Lifecycle Transfer

Status: **IN STUDY — EXECUTABLE VALIDATION STARTED / NO PASS YET**  
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

## EXECUTABLE VALIDATION — PENDING
Workflow: `.github/workflows/m002-android-background-lifecycle-validation.yml`  
Initial exact Studio head: `a278de3f2a9015195262b30662b1c240601f336e`  
Target: GitHub-hosted Ubuntu runner + Android Emulator API 35 x86_64 / Pixel 6 profile  
Flutter target: pinned tag `3.47.5`; workflow records exact Flutter checkout and Dart identity.

The fixture exposes two independent observation surfaces:
1. Flutter `WidgetsBindingObserver.didChangeAppLifecycleState` accumulates lifecycle states into visible UI and emits a Flutter log marker.
2. Native `MainActivity` logs `onCreate/onStart/onResume/onPause/onStop` independently.

The fail-fast oracle requires:
- initial launch and non-empty PID;
- HOME background transition;
- same PID remains alive in background;
- relaunch returns with the same PID;
- Flutter UI history contains `paused` and `resumed`;
- native log contains `onPause`, `onStop`, and at least two `onResume` observations;
- natural job completion.

No PASS is awarded until the workflow reaches terminal success and the exact run/job identity is recorded.

## FAILURE MODEL / LIMITS
This fixture can detect missing expected callback/state propagation for the controlled Home/background path and disagreement between Flutter and native lifecycle observation. It does not simulate Android LMK/system-initiated process death, OEM-specific background policy, Doze/app standby, background services/jobs, physical device behavior, iOS, product code, release builds, persistence durability, or production behavior. Same-PID background survival is an oracle for this controlled path, not a guarantee Android must keep background apps alive.

## RELATED DOMAIN CHECK
- **Foundations:** process lifetime and callbacks are distinct mechanisms; callback delivery does not guarantee process survival.
- **Architecture:** lifecycle notifications should not own durable truth or assume guaranteed finalization.
- **Mobile:** M001-M003/M006 checked; this extends M002 with ordinary background/resume rather than repeating force-stop recovery.
- **Data:** no durability claim; persistent state must remain independently protected.
- **Quality:** native callback log and Flutter UI history are separate oracles; natural completion remains required.
- **Systems:** background process priority/resource policy is platform-controlled; no security/release claim.
- **Design Studio:** foreground/background semantics may affect interaction restoration, but no visual/content decision is needed for this mechanism test.
- **Web Manager / Marketing Manager:** not materially relevant to this native lifecycle mechanism.
- **Product source/ref:** no product repository audited; Studio fixture only.

## HANDOFFS
- **Architecture/Data:** do not treat `paused`, `onStop`, or equivalent lifecycle callbacks as a guaranteed final durable-write hook; abrupt termination may skip notifications.
- **Quality:** lifecycle validation should distinguish callback observation from process identity and from persistence/recovery.
- **Mobile:** if this bounded transfer passes, system-initiated process loss remains a separate OPEN class rather than being inferred from Home/background behavior.

## OPEN / CHANGE WATCH
- Workflow terminal result and exact run/job identity are OPEN.
- Android system-initiated kill/LMK, OEM policy, physical device, iOS and product transfer remain OPEN.
- Android lifecycle policy and Flutter lifecycle mapping are version-sensitive; preserve exact SDK/OS identity for later replication.
