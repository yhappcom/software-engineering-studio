# S006 — Rename visibility vs directory-sync publication durability

Date: 2026-09-19
Status: **IN STUDY — executable Linux failure boundary**

## Problem
D005 established that backup candidate generation, completion, validation and publication are separate states. This block asks a narrower Systems question: after a validated candidate is renamed into its final pathname, does pathname visibility itself prove crash-durable publication?

## SOURCE
- POSIX/Linux `rename()` provides pathname replacement semantics; successful rename is not by itself a claim that directory metadata has reached nonvolatile media. Linux also documents network-filesystem ambiguity around rename failures.
- SQLite's atomic-commit documentation explicitly synchronizes a containing directory where power-loss visibility of newly created metadata matters, and `PRAGMA synchronous=EXTRA` adds a directory sync after rollback-journal unlink because this can improve durability when power loss closely follows commit.

Primary references checked 2026-09-19:
- Linux `rename(2)`: https://man7.org/linux/man-pages/man2/rename.2.html
- SQLite Atomic Commit: https://www.sqlite.org/atomiccommit.html
- SQLite `PRAGMA synchronous`: https://sqlite.org/pragma.html#pragma_synchronous

## VALIDATION
Fixture: `research/systems/fixtures/S006_directory_fsync_publication_boundary.py`

Environment: Linux 6.18.44 x86_64, Python 3.13.5, GCC available; execution date 2026-09-19.

Protocol under test:
1. write private candidate;
2. flush userspace buffer;
3. `fsync(candidate)`;
4. `os.replace(candidate, final)`;
5. open containing directory;
6. `fsync(directory)`;
7. only then accept publication success.

An LD_PRELOAD shim delegates ordinary `fsync()` calls but returns `EIO` for directory file descriptors. Control execution completed successfully. Under the injected directory-sync failure, the publisher exited with `OSError: [Errno 5] Input/output error`, yet `published.bin` already existed at the final pathname and contained the expected bytes.

### Claim / oracle
**CLAIM:** final-path visibility after rename is not a sufficient success oracle for a publication protocol whose contract includes successful directory synchronization.

**ORACLE:** the protocol succeeds only if all required steps through directory `fsync()` succeed. The injected run therefore fails even though the final pathname is visible.

**OBSERVATION:** control succeeded; injected directory `fsync` failed with EIO; final pathname was nevertheless visible after the failed synchronization.

**VERDICT:** PASS for the bounded oracle-discrimination claim. This is not hard-power-loss evidence.

## SYNTHESIS
`candidate valid` → `file data synchronized` → `rename visible` → `directory metadata synchronized` → `publication accepted` are distinct claims. A process can observe the new final pathname before the protocol has evidence for its required metadata synchronization. Therefore application success state must not be inferred solely from `exists(final)` or successful rename when crash-durable publication is required.

## ENGINEERING JUDGMENT
For high-value backup replacement on Unix-like filesystems, a defensible acceptance protocol should explicitly define candidate validation, file-data synchronization, replacement semantics, containing-directory synchronization, and error handling. Exact requirements remain filesystem/platform specific; this note does not prescribe the same syscall sequence for Android, iOS, Windows, browser storage, cloud/object stores or network filesystems.

## CONTRADICTION / failure of a tempting assumption
The bounded run falsifies the assumption `final pathname visible => every required publication-durability step succeeded`. Visibility survived a deliberately failed directory-sync step.

## EVIDENCE LIMIT / OPEN
- No physical power cut, reboot, controller-cache loss or filesystem crash was performed.
- The run does not show what bytes/metadata would survive such a failure.
- It does not validate ext4/APFS/mobile/filesystem-specific ordering, atomic replacement guarantees, or lying-successful `fsync`.
- It does not validate a current LogMate backup implementation.
- Direct Dart/Flutter execution remained unavailable on 2026-09-19.

## RELATED DOMAIN CHECK
- Foundations: F001 process/I/O boundary relevant; direct Dart/Flutter OPEN.
- Architecture: publication states are explicit semantic boundaries.
- Mobile: exact Android/iOS/Flutter storage replacement semantics require transfer validation.
- Data: extends D005 candidate/completion/validation/publication work at the filesystem publication boundary.
- Quality: acceptance oracle must distinguish visible pathname from completed durability protocol.
- Systems: owning track; S006 release/rollback/change-safety semantics apply.
- Design Studio: no canonical design conclusion changes this low-level mechanism.
- Web Manager: web deployment/storage mechanisms differ; no transfer assumed.
- Marketing Manager: not materially relevant.
- Product source: no product implementation claim made; no product audit required for this mechanism block.

## HANDOFFS
- **Data:** treat directory-sync/replacement evidence as a separate publication-durability requirement from database-aware backup completion.
- **Quality:** add deliberate post-rename/pre-acceptance synchronization failure when a product implementation exposes this boundary.
- **Mobile:** reproduce with the exact platform storage API/filesystem and process/power failure mechanisms before claiming mobile durability.

## CHANGE WATCH
Filesystem, kernel, platform storage APIs and framework wrappers can change the applicable durability mechanism. Revalidate against exact target platform and artifact.
