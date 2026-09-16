# A002 — Dependency Direction, State Ownership & Derived Projections

Status: **IN STUDY — ownership failure + dependency-structure alternative evidence complete**
Date: 2026-09-16
Lead: Architecture

## Problem
A layered diagram does not establish sound dependency direction. The practical questions are: who owns authoritative state, who may mutate it, which components merely derive/project it, and what dependency structure keeps semantic policy stable when mechanisms change?

## SOURCE
David L. Parnas, *Designing Software for Ease of Extension and Contraction*, IEEE TSE SE-5(2), 1979, treats the software `uses` relation as a critical structure: A uses B when correct execution of B may be necessary for A to satisfy its specification; this is not identical to merely invoking B.

Robert C. Martin, *The Dependency Inversion Principle*, C++ Report, 1996, states the later object-oriented formulation that high-level modules should not depend on low-level modules and that abstractions should not depend on details. The primary paper was checked via the University of Texas hosted PDF on 2026-09-16. A002 treats this as a candidate structural technique, not a universal requirement to add interfaces.

## SYNTHESIS
### 1. Call direction, data-flow direction and architectural dependency are not synonyms
Runtime invocation does not by itself establish which policy should know which mechanism. A high-level semantic operation may call through a contract whose implementation performs low-level I/O; source dependency can still point from the detail toward the policy-owned contract.

### 2. State ownership has three separate questions
For important state identify:
- **authority:** which state defines truth when copies disagree?
- **mutation authority:** which operation/component may commit changes?
- **projection/cache ownership:** which components hold derived copies, and how are they invalidated/rebuilt?

A projection can be a legitimate copy without being a second writer.

### 3. Dependency inversion is valuable when it protects a semantic policy from a volatile mechanism
The important inversion is not "add an interface". It is that the stable semantic need defines the contract it requires, while the volatile detail adapts to that contract. If no independently varying mechanism/policy exists, A001's over-abstraction counterexample still applies.

### 4. Multiple writers require explicit reconciliation
If two components independently mutate semantically equivalent state, the architecture either intentionally created multiple authorities and needs ordering/conflict/reconciliation semantics, or accidentally created inconsistency.

## EXECUTABLE VALIDATION A — second-writer ownership failure
Fixture: `research/architecture/fixtures/A002_state_ownership.py`

Environment: Python 3.13.5 / Linux, 2026-09-16.

- **CLAIM:** a derived projection that is independently writable can diverge from authoritative state; one mutation authority plus revision invalidation prevents that bounded inconsistency.
- **SPEC/PROPERTY:** total block minutes equals authoritative Flight rows; stale projection revision is not current.
- **INPUT:** A=60, B=90; attempted A→120.
- **ORACLE:** independently sum Ledger rows and compare with Projection.
- **OBSERVATION:** direct projection mutation reported 210 while Ledger remained 150; rebuild erased the unauthorized write and restored 150. Routing A→120 through Ledger incremented revision, stale projection read failed, refresh restored consistent 210.
- **ROOT CAUSE:** derived representation acted as a second mutation authority.
- **EVIDENCE LIMIT:** synchronous in-memory fixture; no persistence, Flutter, concurrency, process death or sync claim.

## EXECUTABLE VALIDATION B — materially different dependency structures
Fixture: `research/architecture/fixtures/A002_dependency_direction.py`

Environment: Python 3.13.5 / Linux, 2026-09-16.

Scenario: a summary policy formats block time according to a user preference. The mechanism changes from `FileSettings.read_units()` returning `minutes|hours` to `RemoteSettings.fetch()` returning `{display_hours: bool}` while semantic behavior remains unchanged.

### Direct-detail structure
`BadSummaryPolicy` knows the concrete settings API and representation. When the mechanism changes, `BadSummaryPolicyV2` must be changed to decode the new remote representation.

### Policy-owned contract structure
`GoodSummaryPolicy` depends only on semantic `UnitPreference.unit()`. `FileUnitPreference` and `RemoteUnitPreference` adapt the two mechanisms. The policy implementation remains unchanged across the mechanism change.

