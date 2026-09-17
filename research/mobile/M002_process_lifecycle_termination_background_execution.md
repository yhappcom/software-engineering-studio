# M002 — Process Lifecycle, Termination & Background Execution

Status: **IN STUDY — first integrated source/failure-model block**  
Date: 2026-09-17  
Lead: Mobile

## Problem
Mobile correctness fails when UI/activity/scene lifecycle, process lifetime, suspension, background execution entitlement, transient restoration state, and durable application state are treated as one guarantee. M001 established that Flutter lifecycle callbacks are observations rather than guaranteed persistence hooks. M002 narrows the platform boundary: what Android/iOS actually promise when work leaves the foreground, processes become killable/suspended, and later execution may be a recreation or a fresh launch.

## SOURCE
Primary sources checked 2026-09-17.

### Android
- Android `Activity` API/process-lifecycle documentation states that activity lifecycle and process lifetime differ; under extreme memory pressure the system can kill the application process, and `onSaveInstanceState` is not a universal persistent-data hook.
- The Activity documentation explicitly directs persistent data to a persistence boundary rather than treating saved-instance state as durable application storage.

### Apple UIKit
- `Managing your app’s life cycle` distinguishes per-scene lifecycle from app/process lifecycle. Multiple scenes may occupy different execution states while sharing one process; a background or suspended scene can be disconnected to reclaim resources.
- `About the background execution sequence` shows that apps may be launched directly into the background for supported events, or resumed from suspension, then suspended again.
- `beginBackgroundTask(expirationHandler:)` is a bounded request for additional execution time, not indefinite background execution. The API can fail to grant usable background execution, has finite time, and requires explicit ending; failure to end can terminate the app.
- Apple’s current background-execution guidance states that background runtime is opportunistic/discretionary and system-managed rather than guaranteed.

### Flutter transfer boundary
M001 already established from Flutter `AppLifecycleState` documentation that Flutter may synthesize lifecycle states and applications must not rely on receiving every lifecycle notification. M002 does not promote Flutter’s normalized state vocabulary into Android/iOS process guarantees.

## SYNTHESIS — lifecycle/process model
Use separate state axes:

`UI/activity/scene state`

`process state: running ↔ background-eligible ↔ suspended/not scheduled ↔ terminated`

`work state: not-started → running → checkpointed/committed → complete`

`durable application state: absent/pending/committed/recoverable`

These axes correlate but are not equivalent. In particular:
- `Activity stopped` does not mean `process terminated`;
- `scene disconnected` does not necessarily mean `app process terminated`;
- `background` does not mean `CPU execution guaranteed`;
- `background task requested` does not mean `task completion guaranteed`;
- `process survived` does not mean a specific scene/activity instance survived;
- `process restarted` does not imply transient in-memory work can be reconstructed;
- transient restoration state is not automatically durable domain data.

## FAILURE MODEL — interruption points
For a logical operation that must survive interruption, model at least:

1. mutation accepted in memory;
2. durable checkpoint/commit begins;
3. durable checkpoint/commit completes;
4. optional background continuation requested;
5. process suspended or killed;
6. app/process later launches or resumes;
7. recovery reconstructs terminal application state.

The dangerous interval is any point where user-visible acceptance precedes the durable/recoverable boundary. A lifecycle callback or background-time request can reduce the probability of interruption in a particular flow, but cannot serve as the independent semantic oracle for durability.

## VALIDATION — what is and is not established
No Android emulator/device, iOS simulator/device, Dart SDK, or Flutter SDK is available in the current execution environment. Therefore this block deliberately does **not** claim Android process-death execution, iOS suspension/termination execution, Flutter callback execution, filesystem durability, or background-task scheduling evidence.

Q006 supplies a reusable campaign shape for future transfer:

`exact platform prestate → inject process/lifecycle interruption → relaunch/recreate → inspect durable terminal state → compare against independent application invariant`.

Required future cases include:
- Android activity recreation with process retained;
- Android process death after durable commit vs before durable commit;
- Android saved-instance-state restoration separated from durable domain-data restoration;
- iOS foreground→background→suspension and subsequent resume;
- iOS process termination followed by fresh launch;
- iOS scene disconnection while another scene/process remains alive where supported;
- background task expiration/denial with resumable/checkpointed work;
- exact Flutter mapping on both platforms.

