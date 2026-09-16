# M001 — Flutter Runtime, Widget/Render/State, Lifecycle & Platform Boundary

Status: **IN STUDY — first integrated Foundation block**  
Date: 2026-09-16  
Lead: Mobile

## Problem
Flutter makes one application codebase span multiple platforms, but it does not collapse framework, engine, embedder, OS lifecycle, process lifetime, persistent state, and UI configuration into one boundary. Product code becomes unreliable when these are treated as interchangeable.

## SOURCE
Primary sources checked 2026-09-16:

1. Flutter architectural overview — https://docs.flutter.dev/resources/architectural-overview
   - Flutter is layered: Dart framework → engine → platform-specific embedder/runner → OS.
   - Widgets are immutable UI configuration; a persistent element tree mediates widget configuration and render objects.
   - `StatefulWidget` stores mutable UI state in a separate `State` object.
   - `build()` maps state to UI and should be free of side effects because the framework may call it whenever needed.
   - render objects perform layout/painting; widget, element and render-object trees are distinct concepts.
2. Flutter `AppLifecycleState` API — https://api.flutter.dev/flutter/dart-ui/AppLifecycleState.html
   - Flutter synthesizes unsupported lifecycle states so implementations share a state machine, but names do not map one-to-one to every platform.
   - applications must not rely on receiving every lifecycle notification; abrupt termination can skip notifications.
3. Flutter `AppLifecycleListener` / `WidgetsBindingObserver` API — lifecycle state is exposed through framework notifications sourced from the platform lifecycle channel.
4. Android `Activity` lifecycle / process documentation — https://developer.android.com/reference/android/app/Activity and https://developer.android.com/guide/components/processes-and-threads
   - Activity instance lifecycle and hosting process lifetime are distinct; a process may be killed without another Activity callback.
5. Apple UIKit app lifecycle — https://developer.apple.com/documentation/uikit/managing-your-app-s-life-cycle
   - foreground/background/suspended execution changes resource permissions/expectations; scene lifecycle can differ per scene and multiple scenes share one process.
6. Dart overview — https://dart.dev/overview
   - native development uses Dart VM/JIT while production native deployment can use AOT machine code; web compilation targets JavaScript or WebAssembly.

## SYNTHESIS — boundary model
Do not reason about a Flutter app as one lifecycle or one tree.

### Execution layers
`app Dart code → Flutter framework → dart:ui/engine → platform embedder/runner → OS process/platform services`

A framework API can normalize an event vocabulary without turning it into an OS guarantee.

### UI/state layers
- **Widget:** immutable configuration/description.
- **Element:** persistent location/association that allows configuration replacement while retaining framework identity/state relationships.
- **State:** mutable UI-associated state for a `StatefulWidget`; it is not automatically durable application data.
- **RenderObject:** layout/painting/hit-testing/accessibility mechanics where applicable.

Therefore these shortcuts are invalid:
- widget object identity = durable state identity;
- `setState()` = data persistence;
- rebuild = process restart;
- lifecycle callback = guaranteed pre-termination hook;
- Flutter lifecycle vocabulary = one-to-one Android/iOS lifecycle mapping.

## EXECUTABLE MODEL VALIDATION — lifecycle notification gap
Fixture: `research/mobile/fixtures/M001_lifecycle_notification_gap.py`

This fixture is deliberately a **model test, not Flutter/platform runtime evidence**.

### Test Evidence Contract
- **CLAIM:** correctness that depends solely on receiving a later lifecycle callback has an uncovered failure path if abrupt termination can skip that callback.
- **SPEC/PROPERTY:** a user edit intended to survive termination must reach the modeled commit boundary before termination.
- **TARGET:** two application policies: save only on modeled `paused` notification vs commit at semantic mutation boundary.
- **INPUT/STATE:** edit `flight-123`; compare normal `resumed → inactive → hidden → paused → terminated` with abrupt `resumed → terminated`.
- **ORACLE:** modeled durable value after termination must equal `flight-123`.
- **ENVIRONMENT:** Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41.
- **OBSERVATION:** save-on-paused preserved the edit on the normal sequence but lost it when termination occurred before `paused`; commit-at-mutation preserved the modeled value in both sequences.
- **VERDICT:** lifecycle-notification arrival cannot be the sole correctness guarantee for data that must survive abrupt termination.
- **FAILURE MODEL:** skipped lifecycle callback before termination.
- **EVIDENCE LIMIT:** this does not validate Flutter callbacks, Android/iOS timing, filesystem durability, power-loss survival, database transactions, or the correct product commit frequency. The alternative only demonstrates moving correctness away from a callback whose arrival is not guaranteed.

### ROOT CAUSE
The failing policy confuses a **notification opportunity** with a **commit guarantee**. Once the notification is skipped, no remaining mechanism satisfies the persistence property.

