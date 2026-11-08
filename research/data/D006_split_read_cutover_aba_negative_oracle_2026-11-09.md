# D006 — Split-read authority cutover and ABA negative oracle (2026-11-09)

**VERIFIED EXECUTION (bounded synthetic model)** — Python 3.13.5, file-backed SQLite WAL, two separate database files and additional concurrent open connections. Executed local source SHA-256 `b1b88afad28f4a96236ce780d48c876eba83df1bded33734907c94055bec335b`. Command: `python d006_concurrent_cutover.py`. Observed `D006_CONCURRENT_CUTOVER 8 / 8`. This is not product/Firebase execution.

## New independent negative evidence
The previous PREPARING/READY sequential cutover can be bypassed **by a reader that caches an old READY authority decision and separately reads fresh events**: the authority read yields (epoch1,READY) and the event read yields (epoch2,new). An epoch comparison rejects this mixed read. However, if both databases are returned to epoch1 while event content changes, an epoch-only comparison falsely accepts altered content. Re-reading authority after the event read catches a 1→2 transition but **does not catch a 1→2→1 ABA rollback**. This narrows, rather than closes, the prior two-file cutover evidence.

A separate actual WAL two-connection check held a reader transaction open while another connection committed authority (epoch3,PREPARING): the first reader saw the original snapshot until COMMIT, and saw PREPARING on its next read. This does not make independent event/authority DB snapshots atomic.

## Reproduction and oracle
Eight asserted observations: unsafe mixed read present; epoch mismatch rejected; same-epoch altered content falsely accepted by epoch-only check; PREPARING rejected; new READY accepted; double-read detects epoch transition; double-read misses ABA; WAL reader snapshot stable until transaction end. Synthetic input and assertions are in `research/data/fixtures/D006_split_read_cutover_canary.py` (the identical source used for this execution, copied from local file). Re-execution on GitHub-hosted runners is NOT performed.

## Root cause / alternatives / limits
**SYNTHESIS:** Cross-file PREPARING/READY does not enforce a *reader's* consistent observation boundary unless the reader uses validated epoch/content identity and revalidation. Double-read detects some interleavings, but not ABA; epoch-only checks do not authenticate event bytes. A nonrollbackable authority plus content-bound signed witness is a candidate, not validated here. Another candidate is a single transactional DB for authority and events when the product architecture permits it. The interleavings were orchestrated sequentially except for the actual overlapping WAL reader/writer connections; no adversarial thread scheduler, fsync/power-loss, distributed server, key management, Firebase or product tests.

**Product context (READ ONLY):** `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → declared 1.0.0+1 → 2026-11-09` based on prior pinned SHA plus fresh default-branch MASTER.md content; exact fresh main commit not independently resolved in this run, so do not treat that historical SHA as a new HEAD check. 69 branches and 20 open PRs observed; #52→#53→#54 are distinct unmerged Native Writer work, not D006 Production Sync. No product changes, CI or release validation. D006 Stage 1 remains OPEN.

## RELATED DOMAIN CHECK / HANDOFFS
- **Foundations:** two independent transactions lack a shared atomic read boundary.
- **Architecture:** specify who owns epoch, event content identity and read admission; fail closed on mixed epochs.
- **Mobile:** offline clients must reject stale/ABA witness after restore.
- **Data (owner):** preserve cursor, content hash and authority identity in an authenticated stream contract; do not infer policy approval from this model.
- **Quality:** require negative interleaving, ABA, tampered content, process restart and independent replay; distinguish observed 8/8 synthetic from product PASS.
- **Systems:** nonrollbackable epoch and authenticated content binding need security threat model and backend custody.
- **Design/Web/Marketing:** not materially relevant to this bounded storage/concurrency mechanism.
- **LogMate/Codex (approval dependency):** actual D006 implementation/server tests only on explicitly authorized product Work; no private code or user data in public Studio.
