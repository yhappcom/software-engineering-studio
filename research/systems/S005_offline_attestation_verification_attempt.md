# S005 — Offline attestation verification attempt

Status: **IN STUDY — BOUNDED GENERIC OFFLINE VERIFICATION CLOSED; EXACT-PRODUCT/RELEASE TRANSFER OPEN**  
Evidence date: 2026-09-23

## Problem / scope
Separate attestation generation, repository publication/retrieval, evidence preservation and offline verification into independently observable release predicates.

## SOURCE
GitHub documentation rechecked 2026-09-23 states that offline verification requires the artifact, downloaded attestation bundle, trusted-root material and verifier. The documented preparation is `gh attestation download <artifact> -R <owner/repo>` plus `gh attestation trusted-root > trusted_root.jsonl`; verification uses `--bundle` and `--custom-trusted-root`.

Current generation guidance uses `actions/attest@v4` with OIDC and attestation permissions. The action's primary repository states that created attestations are also stored on the runner filesystem and paths appended to `${RUNNER_TEMP}/created_attestation_paths.txt`. GitHub lifecycle documentation supports explicit attestation deletion and recommends downloading before deletion. Lifecycle mutability is therefore a real service property, but this does not prove deletion caused the historical 404.

Primary sources:
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/manage-attestations
- https://github.com/actions/attest

## Historical contradiction
Historical subject from generation commit `ab6dbf4307078fc82ddc056029f686dd61eae3a7`, SHA-256 `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`, had prior hosted online verification. Exact head `53971088727987560f3dde2f3c31e9b999af4627`, run/job `35818471643` / `107045026937`, later received authenticated HTTP 404 for that digest. Run-bound artifact `10731184861` preserved the failure.

**CONTRADICTION:** prior verification vs later 404 remains real. Deletion/retention/indexing/historical-identity cause remains OPEN; no unsupported ROOT CAUSE is assigned.

## Run 6 — fresh generation discriminator
Exact head `e43d3625be67f7d7699e703a06e181c07db16473`, run/job `35826775258` / `107070135294`, completed failure. Fresh subject creation, `actions/attest@v4` generation, runner-local attestation preservation, immediate repository bundle download and trusted-root export succeeded; the isolated positive verifier failed before its stderr/exit status was preserved.

Run-bound artifact `10735746062`, digest `sha256:d7916d68076e9b13d113ea47f82d9c6045a9783e49e0bc4328e14a9dc9bbe7c3`, was directly inspected. Subject SHA-256 was `9c6dd50d28b2a736cd9ff0a488f4f5ad4d93cf1f36258209374a89fdb28e6264`. The runner-local attestation and immediately downloaded repository bundle were byte-identical at SHA-256 `89e64a6f11e4033240b29bc4c562cfe182ae4a08a2819bc822f4dbf11152a338`.

**VALIDATION:** fresh generation, publication/retrieval and generation-time preservation are distinct and were validated. Historical 404 is not evidence of a generic current inability to publish/retrieve attestations.

## Run 7 — bounded generic offline closure
Diagnostic repair exact head `c1ca5a8ae09717fc794b7e064358938e346b56cb`, run/job `35826855911` / `107070382027`, completed **success** on the GitHub-hosted `ubuntu-latest` runner. GitHub's run/job API records success for each semantic stage: fresh subject creation, provenance generation, local attestation preservation, immediate repository bundle download, trusted-root export, network-isolated positive verification, wrong-repository rejection, mutated-subject rejection, and semantic evidence preservation. The fail-closed positive-verification fallback was skipped because the positive producer succeeded.

Run-bound artifact metadata binds `s005-offline-attestation-evidence` artifact `10735831041`, size 20,280 bytes, digest `sha256:3037d37b392b8d7b8567f11fc7cffaf501100d6f96a71f60952d48ff674cdabd`, to exact head `c1ca5a8ae09717fc794b7e064358938e346b56cb` and run `35826855911`. In this execution context the binary archive itself was not independently opened, so this note does not invent its internal stdout/stderr contents; the bounded verdict relies on the fail-closed workflow semantics plus GitHub's per-step terminal results and artifact identity metadata.

**VALIDATION:** the generic fixture now demonstrates the complete bounded lifecycle `fresh subject → attestation generation → generation-time preservation → immediate repository retrieval → trusted-root preservation → outbound-network isolation → positive offline verification → wrong-repository rejection → mutated-subject rejection`.

**FAILURE/REGRESSION CHAIN:** historical retrieval contradiction → fresh generation/retrieval success → opaque offline-positive failure → diagnostic preservation repair → exact-head hosted regression success.

## SYNTHESIS
Generation, repository publication/retrievability, evidence preservation and verification are distinct predicates. Release evidence requiring later offline verification should preserve signed material and roots at release time rather than depend solely on future service retrieval.

## ENGINEERING JUDGMENT
The generic S005 fixture has reached a bounded professional boundary. Repeating equivalent synthetic attestation variants has low marginal value. The next stronger evidence class is exact-product/release provenance bound to a canonical build artifact, exact source ref/version, digest, signing/release policy and retained verification material.

## RELATED DOMAIN CHECK
- Foundations: direct Dart JIT/AOT and bounded Flutter runtime exist; not this block's blocker.
- Architecture: generated, published/retrievable, preserved and verified are distinct lifecycle states.
- Mobile: no app artifact/mobile signing transfer occurred.
- Data: evidence retention is relevant but does not establish application-data durability.
- Quality: Q006 preservation-vs-verdict discipline transferred naturally; the run-6 failure and run-7 repair preserve the failure→diagnostic→regression chain.
- Systems: S005 remains owner.
- Design Studio / Web Manager / Marketing Manager: considered; no canonical decision changes this supply-chain boundary.
- Product repositories: no product audit or production claim in run 7; exact-product transfer remains OPEN.

## HANDOFFS
### TO Quality / release engineering
Retain independent oracles for generation, publication/retrieval, local evidence preservation, network isolation, verifier success and negative identity/content rejection. Preserve producer verdict separately from diagnostic output.

### TO Mobile / product release
Future transfer must bind `repository → exact ref/tag/branch/commit → declared version → evidence date → canonical build path → artifact digest → preserved attestation/root → verification policy`. Generic Studio attestation is not delivered-product provenance.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN: historical 404 deeper cause remains unresolved; lifecycle documentation alone is not deletion evidence.
- VALIDATION: exact-product/release transfer remains required after generic closure.
- VALIDATION: Android/iOS signing/deployment and independent-host verification remain outside this fixture.
- CHANGE WATCH: GitHub CLI, `actions/attest`, attestation API, Sigstore roots and hosted-runner images are version/service sensitive.

## Gate effect
No Systems Stage 1 PASS. The bounded generic offline-attestation verification boundary is closed by exact-head hosted regression, including positive isolated verification and two negative controls. Product/release provenance, signing/deployment, independent-host reproducibility and production evidence remain materially open.