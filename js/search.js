
/* search.js - Search features for apps and page content */
import { renderSearchResults } from './ui.js';

export function initializeSearch(apps) {
    const input = document.querySelector('#searchInput');
    const results = document.querySelector('#searchResults');
    if (!input || !results) return;

    input.addEventListener('input', () => {
        const query = input.value.trim().toLowerCase();
        const filtered = filterApps(apps, query);
        renderSearchResults(filtered, results);
    });

    renderSearchResults(apps.slice(0, 6), results);
}

export function filterApps(apps, query) {
    if (!query) {
        return apps.slice(0, 12);
    }
    return apps.filter((app) => {
        return app.name.toLowerCase().includes(query) ||
            app.category.toLowerCase().includes(query) ||
            app.description.toLowerCase().includes(query);
    });
}
