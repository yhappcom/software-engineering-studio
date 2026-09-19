# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + first Flutter framework execution; F004 isolate; F005 async; F006 harness containment validated but socket verdict/root cause OPEN; F002/F003 transfer OPEN |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 decision governance evidence |
| Mobile | Stage 1 IN STUDY — M001 first direct Flutter framework execution; native/browser/EFB/product transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 product-derived lock enforcement now validates exact-toolchain sensitivity and hash fail-closed behavior; canonical product toolchain/build/artifact identity OPEN |

No specialist has passed Foundation.

## Meaningful new evidence

### S004 — exact-toolchain lock-enforcement transfer completed
Product evidence identity: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19`; production identity remains unknown and `main` is not assumed production.

Workflow head `0426836a14866f00dd9de4811c7083bb1f1c0675`, run `35443257511` produced a controlled alternative comparison on Ubuntu 24.04.5.

**VALIDATION — accepting toolchain:** Flutter 3.38.10, framework `c6f67dede3d4aa1aa7a69dd56a3494a5cde6cc80`, engine `cafcda5721a78a7884db92f13c5e89f7643d52dd`, Dart 3.10.9 accepted the exact product-derived committed lock under `flutter pub get --enforce-lockfile`; byte comparison confirmed no lock rewrite. A deliberate one-nibble mutation of the locked `cupertino_icons 1.0.9` SHA-256 returned exit 65 and explicit content-hash mismatch, proving fail-closed sensitivity.

**ALTERNATIVE / CONTRADICTION — later toolchain:** Flutter 3.47.0, framework `4cf24164269a5ebf0c16a028a00727d0e77bbb05`, engine `5f77625673248ee5846fbcaf5d3e1a3878386fd7`, Dart 3.13.0 rejected the unchanged lock because seven SDK-coupled/transitive dependencies would change (`characters`, `intl`, `matcher`, `material_color_utilities`, `meta`, `test_api`, `vector_math`). The prior unknown-cause 3.47.0 failure is therefore narrowed to resolution/toolchain incompatibility, not unchanged-lock content-hash corruption.

**TRANSFER VALIDATION:** `SDK compatibility range != exact toolchain identity != demonstrated lock acceptance`. Success under 3.38.10 does not establish that 3.38.10 is LogMate's canonical toolchain. This closes only the Studio product-derived dependency-lock execution rung.

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
- **Systems / Quality:** preserve three distinct S004 observations: valid unchanged-lock acceptance, deliberate content-hash fail-closed rejection, and later-SDK resolver rejection.
- **Systems / Mobile / LogMate:** do not infer product policy from 3.38.10 acceptance. Canonical release evidence still needs product-owned exact toolchain identity → source build → artifact digest/identity.
- **Quality / Systems:** F006 outer deadline containment remains reusable validation-harness evidence.
- **Data / Architecture:** transport termination remains distinct from application completion/ACK/durable effect.
- **Design Studio / Web Manager / Marketing Manager:** considered under the cross-repository contract; this dependency-resolution block does not alter their canonical decisions; no files edited there.

## Current Balance Loop
The S004 lock-enforcement professional boundary is complete enough to stop repeating SDK matrices. Next priority is to recover trustworthy product-owned LogMate toolchain identity if accessible. If that identity cannot be established, do not simulate a canonical build or declare 3.38.10 canonical; advance the highest-value independent evidence class instead. F002/F003 remain Foundation alternatives. F006 close-order variants and S005 policy-flag permutations remain deprioritized.

## CHANGE WATCH
- Flutter/Dart runtime/build/pub behavior is version-sensitive; exact SDK/ref/engine identity matters.
- A moving Flutter `stable` label is not sufficient artifact identity.
- Exact canonical Flutter SDK/engine and any external CI/operator toolchain pin for inspected LogMate remain unknown from product repository evidence.
- Canonical LogMate source build/artifact identity remains OPEN.
- F006 direct Dart socket root cause/verdict is OPEN.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- GitHub Actions/CLI/attestation API/Sigstore roots/OIDC/hosted-runner behavior are service/tool-version sensitive; hosted verification has contradictory success/failure evidence.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
