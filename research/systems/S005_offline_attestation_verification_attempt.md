# S005 — Offline attestation verification attempt

Status: **IN STUDY — OFFLINE VERIFICATION NOT ESTABLISHED; BUNDLE EXPORT 404 ISOLATED**  
Evidence date: 2026-09-23

## Problem / scope
Separate online attestation retrieval from verification and execute verification with a local attestation bundle and trusted-root material while outbound networking is unavailable.

## SOURCE
Current GitHub documentation rechecked 2026-09-23 states that offline verification requires the artifact, downloaded attestation bundle, trusted-root material and verifier. The documented preparation is `gh attestation download <artifact> -R <owner/repo>` plus `gh attestation trusted-root > trusted_root.jsonl`; verification then uses `--bundle` and `--custom-trusted-root`. Repository attestation lookup accepts a `sha256:<digest>` subject and may return 404; public-repository lookup can be unauthenticated, while authenticated fine-grained access requires attestations read permission.

Primary sources:
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline
- https://docs.github.com/en/rest/repos/attestations
- https://cli.github.com/manual/gh_attestation_download

## TARGET
- repository: `yhappcom/software-engineering-studio`
- generation commit: `ab6dbf4307078fc82ddc056029f686dd61eae3a7`
- subject SHA-256: `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`
- prior successful hosted verification run/job: `35409747108` / `105806806534`
- workflow: `.github/workflows/s005-offline-attestation-verification.yml`

## VALIDATION / FAILURE / DEBUGGING
Runs 1–4 progressively isolated the failure from subject reconstruction and combined export to canonical CLI bundle export. Run 5, exact head `53971088727987560f3dde2f3c31e9b999af4627`, run/job `35818471643` / `107045026937`, completed **failure** while preserving diagnostics.

Run-bound artifact `10731184861`, digest `sha256:f64bb749ae4ac777b2aa8081652b0cd1a6f75b89e989b57c2fcf5ee5e535102e`, was directly inspected. It records:
- GitHub CLI `2.100.0 (2026-09-03)`;
- authenticated `github-actions[bot]` via `GH_TOKEN`;
- reconstructed subject commit `ab6dbf4307078fc82ddc056029f686dd61eae3a7`;
- bundle producer exit code `1`;
- exact stderr: attestation fetch returned HTTP 404 for repository `yhappcom/software-engineering-studio` and subject digest `sha256:9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`.

The fail-closed step then failed and trusted-root/offline verification steps were skipped. Thus the current failure is no longer an opaque CLI/token setup failure: the authenticated CLI reached the repository-attestation lookup and that lookup returned 404 for the exact subject digest.

## SYNTHESIS
Online verification and later offline-input export are temporally distinct predicates. A previously verified subject does not prove that its bundle remains retrievable later. Offline verification therefore requires preservation/export of the bundle as part of the evidence lifecycle, not merely a historical online verification result.

## CONTRADICTION
Prior hosted online verification reportedly succeeded for this exact subject/repository, whereas the current repository-attestation lookup returns 404. This is a real temporal evidence contradiction, but the available execution does **not** distinguish among attestation deletion/retention/lifecycle change, historical identity error, service-side indexing/state change, or another repository-attestation availability mechanism. Do not assign a deeper root cause without direct evidence.

## ENGINEERING JUDGMENT
Treat attestation bundle availability as a release artifact-retention dependency. If offline verification is required, export and preserve the bundle and trusted roots at attestation/release time rather than depending on indefinite future API retrieval.

## RELATED DOMAIN CHECK
- Foundations: current F001 direct Dart/Flutter evidence means it is not this block's blocker.
- Architecture: release state must distinguish verification-at-time-T from later evidence retrievability.
- Mobile: no app artifact/mobile signing transfer occurred.
- Data: evidence retention/lifecycle is materially implicated as a systems concern; no storage PASS awarded.
- Quality: Q006 evidence-preservation vs verdict-propagation transfer succeeded here; producer failure remained red while diagnostics survived.
- Systems: S005 remains owner.
- Design Studio / Web Manager / Marketing Manager: no canonical decision materially changes this supply-chain boundary.
- Product repositories: no product audit or production claim in this block.

## HANDOFFS
### TO Quality / release engineering
For provenance gates, preserve run-bound bundle/trusted-root evidence when generated. A later green/failed lookup is not a substitute for the original signed-material evidence.

### TO Mobile / product release
Offline provenance transfer still requires exact product repository/ref/version, canonical artifact digest, preserved attestation bundle/root inputs, executed identity policy and delivered-artifact identity.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN: explain the temporal contradiction between prior successful online verification and current 404 only with direct evidence; do not speculate.
- VALIDATION: generate or identify a currently retrievable attested subject, export its bundle immediately, and preserve it run-bound.
- VALIDATION: export trusted roots and perform positive verification inside demonstrable network isolation.
- VALIDATION: wrong-repository and mutated-subject rejection in that same isolated context.
- CHANGE WATCH: GitHub CLI, attestation API, Sigstore roots and hosted-runner images are version/service sensitive.

## Gate effect
No Systems PASS. Run 5 closes the opaque-export diagnostic boundary: the exact current failure is repository-attestation lookup HTTP 404 for the historical subject. Offline verification remains OPEN.