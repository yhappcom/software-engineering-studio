import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const root = new URL('.', import.meta.url).pathname;
const profile = await mkdtemp(join(tmpdir(), 'm006-profile-'));
const server = spawn('python3', ['-m', 'http.server', '8766', '--bind', '127.0.0.1', '--directory', root], {stdio:'inherit'});
const sleep = ms => new Promise(r => setTimeout(r, ms));
let first;
let second;
try {
  await sleep(800);
  first = await chromium.launchPersistentContext(profile, {headless:true, serviceWorkers:'allow'});
  const firstPage = await first.newPage();
  await firstPage.goto('http://127.0.0.1:8766/', {waitUntil:'load'});
  const firstPayload = (await firstPage.evaluate(() => window.fixtureReady)).trim();
  if (firstPayload !== 'M006-CACHED-PAYLOAD-v1') throw new Error(`first-session setup oracle failed: ${firstPayload}`);
  if (!(await firstPage.evaluate(() => !!navigator.serviceWorker.controller))) throw new Error('first session is not service-worker controlled');
  const version = first.browser()?.version() ?? 'unknown';
  await first.close();
  first = undefined;

  // Re-launch a new browser process against the same persistent profile. Navigation is
  // intentionally online so this test isolates persisted service-worker/cache state
  // across restart rather than claiming offline cold-start shell availability.
  second = await chromium.launchPersistentContext(profile, {headless:true, serviceWorkers:'allow'});
  const secondPage = await second.newPage();
  await secondPage.goto('http://127.0.0.1:8766/', {waitUntil:'load'});
  const controlledAfterRestart = await secondPage.evaluate(() => !!navigator.serviceWorker.controller);
  if (!controlledAfterRestart) throw new Error('service worker control did not survive browser restart/profile reuse');

  await second.setOffline(true);
  const cachedAfterRestart = await secondPage.evaluate(async () => (await (await fetch('/payload.txt?after-restart=1')).text()).trim());
  if (cachedAfterRestart !== 'M006-CACHED-PAYLOAD-v1') throw new Error(`persisted-cache oracle failed: ${cachedAfterRestart}`);
  const uncachedFailed = await secondPage.evaluate(async () => {
    try { await fetch('/never-cached-after-restart.txt'); return false; } catch (_) { return true; }
  });
  if (!uncachedFailed) throw new Error('negative restart oracle failed: uncached offline fetch unexpectedly succeeded');

  console.log(JSON.stringify({browserVersion:version, controlledAfterRestart, cachedAfterRestart, uncachedFailed, verdict:'PASS'}));
} finally {
  if (first) await first.close();
  if (second) await second.close();
  server.kill('SIGTERM');
  await rm(profile, {recursive:true, force:true});
}
