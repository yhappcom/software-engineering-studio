# D006 — Contiguous Applied Cursor and Owner/Generation Fencing: Independent Failure-First Experiment

**Evidence date:** 2026-11-08 Asia/Seoul. **Lead:** Data D006; support Quality, Architecture, Systems, Foundations and Mobile. **Class:** VERIFIED EXECUTION (independent synthetic Python/SQLite), NEGATIVE ORACLE, ENGINEERING JUDGMENT, TRANSFER OPEN. **Not LogMate implementation or product acceptance.**

## Exact sources and boundaries

- Studio before this study: `yhappcom/software-engineering-studio → main@8e6343f0a178a1f604a60b377f4eebb8b98e2032 → 2026-11-08`.
- Private product, **read only**: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`, production ref unknown.
- Active unmerged W013 Draft `#51 docs/w013-ios-boundary-adoption-20261108@62d7295da6b447ba45dd3f0196c81ec449f2cdf9` on Draft `#50 verify/w013-android-runtime-20261108@c08feb25517c32a6104f4cc1ef49e7a4a9f33ddd`. Enumerated **66 branches, 17 open PRs**. These are stacked unmerged sources, not production.
- Owner-approved Sync contract: `docs/specs/local-first-manual-delta-sync-contract.md` blob `1b7441bf6bf06bcd8953ff87c7660de159e2c19e`, as seen in PR51 stack; automatic/manual delta policy is not implementation.
- Previous independent model: `research/data/D006_sqlite_receipt_cursor_atomicity_failure_first_2026-11-08.md`, 6/6 SQLite ACK/cursor atomicity experiment. This study **extends a different boundary**: contiguous sequence gaps, historical replay and owner/generation mismatch.
- No private code, credentials, real logbooks, private fixtures, product CI, product writes or deploys used.

## Reproducible input, oracle, environment

A standalone Python 3.13.5 stdlib `sqlite3` program used a disposable temporary file-backed SQLite WAL database, with tables `state(owner,generation,cursor)`, `records(k,v)`, and `applied(seq PRIMARY KEY,opid UNIQUE)`. Synthetic inputs `A/g1`, `B/g2`, sequence 1–4, and invented `op1`–`op4` contain no product/user data. Local experiment file: `/mnt/data/studio_validation/D006_sequence_gap_owner_generation_canary.py`. SHA-256 of final executed file: `224c274360ca379cb66e00c80c6585630701cdcaf8d6e4f87ebc25ebc0995097`. Executed command `python /mnt/data/studio_validation/D006_sequence_gap_owner_generation_canary.py`; process exit 0 and terminal `D006_GAP_CONTEXT_CANARY 9/9`. **Script remains in local experiment workspace, not yet committed to Studio.** This is an evidence/reproduction availability limit; do not call it a hosted fixture.

Apply algorithm: `BEGIN IMMEDIATE` per event; check both local expected context and event Owner/Generation, require next `seq=cursor+1`, write record and applied identity, update cursor and `COMMIT` atomically; rollback on mismatch/crash. For replayed sequence at or below cursor, compare the durable historical `seq→opid` identity; do not silently accept a conflicting older event.

## Observed nine controls

| Control | Expected negative/positive oracle | Observed |
| --- | --- | --- |
| Receive seq 1 then seq 3 | Gap 2 rejects 3; cursor stays 1, no record3 | PASS |
| Supply seq 2 and 3 | Contiguous replay reaches cursor3 | PASS |
| Replay identical seq3 | No duplicate applied row | PASS |
| Replay seq3 with different opid | Conflict rejected | PASS |
| Receive seq4 with wrong remote owner B or generation g2 | Both rejected; cursor unchanged | PASS |
| Local generation changes to g2 while caller expects g1 | Stale caller rejected | PASS |
| Crash after record write, before cursor commit; close/reopen | Neither record4 nor cursor4 persists; retry commits | PASS |
| Deliberately unsafe implementation sets cursor3 without records | Data-loss/gap-skipping counterexample reproduced | PASS |
| Historical seq1 after cursor4 | Forged opid rejected; matching historical opid accepted idempotently | PASS |

