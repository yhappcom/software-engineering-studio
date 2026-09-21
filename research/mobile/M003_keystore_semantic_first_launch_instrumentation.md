# M003 — Keystore semantic first-launch instrumentation

Status: **IN STUDY — bounded semantic REPLICATION achieved; intermittent first-launch ROOT CAUSE remains OPEN**  
Evidence date: 2026-09-21

## Problem
The original Android Keystore semantic fixture has one complete bounded PASS and multiple first-launch-adjacent failures. A simplified fixture subsequently proved that package PID, Activity entry, native completion, UI publication/resume, and UI-automation observation can all succeed in the available API-35 emulator environment, but it removed Keystore/AES-GCM semantics and therefore could not establish root cause.

The professional boundary required a complete repeated semantic execution under instrumentation that can discriminate startup, native cryptographic completion, UI publication, and UI-automation observation without changing the security semantics.

## Balance Loop selection
This continuation outranked a new shallow topic because it was a bounded unresolved contradiction with direct Mobile ownership and Quality/Systems leverage. Physical Android/iOS/Safari and canonical product runtime remain stronger eventual transfer rungs but are not available in this execution context; S004 product source build remains authorization-dependent. Re-running the unchanged oracle was explicitly rejected.

## Instrumented semantic experiment
Workflow: `.github/workflows/m003-android-keystore-secure-storage-validation.yml`  
Initial instrumented head: `d6641234713784620fd6bcfe8e6c12e519b33c87`  
Metadata-observable head: `8163960e333751df91f4dc639c59590f23eea1e8`  
Successful run: `35557564657`, attempt 1, job `106204067727`  
Target remains the isolated Flutter-created Android app with pinned Flutter `3.47.5`, Android API 35 x86_64 emulator, AndroidKeyStore AES-256/GCM key, app-private ciphertext, force-stop/fresh-process recovery, external ciphertext mutation, and authentication rejection.

### Preserved semantics
The key alias, AndroidKeyStore provider, AES/GCM primitive, 256-bit key request, key purposes, block mode, padding, ciphertext/IV representation, marker value, app-private file, force-stop/recovery sequence, external tamper mutation, and final `AUTH_FAIL` semantic oracle are unchanged. The later head changes failure reporting only.

### Independent signals
The application emits independent native log markers around the original semantic path:
1. `ACTIVITY_ONCREATE_ENTER` before `super.onCreate`;
2. `FLUTTER_SUPER_ONCREATE_RETURNED` after the Flutter activity superclass returns;
3. `NATIVE_RESULT:WROTE:secure-v1:NONEXPORTABLE` only after the original Keystore/AES-GCM write path completes;
4. `UI_PUBLISHED:WROTE:secure-v1:NONEXPORTABLE` after `setContentView` publishes the result;
5. `ACTIVITY_ONRESUME` from the Activity lifecycle callback;
6. independent `uiautomator` observation of the same semantic result.

The harness separately records phases `first_launch_start`, `first_launch_pid`, `first_launch_activity`, `first_launch_native`, `first_launch_ui_publish`, `first_launch_resume`, and `first_launch_ui_observe` before proceeding to the unchanged recovery/tamper phases. It polls boundedly rather than treating a fixed three-second sleep as the only readiness criterion.

## CONTRADICTION — run 35554495251
Exact head `d6641234713784620fd6bcfe8e6c12e519b33c87`, job `106195370405` completed failure. Checkout, pinned Flutter installation, toolchain recording, fixture creation/build, independent oracle creation and KVM setup all succeeded. The emulator action trapped its internal result, but ordinary Actions metadata exposed only the aggregate `Require complete oracle` failure, so the exact first absent signal could not be recovered.

**VERDICT:** this reproduced the semantic failure class but did not localize it. ROOT CAUSE remained OPEN. The evidence-channel weakness motivated named phase verdicts rather than a semantic change.

## REPLICATION — run 35557564657
Exact head `8163960e333751df91f4dc639c59590f23eea1e8`, attempt 1, job `106204067727` completed **success**. Checkout, pinned Flutter installation, toolchain recording, isolated fixture build, independently instrumented oracle, KVM setup, emulator execution and natural job completion all succeeded. Every named failure-phase step was skipped and the explicit `M003 bounded Keystore oracle passed` step succeeded.

**VALIDATION:** the original Keystore semantic path completed again under stronger phase-observable instrumentation. This supplies a second complete semantic execution in the same bounded API-35 emulator class while preserving key/crypto/ciphertext/recovery/tamper semantics.

**REPLICATION:** awarded at this bounded semantic/environment scope. This is stronger than the earlier one-off PASS because a later independently executed workflow instance again reached the complete oracle after intervening failures. It is not cross-device, physical-device, StrongBox, iOS, product, or production replication.

**CONTRADICTION retained:** earlier runs failed first-launch-adjacent, including a same-head retry of the first successful fixture and the first instrumented semantic run. The new success proves the semantic target is not deterministically broken; it does not explain why those failures occurred.

**ROOT CAUSE:** remains OPEN. Because the successful run contains no failing phase, it cannot localize the intermittent defect. Do not relabel timing/readiness, emulator scheduling, Keystore latency, Activity startup, or UI automation as root cause without a reproduced failing run whose independent phase marker is externally visible and a causal falsification experiment.

## Failure interpretation rules
- no PID: startup/process boundary;
- PID but no Activity marker: Activity entry boundary;
- Activity entry but no expected native result: native/Keystore/AES-GCM semantic boundary;
- native result but no UI-published marker: publication boundary;
- UI published/resumed but no `uiautomator` result: observation/readiness boundary;
- complete first launch but later failure: preserve the exact recovery/tamper phase rather than relabeling it first-launch failure.

A reproduced failure phase is not automatically root cause. Causal repair still requires a hypothesis and falsification/check matched to the localized boundary.

## RELATED DOMAIN CHECK
- Foundations: direct Dart/Flutter execution exists; no new Foundations prerequisite blocks this diagnostic.
- Architecture: no application contract is changed; instrumentation is observational.
- Mobile: lead owner; Android runtime/platform boundary under test.
- Data: recovery remains logical fresh-process recovery, not physical durability/backup evidence.
- Quality: independent signals strengthen fault isolation; the evidence channel now exposes phase verdicts through named job steps.
- Systems: cryptographic/key semantics are preserved, but this is emulator evidence and does not establish StrongBox/hardware backing/auth policy.
- Design Studio: not materially relevant; no user interaction contract changes.
- Web Manager / Marketing Manager: not materially relevant to this native diagnostic.
- Product repositories: not inspected because this remains an isolated Studio fixture and makes no MintTap/LogMate implementation claim.

## HANDOFFS
- Mobile → Quality: phase-observable instrumentation can coexist with the original semantic oracle; a future intermittent failure should be localized from named phase metadata before any causal claim.
- Mobile → Systems: bounded semantic replication now exists for emulator AndroidKeyStore process recovery + tamper rejection, but hardware-backed/StrongBox/auth policy/root resistance and product security remain separate evidence classes.
- Mobile → Data: repeated fresh-process recovery is still not fsync/power-loss durability or backup correctness.

## OPEN / CHANGE WATCH
- Intermittent first-launch ROOT CAUSE remains OPEN; do not spend repeated runs merely trying to catch it unless a failure would materially discriminate a causal hypothesis.
- Physical Android/iOS, hardware-backed/StrongBox, auth-bound keys, backup/restore, reinstall/migration and product transfer remain OPEN.
- The bounded semantic REPLICATION does not upgrade Mobile Stage 1 to PASS.
