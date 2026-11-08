# D006 — Two-file authority/event cutover crash boundary (2026-11-08)

**VERIFIED EXECUTION — independent synthetic SQLite only.** This is a new cross-file cutover experiment, not LogMate/Firebase validation or a product defect.

## Environment, input, oracle and result
- Python 3.13.5, SQLite 3.46.1, temporary file-backed `events.db` and `authority.db`, WAL, explicit connection close/reopen.
- Local executed source: `/mnt/data/studio/D006_dual_db_cutover_canary.py`, SHA-256 `f9f9ef50ba442ac6e33e5ec5e8c2383981ce81fc06be1878412d6b8173390f74`. **Local source only; not committed or independently replayed.**
- Run: `python /mnt/data/studio/D006_dual_db_cutover_canary.py`; observed `D006_DUAL_DB_CUTOVER 9 / 9`. All nine assertions passed.
- Initial rows: events=(epoch1, old); authority=(epoch1, READY). Reader oracle accepts only READY and all event epochs equal authority epoch. Cutover target epoch2/new.

## Nine observed controls
1. Epoch1 READY returns old.
2. Unsafe event-first insertion of epoch2 next to epoch1 is rejected by epoch-checking reader.
3. Authority PREPARING epoch2 before event replacement rejects reads.
4. Connection restart after PREPARING still rejects.
5. New event committed while PREPARING still rejects.
6. Restart after new event commit still rejects.
7. Authority READY epoch2 permits new.
8. Restoring event rows to epoch1 while authority remains epoch2 rejects.
9. **Negative:** rolling back both event rows and authority to epoch1 READY permits old again.

## Interpretation and limits
**SYNTHESIS:** a PREPARING/READY authority gate can fail closed across *modeled sequential* cross-database cutover interruptions; a two-file SQLite arrangement is not itself a single atomic transaction. **CONTRADICTION:** rollback of both files defeats an authority gate without an independently nonrollbackable witness. Reader's epoch comparison is deliberately stronger than an epoch-agnostic implementation; it does not cryptographically authenticate event content. **OPEN:** adversarial simultaneous readers/writers, durable fsync/power loss, failover, monotonic external authority, content digest binding, Firebase semantics and product implementation. This model cannot prove crash safety of a real server. No Stage 1 PASS.

## Product boundary and handoff
Read-only product context: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → declared 1.0.0+1 → 2026-11-08`; production ref unknown. Current branch enumeration returned 69 entries; Draft PR54 is stacked on PR53, which is stacked on PR52, **not main**. PR54's product-reported 1414 Flutter PASS/1 SKIP and Android/iOS simulator evidence apply to its bounded isolated Native writer, **not** Production Sync or this D006 oracle. No product write/CI.
- **Data (owner):** define an authenticated, monotonic stream cutover and recovery protocol before cursor acceptance.
- **Architecture:** define authority/event ownership and explicit PREPARING-to-READY transition.
- **Foundations:** two SQLite files do not supply an implicit distributed transaction.
- **Quality:** add simultaneous-reader and kill/reopen tests plus byte-identical hosted replication.
- **Systems:** secure anti-rollback custody, authenticated content and compromised-authority negatives.
- **Mobile:** offline clients must not accept pre-cutover stale stream epochs.
- Design/Web/Marketing: not materially relevant to this synthetic correctness boundary.

**Falsifiable next gate:** concurrent writer/readers with a pinned authority view and a real two-file interruption, plus an external monotonic witness whose own rollback is rejected; transfer only after approved server implementation identity is known.