## ENGINEERING JUDGMENT
Lifecycle callbacks are useful for resource adaptation, refresh, throttling, best-effort flushing and state transitions, but critical data integrity should be specified against an explicit application/data commit contract. The exact persistence mechanism and timing belong with Data/Mobile product design and must account for performance, atomicity and platform storage behavior.

Likewise, `build()` should describe UI from current state rather than own durable mutations or side effects merely because rebuilds are convenient execution points.

## TRANSFER VALIDATION — LogMate scope only
Evidence identity:

`yhappcom/logmate → main commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-16`

The exact `pubspec.yaml` declares Flutter and Dart SDK `^3.10.7`. This establishes that the model is materially relevant to LogMate's technology stack. It does **not** establish that LogMate currently has a lifecycle/persistence defect. No such product claim is made here.

Future LogMate ledger/backup work should preserve the distinction between widget/UI state, application state, local durable commit, sync state and backup state already identified by D001. Product implementation must be audited at the exact working/production ref when those features exist.

## RELATED DOMAIN CHECK
- **Foundations:** F001 layered runtime model reused. Direct Dart JIT/AOT and Flutter runtime execution remain OPEN because the current execution environment has no `dart` or `flutter` executable.
- **Architecture:** A001-A003 reused: UI/runtime boundaries need explicit ownership and semantic contracts rather than pattern names.
- **Data:** D001 directly constrains the meaning of durable application state; `setState`/lifecycle state cannot substitute for persistence semantics.
- **Quality:** Q001 Test Evidence Contract used; future lifecycle tests need exact platform/device/build/prestate and process-death oracles.
- **Systems:** S001 requires build/artifact/runtime identity separation for platform-sensitive evidence.
- **Design Studio:** interaction state semantics can define what must appear preserved/restored, but no design-owned contract is changed in this generic block.
- **Web Manager:** PWA/browser lifecycle is materially different and belongs to M006/Web transfer; no native lifecycle conclusion is transferred to browser behavior here.
- **Marketing Manager:** not materially relevant to this block.
- **Product:** LogMate exact ref checked only for stack relevance; no implementation defect inferred.

## CONTRADICTION / INVALID SHORTCUTS
1. **“Flutter lifecycle states are the platform lifecycle.”** Rejected: Flutter documents synthesized states and non-1:1 platform naming.
2. **“paused/detached will always run before termination.”** Rejected: Flutter explicitly says applications should not rely on all notifications being delivered.
3. **“StatefulWidget state is persistent application state.”** Rejected: framework `State` is UI lifecycle state; durability is a separate data/storage contract.
4. **“One Flutter abstraction proves Android/iOS behavior is identical.”** Rejected: framework normalization does not erase platform process/background/scene constraints.

## OPEN / VALIDATION
- Direct Dart JIT/AOT execution and Flutter debug/profile/release execution remain OPEN with F001.
- Real Flutter widget/element/state lifecycle execution is OPEN.
- Android process-death/recreation validation is OPEN for M002.
- iOS scene/background/suspension/termination validation is OPEN for M002.
- Platform-channel/plugin failure boundary is OPEN for M004.
- Native vs PWA lifecycle/deployment transfer is OPEN for M006.
- Product-level persistence/lifecycle behavior must not be inferred until exact implementation refs are audited.

## CHANGE WATCH
- Flutter engine/threading details are version-sensitive. The current architecture documentation notes Android/iOS UI/platform thread merging as of Flutter 3.29; recheck before runtime/performance claims.
- Android/iOS lifecycle/background policies and Flutter lifecycle mappings require current platform/framework verification when used for a release decision.

## HANDOFFS
- **TO Data:** durable commit must not depend solely on a lifecycle callback whose delivery is not guaranteed; define commit/recovery semantics independently.
- **TO Quality:** lifecycle tests need skipped-callback/process-death cases, not only orderly background/foreground transitions.
- **TO Architecture:** distinguish UI configuration/state ownership from durable domain/data ownership.
- **TO Systems:** record exact Flutter/Dart/build/platform identity for runtime evidence; framework normalization is not a platform guarantee.
- **TO LogMate project (advisory only):** when local ledger is implemented, do not use `paused`/`detached` as the sole persistence boundary for user-entered flight data.

## Current conclusion
Flutter should be reasoned about as a layered runtime plus several distinct state/lifecycle structures. Widgets describe UI; elements preserve framework identity relationships; `State` is mutable UI-associated state; render objects implement rendering mechanics; platform lifecycle notifications are observations/opportunities rather than guaranteed durable-commit hooks. Cross-platform API normalization reduces application branching but does not erase Android/iOS process, lifecycle or storage semantics.
