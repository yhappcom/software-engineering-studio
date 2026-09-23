# S005 — Offline attestation verification attempt

Status: **IN STUDY — OFFLINE VERIFICATION NOT YET ESTABLISHED; BUNDLE-EXPORT DIAGNOSTIC REGRESSION RUNNING**  
Evidence date: 2026-09-23

## Problem / scope
Separate online attestation retrieval from verification and execute verification with a local attestation bundle and trusted-root material while outbound networking is unavailable. Prior runs isolated failure to bundle export but lacked command-level stderr, so no root cause was assigned.

## SOURCE
Current GitHub documentation and GitHub CLI manual were rechecked 2026-09-23. Offline verification requires the artifact, downloaded attestation bundle, trusted-root material and verifier. The documented online preparation is `gh attestation download <artifact> -R <owner/repo>` followed by `gh attestation trusted-root > trusted_root.jsonl`; offline verification uses `gh attestation verify ... --bundle ... --custom-trusted-root ...`. `gh attestation download` remains public preview and therefore CHANGE WATCH. GitHub CLI automation documentation states that Actions should expose `${{ github.token }}` through `GH_TOKEN`.

Primary sources:
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline
- https://cli.github.com/manual/gh_attestation_download
- https://cli.github.com/manual/gh_attestation_trusted-root
- https://cli.github.com/manual/gh_attestation_verify
- https://cli.github.com/manual/gh_auth_login

## F001 / Balance Loop prerequisite check
Canonical Foundations status now supersedes the stale 2026-09-19 environment note: direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution exist. F001 is therefore not the blocker for this S005 block. Balance Loop selected S005 because the unresolved provenance verifier boundary has release/supply-chain leverage, an existing real contradiction, and cross-track Quality/Systems reuse value without repeating the professionally closed Safari lifecycle block.

## TARGET
Exact prior attested subject:
- repository: `yhappcom/software-engineering-studio`
- generation commit: `ab6dbf4307078fc82ddc056029f686dd61eae3a7`
- subject SHA-256: `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`
- prior successful hosted verification run/job: `35409747108` / `105806806534`
- workflow: `.github/workflows/s005-offline-attestation-verification.yml`

## VALIDATION / FAILURE / DEBUGGING
### Run 1 — oracle fixture defect
Commit `b6fbbae2191b8d7b415d893f089515e66cce30f8`, run/job `35412950674` / `105816006131`: exact subject reconstruction failed. Root cause was a fixture byte mismatch, not attestation behavior.

### Run 2 — combined input-export failure
Commit `c1fd34167619f4dbe4f695c1b1b49f5cf0741e7e`, run/job `35412968384` / `105816055855`: exact subject reconstruction passed; combined bundle/root export failed; later steps skipped.

### Run 3 — REST-style bundle export failure
Commit `dffe6476cd7d63297bdfe5ba560ee1fefc8e9d16`, run/job `35412983659` / `105816098288`: failure isolated to the bundle export implementation; command stderr unavailable.

### Run 4 — canonical CLI bundle export failure
Commit `66dd238e6bf0041c18fbd4e8aea3027c48a48d59`, run/job `35413003999` / `105816156294`: exact subject reconstruction succeeded and `Export attestation bundle while online` failed; trusted-root and offline verification were skipped. Exact workflow inspection confirms `contents: read`, `attestations: read`, and `GH_TOKEN: ${{ github.token }}` were already present, so the current GitHub CLI automation guidance does not justify a missing-token root-cause claim.

### Run 5 — diagnostic preservation repair
Commit `53971088727987560f3dde2f3c31e9b999af4627` modifies only the validation harness. Bundle export now records GitHub CLI version/auth status, stdout, stderr and producer exit code, uploads those diagnostics with `if: always()`, and then fails closed if export failed. This prevents the prior evidence channel from discarding the exact failure payload while preserving the same canonical `gh attestation download` operation.

Run `35818471643` is currently in progress. **No verdict is assigned until terminal run state and run-bound diagnostic artifact are inspected.**

## SYNTHESIS
Online verification and offline-input export are distinct executable predicates. A release gate that claims offline provenance verification must prove both acquisition of fixed verification inputs and verification without network access. Failure diagnostics are part of the evidence contract when root-cause classification depends on external CLI/service behavior.

## CONTRADICTION
Prior hosted online verification succeeded for the exact subject/repository, while explicit bundle-export attempts failed. These observations remain non-logically-inconsistent but operationally contradictory enough to require command-level evidence. Do not infer service outage, token scope defect, subject absence, CLI defect or attestation expiration before run 5 diagnostics establish one of them.

## ENGINEERING JUDGMENT
Do not make offline verification a release requirement until the pipeline deterministically exports and preserves bundle/root inputs and independently verifies them. Diagnostic preservation must itself fail closed: evidence capture may not convert a producer failure into a green release verdict.

## RELATED DOMAIN CHECK
- Foundations: current F001 evidence checked; direct Dart/Flutter is no longer the blocker.
- Architecture: release decisions must distinguish online verification, input acquisition and offline verification states.
- Mobile: no app artifact/mobile signing transfer occurred.
- Data: not materially changed.
- Quality: Q006 verdict/evidence separation directly informs the run-5 fail-closed diagnostic design.
- Systems: S001/S004/S005 directly relevant.
- Design Studio / Web Manager / Marketing Manager: considered; no canonical decision there changes this bounded supply-chain mechanism.
- Product repositories: no product audit in this block; no MintTap/LogMate production claim.

## HANDOFFS
### TO Quality
Run 5 is a natural transfer of Q006: diagnostic preservation and producer verdict propagation are separate controls. Inspect both artifact content and terminal outcome before accepting any S005 result.

### TO release engineering / Mobile
Do not claim offline provenance verification from hosted online verification. Product transfer still requires exact product ref/version, canonical artifact digest, exportable bundle/trusted roots, executed identity policy and delivered-artifact identity.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN / DEBUG: inspect run `35818471643` terminal result and diagnostic artifact; assign root cause only if payload supports it.
- VALIDATION: successful `gh attestation download` or equivalent exact bundle export for the known subject.
- VALIDATION: successful trusted-root export.
- VALIDATION: positive verification inside a demonstrably network-isolated environment using only artifact + bundle + trusted root + verifier.
- VALIDATION: wrong-repository and mutated-subject rejection in that same isolated context.
- CHANGE WATCH: `gh attestation download` is public preview; GitHub CLI, Actions, attestation API, Sigstore roots and hosted-runner images are version/service sensitive.

## Gate effect
No PASS awarded. The professional boundary advanced from opaque export failure to a fail-closed, artifact-preserving diagnostic execution; root cause and offline verification remain OPEN.