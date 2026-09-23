# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-23

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
**IN STUDY — repository semantic CI audit; third-party-action executable negative control now committed, hosted observation pending.**  
Canonical includes `research/quality/Q006_complete_workflow_verdict_risk_inventory.md` and `research/quality/Q006_third_party_action_verdict_boundary.md`.

Retained evidence includes the hosted Bash verdict discriminator, the exact-head 29-workflow/131-hit selected-pattern inventory, and the repaired S005 natural false-green aggregate-verdict defect. These remain bounded evidence, not repository-wide correctness PASS.

Third-party action propagation is a distinct non-pattern class. M002 delegates a verdict-bearing oracle to `reactivecircus/android-emulator-runner@v2`; source inspection supports fail-closed propagation but the moving tag remains a provenance dependency.

**NEW VALIDATION WORK:** commit `9ea9c97838d443c8fa81b04729e0447aee54c175` adds `q006-third-party-action-nonzero-propagation.yml`. It intentionally delegates `exit 37` through the same action and then requires the GitHub step `outcome` to be `failure`. The control also requires later log inspection for `Q006_INTENTIONAL_DELEGATED_FAILURE`, because emulator provisioning failure would otherwise be an alternative cause of the same action outcome. Immediately after introduction no Actions run was yet returned for the head, so runtime PASS is explicitly withheld.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. The Q006 semantic-audit boundary has advanced from source-only third-party wrapper analysis to an executable negative-control design, but hosted observation, exact resolved action identity, remaining semantic classification, broader non-pattern/GitHub-expression review, non-Bash transfer and production release-gate evidence remain incomplete.

## Dependencies / handoffs
- **Foundations:** direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution exist; historical SDK blocker is stale.
- **Architecture:** contracts/invariants and externally meaningful progress state supply semantic recovery oracles.
- **Mobile:** M002 supplies the representative delegated action boundary; the new control does not revalidate Android process-death behavior.
- **Data:** recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** action identity/pinning remains material supply-chain provenance; a runtime control cannot make moving `@v2` immutable.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this bounded CI-verdict mechanism.

## CHANGE WATCH / OPEN
- Hosted execution of `q006-third-party-action-nonzero-propagation.yml` must reach the intentional marker and expose action `outcome=failure` before PASS.
- Exact resolved `reactivecircus/android-emulator-runner@v2` commit identity remains OPEN.
- Remaining selected-pattern semantic classification and broader verdict-bearing non-pattern/GitHub-expression/action-output paths remain OPEN.
- PowerShell/cmd/other CI-shell transfer, physical/mobile/backend/storage-power and production release-gate evidence remain OPEN.

## Next work
First inspect the hosted negative-control run when available; distinguish delegated-script failure from provisioning failure. If valid, record exact head/run/job/action identity and close only that wrapper-propagation gap. Then continue GitHub-expression/action-output and remaining semantic verdict-path review.
