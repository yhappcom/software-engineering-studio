document.title='M006_APP_READY';
window.registerSW=async()=>{await navigator.serviceWorker.register('/sw.js'); await navigator.serviceWorker.ready; if(!navigator.serviceWorker.controller){location.reload(); return;} document.title='M006_CONTROLLED';};
