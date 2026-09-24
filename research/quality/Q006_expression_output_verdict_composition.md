# Q006 — GitHub Expression / Job-Output Verdict Composition Boundary

Date: 2026-09-24
Lead: Quality
Status: **IN STUDY — SOURCE/SYNTHESIS + EXECUTABLE CONTROL COMMITTED; HOSTED VALIDATION OPEN**

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

This complements, rather than replaces, Q006's prior third-party-action finding:

1. producer/oracle semantics;
2. wrapper/step failure propagation;
3. job execution result;
4. output/value transport;
5. downstream semantic acceptance.

A green state at one layer does not imply green at the next.

## Executable control

Committed workflow:

`.github/workflows/q006-expression-output-verdict-composition.yml`

Exact commit introducing control:

`6e0fc7cbac5e97a55c14f40c136f20bb48b33316`

The producer intentionally exits successfully while emitting:

- `semantic_verdict=FAIL`
- `diagnostic_verdict=PASS`

The downstream acceptance job independently checks:

1. `needs.producer.result == success` — transport/execution success;
2. a weak acceptance control that would accept on producer result alone but fails when it also checks `semantic_verdict == PASS`;
3. the failed control's `steps.<id>.outcome == failure` and corrected `conclusion == success`;
4. a separate fail-closed semantic-output assertion that must reject the `FAIL` value.

This structure is designed to prove that successful job transport and failed semantic verdict can coexist, and that the verdict must be part of the acceptance predicate.

## VALIDATION

**OPEN.** Immediately after commit `6e0fc7c...`, GitHub Actions had not yet registered a workflow run for that head. No hosted PASS is claimed.

Required hosted evidence:

- exact head/run/job identity;
- producer job terminal success;
- acceptance job terminal success;
- weak control step `outcome=failure`, corrected `conclusion=success`;
- final fail-closed oracle completes and emits `Q006_EXPRESSION_OUTPUT_VERDICT_COMPOSITION_PASS`.

If any condition differs, investigate rather than reinterpret a green workflow as proof.

## Failure model / limits

This control targets semantic verdict represented as job output while the producer process/job succeeds. It does not yet establish:

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

Wait for and inspect the exact hosted run of commit `6e0fc7c...`. If validated, update Q006 canonical/status/index and then move to another materially different acceptance path rather than repeating equivalent output controls.
