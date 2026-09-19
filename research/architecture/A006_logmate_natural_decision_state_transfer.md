# A006 — LogMate Natural Decision-State Transfer

Status: **IN STUDY — NATURAL PRODUCT DECISION CORPUS TRANSFER ADDED / NOT ADR EQUIVALENCE**  
Evidence date: 2026-09-20

## Why this block
Balance Loop selected A006 because the stronger Mobile/Systems runtime rungs currently require platform/device or authorized private-source execution, while LogMate contains a natural, exact-ref product decision/state corpus that can test whether A006's evidence-preserving decision model survives outside the synthetic ADR fixture. This does not substitute reading for executable correctness: A006 already has executable governance-sensitivity evidence; this block is a natural product-history transfer and deliberately does not award PASS.

## Product identity
`yhappcom/logmate → main history → 05b4209e609ec7e9a524010339c4e0cbce0d4bb1 → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 at head → evidence date 2026-09-20`.

Production identity is unknown. Default branch is not assumed production.

## SOURCE / NATURAL CORPUS
At both inspected refs, `MASTER.md` declares itself the current product-state authority and defines separate vocabularies for product decision state (`CONFIRMED`, `OPEN`, `DEFERRED`, `OUT OF SCOPE`, `SUPERSEDED`) and implementation/evidence state (`IMPLEMENTED`, `NOT IMPLEMENTED`, `POC VERIFIED`, `POC FAILED`, `POC INCONCLUSIVE`). It also explicitly warns that past POC PASS is not current-product PASS.

The head `pubspec.yaml` declares `1.0.0+1`.

Git history establishes that `b551ce4...` is exactly one commit ahead of `05b4209...`, commit message `feat(view-logbook): implement customize v1 catalog`. The compare contains five changed files: `MASTER.md`, two product specs, `lib/screens/view_logbook_screen.dart`, and `test/widget_test.dart`.

## TRANSFER VALIDATION
The natural history preserves a distinction that the A006 model predicts is necessary:

1. **Decision truth and implementation truth evolve on separate axes.** At the base ref, the Customize V1 catalog/group behavior is already `CONFIRMED` while implementation is explicitly absent beyond the temporary shell. At the head, the same product contract remains confirmed while the mock/session projection becomes `IMPLEMENTED` for the bounded presentation behavior.
2. **Implementation progress does not silently close unrelated OPEN decisions.** The head records the 35-item catalog, stable hidden order, visible reorder and system groups as implemented, while Custom Field creation/rename/value UI, configuration persistence/Sync, canonical schema details, calculations/local ledger and other unresolved contracts remain explicitly NOT IMPLEMENTED or OPEN.
3. **Evidence scope is preserved rather than upgraded by adjacency.** The master distinguishes mock/session presentation implementation from persistence, calculation, Sync, Backup/Export and production/runtime verification. A large UI/test change therefore does not automatically become evidence for those other claims.
4. **Coordinated multi-file change is not itself duplicated ownership.** The same semantic change legitimately updates product-state authority, narrower specs, implementation and tests. This reinforces A005's earlier correction: changed-file count is not a technical-debt oracle.

**SYNTHESIS:** an evidence-preserving decision system needs at least two independently updateable dimensions when product work can have a stable semantic decision before implementation exists: decision status and implementation/evidence status. Collapsing them into one `done/not done` field loses information and encourages false closure.

**ENGINEERING JUDGMENT:** LogMate's natural status vocabulary is a useful project-specific decision ledger, but it is not automatically an ADR system. It captures current authority, unresolved decisions and implementation/evidence boundaries well; this inspection does not establish that every architecturally significant decision preserves alternatives, rationale, consequences, supersession links and validation triggers at ADR-level completeness.

## CONTRADICTION / REFINEMENT
A006 previously left a `natural ADR-corpus validation` gap. The inspected LogMate corpus is natural decision-governance evidence but is **not an ADR corpus**. Relabeling it as ADR evidence would violate the Studio's evidence-boundary rules. The gap is therefore refined into two separate questions:

- natural product decision-state transfer: **advanced by this block**;
- natural ADR lifecycle corpus with explicit rationale/alternatives/consequences/supersession semantics: **OPEN**.

## VALIDATION / EVIDENCE LIMIT
This block is repository-history inspection, not runtime validation. No claim is made that the implemented Customize behavior is correct at runtime, that tests pass, that `main` is production, or that the decision text is substantively correct. The existing A006 executable validator remains the bounded evidence that malformed governance records can be mechanically rejected; this natural transfer instead tests whether the model describes a real product history without forcing that history into the synthetic schema.

## RELATED DOMAIN CHECK
- Foundations: not materially determinative; no runtime-mechanism claim is made.
- Architecture: lead track. A005 natural evolution evidence is directly relevant and is reinforced, not duplicated.
- Mobile: implementation includes Flutter UI behavior, but no Flutter/runtime verdict is inferred.
- Data: OPEN persistence/Sync/schema decisions remain explicitly separate from presentation implementation; this is a positive ownership boundary.
- Quality: test-file change is not treated as test execution or correctness evidence.
- Systems: artifact/release/production identity remains unknown; source history is not release provenance.
- Design Studio: product presentation semantics may depend on design contracts, but this block audits decision-state mechanics rather than redefining visual/interaction truth; no Design Studio files changed.
- Web Manager: not materially relevant to this product decision-state transfer.
- Marketing Manager: not materially relevant.
- Product: exact refs inspected as recorded above; no LogMate files edited.

## HANDOFFS
- **Architecture → Product governance:** preserve decision status separately from implementation/evidence status when a contract can be confirmed before implementation. Do not auto-close OPEN schema/Sync/data/runtime questions because adjacent UI work ships.
- **Architecture → Quality:** a changed test file is evidence of coordinated evolution, not a passing test. Runtime/test execution needs its own exact-ref evidence.
- **Architecture → Data/Mobile/Systems:** the natural corpus demonstrates useful explicit boundaries: presentation implementation must not silently promote persistence/Sync, platform runtime, or release claims.

## OPEN / CHANGE WATCH
- Natural ADR lifecycle corpus with explicit alternatives/rationale/consequences/supersession remains OPEN.
- Exact-ref Flutter test/runtime execution for `b551ce4...` remains outside this block.
- Long-horizon product history with multiple supersession cycles remains OPEN.
- Product decision vocabulary is project-specific and should not be generalized as a universal ADR schema without transfer validation.
