# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 refactoring/debt + A006 evidence-preserving decision lifecycle first integrated blocks complete |
| Mobile | Stage 1 IN STUDY — M001-M004 first professional/model boundaries complete; direct Flutter/native transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated with persistence/migration/cache/restore/sync evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 executable counterexample/shrinking evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### A006 — Evidence-preserving architecture decisions and ADR lifecycle
Canonical: `research/architecture/A006_evidence_preserving_architecture_decisions.md`

Current AWS Prescriptive Guidance and Microsoft Azure Well-Architected guidance establish ADR context/rationale/options/decision/consequences/status and supersession as durable decision-history concerns. Studio synthesis strengthens this for evidence-critical engineering: preserve exact evidence/ref, assumptions/uncertainty, validation status and reconsideration triggers when they materially affect later evaluation.

Critical separation: `ADR Accepted != validation PASS`. A decision can be accepted under current constraints while transfer/production validation remains OPEN. Accepted decision history should be superseded rather than silently rewritten when later evidence changes the choice, otherwise the repository loses whether the original decision was wrong or its assumptions later changed.

A document-level adversarial oracle now asks whether a future reviewer can reconstruct the decision question, distinguish evidence from judgment/decision, identify assumptions/evidence limits, recover rejected-option rationale, determine current/superseded status and identify reconsideration triggers. This is governance/model evidence, not runtime/product evidence.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 now cover change pressure, ownership/dependency, semantic contracts, refactoring/debt and evidence-preserving decision lifecycle.
- **Mobile:** M001-M004 runtime/state, lifecycle/process/background, storage/permission/security and plugin/native boundaries retained; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 includes executable generated counterexample/shrinking.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Quality:** ADR status cannot replace a validation verdict; decision records should link evidence with its oracle/environment/limits.
- **Mobile/Systems:** volatile platform/build/security facts used in decisions need exact version/ref/date plus CHANGE WATCH/TRANSFER VALIDATION.
- **Data:** migration/sync/recovery decisions should preserve compatibility/failure assumptions and recovery validation dependencies.
- **Design Studio:** interaction semantics remain Design-owned; Engineering ADRs should link exact design contracts rather than silently redefine them.
- **Web Manager:** PWA/browser/hosting decisions should link current web requirements and versioned technical evidence; no canonical web files changed.
- **Marketing Manager:** not materially relevant to this A006 Foundation block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available.

A006 removes the main untouched Architecture decision-governance boundary at first professional level. Current strongest independent candidates are:
1. `M005` cross-platform architecture, portability and platform divergence — next untouched Mobile boundary with high LogMate/native/PWA leverage, though real transfer remains runtime-constrained;
2. `Q004` deliberate mutation sensitivity plus exhaustive-vs-generated comparison — executable and capable of strengthening test-method evidence without Dart/Flutter;
3. `A006` executable ADR-corpus governance checker — useful cross-track reuse, but lower immediate product leverage than M005 unless a live decision-log need appears;
4. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter platform-channel/plugin registration, background-isolate, federated-plugin and native API behavior are version-sensitive.
- Android storage/permission/backup behavior and Apple Data Protection/Keychain behavior are platform/version sensitive.
- Deployment-platform rollback semantics and app-store/browser delivery policies are service/version sensitive.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- ADR process guidance checked 2026-09-18; operational guidance can evolve.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
