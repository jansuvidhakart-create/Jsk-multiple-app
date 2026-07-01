
/* app.js - Main application shell that initializes the Digital Hub */
import { initializeSearch } from './search.js';
import { initializeNavigation } from './navigation.js';
import { initializeCategories } from './category.js';
import { initializeTheme } from './theme.js';
import { initializeOffline } from './offline.js';
import { initializeVoice } from './voice.js';
import { fetchJson } from './utils.js';

const state = {
    apps: [],
    categories: [],
    banners: [],
    featured: [],
    settings: {},
};

async function loadAppData() {
    state.apps = await fetchJson('./data/apps.json');
    state.categories = await fetchJson('./data/categories.json');
    state.banners = await fetchJson('./data/banners.json');
    state.featured = await fetchJson('./data/featured.json');
    state.settings = await fetchJson('./data/settings.json');
}

async function init() {
    await loadAppData();
    initializeTheme(state.settings);
    initializeNavigation();
    initializeCategories(state.categories);
    initializeSearch(state.apps);
    initializeOffline();
    initializeVoice();
    document.body.classList.add(state.settings.theme === 'dark' ? 'theme-dark' : 'theme-light');
}

document.addEventListener('DOMContentLoaded', init);
