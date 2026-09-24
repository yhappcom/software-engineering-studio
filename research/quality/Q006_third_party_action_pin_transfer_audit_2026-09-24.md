# Q006 — Third-party action pin transfer audit (2026-09-24)

Status: **IN STUDY — NATURAL CROSS-TRACK REPRODUCIBILITY CONTRADICTION IDENTIFIED; REPAIR/REGRESSION OPEN**

Lead: Quality; support: Systems, Mobile

## Problem / selection rationale

The Balance Loop still ranks S007 exact LogMate Auth transfer highest when implementation exists, but `yhappcom/logmate` remains at documentation-only head `7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3` for the current account-required Welcome change. Manufacturing another synthetic Auth model would not improve product evidence. Q006 therefore continues at a materially different natural transfer boundary: whether the immutable third-party-action provenance rule already validated in the Q006 control survives transfer into older Mobile evidence workflows.

F001 direct Dart JIT/AOT and Flutter browser execution are not blockers; the global status explicitly marks that historical prompt premise stale.

## SOURCE / exact repository context

Studio audit target:

`yhappcom/software-engineering-studio → main → 2f0cf3ac01c08561347f1707350c98eaab22eead → evidence date 2026-09-24`.

Product recheck:

`yhappcom/logmate → main → 7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3 → declared 1.0.0+1 from retained S007 audit → evidence date 2026-09-24`.

Production identity remains unknown; default branch is not assumed production.

Canonical Q006 prior evidence established that `reactivecircus/android-emulator-runner@v2` currently resolves to commit `a421e43855164a8197daf9d8d40fe71c6996bb0d`, and the dedicated causal control was repaired to use that immutable commit. The pinned regression retained the delegated-failure reachability and independent `outcome=failure` oracle.

## TRANSFER VALIDATION / CONTRADICTION

Direct inspection of current natural Mobile workflows shows the provenance repair has **not** transferred uniformly:

- `.github/workflows/m001-android-emulator-runtime-validation.yml` still invokes `reactivecircus/android-emulator-runner@v2`.
- `.github/workflows/m003-android-keystore-secure-storage-validation.yml` still invokes `reactivecircus/android-emulator-runner@v2`.

M003 additionally wraps its emulator script in an explicit semantic protocol: the script records `phase` and `oracle_rc`, deliberately exits zero from its EXIT trap, and downstream workflow steps fail closed unless `phase == complete` and `oracle_rc == 0`. **ENGINEERING JUDGMENT:** this is a valid semantic-verdict composition pattern at the inspected source boundary; the new contradiction is dependency identity/replayability, not an identified false-green in that downstream oracle.

M001 records the Flutter checkout SHA after cloning the moving `stable` branch. That preserves the observed toolchain identity for a completed historical run, but a future rerun of the same workflow source can select a different Flutter commit. This is a distinct reproducibility boundary from the third-party action pin: recorded resolved identity can make an observed run interpretable, while immutable inputs are required when the claim is deterministic replay of the same dependency graph.

## SYNTHESIS

There are two separate provenance contracts:

1. **run interpretation:** record what actually executed, so historical evidence can be bounded to a concrete dependency/toolchain identity;
2. **replay control:** pin dependency/action inputs when a future run is expected to exercise the same dependency implementation.

Recording a resolved version after execution does not make the workflow definition immutable. Conversely, pinning an action does not by itself prove the action behaved correctly; the Q006 causal control required an independent semantic oracle as well.

The Mobile evidence remains useful at its recorded historical run/head/environment boundary. This audit does **not** retroactively invalidate M001/M003 observations. It limits claims that the current workflow source alone is sufficient to reproduce the same third-party action implementation in a later run.

## VALIDATION

This block is a source/provenance transfer audit. No new Android execution was performed and no Mobile PASS is awarded. A professional closure requires:

1. replace moving `reactivecircus/android-emulator-runner@v2` references in each selected evidence-producing workflow with an reviewed immutable commit SHA;
2. record why that SHA is trusted/current enough for the intended experiment;
3. run the changed workflow at an exact head;
4. verify the original semantic oracle still passes/fails as intended;
5. preserve exact run/job/toolchain/action identity and any artifacts required by the claim.

Do not bulk-rewrite unrelated actions without semantic review: action updates can change behavior and should be treated as dependency changes, not formatting.

## FAILURE MODEL / EVIDENCE LIMIT

This audit can detect a moving action reference in inspected source. It does not establish the exact resolved action SHA used by historical M001/M003 runs, because current tag resolution must not be projected backward. It does not prove compromise, malicious behavior, or a runtime defect. It also does not establish repository-wide pin coverage; the inspected natural transfer is bounded to the named workflows.

## RELATED DOMAIN CHECK

- Foundations: checked; direct Dart/Flutter evidence exists and is not the current blocker.
- Architecture: dependency identity is part of an executable evidence contract; no new architecture claim.
- Mobile: materially relevant; M001/M003 natural workflows are the transfer targets.
- Data: considered; not materially relevant to this dependency-provenance mechanism.
- Quality: owner; Q006 immutable-action rule transferred to natural Mobile evidence workflows.
- Systems/Security/Performance/Delivery: materially relevant for supply-chain provenance and reproducible delivery evidence.
- Design Studio: considered; not materially relevant.
- Web Manager: considered; not materially relevant.
- Marketing Manager: considered; not materially relevant.
- Product source: LogMate exact ref rechecked only to decide Balance Loop priority; no product runtime claim made.

## HANDOFFS

### Mobile
The M001 and M003 workflows should not claim replay of the same emulator-runner implementation while using moving `@v2`. Preserve their existing semantic oracles when pinning; rerun rather than treating a textual pin as execution evidence.

### Systems
Treat action identity as supply-chain/release provenance. Historical resolved identity remains OPEN unless the historical run itself supplies trustworthy resolution evidence; current tag state cannot backfill it.

## OPEN / CHANGE WATCH

- OPEN: exact historical resolved action identity for M001/M003.
- OPEN: immutable-pin repair and exact-head hosted regressions for the natural Mobile workflows.
- OPEN: broader repository-wide third-party-action pin inventory; this bounded transfer must not be generalized to every workflow.
- CHANGE WATCH: upstream action commits and Flutter stable move over time; any upgrade is a reviewed dependency change.