### Test Evidence Contract
- **CLAIM:** when a mechanism changes independently while semantic policy remains stable, a policy-owned semantic contract can localize the mechanism change to an adapter.
- **SPEC/PROPERTY:** 90 minutes with an hours preference renders `1.5 h` before and after mechanism replacement.
- **TARGET:** direct concrete dependency versus policy-owned semantic dependency.
- **ORACLE:** exact behavior parity plus source-structure observation of which policy class must change.
- **OBSERVATION:** both structures produced `1.5 h`; direct-detail design required a new/changed policy implementation for the new mechanism, while `GoodSummaryPolicy` remained unchanged and only the detail adapter changed.
- **VERDICT:** dependency inversion protected the bounded semantic policy from this independently changing mechanism.
- **CONTRADICTION / LIMIT:** this does not establish that every concrete dependency needs an interface. If the mechanism is stable, singular, and not semantically distinct, the extra contract may be carrying cost without locality benefit, as A001 validation B already demonstrated.

## ENGINEERING JUDGMENT
A useful dependency inversion test is:
1. identify the semantic policy that should remain stable;
2. identify the detail likely to change independently;
3. define the smallest contract in the vocabulary of the semantic consumer;
4. make the detail implement/adapt that contract;
5. execute a plausible detail change and verify the policy remains unchanged;
6. remove/challenge the interface if no such independent variation or ownership boundary can be demonstrated.

Dependency injection is a wiring technique; it is not itself evidence that dependency inversion or good architecture exists.

## TRANSFER TO LOGMATE
Prior exact-ref evidence remains:
`yhappcom/logmate → b551ce434ad72b1895033e0f3617c73b026d40ea → app 1.0.0+1 → evidence date 2026-09-16`.

At that ref local ledger/persistence and canonical FlightRecord/calculation linkage were not implemented. Therefore no future Repository/Service hierarchy is prescribed. A002 supplies two constraints: canonical flight mutation authority should be named before derived totals/search/import-preview/sync state are introduced, and any future persistence/sync interface should be justified by an actual semantic policy that must survive mechanism change rather than by Clean Architecture vocabulary alone.

## RELATED DOMAIN CHECK
- **Foundations:** F001 execution model checked; current environment again lacks `dart`/`flutter`, so direct Dart/Flutter validation remains OPEN.
- **Architecture:** A001 supplies information-hiding and over-abstraction counterevidence; A002 now adds both ownership failure and alternative dependency-structure evidence.
- **Data:** D001 supplies authority/SSOT semantics; A002 does not claim durability or distributed consistency.
- **Quality:** Q001 Test Evidence Contract applied; alternative structures were behavior-matched under the same oracle.
- **Mobile:** Flutter state/DI frameworks are not architectural proof; M001/M002 runtime evidence remains separate.
- **Systems:** trust/security/build constraints may legitimately force dependency boundaries; not validated here.
- **Design Studio:** saved/synced/recovery UI semantics may be projections of distinct authorities; no design file changed.
- **Web Manager / Marketing Manager:** not materially relevant to this bounded architecture mechanism.
- **Product source:** prior exact LogMate ref reused as timing/context only; no new product behavior inferred.

## HANDOFFS
- **TO Data:** define persistence/cache/sync contracts in semantic authority vocabulary; do not let storage/vendor DTO shape define domain policy interfaces by default.
- **TO Quality:** when testing an interface boundary, include a materially different implementation/mechanism; mockability alone is weak evidence that the boundary is useful.
- **TO Mobile:** distinguish dependency injection frameworks from dependency inversion; test whether platform/vendor replacement actually leaves semantic policy stable.
- **TO LogMate project:** delay generic Repository/Service layering until local ledger ownership and persistence/sync variation are concrete; then place contracts in the vocabulary of the stable consumer policy.

## OPEN / VALIDATION
- A003: interface contracts, invariants, compatibility and evolution remains required before Architecture Stage 1 PASS.
- Add concurrency/event-order failure only after F004/F005/D006 prerequisites.
- Repeat exact-ref LogMate transfer after real ledger/persistence code exists.
- MintTap transfer remains open until materially needed and exact production/ref evidence is available.

## Current conclusion
State and dependency architecture are defensible when authority is explicit and dependency boundaries protect stable semantic policy from independently changing details. The evidence now supports both sides: direct writes to derived state create accidental authority, while a policy-owned contract can localize a real mechanism change. It also preserves A001's counter-rule: interfaces that protect no demonstrated variation or ownership boundary should not be added merely to satisfy a pattern diagram.
