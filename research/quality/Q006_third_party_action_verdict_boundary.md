# Q006 — Third-party action verdict boundary

Date: 2026-09-24
Lead: Quality
Status: IN STUDY — intentional delegated-script failure causality VALIDATED at bounded hosted target; action provenance and broader transfer OPEN

## Problem

The repository-wide selected-token inventory does not detect a distinct CI acceptance boundary: a workflow can delegate a verdict-bearing command to a JavaScript/container action. Correctness then depends on whether the action propagates the delegated command's failure to the GitHub step verdict.

## Exact Studio target

Repository: `yhappcom/software-engineering-studio`
Initial executable control: `9ea9c97838d443c8fa81b04729e0447aee54c175`
Causal-strengthening head: `91f4e5de13974d724b5d46bfbd801ab6af4ed721`
Hosted causal run: `35942964741`
Hosted causal job: `107454700986`
Reachability artifact: `10785418174`, name `q006-delegated-reachability`, digest `sha256:42ad5c3b2bc71dc41e5c9ccd4f8000b4ea12dd14dde9fdc86025d79f7b7c5d8f`
Evidence date: 2026-09-24

Representative consumer: `.github/workflows/m002-android-process-death-storage-validation.yml`, which delegates its fail-fast oracle to `reactivecircus/android-emulator-runner@v2`.

## SOURCE — action implementation boundary

Inspection of the upstream `v2` action source showed user scripts executed through `@actions/exec`; execution errors are caught and passed to `core.setFailed`. This supports a fail-closed wrapper model, but the moving major tag is not immutable provenance and source reading is not runtime validation.

## SYNTHESIS

Verdict propagation has at least three layers: producer/oracle exit semantics; action-wrapper semantics; workflow/job acceptance semantics. A lexical audit of workflow shell cannot prove the action-wrapper layer.

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

GitHub's job record shows:

- delegated Android-emulator action step completed under `continue-on-error`;
- `Persist delegated-script reachability marker` completed successfully;
- `Require wrapper to expose delegated failure` completed successfully.

The run published artifact `10785418174`, digest `sha256:42ad5c3b2bc71dc41e5c9ccd4f8000b4ea12dd14dde9fdc86025d79f7b7c5d8f`. Direct inspection of the downloaded ZIP found exactly one 43-byte file, `q006-delegated-reachability.txt`, whose content is:

`Q006_INTENTIONAL_DELEGATED_FAILURE_REACHED`

The downstream assertion can succeed only when the delegated step's `outcome` is `failure` and its post-continue `conclusion` is `success`.

**VALIDATION verdict:** the prior provisioning/action-internal alternative cause is closed for this bounded run. The delegated script definitely reached the intentional failure path and the action invocation exposed a failure outcome through the wrapper boundary. This validates the intended nonzero-propagation mechanism at this exact hosted target.

## Evidence limit

This does not prove:

- that every command failure mode inside `reactivecircus/android-emulator-runner` propagates identically;
- that future `@v2` resolutions behave identically;
- that the historical M002 action resolved to the same upstream commit;
- repository-wide CI semantic correctness;
- PowerShell/cmd/container/composite-action transfer;
- production release-gate correctness.

The workflow intentionally converts the expected delegated failure into an overall green control job after independently asserting the failure outcome. Therefore the overall green run is evidence only because the negative-control oracle and durable reachability artifact are both inspected; workflow green alone remains insufficient.

## ENGINEERING JUDGMENT

The professional boundary for this specific causal question is now materially stronger than source inspection or outcome metadata alone: producer reachability and wrapper verdict propagation are independently observable. Future third-party-action controls should use the same pattern when infrastructure/setup failure can mimic the expected action outcome.

The remaining high-value issue is provenance: `reactivecircus/android-emulator-runner@v2` is a moving major tag. Runtime propagation evidence cannot make that dependency immutable or establish the exact action source used by historical runs.

## VALIDATION / OPEN

- **VALIDATED, bounded:** delegated script reached the intentional failure path and the third-party action exposed `outcome=failure`; `continue-on-error` preserved downstream observability with `conclusion=success`.
- **VALIDATED, bounded:** durable artifact plus independent step-outcome oracle distinguishes delegated-script reachability from provisioning failure for run `35942964741`.
- **OPEN / DEPENDENCY:** exact resolved `reactivecircus/android-emulator-runner@v2` commit identity for this run and historical M002 runs.
- **OPEN:** semantic review of other third-party actions and GitHub-expression/action-output acceptance paths.
- **OPEN / TRANSFER VALIDATION:** non-Bash shells, other action types, and production release gates.
- No repository-wide semantic correctness PASS is awarded.

## RELATED DOMAIN CHECK

- Foundations: command/process exit semantics are prerequisite; direct Dart/Flutter evidence is already available and is not this block's blocker.
- Architecture: wrapper boundary is an interface contract between delegated oracle and CI runner.
- Mobile: M002 is the representative consumer; this control does not revalidate Android process-death/storage behavior.
- Data: persistent-file semantics are not revalidated.
- Quality: owner; causal delegated-script nonzero propagation is now bounded VALIDATED.
- Systems: moving action identity/pinning remains a supply-chain/provenance dependency.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded CI-verdict mechanism.
- Product source/ref: not required; this block audits Studio CI only.

## HANDOFFS

### Quality → Systems
- Finding: verdict-bearing third-party actions require both runtime wrapper-failure evidence and dependency provenance. The runtime causal gap is now closed for run `35942964741`; moving `@v2` identity remains unresolved.
- Evidence: this note; exact head `91f4e5de...`; run `35942964741`; job `107454700986`; artifact `10785418174`.
- Impact: do not infer immutable supply-chain provenance from successful runtime validation.
- Requested action: preserve/resolution-check exact action identity and compare commit pinning when S004/S005 revisits supply-chain provenance.
- Status: OPEN.
