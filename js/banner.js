
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
