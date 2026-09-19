import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import process from 'node:process';

const root = new URL('.', import.meta.url).pathname;
const server = spawn('python3', ['-m', 'http.server', '8765', '--bind', '127.0.0.1', '--directory', root], {stdio:'inherit'});
const sleep = ms => new Promise(r => setTimeout(r, ms));
let browser;
try {
  await sleep(800);
  browser = await chromium.launch({headless:true});
  const context = await browser.newContext({serviceWorkers:'allow'});
  const page = await context.newPage();
  await page.goto('http://127.0.0.1:8765/', {waitUntil:'load'});
  const online = await page.evaluate(() => window.fixtureReady);
  if (online.trim() !== 'M006-CACHED-PAYLOAD-v1') throw new Error(`online oracle failed: ${online}`);
  const controlled = await page.evaluate(() => !!navigator.serviceWorker.controller);
  if (!controlled) throw new Error('service worker did not control page');

  await context.setOffline(true);
  const offline = await page.evaluate(async () => (await (await fetch('/payload.txt?offline=1')).text()).trim());
  if (offline !== 'M006-CACHED-PAYLOAD-v1') throw new Error(`offline controlled-fetch oracle failed: ${offline}`);

  const uncachedFailed = await page.evaluate(async () => {
    try { await fetch('/never-cached.txt'); return false; } catch (_) { return true; }
  });
  if (!uncachedFailed) throw new Error('negative oracle failed: uncached offline fetch unexpectedly succeeded');

  console.log(JSON.stringify({controlled, online: online.trim(), offline, uncachedFailed, verdict:'PASS'}));
} finally {
  if (browser) await browser.close();
  server.kill('SIGTERM');
}
