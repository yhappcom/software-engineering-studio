# Q006 — Third-party action verdict boundary

Date: 2026-09-24
Lead: Quality
Status: IN STUDY — intentional delegated-script failure causality + immutable pinned-action regression VALIDATED at bounded hosted target; historical run provenance remains OPEN

## Problem

The repository-wide selected-token inventory does not detect a distinct CI acceptance boundary: a workflow can delegate a verdict-bearing command to a JavaScript/container action. Correctness then depends on whether the action propagates the delegated command's failure to the GitHub step verdict.

## Exact Studio target

Repository: `yhappcom/software-engineering-studio`
Initial executable control: `9ea9c97838d443c8fa81b04729e0447aee54c175`
Causal-strengthening head: `91f4e5de13974d724b5d46bfbd801ab6af4ed721`
Hosted causal run: `35942964741`
Hosted causal job: `107454700986`
Reachability artifact: `10785418174`, name `q006-delegated-reachability`, digest `sha256:42ad5c3b2bc71dc41e5c9ccd4f8000b4ea12dd14dde9fdc86025d79f7b7c5d8f`
Provenance-pin commit: `7101e179449d5a222d6c8d4d16a96292526333eb`
Pinned hosted regression run: `35951572264`
Pinned hosted regression job: `107481046377`
Pinned reachability artifact: `10788483491`, digest `sha256:4a6697445957fd4b107cd77178bcefcf9edca00986b253e01ffef568d3285a31`
Evidence date: 2026-09-24

Representative consumer: `.github/workflows/m002-android-process-death-storage-validation.yml`, which delegates its fail-fast oracle to `reactivecircus/android-emulator-runner@v2`.

## SOURCE — action implementation and provenance boundary

Inspection of the upstream `v2` action source showed user scripts executed through `@actions/exec`; execution errors are caught and passed to `core.setFailed`. This supports a fail-closed wrapper model, but source reading is not runtime validation.

Fresh GitHub Git-reference inspection on 2026-09-24 resolves `refs/tags/v2` to annotated tag object `4c44018e59b437e86cdfc41da381398f93ed8808`, whose target is commit `a421e43855164a8197daf9d8d40fe71c6996bb0d`; the tagger timestamp is 2026-07-05T05:06:13Z. This establishes the **current observed tag resolution** at the evidence date. It does not, by itself, prove what commit GitHub Actions resolved for historical run `35942964741` or historical M002 runs because a mutable ref can be force-moved and the job metadata API does not expose the resolved action commit.

## SYNTHESIS

Verdict propagation has at least three layers: producer/oracle exit semantics; action-wrapper semantics; workflow/job acceptance semantics. A lexical audit of workflow shell cannot prove the action-wrapper layer. Dependency provenance is a fourth independent concern: a runtime pass through `@v2` does not make the action source immutable.

## Executable negative control

The strengthened workflow `.github/workflows/q006-third-party-action-nonzero-propagation.yml` delegates this script through the Android emulator action:

```sh
printf '%s\n' 'Q006_INTENTIONAL_DELEGATED_FAILURE_REACHED' > /tmp/q006-delegated-reachability.txt
echo 'Q006_INTENTIONAL_DELEGATED_FAILURE'
exit 37
```

The delegated action step is `continue-on-error: true` only so independent downstream observations can run. An `if: always()` `actions/upload-artifact@v4` step requires the reachability file to exist (`if-no-files-found: error`). A separate fatal shell oracle requires `steps.delegated.outcome == failure` and the expected post-continue `steps.delegated.conclusion == success`.

### Claim

When the action reaches the delegated script and the script executes its intentional failure path, the third-party action exposes a failure outcome through GitHub Actions rather than normalizing the delegated nonzero command to success.

### Oracle independence

Two distinct observations are required:

1. durable artifact content proves execution reached the statement immediately before the intentional `exit 37` path;
2. GitHub step metadata plus the downstream assertion prove the delegated action exposed `outcome=failure` across the wrapper/`continue-on-error` boundary.

Provisioning failure before the delegated script cannot create the committed reachability marker. Conversely, marker existence alone cannot establish wrapper failure propagation. Requiring both removes the alternative cause that weakened the first run.

## VALIDATION — hosted causal observation

At exact head `91f4e5de13974d724b5d46bfbd801ab6af4ed721`, workflow run `35942964741`, job `107454700986`, completed `success`.

