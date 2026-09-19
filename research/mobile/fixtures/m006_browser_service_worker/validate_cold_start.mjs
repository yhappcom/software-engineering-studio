import { chromium } from 'playwright';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const profile = await mkdtemp(join(tmpdir(), 'm006-cold-profile-'));
let warm;
let cold;
try {
  warm = await chromium.launchPersistentContext(profile, {headless:true, serviceWorkers:'allow'});
  const warmPage = await warm.newPage();
  await warmPage.goto('http://127.0.0.1:8768/cold.html', {waitUntil:'load'});
  const warmPayload = (await warmPage.evaluate(() => window.fixtureReady)).trim();
  if (warmPayload !== 'M006-CACHED-PAYLOAD-v1') throw new Error(`warm setup failed: ${warmPayload}`);
  if (!(await warmPage.evaluate(() => !!navigator.serviceWorker.controller))) throw new Error('warm page is not controlled');
  const browserVersion = warm.browser()?.version() ?? 'unknown';
  await warm.close();
  warm = undefined;

  cold = await chromium.launchPersistentContext(profile, {headless:true, serviceWorkers:'allow'});
  await cold.setOffline(true);
  const coldPage = await cold.newPage();
  const response = await coldPage.goto('http://127.0.0.1:8768/cold.html?offline-cold=1', {waitUntil:'load'});
  if (!response || !response.ok()) throw new Error(`offline cold navigation failed: ${response?.status() ?? 'no-response'}`);
  const controlled = await coldPage.evaluate(() => !!navigator.serviceWorker.controller);
  if (!controlled) throw new Error('offline cold-start page is not service-worker controlled');
  const shellText = await coldPage.locator('body').innerText();
  if (!shellText.includes('M006 cold shell')) throw new Error(`offline shell oracle failed: ${shellText}`);
  const cachedPayload = await coldPage.evaluate(async () => (await (await fetch('/payload.txt?offline-cold=1')).text()).trim());
  if (cachedPayload !== 'M006-CACHED-PAYLOAD-v1') throw new Error(`offline cold payload failed: ${cachedPayload}`);
  const uncachedFailed = await coldPage.evaluate(async () => {
    try { await fetch('/never-cached-cold.txt'); return false; } catch (_) { return true; }
  });
  if (!uncachedFailed) throw new Error('negative cold-start oracle failed: uncached fetch unexpectedly succeeded');
  console.log(JSON.stringify({browserVersion, controlled, shellText, cachedPayload, uncachedFailed, verdict:'PASS'}));
} finally {
  if (warm) await warm.close();
  if (cold) await cold.close();
  await rm(profile, {recursive:true, force:true});
}
