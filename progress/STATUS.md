# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + first Flutter framework execution; F004 isolate; F005 async; F006 harness containment validated but socket verdict/root cause OPEN; F002/F003 transfer OPEN |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 decision governance evidence |
| Mobile | Stage 1 IN STUDY — M001 first direct Flutter framework execution; native/browser/EFB/product runtime transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 product-owned Flutter 3.38.7 project baseline recovered and dependency-lock transfer validated; operational release toolchain/source build/artifact identity OPEN |

No specialist has passed Foundation.

## Meaningful new evidence

### S004 — LogMate product-owned Flutter baseline recovered and executed
Product evidence identity: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19`; production identity remains unknown and `main` is not assumed production.

**SOURCE:** exact product `.metadata` records Flutter revision `3b62efc2a3da49882f43c372e0bc53daef7295a6`, stable channel, and matching create/base migration revisions. Official `flutter/flutter` tag `3.38.7` resolves exactly to that revision. This corrects the prior over-broad statement that no exact Flutter identity existed in product evidence: an exact project-generation/migration baseline exists, while explicit operational/release-toolchain identity remains unknown.

**VALIDATION:** workflow head `7815772bc11f8902dee2816165195c56ad45fef9`, run `35449021735`, job `105912825103` installed exact Flutter 3.38.7, recorded toolchain identity, accepted the exact product-derived committed lock unchanged under `flutter pub get --enforce-lockfile`, and rejected a deliberate one-nibble hosted-package content-hash mutation. Job `105912825084` replicated the 3.38.10 positive+negative result. Job `105912824971` reproduced the expected 3.47.0 unchanged-lock rejection. Overall matrix conclusion is failure solely because the deliberately retained incompatible 3.47.0 leg fails its positive prerequisite.

**TRANSFER VALIDATION:** `product .metadata revision → official Flutter 3.38.7 → executable lock acceptance + integrity-negative rejection` is demonstrated. This closes the product-baseline dependency-lock rung, not canonical release/build/artifact provenance.

## Retained evidence
- F001: direct Dart JIT/AOT and first Flutter framework/test-binding execution successful.
- F004/F005: direct Dart isolate and async transfers successful at bounded hosted-Linux scope.
- F006: reproduced hang, falsified close-order hypothesis and successful outer CI containment; socket correctness/root cause OPEN.
- Architecture: A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, evolution and evidence-preserving decisions.
- Mobile: M001 direct framework execution; M002-M006 model/professional boundaries; native/browser/EFB transfer OPEN.
- Data: D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- Quality: Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- Systems: S001-S006 retained; S005 hosted attestation evidence plus verifier contradiction; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Systems / Mobile / Quality:** use Flutter 3.38.7 as the exact product-owned project baseline, not automatically as release policy. Preserve 3.38.7/3.38.10 accepting evidence and 3.47.0 resolver rejection as distinct upgrade-regression classes.
- **Systems / LogMate:** next missing identity is explicit CI/operator/release toolchain/build path; no product files were edited.
- **Quality / Systems:** F006 outer deadline containment remains reusable validation-harness evidence.
- **Data / Architecture:** transport termination remains distinct from application completion/ACK/durable effect.
- **Design Studio / Web Manager / Marketing Manager:** considered under the cross-repository contract; no canonical decisions changed and no files edited there.

## Current Balance Loop
Do not repeat arbitrary Flutter SDK matrices. The strongest next S004/S005 rung is explicit product CI/operator/release toolchain/build-path evidence → canonical or explicitly baseline-labeled source build → artifact identity. If release identity cannot be recovered, do not relabel `.metadata` or 3.38.7 as production; move to the highest-value independent evidence class such as F002/F003 or a materially stronger platform/product transfer. F006 close-order variants and S005 flag permutations remain deprioritized.

## CHANGE WATCH
- Flutter/Dart runtime/build/pub behavior is version-sensitive; exact SDK/ref/engine identity matters.
- A moving Flutter `stable` label is not sufficient artifact identity.
- Product-owned LogMate project baseline is exact Flutter 3.38.7; operational release toolchain/production identity remains unknown.
- Canonical LogMate source build/artifact identity remains OPEN.
- F006 direct Dart socket root cause/verdict is OPEN.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool-version sensitive; hosted verification has contradictory success/failure evidence.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
