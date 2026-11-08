# D006 — External rollback authority and page-content binding counterexamples (2026-11-08)

**Classification: VERIFIED EXECUTION, independent synthetic SQLite only; product/Firebase OPEN.** Lead: Data. This extends the preceding D006 metadata ABA study without re-running its identical oracle.

## Exact execution and evidence
- Local environment: Python 3.13.5, SQLite 3.46.1, file-backed independent stream and authority SQLite databases, SQLite backup/restore, HMAC-SHA256 with intentionally public demonstration key.
- Executed command: `python /mnt/data/d006_external_authority_canary.py`; output: `D006_EXTERNAL_AUTHORITY 6 / 6 sqlite 3.46.1`. Source SHA-256: `265796257e741d310ab98cfbba05ffbc6d53551402c489d0244c50618f2ec4e7`.
- Reusable fixture: `research/data/fixtures/D006_external_authority_rollback_canary.py`. Transcribed exactly from executed source; byte identity and hosted replay **not verified**.
- Studio preceding main commit `151ba1c00896495c75ff4c79e1291b1b8968c2e7`. Product reference read-only: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → declared 1.0.0+1 → 2026-11-08`. Production ref unknown. Latest available branch enumeration yielded 69 entries; open PR search returned no items despite previous observed 20, so PR inventory is **not verified this run**; do not infer closure. No product test, write or CI dispatch.

## Failure-first oracle
Two independent SQLite databases hold (a) restorable event rows and (b) external stream epoch. Starting epoch7 and rows old1/old2, a backup of event DB is taken, authority epoch advances to8, row2 changes, then the old event DB snapshot is restored. **Observed 6/6 expected:**
1. restored row2 is old2;
2. original epoch7 witness HMAC remains mathematically valid;
3. authoritative epoch8 rejects epoch7 witness;
4. new epoch8 witness verifies;
5. **negative**: deliberately rolling external authority back to7 makes the old witness acceptable again;
6. **negative**: changing event contents without advancing epoch8 leaves the epoch8 witness valid, proving that epoch-only authentication does not bind page contents.

## Interpretation, limits and next falsifiable gate
**SYNTHESIS:** a genuinely independent, nonrollbackable authority can reject stale epochs after restoring only the event database. **CONTRADICTION:** external storage *location alone* is insufficient if authority can itself roll back; monotonic epoch alone is insufficient to authenticate event contents. Real security requires independently enforced monotonic authority and page/event-set binding plus authorized writer and trust boundaries. The demo HMAC key is public; no actual authentication, server distributed transaction, crash power-loss, adversarial concurrency, or Firebase implementation was tested. No LogMate defect or D006 Stage 1 PASS is claimed.

**VALIDATION OPEN:** run a model with authenticated page digest/Merkle binding, atomic issuance or rejection on concurrent epoch advance, and independent authority rollback/failover, then transfer to an approved Firebase contract. Preserve current owner-approved Automatic+Manual Delta policy without treating Draft implementation as production.

## RELATED DOMAIN CHECK / HANDOFFS
- Foundations: SQLite transaction/backup and independent file identity; does not model OS crash durability.
- Architecture: authority and event-store lifecycles must have distinct ownership and explicit consistency protocol.
- Mobile: offline clients must reject old stream incarnation on reconnection; no native runtime tested.
- Data: owns receipt/cursor/page/epoch semantics.
- Quality: six negative/positive controls; hosted reproduction and source-byte identity still OPEN.
- Systems: authority compromise/rollback and MAC key trust; public key not a security proof.
- Design, Web Manager, Marketing Manager: not materially relevant to this bounded synthetic oracle; do not claim shipped Sync.
- **HANDOFF to LogMate/Codex (advice only):** define stream incarnation issuer, monotonicity under restore/failover, signed page-content binding and server read transaction; exact product implementation/execution requires separate approval.
