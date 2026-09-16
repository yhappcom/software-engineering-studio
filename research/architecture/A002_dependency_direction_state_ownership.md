# A002 — Dependency Direction, State Ownership & Derived Projections

Status: **IN STUDY — first integrated block**
Date: 2026-09-16
Lead: Architecture

## Problem
A layered diagram does not establish sound dependency direction. The practical questions are: who owns authoritative state, who may mutate it, which components merely derive/project it, and what dependency structure keeps those rules enforceable as the application grows?

## SOURCE
David L. Parnas, *Designing Software for Ease of Extension and Contraction*, IEEE Transactions on Software Engineering SE-5(2), 1979, treats design for extension/contraction as design for change and identifies the software `uses` relation as a critical structure. A uses B when correct execution of B may be necessary for A to satisfy its specification; this is not identical to merely invoking B.

This extends A001: information hiding asks which knowledge a module owns; the uses/dependency structure asks which lower capabilities must remain correct/available for another component to fulfill its contract.

## SYNTHESIS
### 1. Call direction, data-flow direction and dependency direction are not synonyms
A UI can call an application operation, while the implementation of that operation depends on an authority contract implemented by persistence code. Runtime calls alone do not determine architectural ownership.

### 2. State ownership has three separate questions
For any important state identify:
- **authority:** which state defines truth when copies disagree?
- **mutation authority:** which operation/component is allowed to commit changes to that truth?
- **projection/cache ownership:** which components may hold derived copies, and how are they invalidated/rebuilt?

A cache/projection may be a legitimate copy without becoming a second writer.

### 3. Dependency direction should protect policy and invariants
A useful direction is one that lets high-value semantic policy specify what it needs without forcing it to know volatile UI/storage/vendor representation. This does not imply a universal `domain → repository interface → adapter` template. A001 still applies: every boundary must earn its indirection.

### 4. Multiple writers require explicit reconciliation, not wishful consistency
If two components can independently mutate semantically equivalent state, the architecture has either:
- intentionally created multiple authorities and therefore needs ordering/conflict/reconciliation semantics; or
- accidentally created an inconsistent system.

For ordinary derived totals/search indexes/UI projections, independent mutation is normally the latter.

## EXECUTABLE VALIDATION
Fixture: `research/architecture/fixtures/A002_state_ownership.py`

Environment: Python 3.13.5 / Linux execution environment, 2026-09-16.

### Test Evidence Contract
- **CLAIM:** a derived projection that is independently writable can diverge from authoritative state even when both components individually behave as coded; routing mutation through one authority plus revision-based invalidation prevents that bounded inconsistency.
- **SPEC/PROPERTY:** total block minutes must equal the sum of authoritative Flight rows; a projection whose revision differs from authority must not be accepted as current.
- **TARGET:** in-memory Ledger authority + derived total Projection.
- **INPUT/STATE:** flights A=60, B=90; attempted edit A→120.
- **ORACLE:** independently sum Ledger rows and compare with Projection; stale revision must raise before refresh.
- **OBSERVATION:** direct projection mutation reported 210 while Ledger remained 150. Rebuilding the projection from authority reverted the unauthorized write to 150. Routing the edit through Ledger incremented its revision, caused stale projection rejection, then refresh produced 210 in both authority-derived calculation and projection.
- **VERDICT:** the deliberate second-writer path reproduced inconsistency/lost derived mutation; the single-authority path preserved the bounded invariant.
- **ROOT CAUSE:** the bad path changed a derived representation while bypassing the mutation authority, creating two incompatible meanings of “current”.
- **EVIDENCE LIMIT:** in-memory synchronous fixture only. It does not establish database transaction, Flutter state-management, multi-process, network sync, concurrent-writer, crash, or mobile lifecycle behavior.

## CONTRADICTION / FAILURE LESSON
The failure did not require threads, networking, or a database. Architectural inconsistency can arise simply because two components are allowed to act as writers for one semantic fact. Therefore “single source of truth” is not a database slogan; it is an enforceable mutation/reconciliation contract.

## ALTERNATIVES
1. **Single authority + rebuildable projection** — simplest when derived state is cheap enough and one writer is intended.
2. **Single authority + incremental projection with revision/event tracking** — useful when recomputation is expensive; requires stronger invalidation/event correctness.
3. **Intentional multi-writer state** — legitimate for sync/local-first systems, but must define identity, ordering, conflict, merge and durability semantics; belongs later with D006 rather than being smuggled into UI architecture.

## ENGINEERING JUDGMENT
Do not select dependency direction by visual layer purity. Select it so that important invariants and mutation authority can be stated and tested without volatile mechanisms becoming co-owners of semantic state.

## TRANSFER TO LOGMATE
Prior exact-ref evidence remains:
`yhappcom/logmate → b551ce434ad72b1895033e0f3617c73b026d40ea → app 1.0.0+1 → evidence date 2026-09-16`.

At that ref local ledger/persistence and canonical FlightRecord/calculation linkage were not implemented. Therefore this study makes no product implementation claim. It supplies a constraint for future design: UI session state, derived monthly/yearly totals, search indexes, import preview and future sync state must not silently become independent authorities for canonical flight records. Exact-ref transfer must be repeated when ledger implementation exists.

## RELATED DOMAIN CHECK
- **Foundations:** F001 distinguishes process/runtime boundaries from application dependency boundaries. Dart/Flutter executable gap remains OPEN.
- **Architecture:** A001 supplies the rule that a boundary must hide/own something real; A002 adds authority and dependency structure.
- **Data:** D001 supplies logical SSOT, commit and durability distinctions. A002 intentionally does not claim persistence durability.
- **Quality:** Q001 Test Evidence Contract used; oracle independently derives total from authority rather than trusting projection logic.
- **Mobile:** Flutter widget/provider/state-container choices are not architectural authorities by default; runtime validation remains for M001/M002.
- **Systems:** security/trust/performance may constrain who may mutate state; not materially validated in this fixture.
- **Design Studio:** user-facing saved/synced/recovery semantics may require distinct projections but must map to engineering authority states; no design canonical file changed.
- **Web Manager / Marketing Manager:** not materially relevant to this foundation mechanism.
- **Product source:** LogMate prior exact ref reused only as timing/context; no new code behavior inferred.

## HANDOFFS
- **TO Data:** D002–D006 should preserve the distinction between mutation authority and derived copies; intentional multi-writer designs must define reconciliation explicitly.
- **TO Quality:** future tests should deliberately mutate/bypass projections and verify rebuild/invalidation rather than only testing happy-path state updates.
- **TO Mobile:** compare Flutter state containers by lifecycle/ownership semantics, not by treating provider/store objects automatically as sources of truth.
- **TO LogMate project:** before implementing the ledger, name canonical FlightRecord mutation authority and classify totals/search/import-preview/sync metadata as authoritative, derived, or staged state.

## OPEN / VALIDATION
- Add a materially different dependency structure comparison, not just second-writer failure.
- Study dependency inversion/interface placement without assuming Clean Architecture vocabulary.
- Add concurrency/event-order failure only after F004/F005/D006 prerequisites.
- Repeat exact-ref LogMate transfer after real ledger/persistence code exists.

## Current conclusion
State architecture becomes defensible when every important datum has an explicit authority, every mutation path is intentional, derived copies have invalidation/rebuild semantics, and dependency direction protects those contracts. A diagram or state-management library does not establish these properties by itself.
