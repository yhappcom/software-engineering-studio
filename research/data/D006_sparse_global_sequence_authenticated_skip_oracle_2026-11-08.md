# D006 — Sparse Global Sequence versus Owner-Stream Cursor: Failure-First Canary

**Date:** 2026-11-08 Asia/Seoul. **Class:** VERIFIED EXECUTION (independent SQLite synthetic model), NEGATIVE ORACLE, ENGINEERING JUDGMENT, TRANSFER OPEN. **Not LogMate product runtime, production admission, cryptographic proof, or Firebase acceptance.**

## Source and evidence identity
- Studio starting source: `yhappcom/software-engineering-studio → main@a8526a2d942d717cf37c9555a5639244eb781ca9 → 2026-11-08`.
- LogMate READ ONLY: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`; this main is not assumed production. Branches: 66; open Draft PRs: 17, including PR51 `docs/w013-ios-boundary-adoption-20261108@62d7295da6b447ba45dd3f0196c81ec449f2cdf9` stacked on PR50 `verify/w013-android-runtime-20261108@c08feb25517c32a6104f4cc1ef49e7a4a9f33ddd`. PR42 policy `docs/w013-policy-execution-alignment-20261106@71d8a1d4c3650fce0200677fa0db2345e444712d` remains unmerged. Current product spec main `docs/specs/local-first-manual-delta-sync-contract.md` blob `97faecf317df1346f4b1b58c8d37c891f805e436` describes UID-scoped server operation log and a contiguous Applied Cursor, but does not specify a globally sparse sequence proof format.
- Experiment environment: Python **3.13.5**, stdlib `sqlite3`, file-backed SQLite WAL in temporary directory, close/reopen, `BEGIN IMMEDIATE`, deliberate exception after record insert. Local source `d006_sparse_cursor_canary.py` SHA256 `d1a11263856029f58fcf07699efead80eef2fc344e62bcc471a2ae8b2848faad`. Executed locally; source is **not yet in Studio**. The script was authored without any private product code or user data.

## Hypothesis and alternative models
An owner's authenticated event stream may be **dense owner-local** (sequence 1,2,3 for that owner), or it may use **global sparse sequence** (owner A events 1,3 while event 2 belongs to B). A client cannot safely infer from seeing event 3 that owner A's event 2 does not exist. Blind `cursor = max(received seq)` is a data-loss bug in the dense-owner model, while requiring `cursor+1` across all global sequence slots deadlocks the sparse-global model.

Two valid implementation options require different proof:
1. **Owner-local dense stream**: enforce all `cursor+1 ... target` owner events, atomically apply and persist cursor. No skip proof needed.
2. **Global sparse stream**: authenticated, scope-bound, complete absence/skip evidence for every skipped global slot or a server-authenticated pagination watermark with defined completeness semantics; bind it to UID/Generation, requested cursor, target cursor, server log epoch and page/filter identity. Reject unproven or truncated pages. This is a **design alternative**, not a newly approved LogMate policy.

A naked `hasMore=false` or client-set `authenticated=true` is **not** proof. In this synthetic model, a boolean flag stands in for an assumed already-verified server attestation solely to test downstream local transaction behavior; no cryptographic verification or backend implementation exists.

## Executed oracle and observations

12/12 checks passed in the local synthetic Python SQLite run:

1. Gap 1→3 without proof rejected.
2. No partial durable state after that rejection.
3. Initial owner A event 1 applied.
4. Unauthenticated skip marker rejected.
5. Skip marker bound to wrong owner rejected.
6. Incomplete skip set rejected.
7. Cross-owner payload rejected.
8. Injected interruption after event insertion but before cursor update rolled back.
9. Reopen after interruption preserved cursor 1 and only event 1.
10. Complete assumed-authenticated skip for slot 2 permitted owner A event 3.
11. Final cursor 3 and events 1,3 were persisted.
12. Replaying a nonadvancing target was rejected by this model.

The experiment demonstrates **model conditionality**: a cursor algorithm cannot be judged correct without first declaring whether its server sequence is owner-local dense or global sparse and what a complete response means. It does not show that LogMate's planned server sequence is sparse, that a boolean marker is secure, or that the product implements the unsafe variant.

## Reproducibility and limits

Exact local script SHA256 is above; no public repository fixture or hosted CI rerun yet. The script is available in this session as a separate artifact. Tests use one SQLite writer and a synthetic proof predicate; no network, Firebase token, concurrent writer, adversarial attestation, server paging race, compaction, generation epoch, malicious backend or Flutter/Sembast transfer. A single local PASS does not prove OS power-loss durability or device behavior.

## RELATED DOMAIN CHECK / HANDOFFS
- **Data (owner):** define owner-local vs global sequence and cursor completeness before protocol implementation. Receipt is not Applied Cursor.
- **Architecture:** expose stream identity and completeness as an explicit typed contract; reject client guesses about skipped events.
- **Foundations:** distinguish total ordering from a filtered subsequence; max observed element does not imply complete prefix.
- **Quality:** add gap, wrong-scope, truncated page, stale proof, concurrent pagination, replay and interrupted transaction negatives to future product test acceptance.
- **Systems:** authenticated server-side admission/attestation, UID/Generation/epoch binding and old-client replay/retention constraints; boolean marker is insufficient.
- **Mobile:** resume/offline PWA and native catch-up must not turn incomplete pages into success.
- **Design/Web/Marketing:** no policy change required; managed EFB data retention remains separately OPEN.

**Project handoff only:** user-approved Automatic+Manual Delta policy remains; do not invent or approve a wire format. Ask product/Codex implementation to select and document exact sequence namespace and completeness contract, then run exact-source Dart/Sembast/Firebase multi-device tests under separate authorization. No LogMate write/CI was performed.

**Gate:** D006 Stage 1 NOT PASS. Sparse-global correctness is conditional on a real authenticated completeness oracle; product transfer and hosted fixture execution OPEN.
