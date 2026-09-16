# A001 — Information Hiding, Cohesion, Coupling & Change Pressure

Status: **SUBSTANTIAL FOUNDATION BLOCK COMPLETE — TRACK NOT YET PASSED**
Date: 2026-09-16
Lead: Architecture

## Problem
Architecture advice often starts from named patterns or layers. A more durable starting point is: what design decisions are likely to change, which modules must know them, how far does a change propagate, and what carrying cost does each added boundary impose?

## SOURCE
David Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules*, Communications of the ACM 15(12), 1972, is the historical primary source for the information-hiding decomposition criterion. The paper contrasts a conventional processing-step decomposition with a decomposition that assigns modules around design decisions likely to change, hiding those decisions behind interfaces. Its core purpose is not “make more classes”; it is to reduce the number of modules that must understand a changeable decision.

Supporting source checked: University of Maryland software-engineering course material identifies the Parnas 1972 paper as the decomposition case study and preserves the original citation.

## MODEL
### 1. Abstraction and information hiding are related but not identical
- **Abstraction** gives a useful model/interface that omits irrelevant detail for a caller.
- **Information hiding** is a design responsibility: a module owns a design decision and prevents other modules from depending on its volatile representation/mechanism.

A convenient API can still leak a volatile decision. Conversely, a small internal module can hide a decision even when its abstraction is not domain-rich.

### 2. Change pressure is the practical test
For a proposed boundary ask:
1. What decision does this module own?
2. Why might that decision change independently?
3. Which callers currently know that decision?
4. If it changes, how many modules must change or be retested?
5. What new collaborators, call edges, failure paths, configuration, test doubles, and names does the boundary add?

A boundary is valuable when it localizes plausible independent change, creates a real substitution seam, centralizes ownership, or enables a needed policy/security/runtime boundary. Extra indirection without one of those benefits is not automatically architecture improvement.

### 3. Cohesion
Cohesion is strongest when responsibilities belong together because they implement/maintain the same contract or change for the same reason. Merely putting similar-looking functions in one file is weaker evidence.

### 4. Coupling
Coupling is not simply “number of imports”. The dangerous form is dependency on another module's unstable knowledge: storage schema, serialization shape, vendor API, lifecycle timing, calculation convention, or mutation rules. Stable contracts can permit necessary coupling without exposing volatile internals.

### 5. Carrying cost is real but not reducible to one metric
Every added abstraction can introduce some combination of:
- another concept/name to learn;
- another collaborator or dependency edge;
- construction/configuration wiring;
- another location to navigate while debugging;
- possible test doubles and contract tests;
- possible mismatch between the abstraction and the concrete capability beneath it.

These costs may be justified by change locality or substitutability. Node/edge counts, LOC, or stack depth are **not universal maintainability scores**; they are bounded evidence that extra mechanism exists and therefore needs a reason.

## EXECUTABLE VALIDATION A — when hiding volatile knowledge helps
Fixture: `research/architecture/fixtures/A001_change_locality.py`

### Test Evidence Contract
- **CLAIM:** when a representation decision changes, centralizing that knowledge behind a semantic boundary can preserve consumers.
- **SPEC/PROPERTY:** semantic clients should continue to operate when only the storage/transport representation changes.
- **TARGET:** hidden-representation design versus clients that parse the representation directly.
- **ORACLE:** unchanged semantic client results across representation V1/V2; deliberate failure of V1-specific leaky clients against V2.
- **FAILURE MODEL:** representation changes while business meaning remains the same.
- **EVIDENCE LIMIT:** bounded fixture; not proof that every wrapper/layer improves maintainability.

The fixture compares two representation versions (`"callsign|minutes"` and a keyed record) and establishes:
- hidden clients remain unchanged across representation versions;
- the representation owner changes once;
- leaky clients fail against the new representation until each is modified.

### ROOT CAUSE
The deliberate failure is caused by knowledge duplication: parsing syntax is repeated outside the owner. The representation change therefore propagates through all consumers that know the old syntax.

