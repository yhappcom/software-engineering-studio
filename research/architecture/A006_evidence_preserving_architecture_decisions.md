# A006 — Evidence-Preserving Architecture Decisions & ADR Lifecycle

Status: **IN STUDY — two integrated Foundation blocks complete / track not passed**  
Date: 2026-09-18  
Lead: Architecture

## Problem and scope

Architecture decisions outlive the conversation that produced them. A decision record must preserve enough context, alternatives, evidence, uncertainty, consequences and supersession history for a later engineer to determine whether the decision still applies. This study treats an ADR as a decision/evidence artifact, not as architecture itself, a design guide, or a permanent command detached from its assumptions.

## SOURCE

- AWS Prescriptive Guidance defines an ADR as a record of an architecturally significant decision, its context and consequences. Its current process guidance says accepted/rejected ADRs should be treated as immutable history; changed decisions are represented by a new ADR that supersedes the old one. AWS also requires at least context, decision, consequences, status and change history, and recommends recording alternatives considered.
- Microsoft Azure Well-Architected guidance, updated 2026-04-13, recommends problem/context, options, decision outcome/trade-offs, confidence and status such as Proposed/Accepted/Superseded. It explicitly warns that a record without rationale loses value when circumstances change and that ADRs should not become design guides.
- A005 established that architecture and architecture description are distinct. Therefore an ADR is evidence about a decision affecting architecture, not the architecture itself.

## SYNTHESIS — decision evidence contract

For Studio use, an architecturally significant decision should preserve, where applicable:

`decision question → context/constraints → options → evaluation criteria → evidence/ref → assumptions/uncertainty → decision → consequences/trade-offs → validation/acceptance evidence → status → supersession trigger/history`.

The minimum context/decision/consequences form is useful but insufficient for high-risk engineering when later re-evaluation depends on exact evidence or assumptions.

### Evidence-preserving rules

1. **Decision is not evidence.** `We use X` records a choice; it does not establish that X satisfies the required property.
2. **Evidence is scoped.** A benchmark, platform test, product audit or failure reproduction must retain its exact environment/ref and evidence limits.
3. **Unknown is data.** Low confidence, unresolved transfer, missing production ref or unavailable runtime stays explicit rather than being converted into rationale.
4. **Alternatives matter.** A rejected option should retain the decisive reason when that reason could later change.
5. **Accepted history is not silently rewritten.** New evidence that changes the decision should supersede the old decision while preserving why the earlier choice was reasonable under its original context.
6. **Validation status is independent of ADR status.** An ADR may be Accepted while some transfer/production validation remains OPEN; Accepted must not be overloaded to mean empirically proven.

## FAILURE MODEL — stale evidence and silent rewrite

Consider an ADR choosing storage mechanism `A` because assumption `P` holds on platform version `V1`.

Unsafe record:

`Decision: use A because it is durable.`

Evidence-preserving record:

`Context: authoritative state must survive process death; uninstall survival is not required. Option A was validated on V1 for process-death persistence; uninstall behavior was explicitly out of scope. Decision: use A. CHANGE WATCH: revalidate when platform storage/backup semantics change.`

If platform `V2` changes the relevant property, editing the old rationale to say `A is not durable; use B` destroys the historical explanation and makes it impossible to distinguish an originally bad decision from a later invalidated assumption. The correct lifecycle is a new decision that references the new evidence and supersedes the old record.

## ALTERNATIVE COMPARISON

### Mutable wiki/current-state note
Useful for current instructions, but weak as a decision-history mechanism when old rationale/evidence can disappear.

### Immutable/superseded ADR chain
Preserves temporal reasoning and allows later audits to answer: what was known, what was assumed, what changed, and which decision is current. Cost: more records and explicit lifecycle management.

### Code comment only
Useful near implementation details, but normally too local to preserve cross-cutting alternatives, consequences, evidence provenance and supersession history.

**ENGINEERING JUDGMENT:** use ADRs selectively for decisions with material structural, interface, dependency, quality-attribute, construction/release or evolutionary consequences. Recording every trivial implementation choice creates retrieval noise and weakens the decision log.

## VALIDATION 1 — document-level adversarial review

The first block defined an adversarial decision-review oracle:

- Can a later reviewer identify the original decision question?
- Can they distinguish SOURCE/VALIDATION from ENGINEERING JUDGMENT and PROJECT DECISION?
- Can they identify assumptions and evidence limits?
- Can they reconstruct why an alternative was rejected?
- Can they tell whether the decision is current or superseded without rewriting history?
- Can they identify what new evidence would trigger reconsideration?

A minimal `context/decision/consequences` record can fail these questions while still satisfying a basic template. The Studio's stronger contract is therefore a governance synthesis for evidence-critical engineering, not a claim that AWS/Microsoft mandate every field above.

## VALIDATION 2 — bounded executable ADR-corpus governance check

Fixture: `research/architecture/fixtures/A006_adr_governance_validator.py`.

### Test Evidence Contract

