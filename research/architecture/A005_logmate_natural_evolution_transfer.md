# A005 — LogMate Natural Evolution / Contract-to-Implementation Transfer

Status: **TRANSFER VALIDATION — natural exact-ref product history / no product execution**  
Date: 2026-09-18  
Lead: Architecture

## Problem

The prior A005 repeated-change block explicitly left natural product history OPEN. Its bounded fixture showed that duplicated semantic ownership can admit partial migration, but synthetic evidence cannot establish how a real product coordinates a confirmed contract, implementation, tests, and documentation during evolution.

This block inspects one natural LogMate change where a previously documented View Logbook Customize V1 contract was implemented in the immediately following commit.

## Product evidence identity

- repository: `yhappcom/logmate`
- base ref: `05b4209e609ec7e9a524010339c4e0cbce0d4bb1` — `docs: finalize view logbook customize v1 contract`
- head ref: `b551ce434ad72b1895033e0f3617c73b026d40ea` — `feat(view-logbook): implement customize v1 catalog`
- relationship: head is exactly one commit ahead of base
- declared version at base: `1.0.0+1` from `pubspec.yaml`; head is the same currently inspected product line
- evidence date: 2026-09-18
- production identity: **UNKNOWN**; neither `main` nor either inspected ref is assumed to equal production.

## SOURCE / observed change

At the base ref, `docs/specs/logbook-configuration-spec.md` marks Customize V1 as a confirmed contract but explicitly says it is not implemented beyond the temporary pre-V1 mock shell. The contract fixes the zero-configuration Standard projection, nine default-ON top-level items producing ten leaves, Route as a system presentation group, a 35-item stable catalog, visible reorder, stable hidden order, system groups, Known Field naming, immediate changes, Reset semantics, and explicit OPEN persistence/Sync/schema boundaries.

The single head commit changes exactly five tracked files: `MASTER.md`, `docs/specs/logbook-configuration-spec.md`, `docs/specs/ui-contract.md`, `lib/screens/view_logbook_screen.dart`, and `test/widget_test.dart`. The implementation file changes by +861/-118 and the test file by +729/-260. The head implementation replaces the old independent-column debug seams with catalog/group-oriented state, declares the 35 catalog definitions, establishes the Standard item order, and expands renderer column definitions beyond the former nine-leaf shell. The product documentation simultaneously changes status from contract-only/pre-V1 shell to presentation-only in-memory V1 projection shell, while preserving Custom Field persistence/real ledger/Sync as NOT IMPLEMENTED.

## SYNTHESIS

This natural history supports a stronger evolutionary-architecture distinction than raw edit-count reasoning:

`confirmed semantic contract → explicit implementation boundary → coordinated code/test/doc change → preserved NOT IMPLEMENTED/OPEN boundary`.

The important architectural signal is not that five files changed or that the diff is large. It is that multiple artifacts represent different obligations around one change:

- product/domain documentation defines what the projection/configuration means and what it does not mean;
- implementation realizes the presentation/session mechanism;
- tests encode executable observer expectations;
- status documentation updates implementation truth without silently promoting persistence, Sync, calculation, or canonical-data semantics.

A coordinated multi-file change is therefore not itself evidence of harmful coupling. When files have distinct responsibilities but one externally meaningful contract changes, coordinated edits can be required and healthy. The debt question is whether the same semantic decision is independently reimplemented such that partial updates can disagree, not whether more than one artifact must change.

## CONTRADICTION / refinement of the synthetic model

The prior synthetic fixture deliberately made three consumers duplicate one policy and demonstrated a partial-update failure. This product transfer prevents over-generalizing that result:

- `many changed files => duplicated semantic ownership` is false;
- `one semantic owner => one changed file` is false;
- documentation, tests, implementation, and status records may all need coordinated change because they serve different evidence/observer roles;
- duplication becomes an evolution liability when independently editable copies can disagree about the same semantic rule, not merely when a decision is represented in multiple forms.

## VALIDATION

No Dart/Flutter executable is available in the current execution environment, so the head product tests were **not executed**. Reading a large `test/widget_test.dart` diff does not establish that tests pass, that the oracle is correct, or that the implementation satisfies the full contract.

The natural-history validation performed here is repository-structural and semantic:

1. exact base/head relationship verified;
2. declared product version at base verified;
3. base contract boundary inspected;
4. one-commit file set inspected;
5. head implementation/status changes inspected;
6. claims are limited to observed repository evolution, not runtime correctness.

## ENGINEERING JUDGMENT

For future technical-debt/evolution audits, classify coordinated-change obligations before treating edit dispersion as coupling:

1. **same semantic rule copied into multiple executable owners** — high partial-migration risk;
2. **one semantic rule represented across spec, tests, implementation and status/evidence** — coordination may be required and desirable;
3. **independent policies that happen to change together once** — no debt inference without repeated change-pressure evidence.

A useful audit asks which artifact is authoritative for each claim, which observer detects disagreement, and whether a partial update can create accepted contradictory product behavior.

## RELATED DOMAIN CHECK

- **Foundations:** F002 ownership/aliasing and F003 cost reasoning considered; no runtime claim made.
- **Architecture:** A001 change pressure, A002 ownership, A003 contracts, A005 repeated-change model and A006 evidence preservation directly reused.
- **Mobile:** the target is Flutter UI code, but direct Flutter execution is unavailable; runtime transfer remains OPEN.
- **Data:** the product explicitly keeps configuration persistence/Sync/canonical-data semantics outside this implementation boundary; this separation materially limits the claim.
- **Quality:** tests changed with the implementation, but were not executed; test presence is not PASS evidence.
- **Systems:** exact refs/version/evidence date preserved; production/release identity unknown.
- **Design Studio:** materially related interaction semantics may inform the product contract, but no Design Studio canonical file was needed to establish this repository-history mechanism and none was edited.
- **Web Manager / Marketing Manager:** not materially relevant to this contract-to-implementation evolution mechanism.
- **Product source:** exact LogMate base/head refs inspected; product repository remains implementation truth.

## HANDOFFS

- **Quality:** when Flutter execution becomes available, run the exact head tests and deliberately mutate one contract obligation (for example stable hidden order or group projection) to establish oracle sensitivity rather than inferring quality from test volume.
- **Mobile:** exact-ref Flutter execution should validate that catalog/group/session behavior survives framework/runtime behavior; preserve exact SDK/ref and device/build identity.
- **Product teams:** do not classify a change as architectural debt from changed-file count. First distinguish semantic duplication from legitimate spec/test/implementation/evidence coordination.
- **Architecture/A006:** this natural change is a candidate decision-evidence corpus, but it is not automatically an ADR and should not be relabeled as one.

## OPEN / TRANSFER VALIDATION

- **OPEN:** direct Dart/Flutter execution of either product ref.
- **OPEN:** whether the changed tests fully discriminate every confirmed Customize V1 semantic.
- **OPEN:** persistence/Sync/configuration-schema evolution once those product decisions are implemented.
- **OPEN:** repeated natural product history across multiple later requirement generations; this block observes one contract-to-implementation transition, not long-horizon maintenance cost.
- **TRANSFER VALIDATION:** apply the same coordination-obligation classification to a future persisted-schema or release change where partial publication has correctness consequences.

## Conclusion

A005's named exact-ref product-evolution gap is advanced with natural LogMate history. The evidence refines the synthetic model: coordinated multi-file evolution can be healthy when spec, tests, implementation and status carry different responsibilities around one semantic contract. Technical-debt inference requires evidence of independently editable semantic duplication or repeated coordination failure, not edit dispersion alone. Runtime correctness and product PASS remain unestablished.