# S005 — Offline attestation verification attempt

Status: **IN STUDY — FRESH GENERATION/PUBLICATION/PRESERVATION VALIDATED; OFFLINE VERIFIER FAILURE DIAGNOSTIC PENDING**  
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
Exact head `e43d3625be67f7d7699e703a06e181c07db16473`, run/job `35826775258` / `107070135294`, completed **failure**. Step-level evidence is discriminating rather than globally negative:
- fresh deterministic subject creation: success;
- `actions/attest@v4` provenance generation: success;
- runner-local attestation-path preservation: success;
- immediate repository bundle download: success;
- current trusted-root export: success;
- isolated positive verification step: failure;
- negative tests skipped because positive verification failed;
- semantic artifact preservation: success.

Run-bound artifact `10735746062`, digest `sha256:d7916d68076e9b13d113ea47f82d9c6045a9783e49e0bc4328e14a9dc9bbe7c3`, was directly inspected. Subject SHA-256 is `9c6dd50d28b2a736cd9ff0a488f4f5ad4d93cf1f36258209374a89fdb28e6264`. The runner-local attestation at `/home/runner/work/_temp/8BCfUo/attestation.json` and immediately downloaded repository bundle are byte-identical by SHA-256: `89e64a6f11e4033240b29bc4c562cfe182ae4a08a2819bc822f4dbf11152a338`. The downloaded bundle is non-empty (11,817 bytes); trusted roots are non-empty and hash to `65ca537f6ed8a47fd0e560c421baa1f6c1efb8b25fc200d8c5c02c0e92eb2b9c`. GitHub CLI is `2.100.0 (2026-09-03)` and authenticated as `github-actions[bot]`.

**VALIDATION:** for this fresh subject, generation-time local signed material and immediate repository retrieval agree byte-for-byte. Therefore the historical 404 is not evidence of a generic current inability of this workflow identity/CLI/repository to generate, publish or immediately retrieve attestations. It remains specifically a historical-attestation availability contradiction.

The artifact's `offline-positive.txt` is zero bytes. Run 6 did not preserve stderr/exit status from the isolated verifier, so the exact reason for step 7 failure is not yet established. It would be invalid to call this a cryptographic/offline-verification failure without separating namespace creation, network-isolation oracle, CLI invocation and signature/policy verification.

## Run 7 diagnostic repair
Commit `c1ca5a8ae09717fc794b7e064358938e346b56cb` changes the positive offline step to preserve stdout, stderr and producer exit status while retaining fail-closed behavior. Negative tests run only after positive offline verification succeeds; the final step fails closed if the positive producer failed. At note time its workflow run had not yet appeared in the Actions API.

## SYNTHESIS
Generation, repository publication/retrievability, evidence preservation and verification are distinct predicates. Run 6 directly validates the first three for a fresh subject and demonstrates a stronger release-evidence pattern: preserve generation-time signed material, then independently check repository retrieval. Historical online verification alone is not an evidence-retention guarantee.

## ENGINEERING JUDGMENT
For releases requiring later offline provenance verification, preserve the attestation bundle and trusted roots at attestation/release time. Do not make future repository lookup the sole evidence-retention mechanism.

## RELATED DOMAIN CHECK
- Foundations: direct Dart JIT/AOT and bounded Flutter runtime exist; not this block's blocker.
- Architecture: generated, published/retrievable, preserved and verified are distinct lifecycle states.
- Mobile: no app artifact/mobile signing transfer occurred.
- Data: evidence retention is relevant but does not establish application-data durability.
- Quality: Q006 preservation-vs-verdict discipline applies; run 6 shows why failed semantic stages require their own diagnostic artifact.
- Systems: S005 remains owner.
- Design Studio / Web Manager / Marketing Manager: considered; no canonical decision changes this supply-chain boundary.
- Product repositories: no product audit or production claim; exact-product transfer remains OPEN.

## HANDOFFS
### TO Quality / release engineering
Use separate oracles for generation, publication/retrieval, local evidence preservation, network isolation and verifier result. Preserve stderr/exit status before assigning a cryptographic root cause.

### TO Mobile / product release
Future transfer must bind `repository → exact ref/tag/branch/commit → declared version → evidence date → canonical build path → artifact digest → preserved attestation/root → verification policy`; this generic Studio fixture is not delivered-product provenance.

## OPEN / VALIDATION / CHANGE WATCH
- VALIDATION: inspect exact-head `c1ca5a8ae09717fc794b7e064358938e346b56cb` terminal run and its run-bound offline-verifier diagnostics.
- OPEN: historical 404 deeper cause remains unresolved; lifecycle documentation alone is not deletion evidence.
- VALIDATION: positive network-isolated verification plus wrong-repository and mutated-subject rejection remain required.
- VALIDATION: exact-product/release transfer remains required after generic closure.
- CHANGE WATCH: GitHub CLI, `actions/attest`, attestation API, Sigstore roots and hosted-runner images are version/service sensitive.

## Gate effect
No Systems PASS. Run 6 materially advances S005 by validating fresh generation→publication/retrieval→preservation identity, but offline verification remains OPEN.