import os
import subprocess
import sys

print(f"parent_pid={os.getpid()}")

child_code = (
    "import os,sys; "
    "print(f'child_pid={os.getpid()}'); "
    "print('child_stdout'); "
    "print('child_stderr', file=sys.stderr); "
    "sys.exit(7)"
)

result = subprocess.run(
    [sys.executable, "-c", child_code],
    text=True,
    capture_output=True,
)

print(f"child_returncode={result.returncode}")
print(f"captured_stdout={result.stdout.strip()!r}")
print(f"captured_stderr={result.stderr.strip()!r}")
