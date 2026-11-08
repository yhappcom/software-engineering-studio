# D006 — Snapshot-bound retention witness: GC race and forged-proof negative oracle

**2026-11-08 Asia/Seoul — VERIFIED EXECUTION (synthetic Node.js model only); D006 Stage 1 NOT PASS.**

## Exact provenance and scope
- Studio prior main `653f6f89d7a93a7863881048722c7b3884c37492`. Independent fixture: `research/data/fixtures/D006_snapshot_retention_witness_canary.js`, SHA-256 of locally executed file `f1bb90a4635c1e1e8689b8033988cb922bddb7b2faf223a112238fbdf07a68cb`. Runtime: Node.js `v22.16.0`, local Linux container, command `node /mnt/data/D006_snapshot_retention_witness_canary.js`, observed `D006_SNAPSHOT_RETENTION_WITNESS_SYNTHETIC_PASS 10/10`. The exact script text was then committed as a public, fully synthetic Studio fixture; **not** independently rerun on GitHub Actions. A later exact-file hash/readback comparison is recommended before treating the GitHub artifact as a byte-verified replay.
- Product read-only source: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`, **not assumed production**. Enumerated 69 branches and 20 open Draft PRs. New PR54 `feat/w013-persistent-writer-20261108@8da33f5ff9b90911df95acf4ff1b707434e20bba` is stacked on PR53 `docs/w013-persistent-contract-review-20261108@442b003eb0ae261e674b56dc5a00822819ebe801`, itself stacked on PR52/PR51. W013 native writer work is separate from production D006 authenticated Sync; neither CI nor product execution was invoked.
- The main branch's older Manual-only wording is not substituted for owner-approved newer Automatic + Manual Delta policy in the unmerged W013 stack. Neither is actual production implementation evidence.

## Claim, model and negative oracles
Prior D006 retention-floor model accepted an unauthenticated Boolean completeness flag; forged `true` and GC advancing between metadata and page read were OPEN. This study adds a **synthetic cryptographic integrity check and explicit snapshot version binding** to test fail-closed classification.

Fixture payload is `{owner,generation,cursor,version,floor,high}`, with a Node HMAC-SHA256 over deterministic JSON encoding and a **hard-coded, public, synthetic-only key**. A server-issued witness for view v10 floor5/high7 is compared to a separate current view v11 floor7/high7. It returns `STALE_RETRY` rather than accepting the outdated witness. Authenticated floor7 with cursor4 returns `RECOVERY_REQUIRED` without claiming missing events were applied. Wrong owner, generation, cursor, malformed MAC, modified floor, forged `true` and invalid high-water all fail closed. A valid same-view synthetic witness is accepted.

**Observed execution:** 10/10 assertions matched the expected outcome. This is a pure deterministic protocol classifier, **not** a concurrent DB transaction or actual garbage collector race. In particular, the model's current view is trusted input; if the view itself can be forged, the HMAC on an older witness does not establish freshness. HMAC also does not prove the server's page completeness, durable event publication, authorization, real key management, replay protection, or distributed consistency. This prevents overpromoting the bounded result to Firebase or LogMate.

## Root-cause distinction and alternatives
- **Boolean-only completeness:** a client cannot authenticate it; reject as a production proof.
- **Signed/HMAC'd metadata but no snapshot identity:** tamper detection alone is insufficient when GC advances between metadata and page reads. Reject as a complete consistency protocol.
- **Witness + version/floor/high bound to a single server snapshot and authenticated owner/generation:** candidate interface. Must additionally ensure the page bytes and cursor advance are bound to the **same consistent view** and verify retention cannot erase required events during that view. If no stable view exists, return an explicit retry or recovery requirement. No such product protocol is approved here.
- **Recovery:** if the old cursor is below retained floor, do not invent a cursor jump. Enter a durable `RECOVERY_REQUIRED` state, separately preserve unsent local operations, and require an owner-authorized full reconciliation/bootstrap contract.

## Falsifiable next gate
Implement a **two-connection file-backed concurrent GC/page-read harness** with actual transaction scheduling and crash/reopen. Assert no accepted page can be produced from a witness whose bound snapshot is no longer available; validate a page-content digest and witness under the same transaction. Then transfer only after explicit authorized LogMate/Codex Work and real Firebase owner-authenticated adapter design. Hosted byte-identical fixture rerun remains OPEN.

## RELATED DOMAIN CHECK / HANDOFFS
- **Foundations:** integrity authentication, concurrency, transactional snapshot and process death are different properties.
- **Architecture:** the page API must expose explicit `ACCEPT / STALE_RETRY / RECOVERY_REQUIRED / REJECT` outcomes and their authority, rather than silently reusing a cursor.
- **Mobile:** offline EFB/PWA and long-suspended native replicas are likely retention-floor clients; no physical-device evidence.
- **Data:** D006 owns cursor/GC/receipt invariants; this closes only a deterministic forged-flag and metadata-version classifier gap, not GC safety.
- **Quality:** 10 negative/positive model assertions with reproducible source; actual concurrent failure injection still required.
- **Systems:** witness key secrecy, principal authorization, replay and server snapshot consistency require separate implementation and validation.
- **Design Studio/Web Manager/Marketing Manager:** no design, web, marketing or product-policy change warranted.
- **LogMate:** READ ONLY; no CI, PR, issue, commit, Work ID, release, database or configuration changes.

**Gate:** D006 remains NOT PASS. No production Sync, Firebase, Dart/Sembast or account deletion integrity conclusion follows from this synthetic Node model.
