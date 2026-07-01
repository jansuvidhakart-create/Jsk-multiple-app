
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
