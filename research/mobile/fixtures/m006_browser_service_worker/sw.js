const CACHE = 'm006-v1';
const PAYLOAD = '/payload.txt';
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.add(PAYLOAD)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', event => event.waitUntil(self.clients.claim()));
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (url.pathname === PAYLOAD) {
    event.respondWith(caches.match(PAYLOAD).then(hit => hit || fetch(event.request)));
  }
});
