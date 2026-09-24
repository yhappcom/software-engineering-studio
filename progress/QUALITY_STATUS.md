# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-24

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Current evidence

### Q001 — Correctness, specification, test oracle and reproducibility
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Canonical: `research/quality/Q001_correctness_specification_oracle_reproducibility.md`.

### Q002 — Test levels, evidence boundaries and trade-offs
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`.

### Q003 — Determinism, nondeterminism, concurrency and flaky-test mechanics
**IN STUDY — two integrated Foundation blocks complete.** Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`.

### Q004 — Property/model-based testing, invariant checking, mutation sensitivity and search strength
**IN STUDY — TWO EXECUTABLE BLOCKS COMPLETE.** Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`, `research/quality/Q004_mutation_sensitivity_search_strength.md`.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — repository semantic CI audit; delegated nonzero causality, immutable pinned-action regression, same-workflow expression/job-output composition, and reusable-workflow output transfer VALIDATED at bounded hosted targets.**  
Canonical includes `research/quality/Q006_complete_workflow_verdict_risk_inventory.md`, `research/quality/Q006_third_party_action_verdict_boundary.md`, `research/quality/Q006_expression_output_verdict_composition.md`, and `research/quality/Q006_reusable_workflow_output_verdict_boundary.md`.

Retained evidence includes the hosted Bash verdict discriminator, the exact-head 29-workflow/131-hit selected-pattern inventory, the repaired S005 natural false-green aggregate-verdict defect, and the causal third-party action control.

**VALIDATION — causal strengthening:** exact head `91f4e5de13974d724b5d46bfbd801ab6af4ed721`, run `35942964741`, job `107454700986`, plus durable artifact `10785418174`, establishes that the delegated script reached its intentional `exit 37` path and the action exposed `outcome=failure`; provisioning-before-script cannot satisfy the same combined oracle.

**SOURCE / PROVENANCE SNAPSHOT:** fresh upstream Git-reference inspection on 2026-09-24 resolves `reactivecircus/android-emulator-runner` annotated tag `v2` to tag object `4c44018e59b437e86cdfc41da381398f93ed8808`, targeting commit `a421e43855164a8197daf9d8d40fe71c6996bb0d`. This is current observed resolution, not proof of historical run resolution.

**REPAIR + VALIDATION — immutable control:** Studio commit `7101e179449d5a222d6c8d4d16a96292526333eb` pins the Q006 causal control to exact action commit `a421e43855164a8197daf9d8d40fe71c6996bb0d`. Exact pinned run `35951572264`, job `107481046377`, completed success. Artifact `10788483491`, digest `sha256:4a6697445957fd4b107cd77178bcefcf9edca00986b253e01ffef568d3285a31`, was directly inspected and contains `Q006_INTENTIONAL_DELEGATED_FAILURE_REACHED`; the independent wrapper-outcome assertion also completed.

**VALIDATION — expression/job-output composition:** exact head `6e0fc7cbac5e97a55c14f40c136f20bb48b33316`, run `35960071095`, producer job `107506554735`, acceptance job `107506578077`, completed success. Producer job success coexisted with exported `semantic_verdict=FAIL`; downstream semantic acceptance must explicitly validate the output.

**NEW VALIDATION — reusable workflow output transfer:** exact caller head `ac6fee0a185912ecefd642a381c787d265496c51`, run `35964842513`, called job `107521033912`, acceptance job `107521051965`, completed success on GitHub-hosted Ubuntu 24.04.5 / runner image `20260920.314.1`. The called reusable workflow itself succeeded while exporting `semantic_verdict=FAIL`. Direct acceptance-job logs show `CALLED_RESULT=success`, `SEMANTIC_VERDICT=FAIL`, intentional semantic acceptance exit `1`, downstream `CONTROL_OUTCOME=failure`, and terminal marker `Q006_REUSABLE_OUTPUT_FAIL_CLOSED_PASS`. This closes only the non-matrix same-repository reusable-workflow boundary. Canonical: `research/quality/Q006_reusable_workflow_output_verdict_boundary.md`.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q006 now covers shell/process propagation, causal third-party wrapper propagation, same-workflow semantic output composition, and reusable-workflow semantic output transfer. Historical resolved action identity, remaining natural semantic classification, matrix/skipped-output paths, non-Bash/action-type transfer and production release-gate evidence remain incomplete.

## Dependencies / handoffs
- **Foundations:** direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution exist; historical SDK blocker is stale.
- **Architecture:** exported CI verdicts are interface values distinct from transport success, including across reusable-workflow boundaries.
- **Mobile:** M002 supplies the representative delegated action boundary; this block does not modify or revalidate Android process-death behavior.
- **Data:** recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** binary release/security reusable workflows should preferably fail internally on required semantic failure; otherwise callers must explicitly validate verdict outputs. Historical action identity remains a supply-chain provenance gap.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this bounded CI-verdict mechanism.

## CHANGE WATCH / OPEN
- Exact resolved action identity for historical causal and M002 runs remains OPEN; do not infer it from current tag state.
- Remaining selected-pattern semantic classification and natural verdict-bearing non-pattern paths remain OPEN.
- Matrix reusable-workflow output aggregation, skipped/redacted outputs, cancellation, cross-repository reusable workflows, PowerShell/cmd/other action-type transfer and production release-gate evidence remain OPEN.

## Next work
Return to Balance Loop. S007 exact-product transfer remains higher live LogMate leverage when implementation becomes available. If it is still unavailable, do not repeat equivalent non-matrix output controls; prefer matrix/skipped-output behavior, a natural repository defect, cross-repository transfer, or a production-oriented release gate.
