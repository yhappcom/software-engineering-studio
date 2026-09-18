# S005 — Real GitHub Actions artifact-attestation boundary

Status: **IN STUDY — REAL CI + ATTESTATION GENERATION EVIDENCE; VERIFICATION/POLICY STILL OPEN**  
Evidence date: 2026-09-19

## Problem / scope
S005 previously had source/model evidence, real OpenSSL signing, bounded reproducibility, and exact-ref product build-identity analysis, but no real GitHub Actions/OIDC/attestation execution. This block tests the actual hosted CI boundary in the canonical Studio repository without treating a green workflow as global release correctness.

## SOURCE
GitHub's current artifact-attestation documentation states that binary provenance generation requires `id-token: write`, `contents: read`, and `attestations: write`, and uses `actions/attest@v4` with a subject path. GitHub also states that attestations bind provenance claims such as repository, commit SHA, triggering event and workflow context, and that generation alone is not the security benefit: verification/policy evaluation is required. Current docs state private/internal repository attestation availability depends on plan; operational use is therefore CHANGE WATCH.

Primary sources checked 2026-09-19:
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
- https://docs.github.com/en/actions/concepts/security/artifact-attestations

## VALIDATION — hosted GitHub Actions + real attestation action
Canonical workflow: `.github/workflows/s005-attestation-boundary.yml`.

### Test Evidence Contract
- **CLAIM:** the canonical private Studio repository can execute a hosted GitHub Actions job that creates an exact-commit subject and successfully executes GitHub's real artifact-attestation action under explicit OIDC/attestation permissions.
- **SPEC/PROPERTY:** checkout and subject creation must succeed; `actions/attest@v4` must itself report `success` for the generated subject.
- **TARGET:** `yhappcom/software-engineering-studio`, branch `main`, exact commit `ab6dbf4307078fc82ddc056029f686dd61eae3a7`, GitHub Actions run `35405920497`, job `105795544174`.
- **INPUT/STATE:** deterministic text subject containing repository `yhappcom/software-engineering-studio` and exact workflow commit SHA; locally reconstructed expected SHA-256 `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`.
- **ORACLE:** GitHub Actions job/step conclusions returned by GitHub's Actions API; the attestation step must independently report `success`, not merely the overall job.
- **ENVIRONMENT:** GitHub-hosted `ubuntu-latest`, runner `GitHub Actions 1000000482`; workflow run created 2026-09-19 KST. Exact hosted image/tool versions were not extracted in this run.
- **OBSERVATION:** checkout `success`; deterministic subject step `success`; `Attest subject provenance` using `actions/attest@v4` `success`; outcome-record step `success`; job and workflow conclusion `success`.
- **VERDICT:** PASS for the bounded claim that real hosted CI and attestation generation executed successfully for this exact Studio commit/subject.
- **FAILURE MODEL:** missing/invalid workflow permission, hosted-CI/action execution failure, or attestation-generation rejection would make the attestation step non-success.
- **REPRODUCTION:** workflow path plus exact commit/run/job IDs above. Subject digest can be reconstructed from the repository and exact commit embedded by the workflow.
- **EVIDENCE LIMIT:** no independent `gh attestation verify`, no policy/identity verification, no downloaded bundle inspection, no SLSA-level claim, no Flutter/mobile build, no release deployment, no production artifact, no proof that this workflow is hermetic or secure.

## FAILURE / CONTRADICTION / ROOT-CAUSE STATUS
The immediately preceding run `35405881832` at commit `eab2972843130b0e997203d5ba5b8c108cb67dde` reached checkout and subject creation successfully but the `Attest subject provenance` step concluded `failure`; overall run failed. The workflow was then changed only to classify the attestation step outcome (`continue-on-error` plus explicit outcome recording), producing commit `ab6dbf4...`; in that second hosted run the attestation step itself concluded `success`.

**CONTRADICTION:** real attestation execution was not stable across these two adjacent runs.

