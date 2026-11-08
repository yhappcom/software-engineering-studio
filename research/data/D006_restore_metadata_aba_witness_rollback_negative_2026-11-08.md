# D006 — Restore-induced metadata ABA and signed-witness replay

**2026-11-08 Asia/Seoul. Lead Data; supporting Systems, Architecture, Foundations and Quality.** Classification **VERIFIED EXECUTION** for independent synthetic file-backed SQLite WAL (9/9 checks); **OPEN** for Firebase, LogMate and any real cryptographic authority. Stage 1 NOT PASS.

## Exact sources and identity

- Studio starting point: `yhappcom/software-engineering-studio → main@f5b6713990b77b22913b37aa22a7c2103eb31861 → 2026-11-08`. Prior D006 GC/page snapshot and snapshot-bound HMAC studies reviewed. The prior study verified version mismatch detection but did **not** test a version reset/ABA after restore.
- Product **read-only**: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`; 69 branches, 20 open Draft PRs. Latest unmerged W013 Draft #54 `feat/w013-persistent-writer-20261108@8da33f5ff9b90911df95acf4ff1b707434e20bba` stacks #53→#52→#51, separate from owner-approved unmerged PR42 Automatic+Manual Delta policy. No product deployment/ref is established; no product tests/CI or mutations.
- Executed local independent synthetic file: `/mnt/data/d006_aba.py`, SHA-256 `018d4f8f40308714b4ba45b98cd50153109784174650613682a752ec53739c1d`. Command `python /mnt/data/d006_aba.py`; observed `D006_ABA_PASS 9/9 sqlite=3.46.1`. Python interpreter version was not independently printed in this run. Temporary file-backed SQLite database, WAL, two live connections A/B, HMAC-SHA256 with a **public nonsecret demonstration key**; no network or product data. A transcription of the source was committed as `research/data/fixtures/D006_metadata_aba_restore_canary.py`; byte equality and exact committed-file replay remain **OPEN**.

## Failure-first claim, setup and oracle

**Claim:** HMAC authenticity of owner/generation/version/floor/high metadata does **not** establish freshness or bind a token to event contents when a restore/rebuild reuses the same metadata values. An incarnation/epoch identifier helps only if it cannot be rolled back or reused.

**Initial state:** owner A, generation1, version10, retention floor1, high4, incarnation101, rows seq1–4 containing `old1..old4`. Sign a witness over metadata **excluding** incarnation. Writer B atomically replaces rows with `new1..new4`, keeps owner/generation/version/floor/high unchanged and sets incarnation102. Connection A sees new row contents but the signed old metadata still verifies. Then sign incarnation101; it fails against 102. Finally writer B deliberately restores incarnation101 with different `third1..third4` contents, reopening the replay despite incarnation signing.

**Nine observed assertions (all matched expected outcomes):**

1. Original metadata HMAC valid.
2. Independent B replacement is visible to A (seq2 now `new2`).
3. Metadata owner/generation/version/floor/high have returned to the same old tuple (ABA).
4. Old HMAC still verifies against the new tuple.
5. New seq2 content differs from old.
6. Signed incarnation101 is rejected while current incarnation102.
7. New signed incarnation102 verifies.
8. Restoring incarnation101 makes old signed token verify again.
9. Row contents after the rollback are `third2`, not the original `old2`.

**Negative result:** a valid MAC is evidence only that the message was signed under the demonstration key, not that the underlying event set is unchanged or that a signed incarnation is monotonic across restore. This test intentionally permits dangerous version/epoch reuse; it is not a product defect report.

## Mechanism, alternatives and falsifiable gate

- **Version-only or signed metadata:** insufficient under reset/restore. A token can be byte-identical across distinct data states.
- **Signed incarnation with durable monotonic server authority:** candidate. The authority must prevent old incarnation reuse across backup restore, rollback, failover and replica rebootstrap. An increment stored only in a restorable snapshot does **not** supply that guarantee.
- **Server-issued random unique stream incarnation + authenticated page/content digest:** candidate to prevent accidental reuse and bind page bytes; still needs authorization, nonreplay/freshness or server state confirmation, retention and transaction/snapshot semantics. A hash without an independently authenticated current root can itself be replayed.
- **Client-side max-seen epoch:** possible additional defense, but new devices or restored client state cannot trust their local max as universal authority; do not treat it as a complete solution.
- **Next executable gate:** simulate server epoch authority in a separate non-restorable database or key domain; inject a backup rollback of the event DB and prove old token rejected, plus process restart, concurrent writer, rotated authority key, forged page digest, owner/generation mismatch and stale-client replay. Then only with explicit product authorization validate exact Firebase Emulator/adapter protocol and LogMate client apply/cursor state.

## RELATED DOMAIN CHECK / HANDOFFS

- **Foundations:** equality of a metadata tuple is not identity of a historical state; ABA and monotonicity need explicit authority.
- **Architecture:** snapshot/page API must bind content, stream incarnation and current authenticated authority rather than exposing reusable counters as freshness proof.
- **Mobile:** offline clients and restored/new PWA/native databases cannot independently certify server freshness; recovery must fail closed when authority is unavailable.
- **Data (owner):** do not advance Applied Cursor on replayed metadata, unverified page or restored stream incarnation; authenticated receipt/sequence and retention boundaries remain independent.
- **Quality:** retain positive HMAC check plus reset/rollback negatives; a valid MAC alone is not the acceptance oracle.
- **Systems:** signing-key custody, epoch issuance, rollback resistance and anti-replay are security boundaries; public synthetic HMAC is not security validation.
- **Design Studio / Web Manager / Marketing Manager:** no material domain handoff.
- **LogMate:** owner-approved sync direction remains unchanged; implementation/production Sync and release acceptance remain OPEN. Do not create a new product policy from this model.

**Limitations:** SQLite's single-file atomic transaction and the synthetic HMAC do not replicate Firebase transactions, multi-node failover, a trusted monotonic service, cryptographic freshness, real backup restore or product code. No CI was run and no Stage 1 gate is promoted.
