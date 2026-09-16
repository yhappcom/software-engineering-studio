# Quality Specialist Status

Track: Quality, Testing & Reliability
Prefix: `Q###`
State: **Stage 1 — READY / NOT YET PASSED**
Last sync: 2026-09-16

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Initial queue
- `Q001` — Correctness, specification, invariants, test oracles and reproducibility.
- `Q002` — Unit/integration/system/e2e test boundaries and trade-offs.
- `Q003` — Determinism, nondeterminism, concurrency and flaky-test mechanics.
- `Q004` — Property-based/model-based testing and invariant checking.
- `Q005` — Debugging, fault isolation, observability and crash analysis.
- `Q006` — Fault injection, recovery verification and regression governance.

## Gate requirement
Foundation PASS requires tests that can fail for the right reason, at least one reproduced defect/failure path, root-cause reasoning, and explicit distinction between test coverage/activity and actual correctness evidence.

## Dependencies / handoffs
Quality is cross-cutting and should challenge all other tracks. It does not own their semantics; it owns evidence quality, reproducibility and failure/recovery verification.

## Current product relevance
Critical to financial/calculation behavior in MintTap and data-loss/synchronization/import risks in LogMate. Product validation requires exact repository refs and specifications.

## Next work
`Q001` should participate early in F001/D001/M001 so executable learning does not become demo-only evidence.
