#!/usr/bin/env python3
"""D005: inject EIO into target SQLite fsync/fdatasync calls via LD_PRELOAD.

Linux/glibc-style bounded validation fixture. It is intentionally not a physical
power-loss/device-failure simulator.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import subprocess
import tempfile
from pathlib import Path

SHIM = r'''
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
static int sync_count = 0;
static int matches(int fd) {
  char link[64], path[PATH_MAX];
  snprintf(link, sizeof(link), "/proc/self/fd/%d", fd);
  ssize_t n = readlink(link, path, sizeof(path)-1);
  if (n < 0) return 0;
  path[n] = 0;
  const char *prefix = getenv("FAULT_PREFIX");
  return prefix && strncmp(path, prefix, strlen(prefix)) == 0;
}
static int should_fail(int fd, const char *name) {
  if (!matches(fd)) return 0;
  sync_count++;
  fprintf(stderr, "SYNC_CALL %d %s fd=%d\n", sync_count, name, fd);
  fflush(stderr);
  const char *s = getenv("FAIL_SYNC_N");
  int target = s ? atoi(s) : 0;
  if (target > 0 && sync_count == target) {
    errno = EIO;
    fprintf(stderr, "INJECT_EIO %d %s\n", sync_count, name);
    fflush(stderr);
    return 1;
  }
  return 0;
}
int fsync(int fd) {
  static int (*real_fsync)(int) = NULL;
  if (!real_fsync) real_fsync = dlsym(RTLD_NEXT, "fsync");
  if (should_fail(fd, "fsync")) return -1;
  return real_fsync(fd);
}
int fdatasync(int fd) {
  static int (*real_fdatasync)(int) = NULL;
  if (!real_fdatasync) real_fdatasync = dlsym(RTLD_NEXT, "fdatasync");
  if (should_fail(fd, "fdatasync")) return -1;
  return real_fdatasync(fd);
}
'''

CHILD = r'''
import sqlite3, sys
p = sys.argv[1]
c = sqlite3.connect(p)
c.execute("PRAGMA journal_mode=DELETE")
c.execute("PRAGMA synchronous=FULL")
try:
    c.execute("BEGIN IMMEDIATE")
    c.execute("INSERT INTO ledger(v) VALUES (200)")
    c.commit()
    print("COMMIT_OK")
except Exception as e:
    print("ERROR", type(e).__name__, str(e), getattr(e, "sqlite_errorcode", None), getattr(e, "sqlite_errorname", None))
    try:
        c.rollback()
    except Exception as rollback_error:
        print("ROLLBACK_ERROR", repr(rollback_error))
c.close()
'''


def inspect(db: Path):
    c = sqlite3.connect(db)
    rows = c.execute("SELECT v FROM ledger ORDER BY rowid").fetchall()
    integrity = c.execute("PRAGMA integrity_check").fetchone()[0]
    c.close()
    return rows, integrity


def run_case(root: Path, shim: Path, baseline: Path, fail_n: int):
    db = root / f"case_{fail_n}.db"
    shutil.copy2(baseline, db)
    env = os.environ.copy()
    env.update({"LD_PRELOAD": str(shim), "FAULT_PREFIX": str(db), "FAIL_SYNC_N": str(fail_n)})
    cp = subprocess.run(["python3", "-c", CHILD, str(db)], env=env, text=True, capture_output=True, check=True)
    return cp.stdout.strip(), cp.stderr.strip(), inspect(db)


def main():
    with tempfile.TemporaryDirectory(prefix="d005_fsync_") as td:
        root = Path(td)
        src, shim = root / "shim.c", root / "shim.so"
        src.write_text(SHIM)
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", "-o", str(shim), str(src), "-ldl"], check=True)

        baseline = root / "baseline.db"
        c = sqlite3.connect(baseline)
        c.execute("PRAGMA journal_mode=DELETE")
        c.execute("PRAGMA synchronous=FULL")
        c.execute("CREATE TABLE ledger(v INTEGER NOT NULL)")
        c.execute("INSERT INTO ledger(v) VALUES (100)")
        c.commit(); c.close()

        control = run_case(root, shim, baseline, 0)
        assert control[0] == "COMMIT_OK"
        assert control[2] == ([(100,), (200,)], "ok")

        for n in (1, 2, 3):
            out, trace, state = run_case(root, shim, baseline, n)
            assert "SQLITE_IOERR_FSYNC" in out and "1034" in out, (n, out, trace)
            assert state == ([(100,)], "ok"), (n, state, out, trace)
            print(f"FAIL_SYNC_N={n}: {out}; reopened={state}; trace={trace!r}")

        late = run_case(root, shim, baseline, 4)
        assert late[0] == "COMMIT_OK" and late[2] == ([(100,), (200,)], "ok")
        print("CONTROL and three injected sync failures behaved as expected.")

if __name__ == "__main__":
    main()
