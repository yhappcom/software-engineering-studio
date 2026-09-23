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
**IN STUDY — two integrated Foundation blocks complete.** Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`. Shared-memory schedule failure plus deterministic timeout/complete/cancel/retry evidence retained.

### Q004 — Property/model-based testing, invariant checking, mutation sensitivity and search strength
**IN STUDY — TWO EXECUTABLE BLOCKS COMPLETE.** Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`, `research/quality/Q004_mutation_sensitivity_search_strength.md`. Broader runtime/platform transfer remains OPEN.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — process-crash recovery + CI verdict-propagation failure/isolation/repair/regression + complete selected-pattern workflow inventory + natural false-green repair + continuing semantic classification.**  
Canonical: `research/quality/Q006_fault_injection_recovery_regression_governance.md`, `research/quality/Q006_real_crash_recovery_oracle_transfer.md`, `research/quality/Q006_ci_pipeline_exit_status_oracle_integrity.md`, `research/quality/Q006_complete_workflow_verdict_risk_inventory.md`, `research/quality/Q006_semantic_verdict_path_classification_2.md`.

The retained hosted Bash discriminator established that evidence preservation and verdict propagation are independent controls. Repaired exact head `bd763b301752b3adebd36b963c06d064aec94ca8`, run `35792678785`, observed control/treatment pipeline statuses 0/23 while both logs preserved the same producer failure payload.

The checkout-local inventory replaced incomplete GitHub code search. Exact head `d573b47f05a1d5f65daea94d4133dcc221973d2a`, run `35837301494`, artifact `10739703444`, directly enumerated 29 workflow files and 131 selected lexical risk hits. **VALIDATION:** this is a complete selected-pattern inventory at that exact ref, not a semantic-correctness PASS.

Semantic review found a genuine false-green path in `s005-attestation-verification-boundary.yml`: positive attestation query/exact-verification checks used `continue-on-error`, but the aggregate oracle asserted only the two negative controls. Commit `6216003dc4d42c1ea2156500bcc1df1d404c045d` added fail-closed assertions for all four required outcomes. **VALIDATION:** run `35843352058`, job `107123462773`, exact repaired head, completed failure with the final aggregate-verdict step failing after diagnostic checks ran. This is intended fail-closed regression evidence: a required positive failure is no longer silently converted to a green job. It does not resolve the separate historical-attestation availability root cause.

A further exact-ref semantic pass at `a87f71d5a4cb1632c21426aa6a6bf4b84093c5b9` classified additional high-risk paths without inventing defects: M003 Keystore's trap/`exit 0` preserves the original oracle status in outputs and is followed by an unconditional fail-closed consumer; M003 first-launch `tee` paths are protected by `pipefail` while `|| true` is confined to diagnostics immediately before explicit failure; M003 one-time expiry uses `continue-on-error` for evidence preservation but separately rejects harness failure and non-success emulator outcome; and M006 Chromium service-worker validation supplies a non-pattern sample whose semantic validators are direct fatal commands. **ENGINEERING JUDGMENT:** these are valid evidence-preservation/status-handoff patterns at the inspected wrapper boundary, not new runtime PASSes. `INCONCLUSIVE_WINDOW_EXHAUSTED` must never be promoted to evidence that expiry occurred.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q001-Q006 have substantial Foundation evidence and Q006 now includes synthetic and natural false-green mechanisms, a repository-wide selected-pattern inventory, a semantic repair/regression, additional safe-path classifications, and an initial non-pattern verdict sample. Repository-wide semantic classification, broader non-pattern sampling, GitHub-expression/third-party-action propagation review, non-Bash/platform transfer, physical/mobile/backend/storage-power and production release-gate evidence remain incomplete.

## Dependencies / handoffs
- **Foundations:** direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution exist; older SDK-unavailable notes are stale.
- **Architecture:** contracts/invariants and externally meaningful progress state supply semantic recovery oracles.
- **Mobile:** M006 supplied the first natural false-green case; M003 demonstrates that normalized fixture exit is acceptable only when original status is preserved and consumed fail-closed. Navigation/property lifetime remains separate from shell verdict propagation.
- **Data:** recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** S005 supplied the second natural verdict-propagation defect. Diagnostic continuation is acceptable only when every required positive/negative outcome participates in a fail-closed aggregate verdict.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical evidence there changes this bounded Quality method.

## CHANGE WATCH / OPEN
- Semantic classification of the remaining selected-pattern hits remains OPEN; 131 lexical hits are not 131 defects.
- Broader verdict-bearing commands outside the selected lexical patterns require sampling.
- GitHub-expression conditions and third-party action output/outcome propagation require semantic review where they participate in acceptance.
- PowerShell/cmd/other CI-shell transfer remains OPEN.
- Q004 broader framework/platform transfer remains OPEN.
- Q006 actual Android/iOS process death, backend/cursor batches, combined network+process faults, filesystem/device/power faults and production release-gate evidence remain OPEN.

## Next work
Continue the same Q006 professional boundary until repository semantic classification is credible. Prioritize remaining verdict-bearing selected-pattern paths plus non-pattern acceptance commands and GitHub-expression/action-output boundaries. Repair and hosted-regress any additional genuine defect before considering semantic-audit closure.