
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
