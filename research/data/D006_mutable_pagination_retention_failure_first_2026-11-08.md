# D006 — Concurrent Pagination, Retention, and Cursor Completeness

**2026-11-08 | VERIFIED EXECUTION — independent SQLite model only.** This study follows the sparse-global sequence analysis, but tests a distinct failure boundary: a paginated event feed may mutate between page requests. No private LogMate code, user data, credentials, CI or product repository mutation was involved.

## Source identity and limits
- Studio source before this work: `yhappcom/software-engineering-studio → main@8a5b56d5d663ca6667ba7f61f641eb7f054d799a`.
- LogMate read-only: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`; main **not** assumed production. Enumerated 66 branches and 17 open Draft PRs. W013 PR51 `docs/w013-ios-boundary-adoption-20261108@62d7295da6b447ba45dd3f0196c81ec449f2cdf9` is stacked on PR50 `verify/w013-android-runtime-20261108@c08feb25517c32a6104f4cc1ef49e7a4a9f33ddd`. Product sync policy PR42 remains unmerged. No product implementation evidence promoted to PASS.
- Independent experiment: Python stdlib sqlite3, **SQLite 3.46.1**, local file-backed SQLite with explicit commits between page reads, seven deterministic synthetic controls. Source SHA256 `84ef180b65b5ea6006ec8b11990340d36e02678792908c389c0aacfc57b51b7d`. Exact source is committed separately as `research/data/fixtures/D006_mutable_page_canary.py`. These are model checks, not product or hosted CI evidence.

## Failure-first mechanism and observed oracles

1. **OFFSET + retention deletion:** initial page [1,2]; delete seq1; `OFFSET 2` yields [] although seq3 remains. **Silent omission reproduced.**
2. **Keyset after deletion:** `seq>2` yields [3]. The shifting-position omission is avoided.
3. **OFFSET + insertion ahead of page boundary:** first [10,20], insert 15, second `OFFSET 2` yields [20,30]; **duplicate seq20 reproduced**.
4. **Keyset + fixed high-water 30:** after first [10,20] and insertion seq15, second `seq>20 AND seq<=30` yields [30], preserving the original bounded set [10,20,30] for this *specific monotonic sequence assumption*.
5. **Future event:** insert seq40 after bound30; fixed-bound page excludes 40, next epoch can include it.
6. **False empty-page completion:** after [1,2], deletion seq1 and `OFFSET 2` yields []; observed union lacks 3. Empty page is not proof of a complete prefix.
7. **Keyset alone is insufficient:** delete seq2 before first read; `seq>0` returns [3]. A cursor cannot infer seq2's contents or safety from keyset ordering alone.

All seven assertions passed in the local executable environment. The canary deliberately mutates a small synthetic table; it does not simulate Firestore read consistency, distributed transaction boundaries, cryptographic authentication, network retries or real product retention.

## Engineering conclusion

**OFFSET pagination on a mutable log is unsafe as a completeness oracle.** Keyset pagination with an immutable, server-committed ordering key eliminates positional shifts, but **does not establish complete history** when old events can be removed, when filtered global sequences are sparse, or when the server fails to bind a page to a consistent high-water mark. A correct protocol needs a clearly defined server-side sequence namespace, snapshot/read bound, retention floor, authenticated page-completeness/continuation semantics and a recovery path when a client's cursor falls below retained history.

The synthetic keyset success assumes the sequence key is monotonic with visibility/commit order and that the original bounded records are not deleted. If a server assigns seq before transaction commit, an event may become visible later with a seq below the captured high-water; a keyset high-water alone then also loses it. This remains an explicit **OPEN negative** rather than an invented product property.

## Alternatives / validation gate

- OFFSET+LIMIT: reject as completeness evidence under concurrent writes/retention.
- Keyset+high-water: conditionally safe for positional stability, **not** sufficient for authenticated completeness.
- Server-issued opaque snapshot/continuation token or owner-scoped append-only ordered log with retention floor and authenticated proof: candidate engineering mechanisms; actual Firebase/LogMate wire policy remains **owner/product decision OPEN**.
- Product acceptance gate: deliberately interleave two pages with insert, delete/GC, concurrent commit, late visibility, server gap, replay and expired cursor; verify no silent omission or duplicate apply, and require explicit recovery if history is no longer available. Execute against exact Dart/Sembast/Firebase source only with separate product approval.

## RELATED DOMAIN CHECK / HANDOFFS

**Foundations:** order, commit visibility and positional indexing are distinct. **Architecture:** continuation contract must expose stable read semantics, not raw database offset. **Mobile:** suspended/offline PWA and native catch-up may span GC or new writes. **Data:** applied cursor and record apply must remain atomic; retention floor is a protocol input. **Quality:** negative interleavings and false empty-page oracle. **Systems:** UID/Generation/epoch binding, server-side authorization and immutable provenance. **Design/Web/Marketing:** no current policy or interface change. **LogMate handoff:** owner-approved Automatic+Manual Delta remains unchanged; request exact sequence namespace, server snapshot/retention guarantee and stale-cursor recovery contract before claiming implementation correctness.

**OPEN:** product Firebase transfer, real authenticated completeness, late-commit ordering, GC/compaction, host CI execution, actual EFB lifecycle and Stage 1 PASS. This study does not reopen or repair S007 account deletion.
