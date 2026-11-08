# D006 — File-backed GC/page snapshot race and late-admission negative oracle

**2026-11-08 Asia/Seoul — VERIFIED EXECUTION, independent Python 3.13.5 / SQLite 3.46.1 WAL, 9/9 synthetic controls. D006 Stage 1 NOT PASS.**

## Exact provenance and authority

- **Studio starting source:** `yhappcom/software-engineering-studio → main@33b83fac07440c245fd48e229691f30b9f4c0e64 → 2026-11-08`. Prior D006 `D006_snapshot_bound_retention_witness_negative_oracle_2026-11-08.md` and its pure Node fixture were read first; that model did not execute concurrent database transactions.
- **Independent executable:** local `/mnt/data/d006_gc_snapshot_canary.py`, SHA-256 `8fde5b2fb8be3ef5427728dfe6c6d14babeb53fb52807fab5bc6a90448572174`, run `python /mnt/data/d006_gc_snapshot_canary.py`; observed `D006_GC_SNAPSHOT_SQLITE_PASS 9/9 sqlite=3.46.1 python=3.13.5`. Fully synthetic temporary SQLite database, two live connections plus reopen, no network/credentials/private product source. A **cleaned equivalent** script was committed at `research/data/fixtures/D006_gc_snapshot_two_connection_canary.py`; the committed text omits some local comments and **is not byte-identical** to the executed local file. Hosted replay and exact committed-byte replay are OPEN.
- **Product read-only:** `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → evidence 2026-11-08`. Current 69 branches and 20 open Draft PRs; latest #54 `feat/w013-persistent-writer-20261108@8da33f5ff9b90911df95acf4ff1b707434e20bba` is stacked on #53→#52→#51 and does not establish D006 Firebase Sync. Main's October Manual-only contract is historical relative to owner-approved unmerged PR42 Automatic + Manual Delta policy; neither proves production implementation. Production/release identity unknown.

## Claim, oracle and actual interleaving

**Hypothesis:** Binding metadata and page content to a real consistent snapshot can prevent a GC interleaving from mixing old metadata with new rows. Merely signing metadata and checking a version at a different instant is insufficient to prove page completeness. SQLite WAL provides a bounded *local* snapshot mechanism, not a Firebase distributed protocol.

**Setup:** SQLite file with events seq1–4, `meta(version=10,floor=1,high=4)`, WAL and two independent connections A (reader) and B (GC writer). Reader A starts `BEGIN` and reads metadata plus all four rows. While A's transaction remains open, B executes one `BEGIN IMMEDIATE` transaction that deletes seq1–2, sets `version=11,floor=3`, and commits. A reads again before rollback; then opens a fresh read. A second uncommitted GC update is closed without commit, followed by an intentionally invalid late seq2 insertion.

**Expected and observed 9 controls (all matched):**

1. Initial snapshot A reads `(10,1,4)` and four events.
2. B commits GC while A's WAL read transaction remains open; B sees `(11,3,4)` and only seq3–4.
3. A's pinned snapshot still sees the original metadata and original four events — **actual concurrent SQLite snapshot isolation**, not a mocked GC flag.
4. After A rolls back, a fresh read sees `(11,3,4)` and seq3–4.
5. Reusing A's old metadata witness after GC is rejected by exact version/floor/high mismatch.
6. Mixing A's old page with a fresh metadata read is detected as cross-view mismatch; independent individually valid reads do not make a consistent page.
7. A replica with applied cursor0 behind the new floor3 cannot silently advance; recovery is required.
8. Closing B after uncommitted deletion/metadata update rolls back both changes; a fresh connection observes the previous committed view.
9. A deliberately inserted **late seq2** after GC remains invisible to `seq>4` catch-up. SQLite permits this unless the application enforces sequence admission/retention invariants; a snapshot protocol alone does not establish event publication linearization.

**Failure-first distinction:** the stale witness and mixed-view path fail the required same-snapshot oracle; a pinned SQLite WAL reader avoids this specific race. The late seq2 negative intentionally demonstrates that an otherwise consistent snapshot and high-water cannot repair an invalid server sequence-admission contract.

## Mechanism, alternatives, limitations

- **Split metadata and page requests without snapshot binding:** reject as sufficient completeness evidence. GC can commit between requests.
- **Single transaction snapshot for metadata + page:** validated in this one SQLite WAL database, under the exact A/B interleaving. The read transaction retains old rows even when GC commits; it does **not** guarantee an indefinitely renewable or externally accessible snapshot.
- **GC atomic metadata+delete:** a necessary local invariant, validated with rollback; independent client synchronization still needs authenticated owner/generation, correct server authorization, retention lease or recovery contract, and page/receipt binding.
- **Late reserved sequence:** a distinct server-admission invariant; require server-published committed-prefix semantics or an authenticated complete sparse sequence view, not only keyset pagination.
- **No page digest/HMAC verification in this Python test:** earlier Node HMAC model remains a separate bounded integrity-classifier exercise. Neither test alone establishes both cryptographic authenticity and actual concurrent page integrity. Combining the two would still not prove real Firebase behavior.
- **SQLite limitation:** a local WAL snapshot is not a Firebase transaction, remote paginated API, multi-node GC, physical device, crash-consistent client apply, or malicious server. Tests are deterministic controlled interleavings, not exhaustive concurrency exploration.

## Falsifiable next gate / product handoff

Define and independently validate the server-side **admission/commit visibility order**, snapshot/page token authority, GC retention lease or stale-cursor recovery, and authenticated owner/generation-bound receipt/cursor. Then run a fault-injected Firebase Emulator/server adapter test at an explicitly approved exact LogMate/Codex Work ref. The Studio cannot claim such product execution from this independent canary and must not dispatch LogMate CI.

## RELATED DOMAIN CHECK / HANDOFFS

- **Foundations:** snapshot isolation and sequence linearization are distinct ordering guarantees.
- **Architecture:** API must atomically bind metadata and page identity, and return explicit retry/recovery when that view is no longer available.
- **Mobile:** long-offline native/PWA devices need a stale-cursor path without silently discarding unsent local changes.
- **Data:** D006 owns retention/GC, cursor and authenticated completeness; one real SQLite interleaving advanced the previously model-only GC boundary.
- **Quality:** 9 executable positive/negative controls; exact cleaned fixture host replay OPEN, broader schedule and crash process kill not covered.
- **Systems:** HMAC/authorization/lease identity, replay and adversarial server remain unvalidated.
- **Design/Web/Marketing:** no policy or implementation change justified.
- **LogMate:** READ ONLY; no PR/issue, CI, Work ID, source, DB, release or deployment mutation.

**Gate:** D006 remains NOT PASS; no Firebase or LogMate production implementation/defect claim.