- **CLAIM:** a machine-checkable repository rule can detect selected evidence-lifecycle defects without treating ADR acceptance as correctness proof.
- **SPEC/PROPERTY:** for the bounded fixture corpus, require non-empty decision question, status, evidence, assumptions, validation and reconsideration trigger; a `SUPERSEDED` record must point to a known successor; deliberately unscoped evidence labels such as `CI passed` are rejected.
- **TARGET:** a two-record synthetic ADR corpus embedded in the canonical Studio fixture. ADR-001 is superseded by ADR-002; ADR-002 is accepted while runtime acceptance remains explicitly OPEN.
- **ORACLE:** independent structural predicates implemented by `validate()`. They inspect required fields, allowed status, successor referential integrity and the deliberately bounded unscoped-evidence vocabulary.
- **ENVIRONMENT:** Python 3.13.5 on Linux, 2026-09-18. `dart` and `flutter` executables were rechecked and unavailable.
- **FAILURE CASES / deliberate mutations:** remove evidence; blank validation while leaving status Accepted; point supersession to unknown `ADR-999`; replace scoped evidence with `CI passed`.
- **OBSERVATION:** all two baseline records passed. Each of four deliberate mutants failed for its intended reason: `missing:EVIDENCE`, `missing:VALIDATION`, `broken:SUPERSEDED BY`, `unscoped:EVIDENCE`.
- **VERDICT:** PASS for the declared bounded governance properties.
- **ROOT CAUSE:** each failure is a direct structural violation of the declared corpus property; this does not diagnose whether the underlying architecture decision is technically good.
- **REPRODUCTION:** run `python3 research/architecture/fixtures/A006_adr_governance_validator.py` in a Python 3.13.5-compatible environment.
- **EVIDENCE LIMIT:** the parser is intentionally tiny, the corpus is synthetic, and the rule cannot judge rationale quality, truth of cited evidence, whether alternatives are adequate, whether a decision is architecturally significant, or whether an Accepted decision works in production. It is not a general ADR linter and is not product evidence.

### SYNTHESIS from the executable block

Governance automation is useful for **mechanically decidable omissions and referential integrity**, but cannot replace architectural review. A schema/linter can require an evidence field; it cannot establish that the evidence supports the decision. This mirrors Q001/Validation Standard: an assertion is a verdict mechanism, not proof that the expected property is correct.

The deliberate `Accepted + empty VALIDATION` mutant is particularly important: decision lifecycle and empirical validation are separate state machines. A repository can mechanically prevent their accidental collapse while leaving substantive acceptance to stronger evidence.

## CONNECTION TO PRIOR STUDIO EVIDENCE

- **A001:** change pressure determines which decisions deserve durable rationale.
- **A003:** compatibility assumptions and retained consumers are explicit decision evidence/constraints.
- **A005:** architecture descriptions are not architecture; debt/refactoring claims need observer/evolution context.
- **Q001 / VALIDATION_STANDARD:** claims require oracle/environment/evidence limits; ADR status cannot replace a validation verdict.
- **Q004:** deliberate mutation is reused here to test governance-rule sensitivity rather than application correctness.
- **S001/S004/S005:** artifact, dependency, build and release evidence must retain exact identity rather than vague `CI passed` rationale.
- **M003/M004:** platform facts are version-sensitive and should carry CHANGE WATCH/TRANSFER VALIDATION instead of being frozen as timeless architecture facts.

## RELATED DOMAIN CHECK

- Foundations: F001 direct Dart/Flutter runtime evidence remains OPEN; environment rechecked 2026-09-18 with no `dart`/`flutter` executable. No execution claim is fabricated.
- Architecture: A001/A003/A005 directly reused.
- Mobile: platform/version assumptions are a primary ADR invalidation trigger; real transfer remains OPEN.
- Data: migration, durability, source-of-truth and conflict policies are candidate architecturally significant decisions when they constrain recovery/compatibility.
- Quality: Validation Standard supplies evidence-contract discipline; Q004 deliberate mutation method transferred to governance sensitivity.
- Systems: artifact/build/security/performance evidence needs exact provenance and change-watch context; `CI passed` is intentionally rejected as insufficiently scoped evidence in the bounded fixture.
- Design Studio: considered; no design decision is being made or redefined by this internal governance mechanism.
- Web Manager: considered; no website decision is being made or redefined.
- Marketing Manager: considered; not materially relevant to this internal governance mechanism.
- Product source: no product implementation audit was required; no MintTap/LogMate implementation claim is made.

## HANDOFFS

- **TO Quality:** repository governance checks can use deliberate mutations to demonstrate sensitivity, but a passing linter is not a correctness oracle for the decision itself.
- **TO Mobile/Systems:** volatile platform/build/security facts used in decisions should carry exact source date/version/ref and explicit revalidation triggers.
- **TO Data:** migration/sync/recovery ADRs should preserve compatibility and failure assumptions plus rollback/recovery validation dependencies.
- **TO product teams (advisory):** supersede architecturally significant decisions rather than silently rewriting accepted rationale; preserve exact product/build refs when evidence comes from product validation.

## OPEN / VALIDATION / CHANGE WATCH

- CLOSED at bounded executable level: selected missing-field, accepted-vs-validation, broken-supersession and unscoped-evidence governance defects are mechanically detectable in the fixture corpus.
- OPEN: exact product transfer against a real MintTap/LogMate architecture decision; requires exact repository/ref/version/evidence date and a live decision question.
- OPEN: validation against a naturally occurring ADR corpus rather than a synthetic corpus.
- VALIDATION: Architecture Stage 1 still needs broader transfer/review evidence; the linter does not judge architectural correctness or production behavior.
- CHANGE WATCH: ADR process guidance can evolve; AWS and Microsoft sources were checked 2026-09-18.

## Current conclusion

An ADR is most useful when it preserves the conditions under which a decision was rational and the evidence needed to reconsider it. It is not architecture itself, not proof that the decision is correct, and not a mutable current-state note. The second block adds executable evidence that selected lifecycle/evidence omissions can be caught mechanically, while also demonstrating the boundary of such automation: repository structure can preserve evidence obligations, but cannot manufacture trustworthy evidence or architectural judgment.
