# A001 — Information Hiding, Cohesion, Coupling & Change Pressure

Status: **IN STUDY — first integrated foundation block**
Date: 2026-09-16
Lead: Architecture

## Problem
Architecture advice often starts from named patterns or layers. A more durable starting point is: what design decisions are likely to change, which modules must know them, and how far does a change propagate?

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

A boundary is valuable when it localizes a plausible independent change. Extra indirection without a change boundary is not automatically architecture improvement.

### 3. Cohesion
Cohesion is strongest when responsibilities belong together because they implement/maintain the same contract or change for the same reason. Merely putting similar-looking functions in one file is weaker evidence.

### 4. Coupling
Coupling is not simply “number of imports”. The dangerous form is dependency on another module's unstable knowledge: storage schema, serialization shape, vendor API, lifecycle timing, calculation convention, or mutation rules. Stable contracts can permit necessary coupling without exposing volatile internals.

### 5. Change propagation as an executable proxy
For a bounded fixture, define a volatile representation rule and two clients.

**Leaky design:** each client decodes the representation itself. Changing the representation requires edits in producer + both clients.

**Hidden design:** one module owns decode/encode; clients consume the semantic contract. Changing representation requires an edit only in the owner while client behavior remains unchanged.

This is not a universal architecture metric; it is a concrete test of one Parnas-style claim: hiding a volatile design decision reduces the change surface for that decision.

## EXECUTABLE VALIDATION
Fixture: `research/architecture/fixtures/A001_change_locality.py`

Claim: when a representation decision changes, a design that centralizes ownership behind a semantic interface preserves clients, whereas clients coupled directly to representation require coordinated changes.

The fixture compares two representation versions (`"callsign|minutes"` and a keyed record) and asserts:
- hidden clients are unchanged across representation versions;
- the representation owner changes once;
- leaky clients fail against the new representation until each is modified.

Evidence level: executable worked example + deliberate failure case. This validates the bounded change-locality mechanism, not a claim that every wrapper/layer improves maintainability.

## FAILURE / ROOT CAUSE
The failure is intentionally caused by clients depending on representation syntax rather than semantic meaning. The root cause is knowledge duplication: the parsing rule is repeated outside the module that should own it. The representation change therefore propagates through all consumers.

## ALTERNATIVE / TRADE-OFF
Information hiding has costs:
- another interface/boundary must be named and maintained;
- over-general interfaces can hide useful capabilities or create awkward lowest-common-denominator APIs;
- speculative abstraction around decisions that never vary can add indirection without reducing change cost;
- a boundary can become a bottleneck if unrelated responsibilities are grouped only to reduce file count.

Therefore “more layers” and “lower coupling” are not independent goals. The target is **appropriate knowledge ownership under realistic change pressure**.

## CONNECTION TO D001
D001 established source of truth as a logical mutation/authority contract. A001 extends that idea architecturally: the component that owns a mutation or representation decision should expose semantic operations/contracts without forcing consumers to know storage or synchronization details. A repository is justified when it hides a real data-source/representation policy; the name `Repository` alone proves nothing.

## CONNECTION TO Q001
Q001 requires an independent specification/oracle. Architecture boundaries should therefore expose contracts that can be tested without reproducing hidden implementation knowledge in the oracle. If every test must know private schema/vendor details, the boundary is leaking those decisions into the quality system.

## PRODUCT TRANSFER
No product-specific implementation conclusion is made in this block. LogMate and MintTap are high-value future transfer targets, but an audit must capture exact repository ref/version before claiming their boundaries leak or hide particular decisions.

Potential LogMate questions for later exact-ref audit:
- does local ledger ownership hide storage schema from UI/calculation code?
- are sync states semantic contracts or Firebase-shaped leakage?
- can import parsers change without changing normalized domain consumers?

Potential MintTap questions:
- are YieldMax calculation rules isolated from presentation/storage representation?
- can Firebase/vendor schema change without rewriting financial-domain calculations?

These are audit questions, not findings.

## RELATED DOMAIN CHECK
- Foundations: F001 process/runtime boundaries checked conceptually; architecture boundaries must not be confused with OS/runtime boundaries.
- Data: D001 authority/SSOT directly reused.
- Quality: Q001 oracle/specification contract directly reused.
- Mobile: platform lifecycle may create legitimate change boundaries; not validated here.
- Systems: vendor/build/security/performance boundaries may constrain interfaces; not materially tested here.
- Design Studio: semantic interaction state can constrain architecture, but no design artifact is needed for this generic foundation block.
- Web Manager / Marketing Manager: not materially relevant to the generic mechanism.
- Product source: intentionally not audited; no product claim made.

## OPEN / VALIDATION
- Compare this representation-hiding fixture with a counterexample where the added boundary creates needless indirection.
- Study interface stability and dependency direction separately in A002/A003.
- Transfer-test against an exact LogMate or MintTap ref before project advice.
- Avoid quantitative claims that cohesion/coupling can be reduced to one universal metric.

## HANDOFFS
- **TO Data:** treat storage representation and sync mechanism as potentially hidden decisions; expose semantic authority contracts.
- **TO Quality:** tests should depend on public semantic contracts where possible, not duplicate hidden representation details.
- **TO Mobile:** distinguish framework/platform lifecycle knowledge that must remain platform-specific from domain semantics that should not leak it.

## Current conclusion
The foundation criterion is not “use Clean Architecture”, “add repositories”, or “minimize imports”. It is: identify volatile design knowledge, give it an owner, expose the smallest stable semantic contract justified by real change pressure, and verify that plausible changes remain local. Named patterns are later implementation options, not the starting proof.