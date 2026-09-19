# S005 — Offline attestation verification attempt

Status: **IN STUDY — OFFLINE VERIFICATION NOT YET ESTABLISHED; INPUT-EXPORT FAILURE ISOLATED**  
Evidence date: 2026-09-19

## Problem / scope
The preceding S005 block established hosted attestation retrieval/verification plus wrong-repository and mutated-subject rejection. The next evidence rung is to separate online retrieval from verification and execute verification with a local attestation bundle and trusted-root material while outbound networking is unavailable.

## SOURCE
GitHub's current offline-verification guidance states that offline verification requires four imported inputs: GitHub CLI, artifact, attestation bundle, and `trusted_root.jsonl`. It documents `gh attestation download`, `gh attestation trusted-root`, and `gh attestation verify ... --bundle ... --custom-trusted-root ...`. GitHub also warns that trusted-root material must be refreshed as key material rotates/revocation knowledge changes.

Primary sources checked 2026-09-19:
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline
- https://cli.github.com/manual/gh_attestation_trusted-root
- https://cli.github.com/manual/gh_attestation_verify

## DEPENDENCY / F001 check
The local execution environment was checked first. No trustworthy `dart` or `flutter` executable was available, so F001 direct Dart JIT/AOT and Flutter runtime validation remains OPEN. The environment also did not expose a local `gh` executable, so the higher S005 rung was attempted on GitHub-hosted Actions rather than simulated locally.

## TARGET
Exact prior attested subject:
- repository: `yhappcom/software-engineering-studio`
- generation commit: `ab6dbf4307078fc82ddc056029f686dd61eae3a7`
- subject SHA-256: `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`
- prior successful hosted verification run/job: `35409747108` / `105806806534`

New workflow: `.github/workflows/s005-offline-attestation-verification.yml`.

## VALIDATION / FAILURE / DEBUGGING
### Run 1 — oracle fixture defect
- commit: `b6fbbae2191b8d7b415d893f089515e66cce30f8`
- run/job: `35412950674` / `105816006131`
- result: failure in `Reconstruct exact attested subject`; all later steps skipped.

Root cause was established by comparing the workflow to the previously successful verification fixture: the new workflow reconstructed different bytes while asserting the old digest. This was a test-fixture defect, not attestation failure. The subject reconstruction was corrected to the exact prior bytes.

### Run 2 — online input-export step failed
- commit: `c1fd34167619f4dbe4f695c1b1b49f5cf0741e7e`
- run/job: `35412968384` / `105816055855`
- exact subject reconstruction: success
- combined bundle/trusted-root export step: failure
- offline verification steps: skipped

Because the combined step contained multiple commands and the available evidence channel did not expose the command log, this run did not isolate which command failed.

### Run 3 — REST-style bundle export isolated and failed
- commit: `dffe6476cd7d63297bdfe5ba560ee1fefc8e9d16`
- run/job: `35412983659` / `105816098288`
- exact subject reconstruction: success
- `Export attestation bundle by exact digest`: failure
- trusted-root and offline verification steps: skipped

This narrowed the failure boundary to bundle export in that implementation, but the current evidence channel still did not expose the command error payload. No permission/service/CLI/network cause is assigned.

### Run 4 — canonical `gh attestation download` export also failed
- commit: `66dd238e6bf0041c18fbd4e8aea3027c48a48d59`
- run/job: `35413003999` / `105816156294`
- exact subject reconstruction: success
- canonical `gh attestation download` bundle-export step: failure
- trusted-root and offline verification steps: skipped

The failure therefore survived a materially different bundle-export implementation, but without command-level stderr it is not sufficient to prove a root cause. It also does not contradict the prior hosted online `gh attestation verify` success, because online verification and explicit offline-bundle export are distinct operations.

## SYNTHESIS
The intended evidence chain is:

`online attestation generation → online bundle/root export → transport of fixed verification inputs → network-isolated cryptographic/identity verification → negative policy cases`.

This run did **not** establish the final offline-verification predicate. It did establish two useful boundaries:
1. exact subject reconstruction is a prerequisite oracle and can itself invalidate the experiment;
2. successful hosted online verification does not establish that the bundle/root export path needed for offline verification is operational in the same CI context.

## CONTRADICTION
Prior hosted online verification succeeded for the exact subject/repository, while the new explicit bundle-export attempts failed. These observations are not logically inconsistent, but they expose a tooling/service-path difference that requires command-level evidence before assigning cause.

## ENGINEERING JUDGMENT
Do not make offline verification a release requirement until the pipeline can deterministically export and preserve the bundle and trusted-root inputs and independently verify them. A policy that names offline verification but cannot produce its verification inputs is not an executable release gate.

## RELATED DOMAIN CHECK
- Foundations: F001 direct Dart/Flutter execution attempted first; still unavailable.
- Architecture: evidence-critical release decisions must distinguish online verification from offline-input availability.
- Mobile: no app artifact or mobile signing transfer occurred.
- Data: no persistence/backup decision changed.
- Quality: run 1 demonstrates a defective test fixture; runs 2-4 preserve failure classification without fabricated root cause.
- Systems: S001/S004/S005 directly relevant; evidence rung did not advance to offline PASS.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded supply-chain verification mechanism; no canonical files edited.
- Product repositories: not audited in this block; no MintTap/LogMate production claim.

## HANDOFFS
### TO Quality
Treat test-fixture identity as part of the oracle contract. Preserve the run-1 subject mismatch as a regression example: a verifier experiment can fail before exercising the verifier.

### TO release engineering / Mobile
Do not claim offline provenance verification from hosted online verification. Product transfer still requires exact product ref/version, canonical artifact digest, exportable attestation bundle/trusted roots, executed identity policy, and delivered-artifact identity.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN / DEBUG: obtain command-level stderr/log evidence for bundle-export failures before assigning root cause.
- VALIDATION: successful `gh attestation download` or equivalent exact bundle export for the known subject.
- VALIDATION: successful trusted-root export.
- VALIDATION: positive verification inside a demonstrably network-isolated environment using only artifact + bundle + trusted root + verifier.
- VALIDATION: wrong-repository and mutated-subject rejection in that same isolated context.
- CHANGE WATCH: GitHub CLI, Actions, attestation API, Sigstore roots and hosted-runner images are version/service sensitive.

## Gate effect
No PASS awarded. S005 gained a real failed higher-rung attempt and a root-caused fixture defect, but offline independent verification remains OPEN.