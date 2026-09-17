# Q004 — Property-Based / Model-Based Testing & Invariant Checking

Status: **IN STUDY — SOURCE/MODEL + EXECUTABLE FIXTURE PREPARED; EXECUTION OPEN**  
Date: 2026-09-17  
Lead: Quality, Testing & Reliability

## Problem
Example-based tests answer whether selected examples satisfy selected expectations. They do not by themselves explore a large input or state-transition space. Q003 showed that explicit enumeration works well for a genuinely tiny event alphabet, while D006 exposed synchronization semantics whose state space grows quickly once duplicate, stale, delete, retry and conflict operations combine. Q004 establishes how generated cases, state-machine models, invariants and counterexample reduction can extend coverage without confusing sampling with proof.

## SOURCE
Primary/current sources checked 2026-09-17:
- Claessen & Hughes, *QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs* (ICFP 2000, DOI 10.1145/357766.351266): properties are executable predicates tested over automatically generated inputs; custom generators are supported; the paper also discusses pitfalls. Chalmers record: https://research.chalmers.se/en/publication/237427
- Claessen & Hughes, *Testing Monadic Code with QuickCheck* (2002, DOI 10.1145/636517.636527): model-based, algebraic and pre/post-condition specifications can be used for testing stateful/imperative behavior. Chalmers record: https://research.chalmers.se/en/publication/170517
- Hypothesis 6.168.0 current stateful-testing documentation: rule-based state machines generate sequences of actions; rules can be chained, invariants can be checked after rules, implementation can be compared with a simplified in-memory model, and failing state-machine executions are reduced to short reproducing programs. https://hypothesis.readthedocs.io/en/latest/stateful.html

## SYNTHESIS — four distinct layers
Do not collapse these concepts:
1. **property/invariant** — the rule that defines correctness;
2. **generator/model transition system** — which inputs/states/action sequences can be explored;
3. **search strategy** — random, exhaustive-to-bound, coverage-guided, weighted, targeted, etc.;
4. **counterexample reduction** — a transformation that seeks a simpler failure while preserving the property violation.

A generated test is only as strong as its property and reachable state space. A sophisticated generator with a duplicated or invalid oracle can produce large amounts of weak evidence.

## MODEL-BASED TEST SHAPE
For stateful systems use an explicit comparison shape when practical:

`initial model/SUT state → generated applicable action → apply to SUT → apply to independent reference model → compare observable invariant/postcondition → repeat`

The reference model need not reproduce implementation architecture. In fact, excessive structural similarity can create correlated defects. It should encode the smallest independent semantics needed by the oracle.

## SHRINKING / REDUCTION
A large failing sequence is often poor debugging evidence. Reduction should preserve the failure while removing irrelevant values/actions. The resulting case is a smaller counterexample under the reduction strategy, **not automatically a mathematically globally minimal counterexample** and not automatically the root cause.

This distinction is important for Q005: shrinking improves isolation input, but the progression remains `counterexample → reproduction → causal hypothesis → falsification/intervention → root cause`.

## EXECUTABLE FIXTURE — PREPARED, NOT YET EXECUTED
Fixture: `research/quality/fixtures/Q004_model_property_sequence_shrinking.py`

The stdlib-only fixture deliberately avoids requiring Hypothesis so the mechanism can be reproduced in a minimal Python environment. It:
- uses fixed seed `20260917`;
- generates up to 500 sequences of 1–8 delivered events from `update_v1`, `update_v2`, `delete_v3`;
- compares a deliberately naive arrival-order replica with an independent version-aware reference model where the highest version wins and delete remains a semantic state;
- defines the property as equality of terminal observable state between SUT model and reference model;
- stops at the first generated violation;
- greedily removes commands while the violation persists;
- checks that the final result is 1-minimal under single-command deletion.

### VALIDATION STATUS
**OPEN / NOT EXECUTED IN THIS RUN.** The available execution tools returned an infrastructure `GatewaySelectionError`, so no runtime observation, counterexample, timing, Python version or verdict is claimed. Creating executable code is not execution evidence. The fixture must be run in a trustworthy environment and its exact output/environment recorded before this block can claim executable validation.

### EXPECTED FAILURE CLASS, NOT OBSERVATION
The intended defect class is the D006 stale-update-after-newer-delete resurrection problem: arrival-order replacement forgets deletion ordering metadata. This is a test-design hypothesis based on prior D006 executable evidence, not a new Q004 execution result.

