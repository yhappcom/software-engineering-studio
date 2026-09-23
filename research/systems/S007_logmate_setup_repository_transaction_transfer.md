# S007 — LogMate setup repository transaction transfer

Status: **EXACT-PRODUCT SOURCE TRANSFER; EXECUTABLE VALIDATION OPEN**
Evidence date: 2026-09-24

## Scope

This block narrows the account-required onboarding work to the existing LogMate local repository primitives and asks what minimum persistence change is required for restart-safe Previous Total resolution and setup completion. It does not modify LogMate.

Exact product evidence: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`. Production identity is unknown; default branch is not assumed production.

## SOURCE — existing repository semantics

At the exact ref, `LogbookRepository` already owns three separate durable concepts: `InitialLogbookSetupState`, optional `PreviousTotalBaselineConfiguration`, and owner access. `InitialLogbookSetupState` has only `notStarted`, `inProgress`, and `completed`; its own contract says it is independent of Auth, baseline presence, import activity and aggregate values.

The Sembast adapter persists setup state in `logmate_initial_setup_v1` and baseline in `logmate_baseline_v1`. `beginInitialLogbookSetup()` and `completeInitialLogbookSetup()` each run their own database transaction. `completeInitialLogbookSetup()` can transition any non-completed setup state directly to `completed`; it does not inspect baseline resolution, owner identity, import decision, or any prerequisite milestone.

Baseline configuration is separately transactional and has dedicated rollback fault-injection stages. Its contract atomically couples accepted baseline data, baseline generation and aggregate-checkpoint publication, but not setup completion. Therefore the current repository cannot atomically express `configured baseline + Previous Total resolved + onboarding completed` as one semantic transition.

## CONTRADICTION sharpened

The newer product direction requires Previous Total to be resolved explicitly as either `configured(value)` or `explicitlyNone` before Home. The current model deliberately treats a missing baseline as a valid source state and deliberately keeps setup completion independent from baseline presence. Consequently:

1. `baseline == null` cannot distinguish `not answered yet` from `explicitly no previous total`;
2. `InitialLogbookSetupState.completed` can currently be written without repository-enforced Previous Total resolution;
3. calling baseline configuration and then setup completion creates an interruption window between two transactions;
4. reversing the calls is worse because a crash can expose `completed` before baseline persistence;
5. record count/import presence cannot repair the ambiguity because those are intentionally separate concepts.

This is not evidence that the existing repository is defective under its old contract. It is a **CONTRADICTION between the old persistence contract and the newly required onboarding invariant**.

## ENGINEERING JUDGMENT — minimum delta

Do not overload `PreviousTotalBaselineConfiguration?` nullability and do not infer resolution from aggregate generation. Add one explicit durable Previous Total decision owned by the repository, for example semantic states equivalent to `pending | explicitlyNone | configured`. `configured` must be valid only when a baseline configuration is durably present.

Prefer one repository command/transaction for each user decision:

- `resolvePreviousTotalNone()` atomically records the explicit-negative decision;
- `resolvePreviousTotalWithBaseline(configuration)` atomically records baseline + baseline generation + aggregate publication + resolved decision;
- a separate `completeInitialLogbookSetup()` may remain only if it validates all mandatory semantic prerequisites inside the same transaction before publishing completion.

An alternative is a structured setup record containing milestone fields rather than a new store. That can reduce cross-store state, but it is a broader codec/migration change. Given the app is pre-launch and no production local-only population needs compatibility, compatibility pressure is lower, but schema changes still require deterministic migration/fixture handling because development/test databases and capability contracts exist.

Do not make import-record presence a completion prerequisite. Whether initial import needs an explicit `skipped/notNow` milestone remains a product/UI decision. Previous Total is the currently confirmed mandatory decision and should be modeled independently.

## Invariant contract for Codex

Before Home is routable, a fresh repository read must establish all of:

- authenticated Firebase UID is resolved;
- durable ledger owner exactly matches that UID and is not explicitly locked;
- Previous Total decision is resolved;
- if decision is `configured`, the baseline exists and passes its stored-anchor/integrity validation;
- setup completion is durably committed only after mandatory prerequisites;
- no inference is made from record count, null baseline, Auth alone, route/widget state, or an async write that has merely started.

The repository should reject an attempt to complete setup while Previous Total is pending. This moves the invariant into the persistence authority rather than relying only on UI sequencing.

## Failure-first executable validation required

Add deterministic repository tests/fault injection for:

1. completion attempted while Previous Total pending → rejected, state unchanged;
2. explicit-none decision → restart/reopen → remains resolved without synthetic zero baseline;
3. baseline decision failure after baseline write but before generation/checkpoint/decision publication → entire transaction rolls back;
4. duplicate baseline resolution → idempotent same semantic result or explicit conflict, never duplicate generation advancement;
5. configured decision with missing/corrupt baseline → fail closed;
6. crash/reopen after Previous Total resolution but before setup completion → resume at the next unresolved semantic milestone;
7. setup-completion write failure → Home remains unavailable;
8. wrong UID/locked owner → cannot resolve or complete onboarding;
9. repeated startup/provider callback → no duplicate owner or setup mutation.

The existing `SembastBaselineFailurePoint` mechanism is a useful pattern but does not itself validate the new decision transaction. Add a new failure point only where it discriminates rollback at the newly introduced semantic boundary.

## ALTERNATIVES

**A — infer from nullable baseline:** reject. Cannot represent explicit none versus unanswered.

**B — keep three-state setup only and trust UI ordering:** reject for durable correctness. A second caller, crash, future UI refactor or duplicated callback can bypass the intended sequence.

**C — explicit Previous Total decision + repository prerequisite enforcement:** preferred minimum delta. Preserves existing separation of baseline data from setup lifecycle while making the new invariant executable.

**D — replace setup enum with a richer aggregate onboarding record:** viable if onboarding will soon gain multiple mandatory milestones, but broader schema/codec/migration surface should be justified by confirmed product requirements rather than anticipated screens.

## RELATED DOMAIN CHECK

- Foundations: no new execution-model prerequisite; direct Dart/Flutter evidence already exists.
- Architecture: identity, owner access, baseline data, Previous Total decision and setup completion remain separate concepts; repository owns durable invariant enforcement.
- Mobile: restart/process-death semantics motivate persistence but no new platform claim is made.
- Data: primary supporting domain; transaction atomicity and explicit-negative representation are central.
- Quality: failure injection/reopen and invalid-transition tests are required before PASS.
- Systems: owns the Auth/owner/onboarding security boundary and fail-closed Home routing.
- Design Studio: screen composition must not become persistence identity; explicit `No previous total` remains a semantic action.
- Web Manager: not materially relevant to this repository transaction block.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref inspected read-only; no product canonical files edited.

## HANDOFFS

- **LogMate / Codex:** implement an explicit Previous Total resolution state and enforce completion prerequisites in repository authority; do not infer from nullable baseline or UI flow.
- **Data:** review the chosen store/structured-state representation and atomic baseline+decision transaction, including codec/schema migration behavior.
- **Quality:** execute rollback, restart/reopen, duplicate-submit, invalid-transition and wrong-owner tests with independent state reads.
- **Architecture:** keep the minimal delta unless confirmed onboarding requirements justify a richer aggregate state machine.

## OPEN / VALIDATION

- OPEN: exact representation (`decision` store versus richer setup record) is an implementation choice pending product/Codex change design.
- OPEN: whether optional initial import needs a durable initial-decision milestone.
- OPEN: exact capability/schema migration delta and development-database handling.
- VALIDATION: no exact LogMate runtime/repository tests were executed in this block; source inspection does not award PASS.
