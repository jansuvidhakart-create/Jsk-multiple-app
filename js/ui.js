
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