## ENGINEERING JUDGMENT
Property/model-based testing is most valuable when ordinary example tests underrepresent combinations or state histories and when a defensible invariant/model exists. It is not automatically superior for every unit. Small exact examples remain preferable when the relevant state space is tiny and fully enumerable, as in Q003's bounded 24-order matrix.

Use generated testing to search for counterexamples, not to infer universal correctness from `N` passing random cases. For high-risk persistence/sync/recovery protocols, combine it with targeted known failure schedules, deterministic regression cases and real platform/backend fault injection.

## CONTRADICTIONS / INVALID SHORTCUTS
- `many generated cases passed ⇒ property proven` — false; sampling is not proof.
- `fixed seed ⇒ system deterministic` — false; it controls only represented randomness.
- `shrunk case ⇒ root cause proven` — false; reduction preserves failure, not causality.
- `model agrees with SUT ⇒ both are correct` — false if the model/property is wrong or shares the defect.
- `random generation ⇒ good state-space coverage` — false without generator/reachability analysis.
- `stateful PBT replaces targeted regression tests` — rejected; once a defect is known, preserve a deterministic regression reproducer as well.

## TRANSFER VALIDATION
Q003 → Q004: bounded exhaustive schedule enumeration remains the preferred method when the complete relevant alphabet is tractable. Q004 extends, rather than replaces, that method for larger spaces.

D006 → Q004: the stale-update/delete invariant supplies a reusable stateful failure class, but the Data-owned synchronization semantics remain canonical in D006. Q004 owns the generated-testing method, not the product sync policy.

## RELATED DOMAIN CHECK
- **Foundations:** F003 complexity matters because state/action spaces grow combinatorially; F004/F005 supply concurrency/async ordering mechanisms. F001 direct Dart/Flutter execution remains OPEN.
- **Architecture:** A003 contracts/invariants are candidate property sources. A002 state ownership helps define model boundaries.
- **Mobile:** future process-death/background state machines can reuse the method only on exact platform/runtime evidence; no native lifecycle claim is made here.
- **Data:** D006 is the principal current transfer source; generated sync histories should preserve Data-owned conflict/delete semantics.
- **Quality:** Q001 oracle discipline, Q003 schedule exploration, Q005 causal isolation and Q006 fault campaigns are directly reused.
- **Systems:** release use requires exact artifact/environment identity and bounded resource budgets; generated campaigns can become expensive.
- **Design Studio:** considered; no design-owned semantic decision is changed by this testing-method block.
- **Web Manager:** considered; no browser/PWA claim is made.
- **Marketing Manager:** considered; not materially relevant.
- **Product source:** no product behavior audit was required; no MintTap/LogMate implementation claim is made.

## OPEN / VALIDATION
1. Execute the prepared fixture and record exact environment/output/verdict.
2. Add a deliberate mutant and confirm the property campaign detects it; then preserve the minimized failure as a deterministic regression case.
3. Compare generated sampling with bounded exhaustive enumeration on a small state space to measure missed-state risk.
4. Add preconditions/invalid-action handling and distinguish model bug, generator bug, oracle bug and SUT bug.
5. Transfer to a real Dart/Flutter test framework only when a trustworthy SDK is available; do not infer Dart behavior from Python.
6. Later evaluate a maintained PBT framework (e.g. Hypothesis in Python or an appropriate Dart package) by exact version, shrink/reproduction behavior and project fit rather than adopting it from popularity.

## HANDOFFS
- **Quality → Data:** when D006 expands to delete/recreate/tombstone-GC or operation-vs-state sync, define Data-owned invariants first; Q004 can then generate action histories and reduce counterexamples.
- **Quality → Architecture:** expose machine-checkable invariants/contracts where they improve testability, without leaking implementation representation into public contracts.
- **Quality → Mobile:** future lifecycle/process-death campaigns can use generated state/action sequences only after exact platform fault controls and durable-state oracles exist.
- **Quality → Systems:** if generated campaigns enter CI, bind seed/framework/version/artifact/environment and control runtime/resource budgets.

## Current judgment
Q004 now has a professional conceptual boundary and a prepared reproducible fixture, but it does **not** yet have executable evidence because the execution environment failed during this run. Quality Stage 1 remains **NOT PASS**. The next Q004 block should execute and mutation-check the fixture when infrastructure is available; if execution remains blocked, Balance Loop should advance to an independent high-value prerequisite rather than pretending a validation result.
