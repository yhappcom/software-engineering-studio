#!/usr/bin/env bash
set -eu

producer='printf "PRIMARY_ORACLE_FAIL\n"; exit 23'

# Deliberately disable pipefail for the control case. The fixture itself must
# not inherit the workflow shell's fail-closed setting into this discriminator.
set +o pipefail
set +e
bash -c "$producer" 2>&1 | tee /tmp/q006-without-pipefail.txt >/dev/null
without_pipefail=$?
set -e

set -o pipefail
set +e
bash -c "$producer" 2>&1 | tee /tmp/q006-with-pipefail.txt >/dev/null
with_pipefail=$?
set -e

printf 'without_pipefail_rc=%s\n' "$without_pipefail"
printf 'with_pipefail_rc=%s\n' "$with_pipefail"
printf 'without_payload=%s\n' "$(cat /tmp/q006-without-pipefail.txt)"
printf 'with_payload=%s\n' "$(cat /tmp/q006-with-pipefail.txt)"

[[ "$without_pipefail" -eq 0 ]]
[[ "$with_pipefail" -eq 23 ]]
grep -qx 'PRIMARY_ORACLE_FAIL' /tmp/q006-without-pipefail.txt
grep -qx 'PRIMARY_ORACLE_FAIL' /tmp/q006-with-pipefail.txt

echo 'Q006_CI_PIPELINE_EXIT_PROPAGATION_PASS'
