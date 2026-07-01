import os
import json
import textwrap

root = os.path.dirname(os.path.abspath(__file__))

folders = [
    'css',
    'js',
    'data',
    'pages',
    'docs',
    'assets/icons/category-icons',
    'assets/icons/app-icons',
    'assets/icons/banners',
    'assets/icons/logos',
    'assets/icons/images/animations',
    'assets/icons/fonts',
]
for folder in folders:
    os.makedirs(os.path.join(root, folder), exist_ok=True)

css_files = {
    'home.css': textwrap.dedent('''
        /* home.css - Entry point for the PWA stylesheet */
        /* This file imports the full component set for mobile-first styling. */
        @import url('variables.css');
        @import url('theme.css');
        @import url('dark.css');
        @import url('light.css');
        @import url('animation.css');
        @import url('header.css');
        @import url('footer.css');
        @import url('sidebar.css');
        @import url('cards.css');
        @import url('search.css');
        @import url('category.css');
        @import url('bottom-nav.css');
        @import url('buttons.css');
        @import url('responsive.css');

        :root {
            font-family: 'Inter', system-ui, sans-serif;
            min-height: 100%;
            background-color: var(--surface);
            color: var(--text-primary);
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            padding: 0;
            min-height: 100vh;
            background: var(--surface);
            color: var(--text-primary);
        }

        .app-shell {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            width: 100%;
            background: linear-gradient(180deg, var(--surface) 0%, var(--surface-alt) 100%);
        }

        .main-content {
            flex: 1;
            padding: 1rem;
            width: min(1200px, 100%);
            margin: 0 auto;
        }

        .section {
            margin-bottom: 1.6rem;
        }

        .section h2 {
            margin: 0 0 0.8rem;
            font-size: 1.2rem;
            letter-spacing: 0.01em;
            color: var(--text-heading);
        }

        .page-header {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            margin-bottom: 1rem;
        }

        .page-header h1 {
            margin: 0;
            font-size: clamp(1.8rem, 4vw, 2.75rem);
            line-height: 1.05;
        }

        .toast-message,
        .notification-toast {
            position: fixed;
            left: 50%;
            bottom: 2rem;
            transform: translateX(-50%) translateY(20px);
            background: rgba(15, 23, 42, 0.9);
            color: #fff;
            padding: 0.95rem 1.2rem;
            border-radius: 999px;
            box-shadow: 0 14px 35px rgba(15, 23, 42, 0.28);
            opacity: 0;
            pointer-events: none;
            transition: opacity var(--transition), transform var(--transition);
            z-index: 999;
        }

        .toast-message.visible,
        .notification-toast.visible {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
    '''),
    'variables.css': textwrap.dedent('''
        /* variables.css - Design tokens for spacing, typography, and colors */
        :root {
            --surface: #f7f8fc;
            --surface-alt: #ffffff;
            --primary: #1565c0;
            --primary-variant: #0d47a1;
            --secondary: #1e88e5;
            --success: #2e7d32;
            --warning: #f9a825;
            --danger: #d32f2f;
            --text-primary: #111827;
            --text-secondary: #4b5563;
            --text-muted: #6b7280;
            --text-heading: #1f2937;
            --border: rgba(15, 23, 42, 0.12);
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
            --radius: 22px;
            --radius-sm: 14px;
            --max-width: 1180px;
            --grid-gap: 1rem;
            --transition: 240ms ease-in-out;
        }

        .theme-dark {
            --surface: #0f172a;
            --surface-alt: #111827;
            --primary: #60a5fa;
            --secondary: #3b82f6;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --text-heading: #e2e8f0;
            --border: rgba(226, 232, 240, 0.12);
            --shadow: 0 24px 60px rgba(15, 23, 42, 0.35);
        }
    '''),
    'theme.css': textwrap.dedent('''
        /* theme.css - Shared theme helpers and adaptive styling */
        .theme-toggle {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            padding: 0.85rem 1rem;
            border: 1px solid var(--border);
            background: var(--surface-alt);
            color: var(--text-primary);
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all var(--transition);
            font-weight: 700;
        }

        .theme-toggle:hover,
        .theme-toggle:focus-visible {
            transform: translateY(-1px);
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
        }

        .badge {
            display: inline-flex;
            align-items: center;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            background: rgba(30, 64, 175, 0.12);
            color: var(--primary);
            font-size: 0.8rem;
            font-weight: 600;
        }
    '''),
    'animation.css': textwrap.dedent('''
        /* animation.css - Motion and transitions for polished UX */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .animate-fade-up {
            animation: fadeInUp 0.8s ease both;
        }

        .animate-pulse {
            animation: pulse 2.4s infinite ease-in-out;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.6; }
        }
    '''),
    'header.css': textwrap.dedent('''
        /* header.css - App shell header and toolbar styling */
        .header {
            position: sticky;
            top: 0;
            z-index: 50;
            background: rgba(255,255,255,0.96);
            backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--border);
        }

        .header-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            padding: 1rem;
            max-width: var(--max-width);
            margin: 0 auto;
        }

        .brand {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: -0.03em;
        }

        .brand::before {
            content: '📲';
            display: inline-flex;
            font-size: 1.25rem;
        }

        .search-bar {
            flex: 1;
            min-width: 0;
        }
    '''),
    'footer.css': textwrap.dedent('''
        /* footer.css - Bottom section and app information */
        .footer {
            padding: 1rem 1rem 2rem;
            max-width: var(--max-width);
            margin: 0 auto;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .footer .footer-links {
            display: grid;
            gap: 0.75rem;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            margin-top: 1rem;
        }

        .footer a {
            color: inherit;
            text-decoration: none;
        }
    '''),
    'sidebar.css': textwrap.dedent('''
        /* sidebar.css - Category drawer and quick access panel */
        .sidebar {
            display: grid;
            gap: 1rem;
            margin: 1rem 0;
        }

        .sidebar-card {
            padding: 1rem;
            border-radius: var(--radius);
            border: 1px solid var(--border);
            background: var(--surface-alt);
            box-shadow: var(--shadow);
        }
    '''),
    'cards.css': textwrap.dedent('''
        /* cards.css - Common card layouts for services and apps */
        .card-grid {
            display: grid;
            gap: 1rem;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        }

        .card {
            background: var(--surface-alt);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1rem;
            box-shadow: var(--shadow);
            transition: transform var(--transition), border-color var(--transition);
            cursor: pointer;
        }

        .card:hover,
        .card:focus-within {
            transform: translateY(-2px);
            border-color: rgba(59,130,246,0.3);
        }

        .card-icon {
            width: 3rem;
            height: 3rem;
            display: grid;
            place-items: center;
            border-radius: 18px;
            background: rgba(59,130,246,0.12);
            margin-bottom: 0.75rem;
            font-size: 1.35rem;
        }

        .card-title {
            font-size: 1rem;
            margin: 0 0 0.35rem;
            font-weight: 700;
        }

        .card-text {
            margin: 0;
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.55;
        }

        .banner-card {
            display: grid;
            gap: 0.75rem;
        }
    '''),
    'search.css': textwrap.dedent('''
        /* search.css - Search input styling for app and page search */
        .search-input {
            width: 100%;
            border-radius: 999px;
            border: 1px solid var(--border);
            padding: 0.95rem 1rem;
            font-size: 1rem;
            background: var(--surface-alt);
            color: var(--text-primary);
            outline: none;
            transition: border-color var(--transition), box-shadow var(--transition);
        }

        .search-input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(59,130,246,0.08);
        }

        .search-hint {
            display: block;
            margin-top: 0.5rem;
            color: var(--text-muted);
            font-size: 0.9rem;
        }
    '''),
    'category.css': textwrap.dedent('''
        /* category.css - Category tile layout for quick service access */
        .category-grid {
            display: grid;
            gap: 0.85rem;
            grid-template-columns: repeat(auto-fit, minmax(138px, 1fr));
        }

        .category-chip {
            display: inline-flex;
            align-items: center;
            gap: 0.65rem;
            padding: 0.9rem 1rem;
            border-radius: 18px;
            border: 1px solid var(--border);
            background: var(--surface-alt);
            color: var(--text-primary);
            text-decoration: none;
            transition: transform var(--transition), border-color var(--transition);
        }

        .category-chip:hover {
            transform: translateY(-1px);
            border-color: var(--primary);
        }
    '''),
    'bottom-nav.css': textwrap.dedent('''
        /* bottom-nav.css - Mobile bottom navigation bar */
        .bottom-nav {
            position: sticky;
            bottom: 0;
            width: 100%;
            background: var(--surface-alt);
            border-top: 1px solid var(--border);
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            place-items: center;
            padding: 0.75rem 0;
            z-index: 40;
        }

        .bottom-nav button {
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 0.9rem;
            display: grid;
            place-items: center;
            gap: 0.35rem;
            padding: 0.25rem 0;
            cursor: pointer;
        }

        .bottom-nav button.active,
        .bottom-nav button:hover {
            color: var(--primary);
        }
    '''),
    'buttons.css': textwrap.dedent('''
        /* buttons.css - Primary and secondary button styles */
        .button,
        .button-secondary {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            border: none;
            cursor: pointer;
            transition: transform var(--transition), box-shadow var(--transition);
        }

        .button {
            padding: 0.9rem 1.2rem;
            color: #fff;
            background: var(--primary);
            box-shadow: 0 10px 25px rgba(59, 130, 246, 0.18);
        }

        .button-secondary {
            background: var(--surface-alt);
            border: 1px solid var(--border);
            color: var(--text-primary);
        }

        .button:hover,
        .button-secondary:hover {
            transform: translateY(-1px);
        }
    '''),
    'dark.css': textwrap.dedent('''
        /* dark.css - Dark theme overrides for the PWA */
        .theme-dark body,
        .theme-dark .app-shell,
        .theme-dark .header,
        .theme-dark .card,
        .theme-dark .sidebar-card,
        .theme-dark .bottom-nav,
        .theme-dark .footer {
            background: var(--surface);
            color: var(--text-primary);
        }

        .theme-dark .search-input,
        .theme-dark .button-secondary {
            background: #1f2937;
            border-color: rgba(255,255,255,0.08);
            color: #e2e8f0;
        }
    '''),
    'light.css': textwrap.dedent('''
        /* light.css - Light theme enhancements for readability */
        .theme-light body,
        .theme-light .app-shell,
        .theme-light .header,
        .theme-light .card,
        .theme-light .sidebar-card,
        .theme-light .bottom-nav,
        .theme-light .footer {
            background: var(--surface-alt);
            color: var(--text-primary);
        }

        .theme-light .search-input,
        .theme-light .button-secondary {
            background: #ffffff;
            border-color: var(--border);
            color: var(--text-primary);
        }
    '''),
    'responsive.css': textwrap.dedent('''
        /* responsive.css - Mobile-first responsive breakpoints */
        @media (min-width: 640px) {
            .header-inner {
                padding: 1.25rem 1.5rem;
            }

            .main-content {
                padding: 1.5rem;
            }
        }

        @media (min-width: 900px) {
            .main-content {
                padding: 2rem;
            }
        }

        @media (min-width: 1100px) {
            .header-inner {
                gap: 1.5rem;
            }
        }
    '''),
}
for filename, content in css_files.items():
    with open(os.path.join(root, 'css', filename), 'w', encoding='utf-8') as f:
        f.write(content)

