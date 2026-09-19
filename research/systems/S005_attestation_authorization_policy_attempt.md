# S005 — Attestation authorization-policy attempt

Date: 2026-09-19  
Lead: Systems / Security / Delivery  
State: **IN STUDY — hosted authorization policy attempted; baseline verifier instability reproduced**

## Problem

Prior S005 evidence established one successful hosted `gh attestation verify` for a fixed subject/repository and negative rejection of a wrong repository and mutated subject. The next professional boundary is whether a release consumer can narrow authorization to an expected signer workflow and source identity rather than accepting any attestation associated with the repository.

## SOURCE

Current GitHub CLI documentation defines attestation actor identity as repository/owner plus the Actions workflow that produced the attestation and recommends more precise identity enforcement where appropriate. `gh attestation verify` supports `--signer-workflow`, `--source-ref`, and `--source-digest`. GitHub's artifact-attestation guidance states that attestations establish provenance, not artifact safety, and that consumers must define and evaluate policy criteria.

Primary sources checked 2026-09-19:
- https://cli.github.com/manual/gh_attestation_verify
- https://docs.github.com/en/actions/concepts/security/artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/increase-security-rating

## Target / fixed subject

Existing attested subject:
- repository: `yhappcom/software-engineering-studio`
- subject-generating workflow source commit encoded in subject: `ab6dbf4307078fc82ddc056029f686dd61eae3a7`
- subject SHA-256: `9f2ddf6d0d14733ead35f5d1050f4455b19877f501fd19e5220e725ba626b071`
- expected signer workflow: `yhappcom/software-engineering-studio/.github/workflows/s005-attestation-boundary.yml`
- expected source ref candidate: `refs/heads/main`

The earlier successful hosted verification remains run `35409747108` / job `105806806534` at workflow commit `4be94fa07433fe365ac577575883cb6ddb85c71c`.

## Executable attempt

Workflow: `.github/workflows/s005-attestation-authorization-policy.yml`.

### Run 1 — `35415715727`, job `105823866080`, workflow commit `041dc5c85ff12a0172f81d433c4d4a282bc69680`

The subject reconstruction succeeded. GitHub's job summary exposed the exact-policy step and all three negative-policy wrapper steps as successful, but the final classifier failed because the step `outcome` values were not all `success`. Since `continue-on-error` can make job-step conclusion and expression outcome differ, this run did not establish which predicate failed. This is an oracle/reporting defect in the first workflow design, not authorization-policy evidence.

### Run 2 — `35415743203`, job `105823946662`, workflow commit `831bccea0effb5d0ccee18404c236ce7f4acbd3a`

The workflow was changed to fail closed without `continue-on-error` for the exact policy. Subject reconstruction succeeded, but the combined exact authorization verification failed; later negative cases were skipped. Command-level stderr is not available through the current evidence channel, so the failing predicate could not be identified.

### Run 3 — `35415769301`, job `105824020122`, workflow commit `b06adfe5def9fcbf6fa5c7918fb42533a1325fab`

The workflow was changed to isolate the repository-only baseline before signer/ref/digest predicates. Subject reconstruction succeeded, but the baseline command `gh attestation verify subject.txt --repo yhappcom/software-engineering-studio` itself failed. All finer predicate steps were therefore skipped.

## CONTRADICTION

The same fixed subject/repository pair previously passed hosted verification in run `35409747108`, while the repository-only baseline failed in run `35415769301` on 2026-09-19. This reproduces the earlier unexplained hosted verifier failure class and shows that the current online verification path is not stable enough, in the available evidence channel, to use as the foundation for a stronger authorization-policy verdict.

The contradiction does **not** establish that the attestation is invalid, expired, deleted, or inaccessible for any particular reason. No causal label is assigned without command-level error evidence.

## VALIDATION / verdict

- Fixed subject reconstruction: **PASS** in all three new runs.
- Strong signer-workflow/source-ref/source-digest authorization policy: **INCONCLUSIVE / OPEN**.
- Repository-only hosted verification stability: **CONTRADICTION reproduced**; one prior success and multiple later failures exist.
- No Systems PASS awarded.

## SYNTHESIS

A provenance policy has two independent dependencies: (1) policy predicates must be sufficiently narrow, and (2) the verifier/evidence retrieval path must itself be operationally reliable and diagnosable. A strict policy layered on an unstable or opaque baseline verifier cannot produce trustworthy release acceptance merely because its flags are theoretically correct.

## ENGINEERING JUDGMENT

Do not spend further Actions minutes varying signer/ref/digest policy flags until command-level verifier failure output can be captured or an independent verification path is available. Preserve the successful prior run and the contradictory failures as evidence rather than normalizing one side away.

## RELATED DOMAIN CHECK

- Foundations: F001 direct Dart/Flutter remains OPEN; no runtime transfer was claimed.
- Architecture: release decisions must preserve exact verifier/run/subject identity and contradictory evidence.
- Mobile: Studio text subject is not a mobile artifact or release proof.
- Data: no new persistence claim.
- Quality: run 1 is a test-oracle/reporting defect; runs 2-3 are distinct verifier failures without root cause.
- Systems: owning track; S005 authorization policy remains OPEN.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded supply-chain mechanism.
- Product repositories: no product behavior audited; no product canonical files edited.

## OPEN / CHANGE WATCH

- command-level stderr/log access for failed hosted verifier runs;
- reason repository-only verification changed from success to failure for the fixed subject;
- signer-workflow/source-ref/source-digest positive and negative policy execution after baseline stability is restored;
- offline bundle/trusted-root verification remains independently OPEN;
- GitHub Actions, GitHub CLI, attestation API, Sigstore roots and service behavior are version/service sensitive.

## HANDOFFS

### Quality
Treat run 1 as an oracle-design failure: `continue-on-error` plus step conclusion is not a valid substitute for the underlying command outcome. Preserve run 3 as a separate system-under-test contradiction.

### Architecture / release governance
Do not define a release gate as simply `gh attestation verify` without preserving exact subject, repository, signer-policy inputs, verifier/tool identity and diagnosable failure output.
