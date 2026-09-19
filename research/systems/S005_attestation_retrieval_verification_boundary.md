# S005 — Attestation retrieval and verification boundary

Status: **IN STUDY — RETRIEVAL + CRYPTOGRAPHIC/REPOSITORY VERIFICATION + NEGATIVE IDENTITY CASES VALIDATED**  
Evidence date: 2026-09-19

## Problem / scope
The preceding S005 block proved real GitHub-hosted `actions/attest@v4` generation for a deterministic subject. This block tests retrieval, CLI verification, and negative repository/subject identity cases without treating those results as a complete release policy.

## SOURCE
GitHub's current REST documentation provides a repository attestation endpoint keyed by `sha256:HEX_DIGEST` and states that retrieval alone is insufficient: signatures/timestamps must be cryptographically verified and signer identity validated. GitHub documents `gh attestation verify` for verification and states that generation alone provides no security benefit until attestations are verified and evaluated against policy.

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

### Failure / contradiction retained
Verification run 1: commit `0a51b05f7192fb96a70d3c5482f9a5c075a30811`, run/job `35409716823` / `105806716219`. Subject reconstruction succeeded but direct `gh attestation verify subject.txt --repo yhappcom/software-engineering-studio` failed. Negative cases did not execute. Available step evidence did not expose the CLI error payload, so root cause remains OPEN rather than fabricated.

### Successful classified verification run
Verification run 2: commit `4be94fa07433fe365ac577575883cb6ddb85c71c`, run/job `35409747108` / `105806806534`, GitHub-hosted `ubuntu-latest`.

Executed step oracles all completed `success`:
1. deterministic subject reconstruction and exact SHA-256 assertion;
2. repository attestation API query by exact digest, with an assertion requiring at least one returned attestation;
3. `gh attestation verify subject.txt --repo yhappcom/software-engineering-studio`;
4. wrong-repository negative case, which passes only when verification against `yhappcom/design-studio` is rejected;
5. mutated-subject negative case, which passes only when the modified bytes are rejected against the correct Studio repository;
6. final outcome classifier.

**VALIDATION:** for this exact bounded subject, a GitHub-hosted verifier retrieved an attestation, accepted the exact subject under the expected repository identity, rejected the same subject under a wrong repository identity, and rejected modified subject bytes.

## SYNTHESIS
The evidence chain is now:

`generation → exact-digest retrieval → verifier acceptance of exact bytes/repository → negative wrong-repository + wrong-subject rejection → stronger signer/workflow policy → release acceptance`.

The first four predicates are now executable evidence. This materially advances S005 beyond generation-only evidence. It still does not establish that every artifact from the repository is authorized, that a particular workflow/ref/actor is approved, that the build is secure/hermetic/reproducible, or that a delivered product artifact is the attested artifact.

## FAILURE / root-cause discipline
Run 1's failed positive verification and run 2's later success are a real contradiction across adjacent verifier runs. Because the failed CLI output is unavailable, no causal label is assigned. The later success disproves categorical verifier incompatibility for this subject/repository but does not explain the earlier failure.

## ALTERNATIVE / stronger next rung
GitHub documents offline verification using an exported bundle plus trusted roots. That is a materially stronger independence test than another hosted online `gh attestation verify` run because it separates retrieval from verification inputs. A release policy should additionally constrain expected repository/workflow/ref/environment as appropriate and fail closed.

## RELATED DOMAIN CHECK
- Foundations: F001 direct Dart/Flutter execution remains OPEN; no substitution.
- Architecture: preserve exact generation/verification run, job, commit and digest identities; `provenance passed` is too coarse.
- Mobile: no Flutter/mobile artifact or platform signing transfer.
- Data: release-bound backup/migration evidence may later consume this chain; no Data decision changes here.
- Quality: positive and negative verifier predicates were separately executed; retain the unexplained first-run failure as debugging evidence.
- Systems: S001/S004/S005 directly relevant; provenance verification evidence rung advanced.
- Design Studio / Web Manager / Marketing Manager: considered; no owned canonical decision changed and no external repository file was edited.
- Product repositories: not audited; no MintTap/LogMate implementation or production claim.

## HANDOFFS
### TO Quality
Use separate predicates for attestation existence, exact-subject verification and identity-policy rejection. Preserve run `35409716823` as an unresolved failure case rather than erasing it after the successful run.

### TO Mobile / product release engineering
Do not transfer Studio text-subject verification to app-release evidence. Product transfer still requires `product repository → exact ref/version → canonical build/toolchain/lock → artifact digest → attestation → executed policy → delivered artifact identity`.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN / DEBUG: root cause of run `35409716823` positive CLI verification failure.
- VALIDATION: workflow/ref/actor/environment policy constraints beyond repository identity.
- VALIDATION: offline bundle + trusted-root verification or another materially independent verifier context.
- VALIDATION: canonical MintTap/LogMate build artifact and mobile signing/delivery transfer.
- CHANGE WATCH: GitHub CLI, Actions, attestation REST API, Sigstore trust roots and hosted-runner behavior are service/tool-version sensitive.

## Gate effect
S005 now has real generation, exact-digest retrieval, successful CLI verification, wrong-repository rejection and mutated-subject rejection. Systems Stage 1 remains NOT PASS because stronger workflow/signer policy, independent/offline verification, product/mobile build transfer, independent-host reproducibility, deployment/rollback and production evidence remain OPEN.
