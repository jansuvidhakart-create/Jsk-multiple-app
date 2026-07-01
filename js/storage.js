
/* storage.js - Local storage manager for favorites and preferences */
const keys = {
    favorites: 'jskfh_favorites',
    recent: 'jskfh_recent',
    theme: 'jskfh_theme',
};

export function saveItem(key, value) {
    localStorage.setItem(keys[key], JSON.stringify(value));
}

export function loadItem(key, fallback = null) {
    try {
        const item = localStorage.getItem(keys[key]);
        return item ? JSON.parse(item) : fallback;
    } catch (error) {
        return fallback;
    }
}

export function clearItem(key) {
    localStorage.removeItem(keys[key]);
}
