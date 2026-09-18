#!/usr/bin/env python3
"""Bounded reproducible-build experiment using GCC.

Builds identical C source in two different absolute directories and at different
wall-clock times. It compares four cases:
  1. naive build
  2. timestamp normalization only (SOURCE_DATE_EPOCH)
  3. path normalization only (-ffile-prefix-map)
  4. both normalizations

Expected in the recorded GCC/Linux environment: only case 4 is byte-identical.
This is not a Flutter/mobile or hermetic-build test.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

SOURCE = r'''#include <stdio.h>
int main(void) {
    puts(__FILE__);
    puts(__DATE__ " " __TIME__);
    return 0;
}
'''
EPOCH = "1700000000"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(srcdir: Path, *, epoch: bool, prefix_map: bool) -> Path:
    out = srcdir / "app"
    env = os.environ.copy()
    if epoch:
        env["SOURCE_DATE_EPOCH"] = EPOCH
    else:
        env.pop("SOURCE_DATE_EPOCH", None)
    cmd = ["gcc", "-O2", "-g"]
    if prefix_map:
        cmd.append(f"-ffile-prefix-map={srcdir}=/src")
    cmd += ["main.c", "-o", "app"]
    subprocess.run(cmd, cwd=srcdir, env=env, check=True)
    return out


def run_case(a: Path, b: Path, name: str, *, epoch: bool, prefix_map: bool) -> tuple[str, str, bool]:
    for d in (a, b):
        (d / "app").unlink(missing_ok=True)
    aa = build(a, epoch=epoch, prefix_map=prefix_map)
    time.sleep(2)
    bb = build(b, epoch=epoch, prefix_map=prefix_map)
    ha, hb = sha256(aa), sha256(bb)
    same = aa.read_bytes() == bb.read_bytes()
    print(f"{name}: same={same} shaA={ha} shaB={hb}")
    return ha, hb, same


def main() -> None:
    if shutil.which("gcc") is None:
        raise SystemExit("gcc unavailable")
    with tempfile.TemporaryDirectory(prefix="s005-repro-") as root:
        rootp = Path(root)
        a, b = rootp / "build-A", rootp / "build-B"
        a.mkdir(); b.mkdir()
        (a / "main.c").write_text(SOURCE, encoding="utf-8")
        (b / "main.c").write_text(SOURCE, encoding="utf-8")

        results = {
            "naive": run_case(a, b, "naive", epoch=False, prefix_map=False),
            "time_only": run_case(a, b, "time_only", epoch=True, prefix_map=False),
            "path_only": run_case(a, b, "path_only", epoch=False, prefix_map=True),
            "both": run_case(a, b, "both", epoch=True, prefix_map=True),
        }

        assert not results["naive"][2]
        assert not results["time_only"][2]
        assert not results["path_only"][2]
        assert results["both"][2]
        output = subprocess.check_output([str(a / "app")], text=True)
        assert "Nov 14 2023 22:13:20" in output
        print("normalized_runtime_output=" + repr(output))
        print("PASS: timestamp and build-path normalization were both required for byte identity in this bounded build")


if __name__ == "__main__":
    main()
