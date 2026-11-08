// Q005 synthetic run/evidence gate — no account data or network access.
// Execute in a normal Node.js environment:
//   node research/quality/fixtures/Q005_scheduled_run_evidence_gate.js
// This fixture does not query, schedule, or mutate real automations.

function assess(input) {
  const active = input.enabled === true ? 'ENABLED' : 'NOT_ENABLED';
  const run = input.lastRun;
  let execution = 'NOT_OBSERVED';
  if (run) {
    if (run.status === 'failed') {
      execution = 'RECORDED_FAILED';
    } else if (run.status === 'in_progress') {
      execution = 'IN_PROGRESS_UNPROVEN';
    } else if (run.status === 'completed' || run.status === 'no_update') {
      const result = input.lastResult;
      const bound =
        !!result &&
        result.runId === run.id &&
        result.createdAt >= run.startedAt;
      execution = bound
        ? (result.failure === true
          ? 'RECORDED_COMPLETE_WITH_FAILURE_RESULT'
          : 'RECORDED_COMPLETED_BOUND')
        : 'RECORDED_COMPLETED_RESULT_UNBOUND';
    }
  }
  const delivery =
    input.delivery === 'delivered'
      ? 'DELIVERY_RECORDED'
      : 'DELIVERY_NOT_CONFIRMED';
  const persistence =
    input.verifiedCommitLinkedToRun === true
      ? 'COMMIT_LINKED'
      : 'NO_LINKED_COMMIT_EVIDENCE';
  return { active, execution, delivery, persistence };
}

const base = {
  enabled: true,
  lastRun: { id: 'r1', status: 'completed', startedAt: 100 },
  lastResult: { runId: 'r1', createdAt: 120, failure: false },
  delivery: 'unknown',
  verifiedCommitLinkedToRun: false,
};
const cases = [
  ['healthy_no_git_commit', { ...base }, 'RECORDED_COMPLETED_BOUND'],
  ['old_output_mismatch',
    { ...base, lastResult: { runId: 'r0', createdAt: 120, failure: false } },
    'RECORDED_COMPLETED_RESULT_UNBOUND'],
  ['timestamp_stale',
    { ...base, lastResult: { runId: 'r1', createdAt: 99, failure: false } },
    'RECORDED_COMPLETED_RESULT_UNBOUND'],
  ['failed_with_old_success',
    { ...base,
      lastRun: { id: 'r1', status: 'failed', startedAt: 100 },
      lastResult: { runId: 'r0', createdAt: 120, failure: false } },
    'RECORDED_FAILED'],
  ['no_run_history',
    { enabled: true, lastRun: null, lastResult: null, delivery: 'unknown' },
    'NOT_OBSERVED'],
  ['in_progress',
    { ...base, lastRun: { id: 'r1', status: 'in_progress', startedAt: 100 } },
    'IN_PROGRESS_UNPROVEN'],
  ['disabled_historical_success',
    { ...base, enabled: false },
    'RECORDED_COMPLETED_BOUND'],
  ['result_reports_failure',
    { ...base, lastResult: { runId: 'r1', createdAt: 120, failure: true } },
    'RECORDED_COMPLETE_WITH_FAILURE_RESULT'],
];
for (const [name, input, expected] of cases) {
  const got = assess(input);
  if (got.execution !== expected) {
    throw new Error(name + ': expected=' + expected + ', got=' + got.execution);
  }
  if (input.delivery === 'unknown' &&
      got.delivery !== 'DELIVERY_NOT_CONFIRMED') {
    throw new Error(name + ': unknown delivery was promoted to delivered');
  }
  if (input.verifiedCommitLinkedToRun !== true &&
      got.persistence !== 'NO_LINKED_COMMIT_EVIDENCE') {
    throw new Error(name + ': absent commit linkage was promoted');
  }
}
console.log('Q005_SCHEDULED_EVIDENCE_GATE_PASS ' + cases.length + '/' + cases.length);