## EXECUTABLE VALIDATION B — counterexample: abstraction without a boundary benefit
Fixture: `research/architecture/fixtures/A001_abstraction_cost.py`

Environment:
- Python 3.13.5
- Linux 6.18.44 x86_64, glibc 2.41

### Test Evidence Contract
- **CLAIM:** in a fixed single-source/single-policy scenario with no demonstrated independent volatility or substitution requirement, pass-through layers can add structural and diagnostic mechanism without showing change-locality benefit.
- **SPEC/PROPERTY:** direct and layered designs must produce identical observable formatting behavior for the same inputs.
- **TARGET:** one direct function versus Source → Repository → Service → Formatter → Presenter pass-through collaboration.
- **INPUT:** `0, 59, 60, 135, 6000` minutes plus a negative invalid input.
- **ORACLE:** exact output parity for valid samples and the same `ValueError` policy for invalid input.
- **OBSERVATION:** both designs produced identical valid outputs. In the bounded declared collaboration graph, direct design had 1 node / 0 edges; layered design had 6 nodes / 9 declared dependency edges. The invalid-input traceback contained one fixture frame for the direct design and three for the layered path (`layered_format → render → format`).
- **VERDICT:** no change-locality or substitution benefit was demonstrated in this scenario, while additional mechanism was observable.
- **EVIDENCE LIMIT:** this does **not** prove that fewer classes are generally better, that node/edge count predicts maintainability, or that repositories/services are intrinsically wasteful. It is a deliberate counterexample to the universal claim “more abstraction is always better”.

### CONTRADICTION / COUNTEREXAMPLE
The first fixture shows that a boundary can reduce change propagation when it owns volatile knowledge. The second fixture shows that the same architectural vocabulary can be gratuitous when there is no independent variation to isolate.

The combined result is stronger than either alone:

`boundary value = demonstrated ownership/change/substitution benefit − carrying cost`

This is an engineering judgment model, not a numerical formula.

## CONNECTION TO D001
D001 established source of truth as a logical mutation/authority contract. A001 extends that idea architecturally: the component that owns mutation or representation policy should expose semantic operations without forcing consumers to know storage/synchronization details. A repository is justified when it hides a real data-source/representation/consistency policy; the name `Repository` alone proves nothing.

## CONNECTION TO Q001
Q001 requires an independent specification/oracle. Architecture boundaries should expose contracts that can be tested without reproducing hidden implementation knowledge in the oracle. Conversely, abstractions that exist only to make mocking easier but do not correspond to a meaningful contract/change boundary should be challenged rather than automatically retained.

## TRANSFER VALIDATION — LOGMATE EXACT REF
Evidence identity:

`yhappcom/logmate → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared app version 1.0.0+1 → evidence date 2026-09-16`

`pubspec.yaml` at that commit declares Dart SDK `^3.10.7`, Flutter, Firebase Auth/Core/Cloud Functions, and app version `1.0.0+1`.

### Case 1 — AirportLookup: representation ownership has a concrete reason
`lib/airport/airport_lookup.dart` explicitly describes the lookup as offline input assistance and separate from the still-open canonical FlightRecord airport representation. The class owns:
- asset path and loading;
- JSON decoding;
- positional asset-record interpretation;
- conversion to semantic `Airport` objects;
- code normalization/search/order/autocomplete ambiguity policy.

Consumers therefore do not need to know that the bundled asset currently stores airport records as positional JSON lists. This is a concrete Parnas-style boundary: physical reference-data representation and lookup policy have an owner.

**TRANSFER VALIDATION:** this product structure matches A001 fixture A's mechanism. A future change to the bundled asset representation can plausibly be localized inside the lookup boundary if its semantic `Airport` contract remains stable.

**LIMIT:** no such asset-format migration was executed in LogMate during this study. This is source-structure transfer evidence, not runtime migration proof.

