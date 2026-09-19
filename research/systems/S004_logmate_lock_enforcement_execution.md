# S004 — LogMate lock enforcement execution transfer

Date: 2026-09-19
Lead: Systems
Status: IN STUDY — product-owned Flutter project baseline recovered and lock-transfer validated; canonical operational/release toolchain and source build remain OPEN

## Product identity
`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-19`. Production identity is unknown; default branch is not assumed production.

## SOURCE / product-owned metadata identity
At the exact LogMate ref, version-controlled `.metadata` records `version.revision: 3b62efc2a3da49882f43c372e0bc53daef7295a6`, channel `stable`, and the same create/base migration revision across root/android/ios/linux/macos/web/windows. The file says it tracks Flutter project properties for Flutter tooling/upgrades; it does not state that this revision is the current CI/operator/release SDK.

Authoritative upstream GitHub evidence resolves official `flutter/flutter` tag `3.38.7` directly to commit `3b62efc2a3da49882f43c372e0bc53daef7295a6`. The upstream commit is the 3.38.7 stable-hotfix changelog commit and is GitHub-signature verified.

**SYNTHESIS:** LogMate contains a product-owned exact Flutter project-generation/migration baseline that maps to official Flutter 3.38.7.

**CONTRADICTION / correction:** prior wording that no exact Flutter identity existed in product-repository evidence was too broad. Exact project metadata identity exists; explicit operational/release-toolchain identity still does not.

## VALIDATION — product-metadata-grounded transfer
Workflow head `7815772bc11f8902dee2816165195c56ad45fef9`; hosted run `35449021735`; Ubuntu hosted runners. The matrix deliberately included 3.38.7 from product metadata, prior accepting 3.38.10, and prior incompatible 3.47.0. Overall workflow conclusion is `failure` because fail-fast was disabled and 3.47.0 is an expected controlled incompatibility; individual-job verdicts are the evidence.

### Flutter 3.38.7 — VALIDATION success
Job `105912825103` completed success. Flutter installation and toolchain-identity recording succeeded. The exact product-derived manifest/lock pair passed `flutter pub get --enforce-lockfile` unchanged, and the deliberate one-nibble hosted-package content-hash mutation was rejected by the negative oracle. This is executable compatibility evidence at the exact product-owned project baseline, not merely metadata reading.

### Flutter 3.38.10 — REPLICATION success
Job `105912825084` completed success. The prior accepting result reproduced: unchanged-lock enforcement passed and the deliberate hash mutation failed closed.

### Flutter 3.47.0 — CONTRADICTION replicated
Job `105912824971` completed controlled failure at unchanged-lock enforcement; the negative mutation step was skipped because the positive prerequisite failed. This reproduces the prior later-toolchain incompatibility rather than treating the matrix-level failure as a regression in the validated 3.38.x paths.

## TRANSFER VALIDATION
The evidence chain is now stronger:

`product .metadata exact revision → official Flutter 3.38.7 tag → exact product-derived lock accepted unchanged + deliberate hash corruption rejected`

`nearby Flutter 3.38.10 → same positive/negative behavior replicated`

`later Flutter 3.47.0 → same committed graph rejected because SDK-coupled resolution differs (prior run isolated seven changing packages)`

This demonstrates that the committed lock is executable under the product-owned **project baseline** while remaining toolchain-sensitive across later SDK evolution.

## ENGINEERING JUDGMENT
`.metadata` + successful lock execution is materially stronger than choosing an SDK only because dependency ranges permit it. It still does not establish that 3.38.7 built a shipped artifact, was used by CI/operator release tooling, or is production identity. A canonical source-build claim still requires explicit product build path/toolchain evidence or a carefully labeled baseline build that does not masquerade as release provenance.

## RELATED DOMAIN CHECK
- Foundations: hosted Dart/Flutter execution available; no new Foundation semantic claim.
- Architecture: toolchain identity is a release contract when reproducibility/provenance is required.
- Mobile: exact project baseline now has executable dependency-resolution transfer; Android/iOS/browser runtime remains OPEN.
- Data: not materially changed.
- Quality: positive unchanged-lock oracle + deliberate integrity-negative oracle + later-toolchain contradiction were all exercised; 3.38.10 also replicated.
- Systems: lead track; S004 identity/lock rung materially advanced.
- Design Studio / Web Manager / Marketing Manager: considered under cross-repo contract; no canonical decision changed and no files edited.
- Product: exact LogMate ref and `.metadata` checked; no product files edited.

## HANDOFFS
### Systems → Mobile / Quality / LogMate release engineering
Use Flutter 3.38.7 as the exact product-owned **project baseline** when a grounded historical validation target is needed. Do not rename it canonical release SDK without CI/operator/release evidence. Preserve 3.47.0 as an upgrade-compatibility failure class requiring deliberate lock/toolchain migration rather than silent lock rewrite.

## OPEN / CHANGE WATCH
- Explicit canonical operational/release Flutter SDK/engine and external CI/operator pin remain unknown.
- Canonical LogMate source build, target artifact digest, signing/attestation and independent-host reproducibility remain OPEN.
- No production identity is known; `main` is not assumed production.
- Flutter/pub behavior is version-sensitive; preserve exact release/ref/engine/Dart identity for every verdict.
