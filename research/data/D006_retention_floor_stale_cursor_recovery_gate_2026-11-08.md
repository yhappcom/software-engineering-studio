# D006 — Retention Floor and Stale Replica Cursor: Fail-Closed Recovery Gate

**Date:** 2026-11-08 Asia/Seoul. **Result:** VERIFIED EXECUTION, independent synthetic SQLite model only. **Lead:** Data D006. **Stage 1:** NOT PASS.

## Source identity and prerequisite
- Studio before study: `yhappcom/software-engineering-studio → main@c8a4adb80e0e4306bb4b693fb1a600ab422e8755`.
- Product **read only**: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`. **Main is not assumed production.** Exactly **68 branches** and **19 open Draft PRs** enumerated at this read, including PR52 `feat/w013-native-writer-integration-20261108@d427bf62b2422dbdd8af202abe9a74c6bb0672fa` stacked on PR51 and PR53 `docs/w013-persistent-contract-review-20261108@442b003eb0ae261e674b56dc5a00822819ebe801` stacked on PR52. None are merged into main; these W013 restore/native studies are not production Sync acceptance.
- Approved newer product direction resides in unmerged W013 policy stack; the old main's `docs/specs/local-first-manual-delta-sync-contract.md` explicitly defines a durable contiguous Applied Cursor and says 30-day deleted payload compaction, server GC and all-replica replay are unverified. No new product retention policy is inferred.
- Prior Studio D006 `D006_late_commit_visibility_cursor_counterexample_2026-11-08.md` proves that keyset+high-water alone cannot prevent a late-visible earlier sequence; this study addresses **a different missing-history cause: server retention/GC floor ahead of a dormant replica**.

## Claim and synthetic fixture
A dormant replica's durable cursor `1` is behind the server's earliest retained sequence `3` (high-water `4`). A server response containing events `[3,4]` **must not** allow the replica to move its cursor to `4`, because event `2` has been irretrievably omitted from that response. This requires an explicit **RECOVERY_REQUIRED** state, not an implicit zero-delta success or an automatic reset. The fixture models one owner `A`, generation `G1`, and replica `r`; all records are synthetic and non-identifying.

**Execution:** local Python **3.13.5**, stdlib `sqlite3`, file-backed SQLite WAL, `synchronous=FULL`, two connections and independent reopen. Exact executed script local path `/mnt/data/d006_retention_canary.py`, SHA-256 `6032adee8b547c8b224502d17d538976f0a9c0d246bbf85e2e5f883412e5ee85`. This script was **actually executed locally**, not in hosted CI, and is **not yet committed to Studio**. It may not persist outside this run; hash alone does not make it independently reproducible. A separate source publication/re-run is a follow-up gate.

## Observed controls — 11/11 expected results
1. Stale cursor1 vs retained low3: `RECOVERY_REQUIRED`, durable cursor stays 1.
2. While recovery required, ordinary Apply is blocked.
3. Generation G2 cannot consume G1 events.
4. Owner B cannot consume owner A events.
5. Missing completeness flag is rejected.
6. Claimed high-water5 beyond server high4 is rejected.
7. A page with seq4 but missing seq3 is rejected.
8. A page with foreign owner on seq3 is rejected and rolls back.
9. All rejected candidate pages leave cursor unchanged.
10. Valid contiguous page [3,4] starting at cursor2 advances cursor to4.
11. Closing/reopening a separate SQLite connection reads durable cursor4.

**Important limitation:** this is a deliberately small state-machine model. Its `proof` is an untrusted **boolean input**, not a cryptographic signature, authenticated server receipt, consistent snapshot or actual Firestore proof. The test shows how a local gate can reject absent/false evidence, **not** that it validates forged true evidence. Retention metadata is also synthetic and does not model concurrent GC/reader snapshot races. The example cursor2 → [3,4] acceptance assumes the cursor2 represents a previously proven durable prefix; it does not repair cursor1's missing seq2.

## Mechanism, alternatives and next falsifiable gate
A retention floor is a **loss-of-history boundary**, not merely an empty query. A durable Applied Cursor must remain below the floor until a separately authorized recovery/bootstrap protocol can establish an equivalent complete state and a new generation/cursor with explicit lineage. Reusing a stale cursor with a partial server page silently loses edits or tombstones.

- **Reject:** `cursor = max(returned sequence)` after any successful query; may hide GC holes.
- **Reject:** `cursor = retentionFloor - 1` without a separately accepted complete bootstrap; invents applied history.
- **Candidate:** server-authorized stale-cursor response with owner/generation/retention floor/immutable checkpoint bound to a consistent view; client enters durable RECOVERY_REQUIRED and blocks ordinary cursor progress. Bootstrap must independently preserve local unsent changes and owner/generation separation. This is **engineering advice, not an approved product protocol**.
- **Falsifiable next gate:** execute a generic file-backed adversarial race where GC advances between metadata read and page read; require a server-issued, versioned, tamper-resistant completeness witness bound to the same snapshot. A forged true flag must fail; a real snapshot-bound proof must succeed. Then obtain separate owner-approved LogMate/Codex Work to transfer into Dart/Sembast/Firebase. No private product source may be copied into public Studio CI.

## RELATED DOMAIN CHECK / HANDOFFS
**Foundations:** SQLite WAL transaction durability differs from mobile power-loss and Firestore distributed snapshots. **Architecture:** retention-floor and recovery-required must be explicit interface outcomes, not UI heuristics. **Mobile:** long-suspended installed PWA/EFB and offline native replicas are the practical stale-cursor clients. **Data:** GC, tombstone retention and outbox preservation interact; cursor cannot leap a missing prefix. **Quality:** negative controls include false completeness and foreign context; adversarial forged-true/snapshot-race still OPEN. **Systems:** only authenticated owner/generation-bound server authority can establish a valid recovery checkpoint. **Design/Web/Marketing:** no new UI/support/advertising decision is authorized by this research. **LogMate:** read-only advisory, no code, CI, PR, Work ID, deployment or DB modification.

**OPEN:** byte-identical hosted replay, actual server-authenticated proof, concurrent GC, local unsent change reconciliation, real Dart/Sembast and Firebase, physical/managed PWA and release gates. This model is **not evidence of a LogMate defect or Stage 1 PASS**.
