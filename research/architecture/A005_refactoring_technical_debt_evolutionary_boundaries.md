# A005 — Refactoring, Technical Debt & Evolutionary Architecture Boundaries

Status: **IN STUDY — first integrated Foundation block complete / track not passed**  
Date: 2026-09-17  
Lead: Architecture

## Problem and scope

Architecture Stage 1 had strong evidence for information hiding, ownership/dependency direction, and contracts, but still lacked the roadmap boundary between architecture, design, implementation, refactoring, and technical debt. This block closes that conceptual gap without treating every cleanup as architecture or every imperfection as debt.

## SOURCE

- ISO/IEC/IEEE 42010:2022 is the current architecture-description standard. It explicitly distinguishes an entity's architecture from an architecture description. This matters because a diagram/document is evidence about architecture, not the architecture itself.
- CMU SEI describes software architecture as design decisions concerning overall system structure and behavior, used to reason about qualities such as modifiability, availability, and security. SEI's established structures formulation focuses on elements, externally visible properties, and relationships; private details that do not affect interaction are implementation details rather than automatically architectural.
- Martin Fowler defines refactoring as changing internal structure to make software easier to understand/modify without changing observable behavior, normally through small behavior-preserving transformations.
- CMU SEI defines technical debt as an expedient design/construction approach that creates a technical context in which future work can cost more; debt is contingent on future evolution and is not synonymous with any ugly code or defect.

## SYNTHESIS — architecture vs design vs implementation

Use significance and externally consequential structure rather than file/class size as the boundary:

1. **Architecture**: structures, relationships, ownership/dependency/trust/runtime/data boundaries and externally relevant properties/decisions needed to reason about system qualities and evolution.
2. **Design**: solution choices that shape responsibilities, interfaces, algorithms and collaborations, including choices below the system-wide architectural level.
3. **Implementation**: concrete realization details whose replacement does not materially change the retained architectural/design contract.

These are nested reasoning scopes, not mutually exclusive artifact types. A database schema, queue policy, package boundary or function can become architecturally significant when other elements rely on its externally visible properties or when it materially constrains qualities/evolution. Conversely, a class diagram is not automatically architecture.

## SYNTHESIS — refactoring boundary

`refactoring != feature change != bug-fix semantics != migration by default`.

A refactoring may change internal names, decomposition or even an interface when all controlled callers move with it, but its defining oracle is retained observable behavior for the relevant observer set. For published APIs, persisted schemas, network protocols, telemetry contracts, performance/SLOs, security boundaries or user-visible failure semantics, the observer set may be broader than unit-test return values.

Therefore tests are necessary evidence but do not define behavior by themselves. A weak test suite can remain green while a supposedly internal restructuring changes a real contract.

## EXECUTABLE VALIDATION — behavior-preserving restructuring vs semantic-change mutant

Fixture: `research/architecture/fixtures/A005_refactoring_behavior_boundary.py`

### Test Evidence Contract

- **CLAIM:** structural tidiness alone does not make a change a refactoring; retained observable behavior is the discriminator.
- **PROPERTY/ORACLE:** three independently declared cases require `USD 110.00`, `USD 0.00`, and `ERROR:negative principal`.
- **TARGET:** legacy implementation, split-calculation refactoring, and deliberate clamp mutant.
- **ENVIRONMENT:** Python 3.13.5; Linux 6.18.44 x86_64, glibc 2.41; execution date 2026-09-17.
- **OBSERVATION:** legacy and refactored implementations both matched all three oracle cases. The clamp mutant matched normal/zero but changed negative-input behavior to `USD 0.00`; `mutant_failures=['negative']`.
- **VERDICT:** bounded behavior-preserving refactoring PASS; deliberate semantic-change mutant DETECTED.
- **ROOT CAUSE:** the mutant altered the public failure policy while appearing structurally simple. The defect is not structural complexity but an unacknowledged contract change.
- **EVIDENCE LIMIT:** this proves only the declared observer set. It does not prove performance, timing, logging, exception type hierarchy, concurrency, persistence, Dart/Flutter behavior, or production equivalence.

## TECHNICAL DEBT MODEL

Treat a debt item as a concrete contingent liability, not a label of dislike:

