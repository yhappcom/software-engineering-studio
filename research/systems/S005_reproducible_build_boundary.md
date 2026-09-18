# S005 — Bounded Reproducible-Build Boundary

Status: **TRANSFER / EXECUTABLE EVIDENCE — bounded GCC/Linux context**  
Evidence date: 2026-09-18

## Problem / selection
The Balance Loop selected S005 because direct Dart/Flutter execution remained unavailable, while S005 explicitly retained reproducible-build comparison as an OPEN evidence rung. This block tests whether identical source alone yields identical artifact bytes and isolates two concrete nondeterminism inputs rather than repeating the prior signature experiment.

## SOURCE
- GCC 14 documentation defines `-ffile-prefix-map=old=new` and explicitly states it can make reproducible builds location-independent by rewriting recorded path references.
- Reproducible Builds documents `SOURCE_DATE_EPOCH` as a standardized environment variable supplying a fixed reference time to supporting build tools, and separately documents timestamps as a common source of unreproducible output.

Primary sources:
- https://gcc.gnu.org/onlinedocs/gcc-14.1.0/gcc.pdf
- https://reproducible-builds.org/docs/source-date-epoch/
- https://reproducible-builds.org/docs/timestamps/

## SYNTHESIS
`same source` is weaker than `same artifact bytes`. Reproducibility is a relation over a declared build-input/environment equivalence class. If output records wall-clock time or build location, two otherwise equivalent builds can differ. Normalizing only one nondeterministic input is insufficient when another remains.

This is also distinct from **hermeticity**. The fixture does not prevent undeclared environment/tool inputs; it merely controls two observed sources of variation and compares resulting bytes.

## VALIDATION
Canonical fixture: `research/systems/fixtures/S005_reproducible_build_boundary.py`

### Test Evidence Contract
- **CLAIM:** in this GCC/Linux target, identical C source built in different absolute directories and at different wall-clock times is not byte-reproducible by default; timestamp normalization alone and path normalization alone remain insufficient; controlling both yields identical bytes for the bounded target.
- **SPEC/PROPERTY:** repeated builds under the declared normalized-input contract must produce byte-identical executable artifacts.
- **TARGET:** GCC 14.2.0 + GNU ld 2.44 compiling one C program with `-O2 -g` on Linux x86_64.
- **INPUT/STATE:** identical `main.c` in two different absolute build directories. Source embeds `__DATE__`/`__TIME__`; debug output can encode compilation-directory paths. Builds are separated by two seconds.
- **ORACLE:** SHA-256 plus direct byte equality (`cmp`/Python bytes). Expected mechanism comes from GCC prefix-map documentation and SOURCE_DATE_EPOCH documentation, not from duplicated compiler logic.
- **ENVIRONMENT:** GCC 14.2.0 (Debian 14.2.0-19), GNU ld 2.44, Python 3.13.5, Linux x86_64; evidence date 2026-09-18.
- **OBSERVATION:** naive builds differed. `SOURCE_DATE_EPOCH=1700000000` alone still differed. `-ffile-prefix-map=<builddir>=/src` alone still differed. With both controls, the two executables had identical SHA-256 `69c2e47764cc2a982a4a4cc1a535eb06e3a032a6450aee63875ac1fc12395dba` and direct byte comparison succeeded. The normalized executable printed `Nov 14 2023 22:13:20`, matching the fixed epoch's UTC representation used by GCC for the embedded build macros.
- **VERDICT:** PASS for the bounded byte-reproducibility property under the declared source/toolchain/flags and two normalized environmental inputs.
- **FAILURE MODEL:** wall-clock-derived build content and absolute build-location leakage.
- **REPRODUCTION DATA:** fixture, GCC/ld versions, `SOURCE_DATE_EPOCH=1700000000`, `-O2 -g`, two distinct temporary build directories, two-second build separation.
- **EVIDENCE LIMIT:** not a Flutter/Dart build, not a package/archive/app-bundle build, not cross-host or cross-toolchain reproducibility, not hermeticity, not dependency-lock verification, not CI/attestation, not signing, and not production evidence.

## FAILURE / ROOT CAUSE / ALTERNATIVE COMPARISON
The four-case matrix isolates the observed causes:

| Build condition | Byte-identical? | Interpretation |
| --- | --- | --- |
| no normalization | no | at least one uncontrolled build input affects bytes |
| fixed time only | no | build-location variation remains observable |
| path map only | no | wall-clock-derived content remains observable |
| fixed time + path map | yes | both observed variation sources are controlled in this bounded target |

The single-control failures falsify the weaker hypotheses that either timestamp normalization or path normalization alone was sufficient. The combined result supports sufficiency only for this fixture and environment; it does not prove that these are the only nondeterminism sources in a larger build.

## ENGINEERING JUDGMENT
A release pipeline should define what build inputs are intended to be invariant, rebuild independently under that contract, and compare exact artifact identity. A single successful same-machine rebuild is useful evidence but cannot establish cross-host/toolchain reproducibility. Reproducibility strengthens source/input-to-byte confidence; it does not establish source correctness, signer authorization, provenance, or deployment identity.

## RELATED DOMAIN CHECK
- **Foundations:** F001 source→toolchain→artifact distinctions directly apply; direct Dart/Flutter execution remains OPEN.
- **Architecture:** A006 evidence records should preserve exact toolchain/flags/input normalization when reproducibility supports a decision.
- **Mobile:** Flutter/Android/iOS package builds can introduce additional generated metadata, signing, packaging and platform-tool inputs; transfer remains OPEN.
- **Data:** migration/recovery acceptance can use exact artifact identity but does not become correct merely because a build is reproducible.
- **Quality:** byte equality is a valid oracle for the declared reproducibility claim, not for application correctness.
- **Systems:** extends S004 build-input identity and S005 release evidence; complements, rather than replaces, the real signature boundary.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this bounded compiler/build mechanism.
- **Product source/ref:** no product repository audited; no production claim is made.

## HANDOFFS
### TO Mobile
When a trustworthy Flutter/mobile toolchain is available, reproduce the canonical product build twice with captured source ref, lockfile/toolchain, build flags, post-build transforms and artifact hashes. Separate unsigned build reproducibility from signing/package-delivery identity.

### TO Quality
For release validation, treat reproducibility as its own oracle. Deliberately vary one supposedly normalized input to prove the gate can detect drift, and do not infer functional correctness from byte equality.

### TO Systems S004/S006
Build-input identity must include environmental/generated inputs that affect bytes. Rollback to an old source label by rebuilding is not equivalent to redeploying the previously accepted artifact unless reproducibility/equivalence is established.

## OPEN / VALIDATION / CHANGE WATCH
- **OPEN / TRANSFER VALIDATION:** Dart/Flutter canonical build; Android APK/AAB and iOS artifact packaging/signing; independent host/container rebuild; dependency graph/toolchain pinning; archives; CI attestation; production release artifacts.
- **OPEN:** hermeticity remains distinct and untested.
- **CHANGE WATCH:** GCC/toolchain behavior and supported reproducibility controls are version-sensitive; recorded evidence applies to GCC 14.2.0/ld 2.44.

## Gate effect
S005 now contains a real asymmetric-signature mechanism and a separate executable reproducible-build comparison with deliberate single-control failures. Systems Stage 1 remains **NOT PASS** because mobile/toolchain transfer, real CI/OIDC/attestation, authorization/key lifecycle, cross-environment reproducibility, deployment and production evidence remain OPEN.
