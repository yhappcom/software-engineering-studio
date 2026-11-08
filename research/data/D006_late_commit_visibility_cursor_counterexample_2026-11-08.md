# D006 — Sequence Reservation vs Commit Visibility: Cursor High-water Counterexample

**Evidence date:** 2026-11-08 Asia/Seoul. **Lead:** Data (D006), with Foundations, Architecture, Quality and Systems handoffs. **Result class:** VERIFIED EXECUTION, **independent synthetic SQLite model only**. Stage 1 NOT PASS.

## Evidence chain and source boundaries

- Studio preceding HEAD: `yhappcom/software-engineering-studio → main@206794056e4aacee5efe8a76c2f30a7e30e42d08`.
- Product read-only: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`; **main not assumed production**. Enumerated **68 branches and 19 open Draft PRs**, including new stacked W-013 PR52 `feat/w013-native-writer-integration-20261108@d427bf62b2422dbdd8af202abe9a74c6bb0672fa` based on PR51, and PR53 `docs/w013-persistent-contract-review-20261108@442b003eb0ae261e674b56dc5a00822819ebe801` based on PR52. The product sync contract `docs/w013-policy-execution-alignment-20261106@71d8a1d4c3650fce0200677fa0db2345e444712d`, `docs/specs/local-first-manual-delta-sync-contract.md`, states owner-UID immutable Operation Log, monotonic serverSequence and a contiguous Applied Cursor; it does **not** provide executed Firebase proof of transaction/visibility order. W-013 PRs remain unmerged Drafts and do not authorize Studio to execute private product code.
- Independent environment: Python **3.13.5**, stdlib SQLite **3.46.1**, temporary file-backed SQLite **WAL**, three separate connections (allocator/writer/reader), 10 deterministic synthetic checks. Local executed script SHA-256: `833c5a85efb0643ee05c3fba01bfaad0debe5e8b438e7c28ca09e644d0db3615`. **The executed script was local; it is not claimed to be hosted CI or byte-identical to any subsequently published fixture.**
- No private source, real flight data, user account, credentials, Firebase, product CI or product write was used.

## CLAIM / INPUT / ORACLE / OBSERVATION

**Claim under test:** immutable keyset + fixed high-water cannot prove cursor completeness if the server allocates sequence IDs before durable event visibility and permits later IDs to commit first.

**Synthetic failure:** connection A commits reservations seq1 and seq2. Connection B commits payload seq2, while payload seq1 is not yet visible. A client reads `WHERE seq>0 AND seq<=2 ORDER BY seq` and receives **[2]**. A naive client advances its cursor to 2. Later connection B commits payload seq1. `WHERE seq>cursor` then returns **[]**, although server history now contains **[1,2]**. No OFFSET pagination was involved. Thus the previous keyset+high-water improvement is **insufficient under precommit reservation/out-of-order visibility**.

**Safe bounded alternatives tested:**

1. For an **owner-local dense committed stream**, require all integers from cursor+1 through the proposed checkpoint to be visible. With [2], reject progress; with [1,2], allow it. This is **not** suitable for an unproven sparse global sequence without authenticated completeness/skip proof.
2. Within this **single SQLite database**, allocate the sequence and insert the event inside the same `BEGIN IMMEDIATE` transaction. While seq1 is uncommitted, the other connection sees no event and cannot obtain a competing write transaction (SQLite lock). After commit, seq2 can be inserted, and the visible history is [1,2]. This proves a bounded **SQLite transactional serialization** mechanism, **not** a Firestore guarantee or a cross-system distributed commit protocol.

## Exact 10/10 observations

1. Seq2 visible while reserved seq1 absent.
2. Cursor2 permanently misses later-visible seq1.
3. Server history nevertheless contains both events.
4. Fixed high-water2 alone cannot recover seq1 after cursor2.
5. Dense-prefix guard rejects [2].
6. Dense-prefix guard accepts [1,2].
7. Uncommitted seq1 is invisible to separate connection.
8. Competing writer encounters `database is locked`.
9. Competing writer cannot publish seq2 before seq1 transaction commit.
10. Atomic allocation/insert yields [1,2] in committed order.

**Verdict:** 10/10 expected positive/negative outcomes matched in the independent local execution. The failure is a deliberately unsafe synthetic implementation, **not a demonstrated LogMate defect**. The SQLite lock serializes this database's writers; it is not a portable lock model for Firebase, Dart/Sembast, mobile processes or distributed service deployments.

## Reproduction outline (stdlib only)

Use three `sqlite3.connect(path, isolation_level=None)` connections to a temporary WAL database with `reservations(seq INTEGER PRIMARY KEY)`, `events(seq INTEGER PRIMARY KEY, payload TEXT)`, `cursor_state(replica TEXT PRIMARY KEY, applied INTEGER)`. Insert reservations 1 and 2; insert event 2; assert keyset page [2]; set cursor=2; insert event 1; assert keyset `seq>2` empty and server history [1,2]. Reset and assert dense-prefix rejection of [2]. In a separate reset, start `BEGIN IMMEDIATE` on allocator, insert seq1 reservation+event, assert reader sees [], assert competing writer's `BEGIN IMMEDIATE` raises SQLITE_BUSY/locked; commit allocator and insert seq2 atomically; assert visible [1,2]. The exact executed local script hash is recorded above; **no repository/host rerun is claimed**.

## Design implications / alternatives / falsifiable next gate

- **Product decision remains OPEN:** define the **server sequence namespace and commit visibility semantics**, not just `serverSequence` monotonicity. Sequence reservation time, admission commit, event visibility, authenticated snapshot boundary and retention floor must be distinguished.
- If owner-local dense numbering is chosen, the server must prove no committed earlier event can appear after a higher committed sequence is exposed. If a global sparse numbering is used, a client needs authenticated completeness/skip evidence bound to Owner, Generation, range, retention epoch and snapshot.
- A high-water response must not silently promote uncommitted reserved IDs or filtered/missing events into Applied Cursor. An empty page is not proof of a complete prefix.
- **Next falsifiable transfer:** in a separately authorized LogMate product Work, create two concurrent Firebase admission writers with a controlled precommit barrier; read authenticated paginated events with a third client, interrupt and resume, and assert no lower sequence becomes visible after the cursor passes it. Validate UID/Generation, receipt, retention and server-side authorization. No such execution occurred here.

## RELATED DOMAIN CHECK / HANDOFFS

**Foundations:** sequence allocation order differs from transaction commit/visibility order. **Architecture:** API contract must state the linearization point and what a continuation token proves. **Mobile:** offline/long-suspended clients can permanently miss late-visible data after cursor advancement. **Data:** Applied Cursor must be a proven durable prefix, not maximum observed ID. **Quality:** this is a new failure-first negative oracle beyond OFFSET pagination and GC. **Systems:** server-owned admission/authorization and per-owner epoch semantics must bind any proof. **Design Studio / Web Manager / Marketing Manager:** no immediate canonical changes. **LogMate:** read-only advisory; retain owner-approved Automatic+Manual Delta and separate W-013 implementation stack; do not treat this independent experiment as product defect, implementation approval or release PASS.

**OPEN:** exact committed test script is local-only; GitHub-hosted rerun, Firestore transaction ordering, distributed sequencer semantics, authenticated completeness proof, old-cursor GC recovery, and production E2E are NOT VERIFIED.