### Case 2 — AuthEngine: interface has actual substitution and vendor-isolation evidence
`lib/auth/auth_engine.dart` defines `AuthEngine`, a Firebase-backed implementation, and a lightweight `PendingFirebaseAuthEngine` retained for widget previews/tests. `lib/auth/email_auth_screen.dart` accepts/injects `AuthEngine` and performs UI flow against that contract rather than importing Firebase APIs directly.

The Firebase implementation owns:
- Firebase initialization timing;
- Cloud Functions email-account lookup;
- Firebase Auth calls;
- Firebase exception translation into `AuthFailure`;
- email-language configuration.

This boundary therefore has at least two evidenced reasons to exist at the inspected ref:
1. **actual substitution:** Firebase and preview/test implementations exist;
2. **vendor/error-policy isolation:** UI code consumes LogMate auth semantics rather than Firebase exception/API details.

**ENGINEERING JUDGMENT:** this is materially different from adding an interface around a single stable pure function “just in case”. The boundary currently hides volatile vendor/runtime knowledge and is exercised by more than one implementation.

**LIMIT:** this study does not claim `AuthEngine` is complete, optimally shaped, or sufficient for future account/sync architecture. It validates only that the current interface is not evidence-free indirection.

### Product state that constrains future architecture
The exact LogMate commit states that local ledger/persistence, FlightRecord/calculation linkage, configuration persistence, Sync, and Backup/Export remain not implemented. Therefore A001 must **not** infer a future Repository/Service layering scheme from current mock/session UI code. Those boundaries should be introduced only when D001/A002/A003 identify concrete ownership and change-pressure requirements.

## RELATED DOMAIN CHECK
- **Foundations:** F001 process/runtime boundaries checked; architecture boundaries must not be confused with OS/runtime boundaries.
- **Data:** D001 authority/SSOT directly reused; future local-ledger/storage/sync boundaries require explicit mutation and durability semantics.
- **Quality:** Q001 evidence contract used for both positive and counterexample fixtures; public semantic contracts should remain independently testable.
- **Mobile:** Flutter/platform lifecycle can create legitimate volatile knowledge; direct runtime/platform validation remains open in M001/M002.
- **Systems:** vendor initialization, Firebase dependency, build/security/performance boundaries may constrain AuthEngine later; not validated here.
- **Design Studio:** interaction semantics remain design-owned. Engineering boundaries may implement them but must not redefine them for convenience.
- **Web Manager / Marketing Manager:** not materially relevant to this bounded architecture study.
- **Product source:** exact LogMate ref/version audited; no other product ref used.

## HANDOFFS
- **TO Data:** when local ledger appears, justify Repository/storage boundaries by actual durability, schema, migration, cache, and sync ownership—not by pattern convention.
- **TO Quality:** add contract tests where a boundary hides meaningful vendor/representation semantics; avoid multiplying mocks around pass-through layers with no independent contract.
- **TO Mobile:** use AuthEngine as a candidate future case for studying framework/vendor/platform boundary behavior, but validate Flutter/mobile execution separately.
- **TO Systems:** later inspect Firebase initialization/error/security/performance behavior behind AuthEngine rather than assuming the interface neutralizes vendor/runtime risks.
- **TO LogMate project (advisory only; no product files changed):** preserve `AirportLookup`'s separation from canonical FlightRecord representation and avoid deciding future local-ledger/service/repository layers until actual ownership/change-pressure contracts are known.

## OPEN / VALIDATION
- A002: modules/layers/dependency direction/state ownership.
- A003: interface stability, contract evolution, compatibility and invariants.
- Transfer-test the same criteria against MintTap when architecture work there is materially needed.
- Do not reduce cohesion/coupling/maintainability to node count, edge count, LOC, mock count, or any single metric.

## Current conclusion
A useful architecture boundary must **earn its indirection**. The strongest Foundation rule from A001 is:

> Identify independently changeable or substitutable knowledge, give it a clear owner, expose the smallest stable semantic contract, and verify that realistic changes are localized. If a boundary hides nothing, substitutes nothing, owns no policy, and does not protect a trust/runtime/consistency boundary, prefer the simpler structure until evidence changes.

Named patterns remain implementation options. They are not evidence by themselves.