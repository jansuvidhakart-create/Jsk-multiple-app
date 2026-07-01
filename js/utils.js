
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
