const CACHE = 'm006-cold-v1';
const SHELL = '/cold.html';
const PAYLOAD = '/payload.txt';
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll([SHELL, PAYLOAD])).then(() => self.skipWaiting()));
});
self.addEventListener('activate', event => event.waitUntil(self.clients.claim()));
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (event.request.mode === 'navigate') {
    event.respondWith(caches.match(SHELL).then(hit => hit || fetch(event.request)));
    return;
  }
  if (url.pathname === PAYLOAD) {
    event.respondWith(caches.match(PAYLOAD).then(hit => hit || fetch(event.request)));
  }
});