js_files = {
    'app.js': textwrap.dedent('''
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
    '''),
    'search.js': textwrap.dedent('''
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
    '''),
    'navigation.js': textwrap.dedent('''
        /* navigation.js - Handles page routing and menu interactions */
        import { showToast } from './ui.js';

        export function initializeNavigation() {
            const navButtons = document.querySelectorAll('[data-nav]');
            navButtons.forEach((button) => {
                button.addEventListener('click', () => {
                    const target = button.dataset.nav;
                    navigateTo(target);
                });
            });
        }

        export function navigateTo(page) {
            const targetUrl = page === 'home' ? './index.html' : `./pages/${page}.html`;
            showToast(`Navigating to ${page}`);
            window.location.href = targetUrl;
        }
    '''),
    'category.js': textwrap.dedent('''
        /* category.js - Category tiles and quick access sections */
        import { createCategoryChip } from './ui.js';

        export function initializeCategories(categories) {
            const container = document.querySelector('#categoryGrid');
            if (!container) return;
            categories.forEach((category) => {
                const chip = createCategoryChip(category);
                container.appendChild(chip);
            });
        }
    '''),
    'ui.js': textwrap.dedent('''
        /* ui.js - Reusable UI helpers and render helpers */
        export function createCategoryChip(category) {
            const link = document.createElement('a');
            link.href = '#';
            link.className = 'category-chip';
            link.innerHTML = `<span>${category.icon}</span><span>${category.title}</span>`;
            link.title = category.description;
            return link;
        }

        export function renderSearchResults(apps, container) {
            container.innerHTML = '';
            if (!apps.length) {
                container.innerHTML = '<p class="search-hint">No matching services found.</p>';
                return;
            }
            apps.forEach((app) => {
                const card = document.createElement('article');
                card.className = 'card animate-fade-up';
                card.innerHTML = `
                    <div class="card-icon">${app.icon}</div>
                    <h3 class="card-title">${app.name}</h3>
                    <p class="card-text">${app.description}</p>
                `;
                card.addEventListener('click', () => {
                    window.open(app.url, '_blank');
                });
                container.appendChild(card);
            });
        }

        export function showToast(message, duration = 1600) {
            const toast = document.createElement('div');
            toast.className = 'toast-message';
            toast.textContent = message;
            document.body.appendChild(toast);
            requestAnimationFrame(() => toast.classList.add('visible'));
            setTimeout(() => toast.remove(), duration);
        }
    '''),
    'storage.js': textwrap.dedent('''
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
    '''),
    'favorites.js': textwrap.dedent('''
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
    '''),
    'recent.js': textwrap.dedent('''
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
    '''),
    'banner.js': textwrap.dedent('''
        /* banner.js - Banner hero display and promotional content */
        export function renderBanners(banners, container) {
            container.innerHTML = '';
            banners.forEach((banner) => {
                const card = document.createElement('section');
                card.className = 'card banner-card';
                card.innerHTML = `
                    <div class="banner-content">
                        <span class="badge">${banner.badge}</span>
                        <h3 class="card-title">${banner.title}</h3>
                        <p class="card-text">${banner.subtitle}</p>
                    </div>
                `;
                container.appendChild(card);
            });
        }
    '''),
    'slider.js': textwrap.dedent('''
        /* slider.js - Horizontal slider support for featured content */
        export function createSlider(container) {
            if (!container) return;
            container.classList.add('slider');
        }
    '''),
    'notification.js': textwrap.dedent('''
        /* notification.js - In-app notification management */
        export function showNotification(message) {
            const notification = document.createElement('aside');
            notification.className = 'notification-toast';
            notification.textContent = message;
            document.body.appendChild(notification);
            requestAnimationFrame(() => notification.classList.add('visible'));
            setTimeout(() => notification.remove(), 3000);
        }
    '''),
    'theme.js': textwrap.dedent('''
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
    '''),
    'offline.js': textwrap.dedent('''
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
    '''),
    'voice.js': textwrap.dedent('''
        /* voice.js - Voice input and speech search support */
        export function initializeVoice() {
            const voiceToggle = document.querySelector('#voiceSearch');
            const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!voiceToggle || !Recognition) return;

            const recognition = new Recognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            voiceToggle.addEventListener('click', () => {
                recognition.start();
            });

            recognition.addEventListener('result', (event) => {
                const query = event.results[0][0].transcript;
                const input = document.querySelector('#searchInput');
                if (input) {
                    input.value = query;
                    input.dispatchEvent(new Event('input'));
                }
            });
        }
    '''),
    'helper.js': textwrap.dedent('''
        /* helper.js - Utility helpers shared across modules */
        export function safeQuery(selector, root = document) {
            return root.querySelector(selector);
        }

        export function getPageTitle(name) {
            return `${name} | JansuvidhaKart Digital Hub`;
        }
    '''),
    'utils.js': textwrap.dedent('''
        /* utils.js - Common utilities for fetching and parsing data */
        export async function fetchJson(path) {
            try {
                const response = await fetch(path, { cache: 'no-store' });
                if (!response.ok) {
                    throw new Error(`Unable to load ${path}`);
                }
                return response.json();
            } catch (error) {
                console.error(error);
                return [];
            }
        }
    '''),
}
for filename, content in js_files.items():
    with open(os.path.join(root, 'js', filename), 'w', encoding='utf-8') as f:
        f.write(content)