`artifact/decision → short-term benefit/context → future change scenario → extra cost/risk (“interest”) → remediation option/principal → evidence/uncertainty`.

### CONTRADICTION to common shortcuts

- `code smell => technical debt` is invalid: a smell is a diagnostic signal, not proof of future-change liability.
- `bug => technical debt` is invalid: defects and debt can interact but are different categories.
- `old code => technical debt` is invalid without an evidenced costly evolution context.
- `refactor => debt repaid` is invalid unless the targeted liability is actually reduced and behavior/contracts remain acceptable.
- `architecture diagram => architecture` is invalid; 42010 distinguishes architecture from its description.

### ENGINEERING JUDGMENT

Debt priority should depend on plausible change pressure, consequence severity, frequency, coupling radius, recovery/rewrite risk, and remediation cost—not aesthetic discomfort alone. Intentional debt can be rational when its short-term value exceeds expected carrying cost and the risk is visible/manageable. Unknown future work should remain uncertainty rather than fabricated interest estimates.

## CONNECTION TO PRIOR STUDIO EVIDENCE

- **A001:** change pressure and carrying cost provide the mechanism for identifying future-cost liability.
- **A002:** ownership/dependency direction identifies where a local expedient can propagate change cost.
- **A003:** observable contracts define what a refactoring must preserve and when an evolution is instead a compatibility change.
- **Q001/Q004/Q006:** independent oracles, mutation sensitivity and regression evidence are stronger than “tests stayed green”.
- **D003:** persisted-schema evolution is not ordinary internal refactoring when old readers/writers/data are part of the observer set.
- **S001:** build/artifact identity means behavior-preservation evidence attaches to an exact artifact/environment, not source text in the abstract.

## RELATED DOMAIN CHECK

- Foundations: F002 aliasing/lifetime and F003 complexity considered; internal changes can alter resource/identity behavior even when nominal outputs match.
- Architecture: A001-A003 directly reused.
- Mobile: lifecycle/plugin/platform behavior can enlarge the observer set; direct Flutter/mobile runtime remains OPEN.
- Data: schema/durability/migration contracts can turn an apparently internal restructure into externally consequential evolution.
- Quality: Validation Standard used for executable evidence and mutant sensitivity.
- Systems: security/performance/build properties can be architectural observables; exact artifact provenance remains required for release claims.
- Design Studio: not materially changed; user-visible interaction/recovery semantics remain Design-owned and are part of observable behavior when relevant.
- Web Manager: not materially changed; PWA/build/deploy architecture may later transfer this model.
- Marketing Manager: not materially relevant to this Foundation block.
- Product source: no product audit was required; no MintTap/LogMate implementation claim is made.

## HANDOFFS

- **TO Quality:** refactoring tests should declare the observer set and include deliberate semantic mutants where risk warrants; green tests alone do not establish behavior preservation.
- **TO Data:** classify schema/data migrations separately from internal refactoring whenever persisted compatibility/durability is observable.
- **TO Systems:** include performance/security/artifact properties in the observer set when they are contractual or risk-significant.
- **TO product teams (advisory):** record technical-debt items as concrete future-change liabilities with context and consequence, not generic cleanup backlogs.

## OPEN / VALIDATION / CHANGE WATCH

- OPEN: larger evolutionary-architecture evidence showing debt principal/interest over repeated changes rather than one bounded fixture.
- OPEN: exact Dart/Flutter transfer; `dart` and `flutter` executables remain unavailable in the current environment.
- VALIDATION: future product debt claims require exact repository/ref/version/evidence date and an evidenced future-change consequence.
- CHANGE WATCH: ISO/IEC/IEEE 42010:2022 is current as checked 2026-09-17; ISO/IEC/IEEE DIS 42024 architecture fundamentals is under development and should be rechecked before adopting terminology from it.

## Current conclusion

Architecture is not synonymous with diagrams, layers, or “important code.” Refactoring is a behavior-preserving restructuring discipline, not a euphemism for arbitrary rewrite. Technical debt is a contingent future-change liability, not a synonym for defect, smell, age, or aesthetic dissatisfaction. Together with A001-A003, this closes the principal Stage-1 conceptual gap around architecture/design/implementation and refactoring/debt, but Architecture remains NOT PASS pending broader executable/transfer evidence and the remaining queue.