**OPEN / DEBUG:** the available connector exposed step-level conclusions but not the failed action log/error payload, so the first failure's root cause is not established. Do not label it as a plan/permission/transient-network failure without the missing log evidence. The second success disproves a blanket claim that attestation generation is categorically unavailable for this repository/context.

## SYNTHESIS
This advances S005 from simulated/standalone signing into a real CI identity chain:

`repository + exact commit → hosted workflow run/job → deterministic subject bytes/digest → actions/attest execution result`.

It does **not** close the next boundary:

`generated attestation → independently retrieved/cryptographically verified attestation → signer/workflow identity policy → release acceptance`.

A green workflow is therefore still weaker than a verified provenance policy. Likewise, the workflow's `continue-on-error` is deliberately a research observability mechanism and is **not** a recommended release gate: production release logic must fail closed when attestation is required.

## ALTERNATIVES / comparison
- **Standalone OpenSSL signature:** proves exact-byte/key verification mechanics but lacks hosted workflow/OIDC provenance context.
- **GitHub Actions attestation generation (this block):** exercises real hosted CI and provenance generation, but generation success alone does not prove verifier policy or release authorization.
- **Independent attestation verification:** next stronger rung; verify the exact subject digest against expected repository/workflow identity and reject wrong subject/repository/workflow variants.
- **Product build attestation:** stronger transfer only when tied to a canonical MintTap/LogMate build path, exact SDK/dependencies, artifact digest and release identity.

## RELATED DOMAIN CHECK
- **Foundations:** F001 direct Dart/Flutter remains OPEN; this block does not substitute hosted CI for Dart/Flutter runtime understanding.
- **Architecture:** A006 evidence-preserving decisions apply: run/job/commit/subject identity must be retained rather than summarized as `CI passed`.
- **Mobile:** no Flutter/mobile artifact was built or signed; mobile transfer remains OPEN.
- **Data:** migrations/backups should bind validation to exact release artifact/provenance when used as release evidence.
- **Quality:** step-level attestation outcome is a narrower oracle than overall workflow green; release tests still need their own semantic oracles.
- **Systems:** S001/S004/S005 are directly relevant; S006 publication durability is not changed by provenance generation.
- **Design Studio / Web Manager / Marketing Manager:** considered; no owned decision is changed by this low-level CI/provenance evidence and no external canonical file was edited.
- **Product repositories:** not audited in this block; no MintTap/LogMate implementation or production claim is made.

## HANDOFFS
### TO Quality
When provenance becomes a release gate, distinguish overall workflow status from the exact attestation-generation and verification-policy predicates. Preserve negative variants for wrong subject/repository/workflow identity.

### TO Mobile / product release engineering
Do not transfer this Studio text-subject attestation as evidence for a Flutter app build. A product transfer must record `product repo → exact ref → declared version → canonical build command/toolchain/lock → artifact digest → attestation → verification policy → delivered artifact`.

## OPEN / VALIDATION / CHANGE WATCH
- **OPEN / VALIDATION:** retrieve and independently verify the generated attestation for subject digest `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`; test wrong-subject/repository/workflow policy rejection.
- **OPEN / DEBUG:** first-run attestation failure root cause because action logs were not available through the current evidence channel.
- **OPEN:** exact GitHub-hosted image/toolchain identity, reusable release-gate policy, product build transfer, deployment and production evidence.
- **CHANGE WATCH:** GitHub Actions, `actions/attest`, OIDC permission semantics, private-repository availability and verification behavior are service/version/plan sensitive.

## Gate effect
S005 now has **real hosted CI + real GitHub artifact-attestation generation evidence** in addition to prior signing/reproducibility work. Systems Stage 1 remains NOT PASS because independent attestation verification/policy, mobile/product build execution, signer/workflow authorization, independent-host reproducibility, deployment/rollback and production evidence remain OPEN.
