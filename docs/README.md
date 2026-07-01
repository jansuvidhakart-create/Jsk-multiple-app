
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
