
/* theme.js - Theme switcher and preference persistence */
import { saveItem, loadItem } from './storage.js';

const KEY = 'theme';

export function initializeTheme(settings) {
    const currentTheme = loadItem(KEY, settings.theme || 'light');
    document.body.classList.toggle('theme-dark', currentTheme === 'dark');
    document.body.classList.toggle('theme-light', currentTheme === 'light');
    saveItem(KEY, currentTheme);
}

export function toggleTheme() {
    const isDark = document.body.classList.toggle('theme-dark');
    document.body.classList.toggle('theme-light', !isDark);
    saveItem(KEY, isDark ? 'dark' : 'light');
}
