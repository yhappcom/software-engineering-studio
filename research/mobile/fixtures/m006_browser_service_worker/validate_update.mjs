import http from 'node:http';
import assert from 'node:assert/strict';
import { chromium } from 'playwright';

let swVersion = 'v1';
const pageHtml = `<!doctype html><meta charset="utf-8"><title>M006 update</title>`;
const swSource = () => `
const VERSION = '${swVersion}';
self.addEventListener('install', event => {
  ${swVersion === 'v1' ? "self.skipWaiting();" : ''}
});
self.addEventListener('activate', event => {
  event.waitUntil(clients.claim());
});
self.addEventListener('message', event => {
  if (event.data === 'VERSION') event.ports[0].postMessage(VERSION);
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});
`;

const server = http.createServer((req, res) => {
  if (req.url.startsWith('/sw.js')) {
    res.writeHead(200, {'content-type':'application/javascript','cache-control':'no-store'});
    res.end(swSource());
    return;
  }
  res.writeHead(200, {'content-type':'text/html','cache-control':'no-store'});
  res.end(pageHtml);
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const { port } = server.address();
const origin = `http://127.0.0.1:${port}`;

const browser = await chromium.launch({headless:true});
const context = await browser.newContext();
const page = await context.newPage();

async function controllerVersion() {
  return await page.evaluate(async () => {
    const controller = navigator.serviceWorker.controller;
    if (!controller) return null;
    return await new Promise((resolve, reject) => {
      const channel = new MessageChannel();
      const timer = setTimeout(() => reject(new Error('version reply timeout')), 3000);
      channel.port1.onmessage = e => { clearTimeout(timer); resolve(e.data); };
      controller.postMessage('VERSION', [channel.port2]);
    });
  });
}

try {
  await page.goto(origin, {waitUntil:'load'});
  await page.evaluate(async () => {
    await navigator.serviceWorker.register('/sw.js');
    await navigator.serviceWorker.ready;
    if (!navigator.serviceWorker.controller) {
      await new Promise(resolve => navigator.serviceWorker.addEventListener('controllerchange', resolve, {once:true}));
    }
  });
  assert.equal(await controllerVersion(), 'v1');

  swVersion = 'v2';
  await page.evaluate(async () => {
    const reg = await navigator.serviceWorker.getRegistration();
    await reg.update();
    if (!reg.waiting) {
      await new Promise((resolve, reject) => {
        const timer = setTimeout(() => reject(new Error('v2 did not enter waiting')), 5000);
        const installing = reg.installing;
        if (!installing) return reject(new Error('no installing worker after update'));
        installing.addEventListener('statechange', () => {
          if (installing.state === 'installed') { clearTimeout(timer); resolve(); }
        });
      });
    }
  });

  // A newly installed worker must not silently replace the controller while the v1 client is active.
  assert.equal(await controllerVersion(), 'v1');
  const waitingState = await page.evaluate(async () => {
    const reg = await navigator.serviceWorker.getRegistration();
    return reg.waiting?.state ?? null;
  });
  assert.equal(waitingState, 'installed');

  await page.evaluate(async () => {
    const reg = await navigator.serviceWorker.getRegistration();
    if (!reg.waiting) throw new Error('expected waiting v2 worker');
    const changed = new Promise((resolve, reject) => {
      const timer = setTimeout(() => reject(new Error('controllerchange timeout')), 5000);
      navigator.serviceWorker.addEventListener('controllerchange', () => { clearTimeout(timer); resolve(); }, {once:true});
    });
    reg.waiting.postMessage('SKIP_WAITING');
    await changed;
  });
  assert.equal(await controllerVersion(), 'v2');
  console.log(`M006_UPDATE_PASS browser=${browser.version()} old=v1 waiting=v2 active=v2`);
} finally {
  await context.close();
  await browser.close();
  await new Promise(resolve => server.close(resolve));
}