A PASS cannot be awarded from this source/model block.

## ENGINEERING JUDGMENT
Background execution APIs should be treated as constrained scheduling/continuation mechanisms. Correctness-critical operations should define recoverable checkpoints and terminal-state invariants independently of receiving a final lifecycle callback or being granted enough background CPU time.

For long-running work, interruption-safe design generally requires the operation to be restartable, resumable, or idempotent at an application-defined boundary. Which mechanism is appropriate is a Data/Architecture/product decision and is not chosen here.

## CONTRADICTION / INVALID SHORTCUTS
- **“The app entered background, so pending work will finish.”** Rejected by iOS background-runtime constraints and by the general process-lifetime boundary.
- **“Saved instance state is durable business data.”** Rejected as a universal Android persistence rule; restoration state and persistent data have different purposes/lifetimes.
- **“Flutter paused/detached is a guaranteed pre-kill hook.”** Rejected by retained M001 Flutter source evidence.
- **“Scene lifecycle equals process lifecycle on iOS.”** Rejected: scenes have individual lifecycle state while sharing process space.
- **“Requesting background time proves completion.”** Rejected: the request is finite and may not yield enough execution time.

## TRANSFER VALIDATION — LogMate scope
Evidence identity rechecked 2026-09-17:

`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`.

The exact ref remains a Flutter/Dart application and currently documents future local ledger, sync, backup/export work. M002 is therefore a **TRANSFER CANDIDATE** for those durability/recovery features. This study does not establish a current LogMate lifecycle defect and does not assume `main` is production.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F005 process/async boundaries reused; direct Dart/Flutter execution remains OPEN.
- **Architecture:** A002/A003 state ownership and terminal/recovery contracts apply to lifecycle-independent correctness.
- **Mobile:** M001 is the direct prerequisite; M002 adds platform process/background distinctions.
- **Data:** D001/D005/D006 own durability, restore, sync and idempotency semantics; Mobile supplies interruption constraints.
- **Quality:** Q006 fault-point/recovery method is the required future execution shape; no PASS from reading.
- **Systems:** exact build/platform/device identity is required before platform-sensitive evidence is transferable.
- **Design Studio:** interaction/recovery semantics may define what the user expects restored, but no design contract is changed here.
- **Web Manager:** browser/PWA lifecycle is not transferred; M006 remains separate.
- **Marketing Manager:** not materially relevant.
- **Product:** LogMate exact ref checked for relevance only; no product defect inferred.

## OPEN / VALIDATION
- Android emulator/device process-death/recreation campaign.
- iOS simulator/device suspension/termination/background-expiration campaign.
- Direct Dart/Flutter lifecycle execution.
- Durable storage behavior under interruption.
- Exact product persistence/recovery implementation audit once implemented.
- Platform-version/device-specific differences and user force-quit semantics.

## CHANGE WATCH
Android process/background policy, iOS background execution policy, scene lifecycle, and Flutter lifecycle mappings are platform/version-sensitive. Recheck current primary documentation before release-sensitive advice.

## HANDOFFS
- **TO Data:** define durable/recoverable state independently of lifecycle callback arrival; future process-death tests should use Data-owned semantic recovery oracles.
- **TO Quality:** reuse Q006 with real emulator/device fault injection and relaunch, not callback-observation-only tests.
- **TO Architecture:** background work contracts need explicit checkpoint/terminal-state semantics and restart/idempotency policy where interruption is possible.
- **TO Systems:** bind future lifecycle evidence to exact app artifact, OS/device/simulator, build mode and configuration.
- **TO LogMate advisory:** when ledger/sync/backup become implemented, test process death and background expiration against exact implementation refs; do not infer safety from lifecycle callbacks.

## Current conclusion
Android/iOS lifecycle notifications, process lifetime, background execution opportunity, transient restoration state, and durable application state are separate contracts. Background execution can improve continuity but is not a completion guarantee. Correctness under mobile interruption requires a durable/recoverable application boundary plus explicit recovery validation on the actual platform/runtime.