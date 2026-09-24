# Q006 — GitHub Expression / Job-Output Verdict Composition Boundary

Date: 2026-09-24
Lead: Quality
Status: **IN STUDY — HOSTED EXPRESSION/JOB-OUTPUT VERDICT COMPOSITION VALIDATED AT BOUNDED TARGET**

## Problem

A CI job can complete successfully while emitting a semantic verdict such as `FAIL` through `$GITHUB_OUTPUT`. A downstream job that checks only transport/execution state (`needs.<job>.result == success`) can therefore accept a semantically failed producer. This is a different acceptance-path class from shell exit propagation or third-party action wrapper propagation.

## SOURCE

Current GitHub Actions documentation checked 2026-09-24 establishes:

- `jobs.<job_id>.outputs` exposes job outputs to downstream jobs;
- `needs.<job_id>.outputs.<name>` carries those values and `needs.<job_id>.result` separately reports `success`, `failure`, `cancelled`, or `skipped`;
- step `continue-on-error: true` can leave a failed step with `outcome=failure` and corrected `conclusion=success`;
- `if` expressions have implicit status-check behavior unless an explicit status function changes it.

Primary sources:
- https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- https://docs.github.com/en/actions/reference/workflows-and-actions/expressions
- https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs

## SYNTHESIS

Execution transport and semantic acceptance are separate dimensions.

`producer job success` means the producer job executed without an uncorrected failing step. It does **not** imply that an arbitrary semantic value exported by that job is acceptable.

Therefore, when a workflow exports a verdict-bearing output, the downstream acceptance predicate must explicitly consume and validate that output. Checking only `needs.<producer>.result == success` is insufficient whenever the producer intentionally represents domain failure as data rather than process failure.

This complements Q006's prior third-party-action finding:

1. producer/oracle semantics;
2. wrapper/step failure propagation;
3. job execution result;
4. output/value transport;
5. downstream semantic acceptance.

A green state at one layer does not imply green at the next.

## Executable control

Workflow:

`.github/workflows/q006-expression-output-verdict-composition.yml`

Exact control head:

`6e0fc7cbac5e97a55c14f40c136f20bb48b33316`

The producer intentionally exits successfully while emitting:

- `semantic_verdict=FAIL`
- `diagnostic_verdict=PASS`

The downstream acceptance job independently checks:

1. `needs.producer.result == success` — transport/execution success;
2. a weak acceptance control that sees producer success but rejects when it actually checks `semantic_verdict == PASS`;
3. the failed control's `steps.<id>.outcome == failure` and corrected `conclusion == success`;
4. a separate fail-closed semantic-output assertion that must reject the `FAIL` value.

## VALIDATION — hosted observation

Exact head: `6e0fc7cbac5e97a55c14f40c136f20bb48b33316`
Workflow run: `35960071095`
Producer job: `107506554735`
Acceptance job: `107506578077`
Environment: GitHub-hosted `ubuntu-latest`
Evidence date: 2026-09-24

The run completed `success`. The producer job completed `success`; both output-emitting steps completed successfully. The dependent acceptance job also completed `success`.

Within the acceptance job:

- `Require producer transport success` completed;
- `Demonstrate transport success is not semantic acceptance` was intentionally run under `continue-on-error` and the following independent assertion completed, requiring its raw `outcome=failure` and corrected `conclusion=success`;
- `Fail closed on semantic output` likewise intentionally rejected the semantic `FAIL` value under `continue-on-error`;
- `Require fail-closed oracle to reject` completed and requires the raw failure/corrected-success pair before emitting the final PASS marker.

**VALIDATION verdict:** a producer job can be terminally successful while transporting an explicitly failing semantic verdict. Downstream acceptance that cares about that semantic property must validate the verdict-bearing output; job transport success alone is not a sufficient oracle.

This is a bounded GitHub Actions control. It does not establish repository-wide semantic correctness.

## Failure model / limits

This control targets semantic verdict represented as job output while the producer process/job succeeds. It does not establish:

- reusable-workflow output behavior;
- matrix output collisions/order;
- secret-redacted/skipped outputs;
- cancelled/skipped producer semantics;
- PowerShell/cmd transfer;
- third-party action outputs;
- production release-gate correctness.

## RELATED DOMAIN CHECK

- Foundations: process/job completion versus application-level result is the prerequisite distinction.
- Architecture: exported verdict is an interface contract; transport success and domain acceptance are separate postconditions.
- Mobile/Data: no product/runtime semantics changed.
- Quality: owner; this is a materially different Q006 acceptance-path class from delegated-script propagation.
- Systems: CI/CD acceptance and release provenance depend on correct semantic gate composition.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant.
- Product repositories: not required; this control audits Studio CI semantics only.

## HANDOFFS

### Quality → Systems
For release/security-sensitive workflows, inventory not only nonzero propagation but also verdict-bearing outputs. A successful producer job is not sufficient when semantic acceptance is encoded as data. Require explicit downstream validation of the exported semantic value.

## OPEN / next step

- **VALIDATED, bounded:** job-result success and semantic-output failure can coexist; explicit semantic-output acceptance is required when that output carries the verdict.
- **OPEN:** reusable-workflow outputs, matrix output semantics, skipped/redacted outputs, other shells/action types, and production release-gate transfer.
- Do not repeat equivalent producer-success/semantic-FAIL controls. Continue Q006 only with a materially different acceptance path or a natural repository defect/transfer.
