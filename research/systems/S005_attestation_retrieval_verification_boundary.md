# S005 — Attestation retrieval and verification boundary

Status: **IN STUDY — RETRIEVAL VALIDATED; CRYPTOGRAPHIC VERIFICATION INCONCLUSIVE**  
Evidence date: 2026-09-19

## Problem / scope
The preceding S005 block proved real GitHub-hosted `actions/attest@v4` generation for a deterministic subject, but retrieval and independent verification remained OPEN. This block advances exactly that boundary without treating generation success as verification.

## SOURCE
GitHub's current REST documentation provides a repository attestation endpoint keyed by `sha256:HEX_DIGEST` and explicitly states that retrieval alone is insufficient: signatures/timestamps must be cryptographically verified and signer identity validated. GitHub documents `gh attestation verify` for verification. GitHub's attestation overview likewise states that generation alone provides no security benefit until attestations are verified and evaluated against policy.

Primary sources checked 2026-09-19:
- https://docs.github.com/en/rest/repos/attestations
- https://docs.github.com/en/actions/concepts/security/artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline

## VALIDATION
Canonical verification workflow: `.github/workflows/s005-attestation-verification-boundary.yml`.

Attested subject from prior generation:
- repository: `yhappcom/software-engineering-studio`
- generation commit: `ab6dbf4307078fc82ddc056029f686dd61eae3a7`
- SHA-256: `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`
- generation run/job: `35405920497` / `105795544174`

Verification workflow run 1:
- workflow commit: `0a51b05f7192fb96a70d3c5482f9a5c075a30811`
- run/job: `35409716823` / `105806716219`
- subject reconstruction: success
- direct `gh attestation verify subject.txt --repo yhappcom/software-engineering-studio`: failure
- negative cases did not execute because the job stopped at the positive verification failure.

**CONTRADICTION / OPEN DEBUG:** a successful generation step did not immediately imply a successful CLI verification run. The available step-level evidence does not expose the CLI error payload, so the cause is not assigned.

Verification workflow run 2 added explicit retrieval and outcome classification:
- workflow commit: `4be94fa07433fe365ac577575883cb6ddb85c71c`
- run/job: `35409747108` / `105806806534`
- deterministic subject reconstruction and digest assertion: success
- repository attestation API query by the exact subject digest: **success**, and the step's assertion requires at least one returned attestation
- `gh attestation verify` positive verification was still in progress at the last evidence observation; therefore no cryptographic-verification verdict is recorded from this run.

## SYNTHESIS
The evidence chain is now finer-grained:

`attestation generation success → attestation retrievable by exact subject digest → cryptographic signature/timestamp verification → signer/repository/workflow identity policy → release acceptance`.

The first two transitions are now demonstrated for this bounded Studio subject. The third is not closed. Retrieval proves that an attestation record exists for the exact digest; it does not prove its signature, timestamp or identity policy.

## FAILURE / oracle discipline
The first positive CLI verification attempt failed. This is useful failure evidence, not a reason to relabel the prior generation run as false. Generation, storage/retrieval and verifier acceptance are distinct predicates. Root cause requires verifier output/log evidence or an independently downloaded bundle/trusted-root verification path.

The workflow includes wrong-repository and mutated-subject negative tests, but they are **not VALIDATION evidence until execution completes**. Do not award them PASS from workflow text alone.

## RELATED DOMAIN CHECK
- Foundations: F001 direct Dart/Flutter execution remains OPEN; no substitution.
- Architecture: preserve exact generation and verification run/job/commit/digest identities; do not summarize this as `provenance passed`.
- Mobile: no Flutter/mobile artifact or signing transfer.
- Data: release-bound backup/migration evidence may later consume this provenance chain, but no data decision changes here.
- Quality: positive and negative verifier predicates require separate executed oracles; workflow definition alone is not evidence.
- Systems: S001/S004/S005 directly relevant; this advances provenance retrieval only.
- Design Studio / Web Manager / Marketing Manager: considered; no owned canonical decision is materially changed and no external repository file was edited.
- Product repositories: not audited; no MintTap/LogMate implementation or production claim.

## HANDOFFS
### TO Quality
Treat attestation existence, cryptographic verification and identity-policy rejection as independent test predicates. Preserve the failed positive verification as a regression/debugging case until its error payload is available.

### TO Mobile / product release engineering
Do not transfer Studio subject retrieval to product release evidence. Product transfer still requires exact product ref/version, canonical build/toolchain/lock, artifact digest, attestation, executed verification policy and delivered artifact identity.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN / DEBUG: root cause of run `35409716823` positive CLI verification failure.
- VALIDATION: obtain a completed successful cryptographic verification for the exact subject or isolate why it fails.
- VALIDATION: execute and observe wrong-repository and wrong-subject rejection; workflow text alone does not count.
- VALIDATION: workflow/signer identity constraints beyond repository identity.
- CHANGE WATCH: GitHub CLI, Actions, attestation REST API, Sigstore trust roots and hosted-runner behavior are service/tool-version sensitive.

## Gate effect
S005 advances from generation-only to **real exact-digest attestation retrieval plus a real failed positive verifier attempt**. Systems Stage 1 remains NOT PASS. Cryptographic verification/policy, product/mobile build transfer, independent-host reproducibility, deployment/rollback and production evidence remain OPEN.
