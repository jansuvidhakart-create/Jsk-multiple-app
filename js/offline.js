
/* offline.js - Detect offline state and adapt the UI */
import { showNotification } from './notification.js';

export function initializeOffline() {
    window.addEventListener('offline', () => {
        showNotification('You are offline. Some services may be unavailable.');
    });
    window.addEventListener('online', () => {
        showNotification('Back online. Syncing updates.');
    });
}
