
/* recent.js - Recent activity tracking for service visits */
import { loadItem, saveItem } from './storage.js';

const KEY = 'recent';

export function getRecent() {
    return loadItem(KEY, []);
}

export function addRecent(app) {
    const recent = getRecent();
    const filtered = recent.filter((item) => item.id !== app.id);
    filtered.unshift({ ...app, visitedAt: new Date().toISOString() });
    saveItem(KEY, filtered.slice(0, 12));
}