GitHub's job record shows the delegated Android-emulator action step completed under `continue-on-error`; the reachability-artifact upload completed; and the independent wrapper-outcome assertion completed. The artifact contains exact content `Q006_INTENTIONAL_DELEGATED_FAILURE_REACHED`.

**VALIDATION verdict:** the prior provisioning/action-internal alternative cause is closed for this bounded run. The delegated script definitely reached the intentional failure path and the action invocation exposed a failure outcome through the wrapper boundary.

## PROVENANCE REPAIR — immutable future control

Commit `7101e179449d5a222d6c8d4d16a96292526333eb` replaces the Q006 control's moving `reactivecircus/android-emulator-runner@v2` reference with the exact observed target commit:

`reactivecircus/android-emulator-runner@a421e43855164a8197daf9d8d40fe71c6996bb0d`

### VALIDATION — pinned regression

The exact pinned head triggered run `35951572264`, job `107481046377`, on GitHub-hosted `ubuntu-latest`. The run completed `success` on 2026-09-24. The job record shows the delegated action step, durable reachability upload, and independent wrapper-outcome assertion all completed successfully.

Artifact `10788483491` was downloaded and directly inspected. It contains exact content:

`Q006_INTENTIONAL_DELEGATED_FAILURE_REACHED`

The artifact digest reported by GitHub is `sha256:4a6697445957fd4b107cd77178bcefcf9edca00986b253e01ffef568d3285a31`.

**VALIDATION verdict:** the immutable pinned action commit preserves the causal behavior established by the earlier moving-tag control: the delegated script reaches the intentional nonzero path and the wrapper exposes failure to the independent downstream oracle. The future Q006 control is therefore no longer dependent on movement of the `v2` tag.

This does not retroactively establish the exact action commit used by historical causal or M002 runs. The representative M002 workflow is intentionally not changed in this Quality block: changing another validated fixture's dependency would require its own transfer/regression run and belongs in a separate authorized evidence block.

## Evidence limit

This does not prove that every command failure mode inside the action propagates identically; that historical runs resolved to the currently observed commit; repository-wide CI semantic correctness; PowerShell/cmd/container/composite-action transfer; or production release-gate correctness.

## VALIDATION / OPEN

- **VALIDATED, bounded:** delegated script reached the intentional failure path and the third-party action exposed `outcome=failure` in run `35942964741`.
- **SOURCE / provenance snapshot:** on 2026-09-24 upstream `v2` resolved through annotated tag `4c44018...` to commit `a421e438...`.
- **REPAIR + VALIDATION:** Q006 causal control is pinned to `a421e438...` at Studio commit `7101e179...`; pinned run `35951572264` preserved both reachability and wrapper-outcome oracles.
- **OPEN / DEPENDENCY:** exact resolved action commit for historical causal run and historical M002 runs is not established by current tag state.
- **OPEN:** semantic review of other third-party actions and GitHub-expression/action-output acceptance paths.
- **OPEN / TRANSFER VALIDATION:** non-Bash shells, other action types, and production release gates.
- No repository-wide semantic correctness PASS is awarded.

## RELATED DOMAIN CHECK

- Foundations: command/process exit semantics are prerequisite; direct Dart/Flutter evidence already exists.
- Architecture: wrapper boundary is an interface contract between delegated oracle and CI runner.
- Mobile: M002 is the representative consumer; this block does not alter or revalidate its Android process-death/storage evidence.
- Data: persistent-file semantics are not revalidated.
- Quality: owner; causal propagation and immutable pinned regression are validated.
- Systems: exact dependency identity/pinning is a supply-chain provenance concern; current tag resolution is explicit while historical identity remains open.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded CI-verdict/provenance mechanism.
- Product source/ref: not required; this block audits Studio CI only.

## HANDOFFS

### Quality → Systems
- Current upstream `v2` provenance snapshot: annotated tag `4c44018...` → commit `a421e438...` on 2026-09-24.
- Q006 control is pinned to that commit at Studio head `7101e179...` and pinned hosted regression `35951572264` preserves the causal oracle.
- Do not backfill this current resolution as historical-run proof. Historical exact action identity remains OPEN unless run-bound evidence is recovered.
- Apply immutable-reference discipline to verdict-bearing third-party actions in release/security-sensitive workflows, with regression validation after pinning.
