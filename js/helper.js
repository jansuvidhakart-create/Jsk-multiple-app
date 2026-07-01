
/* helper.js - Utility helpers shared across modules */
export function safeQuery(selector, root = document) {
    return root.querySelector(selector);
}

export function getPageTitle(name) {
    return `${name} | JansuvidhaKart Digital Hub`;
}
