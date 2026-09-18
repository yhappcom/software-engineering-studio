# A005 — Repeated-Change / Evolution Evidence

Status: **IN STUDY — second executable block complete / Architecture not passed**  
Date: 2026-09-18  
Lead: Architecture

## Problem

The first A005 block established that refactoring is observer-scoped behavior-preserving restructuring and that technical debt is a contingent future-change liability. The explicit remaining gap was repeated-change evidence: one clean refactoring example cannot show how duplicated policy knowledge creates inconsistent evolution risk across successive requirements.

## SOURCE / retained basis

This block extends, rather than replaces, the source basis in `A005_refactoring_technical_debt_evolutionary_boundaries.md`: ISO/IEC/IEEE 42010:2022 architecture-description distinction, SEI architecture/change reasoning, Fowler's refactoring boundary, and SEI technical-debt framing. No new volatile platform fact is required for this bounded executable extension.

## SYNTHESIS

A useful evolutionary architecture claim is not `fewer files/lines/classes = better architecture`. The stronger mechanism is:

`change pressure → knowledge/decision ownership → number of independently editable semantic copies → partial-change opportunity → observer inconsistency → regression/recovery cost`.

A single semantic owner can reduce the number of places that must change together, but centralization is not automatically superior: it can create an inappropriate shared dependency when consumers genuinely require different policies or independent evolution. The design boundary must follow the semantic invariant/change pressure, not DRY as an aesthetic rule.

## EXECUTABLE VALIDATION

Fixture: `research/architecture/fixtures/A005_repeated_change_pressure.py`

### Test Evidence Contract

- **CLAIM:** when three consumers are required to preserve one policy semantic, duplicated policy knowledge admits a partial evolutionary update that produces inconsistent externally observed behavior; a single semantic owner removes that particular partial-update failure path.
- **SPEC/PROPERTY:** independently declared oracle: reject negative principal; compute `principal × rate`; apply optional cap; then optional minimum. Three observers must agree with that policy: numeric quote, formatted export, and threshold alert.
- **TARGET:** (1) duplicated/coupled implementation, (2) encapsulated single-owner implementation, and (3) deliberate partial-migration mutant.
- **INPUT/STATE:** three requirement generations: R1 rate-only, R2 adds cap, R3 adds minimum; representative boundary/ordinary inputs; explicit negative-input failure contract.
- **ORACLE:** independent `oracle()` plus derived expected observer tuple; the deliberate mutant does not generate expected values.
- **ENVIRONMENT:** Python 3.13.5, Linux execution environment, execution date 2026-09-18. `dart` and `flutter` executables were absent on recheck.
- **OBSERVATION:** both complete implementations matched the oracle across all declared R1-R3 cases. The deliberate partial migration was indistinguishable under a non-cap-triggering R1 case but failed under R2 at principal 2000: observed `(120, '200.00', True)` versus expected `(120, '120.00', True)`. Negative-input failure policy remained preserved by both complete implementations.
- **VERDICT:** PASS for the bounded claim; deliberate repeated-change inconsistency detected.
- **ROOT CAUSE:** R2's cap semantic was changed in the quote path while export/alert retained the previous policy. The inconsistent output is caused by duplicated independently editable policy knowledge, not by formatting itself.
- **ALTERNATIVE:** route all three consumers through one policy evaluator. This removes this specific partial-update path while retaining the same observer contract in the bounded model.
- **REPRODUCTION:** execute `python3 research/architecture/fixtures/A005_repeated_change_pressure.py`; expected terminal summary begins `A005 repeated-change fixture: PASS`.
- **EVIDENCE LIMIT:** this is a deliberately small deterministic model. It does not measure maintenance effort, prove that every duplicated implementation becomes debt, establish a universal superiority of centralization, model team/process/code-review effects, or establish Dart/Flutter/product behavior.

## CONTRADICTIONS / boundaries

- `duplication => technical debt` remains invalid. Duplication becomes a debt candidate only when plausible future changes must stay semantically coordinated and the duplication raises cost/risk.
- `one owner => good architecture` is invalid. Independent change pressure may justify separate owners.
- `number of changed files/LOC => architectural quality` is invalid without a semantic/change-risk model.
- `tests pass today => low future-change cost` is invalid; current correctness and evolution liability are separate claims.

## ENGINEERING JUDGMENT

Repeated-change evidence should focus on *coordination obligations*: which decisions must change together, which observers can detect inconsistency, and which failure/recovery burden follows from a partial migration. Raw edit count can be supporting evidence but is not itself the architectural oracle.

## RELATED DOMAIN CHECK

- **Foundations:** F002 aliasing/ownership and F003 cost reasoning considered; no runtime-transfer claim made.
- **Architecture:** A001 change pressure, A002 ownership/dependency, A003 observer contracts, and the first A005 block directly reused.
- **Mobile:** not materially needed for this language-independent fixture; Flutter/platform transfer remains OPEN.
- **Data:** schema/migration duplication is a high-risk future transfer candidate, but no D003 claim is redefined here.
- **Quality:** independent oracle, deliberate mutant, failure isolation and evidence-limit discipline reused.
- **Systems:** exact execution environment retained; no release/production claim.
- **Design Studio / Web Manager / Marketing Manager:** considered; this bounded internal evolution mechanism does not change their canonical decisions.
- **Product repositories:** no product implementation audit was required; no MintTap/LogMate behavior claim is made.

## HANDOFFS

- **TO Quality:** for evolutionary refactoring tests, inject partial migrations across duplicated semantic owners rather than checking only current happy-path equivalence.
- **TO Data:** migration/schema policy duplicated across readers/writers is a candidate transfer context; validate against exact schema/version/ref before reuse.
- **TO product teams:** technical-debt records should identify the future coordinated-change scenario and observer-visible failure, not merely cite duplication or code smell.

## OPEN / VALIDATION

- **OPEN:** exact Dart/Flutter transfer remains blocked by unavailable SDK executables.
- **OPEN:** exact-ref product evolution/debt transfer remains unperformed; do not infer product debt from this model.
- **VALIDATION:** a stronger future block should use a real commit history or controlled multi-version product fixture to compare repeated evolution and recovery cost without using edit count as the sole oracle.
- **TRANSFER VALIDATION:** apply the coordination-obligation model to a materially different context such as persisted schema evolution, plugin/platform divergence, or release configuration.

## Conclusion

The repeated-change gap is now closed at bounded executable-model level: duplicated semantic ownership can create a concrete partial-evolution failure, while a single semantic owner removes that particular failure path. This strengthens the technical-debt/change-pressure mechanism but does not establish universal architectural superiority or product PASS.
