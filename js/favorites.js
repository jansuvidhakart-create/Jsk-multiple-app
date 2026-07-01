
/* favorites.js - Favorites management for pinned services */
import { loadItem, saveItem } from './storage.js';

export function getFavorites() {
    return loadItem('favorites', []);
}

export function addFavorite(app) {
    const favorites = getFavorites();
    const exists = favorites.some((item) => item.id === app.id);
    if (!exists) {
        favorites.unshift(app);
        saveItem('favorites', favorites);
    }
}

export function removeFavorite(appId) {
    const favorites = getFavorites().filter((item) => item.id !== appId);
    saveItem('favorites', favorites);
}
