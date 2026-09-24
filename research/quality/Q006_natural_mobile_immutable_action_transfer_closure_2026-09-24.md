# Q006 — Natural Mobile immutable-action transfer closure

Date: 2026-09-24
Lead: Quality, Testing & Reliability
Support: Mobile & Cross-Platform Engineering; Systems/Delivery

## Problem

The dedicated Q006 third-party-action control had already pinned `reactivecircus/android-emulator-runner` to immutable commit `a421e43855164a8197daf9d8d40fe71c6996bb0d`, while natural M001 and M003 Android evidence workflows still used moving `@v2`. This created a provenance/replayability gap even though it did not retroactively invalidate the historical semantic observations.

## SOURCE / prior evidence

Canonical prior audit: `research/quality/Q006_third_party_action_pin_transfer_audit_2026-09-24.md`.

The reviewed immutable action identity is:

`reactivecircus/android-emulator-runner@a421e43855164a8197daf9d8d40fe71c6996bb0d`.

## Repair

Two natural Mobile workflows were changed without altering their intended semantic oracle:

- M001 source head: `1f8bf2b66e7f5dea2ac8213a6ecfb5bbb55cd0f4`
- M003 permission source head: `acb1503ab9b14af26780f9ddccf312595558a1f9`

The change replaces the moving emulator-runner tag with the reviewed immutable action commit. This is a dependency-identity repair, not a new Mobile behavior contract.

## TRANSFER VALIDATION

### M001

GitHub-hosted run `35999124221`:

- workflow: `M001 Android emulator Flutter runtime validation`
- exact head: `1f8bf2b66e7f5dea2ac8213a6ecfb5bbb55cd0f4`
- status: completed
- conclusion: success
- run attempt: 1

The hosted regression therefore demonstrates that the natural M001 workflow still completes successfully after immutable dependency pinning.

### M003 permission

GitHub-hosted run `35999145144`:

- workflow: `M003 Android runtime permission validation`
- exact head: `acb1503ab9b14af26780f9ddccf312595558a1f9`
- status: completed
- conclusion: success
- run attempt: 1

The hosted regression therefore demonstrates that the natural M003 permission workflow still completes successfully after immutable dependency pinning.

## SYNTHESIS

The Q006 supply-chain/provenance rule transfers to two natural Android evidence workflows: pinning the third-party action to the reviewed immutable commit did not break their existing hosted acceptance paths. This closes the specific OPEN item "immutable pin + hosted regression for inspected natural M001/M003 workflows."

This does **not** prove historical runs used this same action implementation. Historical resolved identity remains unknown unless independently preserved by historical evidence. It also does not prove all repository actions are immutably pinned or all CI semantics are correct.

## ENGINEERING JUDGMENT

Dependency provenance and semantic correctness are separate evidence dimensions. A workflow may have a sound semantic oracle but weak replay provenance, or immutable dependency identity but a weak oracle. Release-grade evidence needs both when the dependency can materially affect the result.

## VALIDATION boundary

Validated:
- exact-head hosted regression after immutable action pin for M001;
- exact-head hosted regression after immutable action pin for M003 permission;
- preservation of the workflows' successful acceptance path after the provenance repair.

Not established by this note:
- physical Android/OEM behavior;
- iOS behavior;
- exact product runtime;
- production release-gate correctness;
- historical resolved action identity;
- repository-wide immutable dependency coverage.

## RELATED DOMAIN CHECK

- Foundations: direct Dart/Flutter execution already exists; no new foundational blocker.
- Architecture: dependency identity is an execution/evidence contract, not product behavior.
- Mobile: directly affected; natural M001/M003 workflows are the transfer targets.
- Data: not materially relevant to this bounded dependency-provenance repair.
- Quality: owns oracle/provenance evidence interpretation.
- Systems/Delivery: immutable third-party action identity is supply-chain/build provenance.
- Design Studio: not materially relevant.
- Web Manager: not materially relevant.
- Marketing Manager: not materially relevant.
- Product source: no product repository behavior is claimed.

## OPEN / CHANGE WATCH

- Historical resolved action identity remains OPEN where not independently preserved.
- Repository-wide third-party action provenance remains OPEN.
- Q006 secret-redacted/cancelled paths, non-Bash/action-type transfer and production release-gate transfer remain OPEN.
- Mobile physical-device/OEM/iOS/product transfer remains OPEN.

## HANDOFFS

### TO Mobile
Treat M001 and M003 permission immutable-pin regression as validated bounded evidence. Do not infer physical-device or product PASS.

### TO Systems/Delivery
Use the same distinction in release evidence: immutable dependency input identity and semantic verdict integrity are separate required provenance dimensions.

### TO Quality
Remove the now-closed natural M001/M003 immutable-pin regression item from the immediate queue. Do not repeat equivalent pin-only controls; move to a materially different failure/evidence class.