**Debugging/refinement within this execution:** The initial 8/8 model accepted a forged **older** replay at seq1 when cursor4 because its identity check covered only `seq==cursor`. That is an observed defect in the experimental model, not LogMate. The model was corrected to check every historical replay identity; final 9/9 result is at the SHA above. The negative example demonstrates why `seq<=cursor` cannot be treated as unconditional success when history is retained.

## Causal interpretation and alternatives

- **SOURCE / OBSERVATION:** a persisted cursor can claim progress without a record if an implementation jumps gaps. The unsafe synthetic control demonstrates the contradiction directly.
- **ENGINEERING JUDGMENT:** a consumer must not advance a **contiguous applied** cursor beyond a missing event. It may stage out-of-order events separately, or request/replay the gap. A server sequence might have non-visible events filtered by ACL or generation; therefore a naive global `cursor+1` invariant is **not universal**. The protocol must specify whether sequence is per-owner/generation, whether it is dense in the authorized stream, and how filtered events are represented as authenticated no-op/skip proofs.
- **ALTERNATIVE A:** dense per-owner/generation stream and atomic apply+cursor, as modeled; simple, but server ordering/stream density is a prerequisite.
- **ALTERNATIVE B:** sparse global sequence plus explicit durable per-stream high-watermark and authenticated gap/skip metadata, or event journal plus confirmed contiguous set; requires separate proofs and additional metadata.
- **ALTERNATIVE C:** advance high-watermark on maximum received event without a gap proof; rejected by this synthetic counterexample.
- **Historical replay limitation:** the experiment compares seq/opid only, not immutable digest; product must also validate digest for same OpID and distinguish replay from tampering. Unbounded applied-history retention may be costly and needs compaction/checkpoint proofs.
- **Owner/Generation limitation:** local equality checks alone do not establish server-side Firebase authentication, authorization, generation transition, Restore Event or stale-client exclusion.

## Falsifiable next gates

1. Specify the authoritative server sequence namespace (global sparse vs per-owner/generation dense) and design a gap-proof oracle for filtered events; do not adopt a product policy without owner review.
2. Add server-authenticated Owner/Generation binding, OpID+digest checks, tombstones and concurrent server writer sequences to the independent canary.
3. Preserve the executable source in Studio under `research/data/fixtures/` and independently rerun on a pinned runner before asserting reproducibility beyond this session.
4. Only with explicit LogMate/Codex Work approval: exact-ref Dart/Sembast file-backed, Firebase Emulator and physical/installed PWA transfer; product repository remains untouched here.

## RELATED DOMAIN CHECK / HANDOFFS

- **Foundations:** atomic transaction ordering, crash/restart, and sequence-space assumptions.
- **Architecture:** separate server receipt, remote event sequence, local durable applied cursor, and Owner/Generation authority; never conflate them.
- **Mobile:** offline/catch-up may see out-of-order/filtered batches; background suspension must not promote received to applied.
- **Data:** D006 owns contiguous/sparse cursor semantics and historical replay proof.
- **Quality:** gap negative, stale context negative, historical forgery, deliberate unsafe counterexample, restart rollback; preserve final SHA and earlier model defect.
- **Systems:** authenticated skip proofs, server-side authorization and old-client exclusion remain unverified.
- **Design Studio/Web Manager/Marketing Manager:** no material new design/business decision required.
- **LogMate:** handoff only; PR51 W013 iOS bounded evidence and S007 37-store deletion audit are separate and unchanged. No new release or Stage-1 PASS.

**Gate:** D006 Stage 1 remains NOT PASS. Verified independent SQLite model 9/9, not Dart/Sembast/Firebase product correctness.
