# Q004 — Mutation Sensitivity & Search-Strength Comparison

Status: **IN STUDY — SECOND EXECUTABLE BLOCK COMPLETE**  
Date: 2026-09-18  
Lead: Quality, Testing & Reliability

## Problem
The first Q004 block proved that generated histories can find and reduce a counterexample. It did not establish whether the campaign is sensitive to plausible defects or how generated sampling compares with exact enumeration when the bounded state space is tractable. This block closes those two explicit gaps without treating mutation score or enumeration-to-bound as global correctness proof.

## SOURCE / prior evidence
This block reuses the property/model/search/reduction distinctions and primary QuickCheck/Hypothesis evidence in `Q004_property_model_based_testing_invariants.md`, plus the Studio `methods/VALIDATION_STANDARD.md`. No volatile external technical fact was needed to interpret the executable comparison.

## SYNTHESIS
A test campaign and a target defect model are separate objects. Mutation sensitivity asks whether a campaign can distinguish a deliberately incorrect target from the reference property. A surviving mutant can indicate a search/input weakness, an oracle weakness, an equivalent mutant, or a mutation outside the campaign's modeled scope; it is not automatically a test-suite defect.

Likewise, exhaustive enumeration is only exhaustive relative to a declared finite alphabet and bound. For an alphabet of 3 events and sequence lengths 1..4, the complete bounded space is `3 + 9 + 27 + 81 = 120` sequences. Exhaustive-to-bound evidence can therefore provide a stronger statement about that model than a small generated sample, but says nothing about length >4, omitted event kinds, real timing, networks, storage, process death, or platform behavior.

## EXECUTABLE VALIDATION
Fixture: `research/quality/fixtures/Q004_mutation_exhaustive_generated_comparison.py`

### Test Evidence Contract
- **CLAIM:** bounded exhaustive enumeration can expose plausible mutants that a deterministic generated sample misses; deliberate mutation also tests whether the oracle/search combination can disagree with an incorrect SUT.
- **SPEC/PROPERTY:** terminal state must equal an independent highest-version-wins model in which delete is semantic state.
- **TARGET:** two deliberate Python mutants: (1) arrival-order replacement and (2) version-aware updates that incorrectly ignore delete events.
- **INPUT/STATE:** event alphabet `update_v1`, `update_v2`, `delete_v3`; exhaustive lengths 1..4; comparison sample uses seed `20260919`, 3 generated sequences, max length 4.
- **ORACLE:** `model_terminal`, implemented independently of both mutants.
- **ENVIRONMENT:** Python 3.13.5 on Linux; execution date 2026-09-18. Environment recheck found no `dart` or `flutter` executable.
- **OBSERVATION:** all 120 bounded sequences were enumerated. Arrival-order mutant disagreed with the oracle on 61/120; ignore-delete mutant on 86/120. The 3-case generated sample killed ignore-delete once but killed arrival-order zero times. The deterministic prior regression `delete_v3 → update_v2` killed the arrival-order mutant.
- **VERDICT:** **VALIDATION — BOUNDED MUTATION/SEARCH COMPARISON PASS.** Both deliberate mutants are detectable under exact bounded enumeration, while the selected deterministic sample demonstrates a concrete missed-defect risk. The retained deterministic regression closes that particular sampled miss for the known defect class.
- **FAILURE MODEL:** generated sampling can omit distinguishing histories even when they exist abundantly in a bounded state space; mutation sensitivity depends jointly on property, generator/search and target mutant.
- **REPRODUCTION DATA:** fixture path above; seed `20260919`; `SAMPLE_CASES=3`; `MAX_STEPS=4`; stdlib only.
- **EVIDENCE LIMIT:** this does not prove global adequacy, mutation-score sufficiency, real synchronization correctness, or Dart/Flutter behavior. The sample size is deliberately small to demonstrate a mechanism, not to estimate a production miss probability.

## DEBUG / ROOT-CAUSE INTERPRETATION
The sampled campaign's survivor is not caused by an invalid oracle: exact enumeration finds 61 distinguishing sequences for the arrival-order mutant, and the known deterministic regression also distinguishes it. The bounded cause of survival is therefore search/input selection for this seed and sample budget. This isolates a concrete distinction between **property strength** and **search strength**.

## ALTERNATIVE COMPARISON
For small finite spaces, exact enumeration gives a stronger bounded guarantee and should be preferred when affordable. As state/action spaces grow combinatorially, generated/model-based search becomes useful, but should be supplemented by deterministic regressions for known failures, targeted boundary cases, coverage/search diagnostics where defensible, and mutation/fault sensitivity checks proportional to risk.

## CONTRADICTION / invalid shortcuts
- `mutant survived ⇒ oracle is wrong` — not established; this fixture demonstrates a search miss with a distinguishing oracle.
- `all mutants killed ⇒ implementation correct` — false.
- `exhaustive 1..4 ⇒ exhaustive protocol validation` — false; the bound/alphabet define the claim.
- `random sample missed one mutant ⇒ random testing is weak` — overgeneralization; search budget, generator, property and defect distribution matter.
- `high mutation score ⇒ production reliability` — unsupported.

## TRANSFER VALIDATION
Q003's exact schedule enumeration and Q004 generated search now have a direct bounded comparison: enumeration is preferable when the complete modeled space is tractable; generation is a counterexample-search strategy when it is not. D006 can reuse the method for bounded sync transition models, but Data owns actual conflict/delete semantics.

## RELATED DOMAIN CHECK
- **Foundations:** F003 explains combinatorial growth; F004/F005/F006 supply future concurrency/async/network state dimensions. F001 Dart/Flutter execution remains OPEN.
- **Architecture:** A003 invariants remain candidate independent properties.
- **Mobile:** no platform behavior is inferred; future lifecycle/process-death campaigns require exact runtime fault controls.
- **Data:** D006 supplies the reusable stale-update/delete failure class; no product sync claim is made.
- **Quality:** Q001 oracle discipline, Q003 enumeration, Q005 causal isolation and Q006 fault sensitivity directly support this block.
- **Systems:** CI use must bind seed/framework/artifact/environment and resource budget.
- **Design Studio / Web Manager / Marketing Manager:** considered; no materially relevant canonical decision changes this testing-method result.
- **Product source:** no product audit was required.

## OPEN / VALIDATION
1. Direct Dart/Flutter framework transfer remains OPEN until a trustworthy SDK exists.
2. Equivalent-mutant classification and mutation-operator design remain future Intermediate work.
3. Real persistence/network/process-death state machines remain transfer work, not established by this fixture.
4. Q004 still does not justify Foundation PASS by itself; track-level real recovery/runtime evidence remains incomplete.

## HANDOFFS
- **Quality → Data:** use exhaustive bounded enumeration before generated sampling when a synchronization submodel's full state space is genuinely tractable; retain deterministic regressions for known histories.
- **Quality → Systems:** mutation/fault campaigns in CI need exact artifact/environment identity and bounded cost; mutation score alone is not a release oracle.
- **Quality → Mobile:** do not convert this Python search result into lifecycle/PWA evidence; transfer only the test-design method.

## Current judgment
The two explicit Q004 gaps `deliberate mutation sensitivity` and `exhaustive-vs-generated comparison` now have executable bounded evidence. Q004 remains **IN STUDY / NOT PASS** because real Dart/Flutter/runtime transfer and broader failure contexts remain OPEN.