page_template = textwrap.dedent('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
        <title>{title} | JansuvidhaKart Digital Hub</title>
        <meta name="description" content="{description}">
        <link rel="manifest" href="../manifest.json">
        <link rel="stylesheet" href="../css/home.css">
        <meta name="theme-color" content="#1565c0">
    </head>
    <body class="theme-light">
        <div class="app-shell">
            <header class="header">
                <div class="header-inner">
                    <div class="brand">JansuvidhaKart</div>
                    <div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
                        <button class="theme-toggle" type="button" onclick="window.location.href='../index.html'">Home</button>
                        <button class="theme-toggle" type="button" onclick="window.location.reload();">Refresh</button>
                    </div>
                </div>
            </header>
            <main class="main-content">
                <section class="section page-header">
                    <div>
                        <h1>{title}</h1>
                        <p class="search-hint">{description}</p>
                    </div>
                </section>
                <section class="section card-grid">
                    <article class="card">
                        <h2>Scalable Page Layout</h2>
                        <p class="card-text">This page is part of a clean PWA architecture built with mobile-first HTML, CSS, and JavaScript.</p>
                    </article>
                    <article class="card">
                        <h2>Material-inspired Design</h2>
                        <p class="card-text">Consistent spacing, accessible typography, and lightweight interactive patterns.</p>
                    </article>
                </section>
            </main>
            <footer class="footer">
                <div class="footer-links">
                    <a href="../pages/about.html">About</a>
                    <a href="../pages/contact.html">Contact</a>
                    <a href="../pages/privacy.html">Privacy</a>
                    <a href="../pages/terms.html">Terms</a>
                </div>
            </footer>
        </div>
        <script type="module" src="../js/app.js"></script>
    </body>
    </html>
''')

pages = [
    ('home', 'Welcome to JansuvidhaKart', 'A digital services super app for government, banking, education, health, and more.'),
    ('category', 'Category Overview', 'Browse services grouped by category for fast access.'),
    ('app', 'Service Details', 'View details of a digital service with navigation points.'),
    ('search', 'Search Services', 'Search across all digital services and discover recommendations.'),
    ('favorites', 'Your Favorites', 'Keep your most used services in one place for quick access.'),
    ('recent', 'Recent Activity', 'Review recently visited services and continue where you left off.'),
    ('settings', 'Settings', 'Manage your preferences, theme, and app behavior.'),
    ('profile', 'My Profile', 'Update profile details and personalize your Digital Hub account.'),
    ('about', 'About the Digital Hub', 'Learn more about JansuvidhaKart and its mission to simplify digital services.'),
    ('contact', 'Contact Support', 'Reach out for help with services, onboarding, and technical issues.'),
    ('privacy', 'Privacy Policy', 'Understand how your data is protected and used in the app.'),
    ('terms', 'Terms & Conditions', 'Review the usage terms for the JansuvidhaKart Digital Hub.'),
]
for name, title, description in pages:
    with open(os.path.join(root, 'pages', f'{name}.html'), 'w', encoding='utf-8') as f:
        f.write(page_template.format(title=title, description=description))

apps_data = [
    {"id": 1, "name": "Aadhaar Services", "category": "Government Services", "icon": "🆔", "description": "Access Aadhaar updates, enrollment and verification.", "url": "https://uidai.gov.in/", "featured": True, "version": "1.0"},
    {"id": 2, "name": "Digital Banking", "category": "Banking", "icon": "🏦", "description": "Open accounts, pay bills and view statements with ease.", "url": "https://www.onlinesbi.sbi/", "featured": True, "version": "1.1"},
    {"id": 3, "name": "Scholarship Finder", "category": "Education", "icon": "🎓", "description": "Browse scholarships, grants and student support programs.", "url": "https://scholarships.gov.in/", "featured": False, "version": "1.0"},
    {"id": 4, "name": "Health Checkup", "category": "Health", "icon": "🩺", "description": "Schedule telemedicine appointments and wellness services.", "url": "https://health.gov.in/", "featured": False, "version": "1.0"},
    {"id": 5, "name": "Farming Support", "category": "Agriculture", "icon": "🌾", "description": "Find crop guidance, subsidies and market price alerts.", "url": "https://www.digitalindia.gov.in/", "featured": False, "version": "1.0"},
    {"id": 6, "name": "Utility Bills", "category": "Utilities", "icon": "💡", "description": "Pay electricity, gas, water and municipal bills securely.", "url": "https://www.billplz.com/", "featured": True, "version": "1.1"},
    {"id": 7, "name": "AI Assistant", "category": "AI Tools", "icon": "🤖", "description": "Get instant answers, productivity tools and workflow automation.", "url": "https://openai.com/", "featured": False, "version": "1.2"},
    {"id": 8, "name": "Business Support", "category": "Business Services", "icon": "📊", "description": "Register businesses, check compliance, and manage digital documentation.", "url": "https://www.mygov.in/", "featured": False, "version": "1.0"},
    {"id": 9, "name": "Travel Planner", "category": "Travel", "icon": "✈️", "description": "Plan trips, book tickets and monitor travel updates.", "url": "https://www.indianrail.gov.in/", "featured": False, "version": "1.0"},
    {"id": 10, "name": "Jobs Board", "category": "Jobs", "icon": "💼", "description": "Search government and private job listings from one dashboard.", "url": "https://www.ncs.gov.in/", "featured": False, "version": "1.0"},
]
with open(os.path.join(root, 'data', 'apps.json'), 'w', encoding='utf-8') as f:
    json.dump(apps_data, f, indent=2)

categories_data = [
    {"id": 1, "title": "Government Services", "icon": "🏛️", "description": "Official public services and citizen portals."},
    {"id": 2, "title": "Banking", "icon": "🏦", "description": "Digital banking, payments and financial services."},
    {"id": 3, "title": "Education", "icon": "🎓", "description": "Courses, scholarships and student resources."},
    {"id": 4, "title": "Health", "icon": "🩺", "description": "Healthcare access, insurance and telemedicine."},
    {"id": 5, "title": "Agriculture", "icon": "🌾", "description": "Farming support, market data and subsidies."},
    {"id": 6, "title": "Utilities", "icon": "💡", "description": "Manage bills, recharge and essential services."},
    {"id": 7, "title": "AI Tools", "icon": "🤖", "description": "Productivity helpers, chat and automation tools."},
    {"id": 8, "title": "Travel", "icon": "✈️", "description": "Booking, tickets and travel planning."},
]
with open(os.path.join(root, 'data', 'categories.json'), 'w', encoding='utf-8') as f:
    json.dump(categories_data, f, indent=2)

banners_data = [
    {"id": 1, "title": "Digital Services Super App", "subtitle": "One place for government, banking, education, health and utility services.", "badge": "Launch"},
    {"id": 2, "title": "Secure and Accessible", "subtitle": "Mobile-first design with offline-ready PWA support.", "badge": "Secure"},
]
with open(os.path.join(root, 'data', 'banners.json'), 'w', encoding='utf-8') as f:
    json.dump(banners_data, f, indent=2)

featured_data = [
    {"id": 1, "type": "app", "name": "Aadhaar Services"},
    {"id": 2, "type": "app", "name": "Digital Banking"},
    {"id": 6, "type": "app", "name": "Utility Bills"},
]
with open(os.path.join(root, 'data', 'featured.json'), 'w', encoding='utf-8') as f:
    json.dump(featured_data, f, indent=2)

updates_data = [
    {"id": 1, "title": "New Service Added", "message": "AI Assistant and Health Checkup are now available.", "date": "2026-07-01"},
    {"id": 2, "title": "Offline Ready", "message": "Landing pages can now load while offline.", "date": "2026-06-30"},
]
with open(os.path.join(root, 'data', 'updates.json'), 'w', encoding='utf-8') as f:
    json.dump(updates_data, f, indent=2)

settings_data = {
    "theme": "light",
    "language": "en",
    "region": "India",
    "enableVoice": True,
    "showTutorial": False,
}
with open(os.path.join(root, 'data', 'settings.json'), 'w', encoding='utf-8') as f:
    json.dump(settings_data, f, indent=2)

index_html = textwrap.dedent('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
        <title>JansuvidhaKart Digital Hub</title>
        <meta name="description" content="A Progressive Web App to access government, banking, education, health and digital services.">
        <link rel="manifest" href="./manifest.json">
        <link rel="stylesheet" href="./css/home.css">
        <meta name="theme-color" content="#1565c0">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="JansuvidhaKart Digital Hub">
        <link rel="apple-touch-icon" href="./assets/icons/icon-192.svg">
    </head>
    <body class="theme-light">
        <div class="app-shell">
            <header class="header">
                <div class="header-inner">
                    <div class="brand">JansuvidhaKart</div>
                    <button class="theme-toggle" type="button" onclick="window.location.reload();">Refresh</button>
                </div>
            </header>
            <main class="main-content">
                <section class="section page-header">
                    <div>
                        <h1>JansuvidhaKart Digital Hub</h1>
                        <p class="search-hint">Explore government services, banking, education, health, agriculture, travel and more from one responsive PWA.</p>
                    </div>
                </section>
                <section class="section">
                    <input id="searchInput" class="search-input" type="search" placeholder="Search services, categories or tools..." autocomplete="off">
                    <p class="search-hint">Use keywords like Aadhaar, loan, scholarship, health or recharge.</p>
                </section>
                <section class="section">
                    <div class="category-grid" id="categoryGrid"></div>
                </section>
                <section class="section">
                    <h2>Featured Services</h2>
                    <div id="searchResults" class="card-grid"></div>
                </section>
            </main>
            <nav class="bottom-nav">
                <button data-nav="home">Home</button>
                <button data-nav="favorites">Favorites</button>
                <button data-nav="recent">Recent</button>
                <button data-nav="settings">Settings</button>
            </nav>
            <footer class="footer">
                <p>Digital services hub built as a lightweight PWA with clean folder architecture.</p>
            </footer>
        </div>
        <script type="module" src="./js/app.js"></script>
    </body>
    </html>
''')
with open(os.path.join(root, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

manifest = {
    "name": "JansuvidhaKart Digital Hub",
    "short_name": "JansuvidhaKart",
    "description": "A Progressive Web App for government services, banking, education, health, and utilities.",
    "start_url": "./index.html",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#1565c0",
    "scope": "./",
    "orientation": "portrait-primary",
    "icons": [
        {"src": "./assets/icons/icon-192.svg", "sizes": "192x192", "type": "image/svg+xml", "purpose": "any"},
        {"src": "./assets/icons/icon-512.svg", "sizes": "512x512", "type": "image/svg+xml", "purpose": "any"}
    ],
    "categories": ["business", "education", "finance", "health", "travel"],
}
with open(os.path.join(root, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)

sw_content = textwrap.dedent('''
    /* sw.js - Service worker for offline caching and PWA readiness */
    const CACHE_NAME = 'jansk-digital-hub-v1';
    const ASSETS = [
        './',
        './index.html',
        './manifest.json',
        './css/home.css',
        './js/app.js',
        './data/apps.json',
        './data/categories.json',
        './data/banners.json',
        './data/featured.json',
        './data/settings.json',
    ];

    self.addEventListener('install', (event) => {
        event.waitUntil(
            caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
        );
        self.skipWaiting();
    });

    self.addEventListener('activate', (event) => {
        event.waitUntil(
            caches.keys().then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheName !== CACHE_NAME) {
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
        );
        self.clients.claim();
    });

    self.addEventListener('fetch', (event) => {
        if (event.request.method !== 'GET') {
            return;
        }
        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                if (cachedResponse) {
                    return cachedResponse;
                }
                return fetch(event.request)
                    .then((networkResponse) => {
                        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
                            return networkResponse;
                        }
                        const copy = networkResponse.clone();
                        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
                        return networkResponse;
                    })
                    .catch(() => caches.match('./index.html'));
            })
        );
    });
''')
with open(os.path.join(root, 'sw.js'), 'w', encoding='utf-8') as f:
    f.write(sw_content)

readme_root = textwrap.dedent('''
    # JansuvidhaKart Digital Hub

    A clean Progressive Web App scaffold for a digital services super app that provides access to government services, banking, education, health, agriculture, utilities, AI tools, business services, travel, jobs, documentation, recharge, and finance.

    ## Project structure
    - `index.html`: Primary app shell and landing page.
    - `manifest.json`: PWA metadata for installable behavior.
    - `sw.js`: Service worker for offline caching and asset delivery.
    - `css/`: Modular CSS files for mobile-first responsive design.
    - `js/`: ES6 modules for app startup, search, navigation, theme, offline handling, and utilities.
    - `data/`: Sample JSON data for apps, categories, banners, featured content, updates, and app settings.
    - `pages/`: Independent HTML pages for app routes and informational content.
    - `assets/`: Placeholder folders for icons, banners, logos, images, fonts, and animations.
    - `docs/README.md`: Detailed documentation of folder purpose and architecture.

    ## Key features
    - Mobile-first responsive layout
    - Material-inspired UI patterns
    - Dark and light theme support
    - Progressive Web App ready
    - Pure HTML, CSS, and JavaScript
    - Clean folder architecture for scalability

    ## How to use
    1. Open `index.html` in a browser or a local server.
    2. Add app and category data in `data/apps.json` and `data/categories.json`.
    3. Extend UI components by editing CSS files inside `css/`.
    4. Add new pages under `pages/` and reference them from navigation.
''')
with open(os.path.join(root, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(readme_root)

readme_docs = textwrap.dedent('''
    # Project Architecture

    This repository implements a production-ready Progressive Web App structure for `JansuvidhaKart Digital Hub`.

    ## Folder purpose

    - `css/`
      - `home.css`: Root stylesheet with imports for component styles.
      - `variables.css`: Shared CSS variables and theme tokens.
      - `theme.css`: Theme helpers and button styling.
      - `dark.css`, `light.css`: Theme-specific overrides.
      - Component files: `header.css`, `footer.css`, `sidebar.css`, `cards.css`, `search.css`, `category.css`, `bottom-nav.css`, `buttons.css`, `responsive.css`, `animation.css`.

    - `js/`
      - `app.js`: Main entrypoint that initializes app state.
      - `search.js`: Search filtering and result rendering.
      - `navigation.js`: Page navigation and routing.
      - `category.js`: Category tile rendering.
      - `ui.js`: Shared DOM render helpers.
      - `storage.js`: Local storage utilities.
      - `favorites.js`, `recent.js`: Favorites and recent activity management.
      - `banner.js`, `slider.js`, `notification.js`: UI component helpers.
      - `theme.js`: Theme toggling and persistence.
      - `offline.js`: Offline detection and notification.
      - `voice.js`: Voice search support.
      - `helper.js`, `utils.js`: Utility helpers for DOM and data fetching.

    - `data/`
      - `apps.json`: Sample digital service entries.
      - `categories.json`: Sample category definitions.
      - `banners.json`: Promotional banner content.
      - `featured.json`: Featured services data.
      - `updates.json`: Release notes and version history.
      - `settings.json`: Default preferences and theme info.

    - `pages/`
      - Static HTML pages for additional routes and app content.
      - Includes `home`, `category`, `app`, `search`, `favorites`, `recent`, `settings`, `profile`, `about`, `contact`, `privacy`, and `terms`.

    - `assets/`
      - Placeholder asset directories for icons, category icons, app icons, banners, logos, images, animations, and fonts.

    ## Notes

    - The app uses pure web standards with no frameworks.
    - The service worker caches core assets for offline support.
    - Theme variables support dark and light modes through CSS.
    - The folder architecture is designed for maintainability and scalability.
''')
with open(os.path.join(root, 'docs', 'README.md'), 'w', encoding='utf-8') as f:
    f.write(readme_docs)

svg_icon = textwrap.dedent('''
    <svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
      <rect width="512" height="512" rx="96" fill="#1565c0"/>
      <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" font-family="system-ui, sans-serif" font-size="160" fill="#ffffff">JSK</text>
    </svg>
''')
for size in ['icon-192.svg', 'icon-512.svg']:
    with open(os.path.join(root, 'assets/icons', size), 'w', encoding='utf-8') as f:
        f.write(svg_icon)

for folder in folders[5:]:
    gitkeep_path = os.path.join(root, folder, '.gitkeep')
    with open(gitkeep_path, 'w', encoding='utf-8') as f:
        f.write('# placeholder for assets')

print('Scaffold created and files updated successfully.')
