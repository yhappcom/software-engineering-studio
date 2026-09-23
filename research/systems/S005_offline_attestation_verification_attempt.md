# S005 — Offline attestation verification attempt

Status: **IN STUDY — FRESH-ATTESTATION OFFLINE DISCRIMINATOR COMMITTED; EXECUTION PENDING**  
Evidence date: 2026-09-23

## Problem / scope
Separate online attestation retrieval from verification and execute verification with a local attestation bundle and trusted-root material while outbound networking is unavailable.

## SOURCE
Current GitHub documentation rechecked 2026-09-23 states that offline verification requires the artifact, downloaded attestation bundle, trusted-root material and verifier. The documented preparation is `gh attestation download <artifact> -R <owner/repo>` plus `gh attestation trusted-root > trusted_root.jsonl`; verification then uses `--bundle` and `--custom-trusted-root`.

Current GitHub artifact-attestation guidance uses `actions/attest@v4` for new provenance generation with `id-token: write`, `contents: read`, and `attestations: write`. The action's current primary repository additionally states that every created attestation is stored on the runner filesystem and its path appended to `${RUNNER_TEMP}/created_attestation_paths.txt`. This creates an independent preservation surface at generation time, distinct from later repository-API retrieval.

GitHub's attestation lifecycle documentation explicitly supports deletion and recommends downloading a copy before deletion; after deletion the attestation can no longer be found on GitHub. This establishes lifecycle mutability as a real service property, but does not prove that deletion caused the historical 404 below.

Primary sources:
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/manage-attestations
- https://github.com/actions/attest

## Historical target and contradiction
- repository: `yhappcom/software-engineering-studio`
- generation commit: `ab6dbf4307078fc82ddc056029f686dd61eae3a7`
- subject SHA-256: `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`
- prior successful hosted verification run/job: `35409747108` / `105806806534`

Run 5, exact head `53971088727987560f3dde2f3c31e9b999af4627`, run/job `35818471643` / `107045026937`, completed failure while preserving diagnostics. Run-bound artifact `10731184861`, digest `sha256:f64bb749ae4ac777b2aa8081652b0cd1a6f75b89e989b57c2fcf5ee5e535102e`, records GitHub CLI `2.100.0 (2026-09-03)`, authenticated `github-actions[bot]`, bundle producer exit `1`, and repository-attestation HTTP 404 for the exact historical digest.

**CONTRADICTION:** prior hosted online verification reportedly succeeded for this exact subject/repository, whereas current lookup returns 404. GitHub documents that attestations can be deleted, but there is no direct evidence that deletion occurred here. Retention/lifecycle change, historical identity error, service-side indexing/state change, or another availability mechanism remain unresolved; no deeper ROOT CAUSE is assigned.

## New coherent validation block — fresh generation → immediate preservation → isolated verification
Balance Loop comparison favored continuing S005 over new Foundations/Mobile/Data variants because the historical export failure now has a precise boundary, release provenance has cross-product leverage, and the next discriminator can remove the historical-retrievability dependency entirely.

Exact workflow repair/discriminator commit: `e43d3625be67f7d7699e703a06e181c07db16473` (`.github/workflows/s005-offline-attestation-verification.yml`).

The new workflow:
1. creates a fresh deterministic subject;
2. generates provenance with `actions/attest@v4` under explicit OIDC/attestation permissions;
3. proves the runner-local created-attestation path list exists and hashes each local bundle before any later retrieval;
4. immediately downloads the same fresh subject's repository bundle with `gh attestation download` and hashes it;
5. exports and hashes current trusted roots;
6. enters a new Linux network namespace and first proves `api.github.com` is unreachable;
7. performs positive verification using only the local subject, bundle and trusted roots;
8. in separately isolated namespaces requires wrong-repository identity and mutated-subject verification to fail;
9. preserves semantic evidence with `if: always()`.

This is intentionally a causal discriminator. If generation succeeds and immediate API download succeeds, the historical 404 is bounded to historical attestation availability rather than generic current CLI/auth/repository lookup. If runner-local bundle exists but immediate API download fails, local creation vs repository publication/retrieval becomes the next boundary. If offline positive verification fails after successful export, the verifier/root/network-isolation stage becomes independently diagnosable.

At the time of this note, the exact-head Actions run had not yet appeared in the workflow-runs API. Therefore there is **no execution verdict yet** and no PASS is awarded.

## SYNTHESIS
Online verification, later evidence retrieval, and offline verification are distinct predicates. A previously verified subject does not prove indefinite future bundle retrievability. Generation-time preservation is stronger for offline-evidence continuity than relying only on future repository API availability.

## ENGINEERING JUDGMENT
For release paths requiring later offline provenance verification, preserve the attestation bundle and trusted roots as evidence artifacts at attestation/release time. Do not use a historical online verification result as a substitute for preserved signed material.

## RELATED DOMAIN CHECK
- Foundations: direct Dart JIT/AOT and bounded Flutter runtime evidence already exists; not a blocker.
- Architecture: release state must distinguish generated, published/retrievable, verified-online, evidence-preserved, and verified-offline states.
- Mobile: no app artifact/mobile signing transfer occurs in this Studio fixture.
- Data: evidence lifecycle/retention is relevant; this does not establish application-data durability.
- Quality: Q006 preservation-vs-verdict separation is retained; positive and two negative semantic oracles are explicit.
- Systems: S005 owns release provenance and verification.
- Design Studio / Web Manager / Marketing Manager: considered; no current canonical decision changes this supply-chain mechanism.
- Product repositories: no product audit or production claim; exact-product release transfer remains future work.

## HANDOFFS
### TO Quality / release engineering
Treat generation, repository publication/retrievability, local evidence preservation and verification as separate release-gate predicates. Preserve failure evidence without masking producer/verifier verdicts.

### TO Mobile / product release
A later product transfer must bind `repository → exact ref/tag/branch/commit → declared version → evidence date → canonical build path → artifact digest → attestation bundle/root → verification policy`; this generic fixture cannot substitute for delivered-product provenance.

## OPEN / VALIDATION / CHANGE WATCH
- VALIDATION: observe terminal result for exact head `e43d3625be67f7d7699e703a06e181c07db16473` and inspect its run-bound semantic artifact before any PASS.
- OPEN: historical 404 deeper cause remains unresolved; do not infer deletion from lifecycle documentation alone.
- VALIDATION: after generic positive/negative offline verification succeeds, transfer to a real release/product artifact when authorized.
- CHANGE WATCH: GitHub CLI, `actions/attest`, attestation API, Sigstore roots and hosted-runner images are version/service sensitive.

## Gate effect
No Systems PASS. The new discriminator advances the evidence design but has not yet executed.