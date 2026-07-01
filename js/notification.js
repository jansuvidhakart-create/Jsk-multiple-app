
/* notification.js - In-app notification management */
export function showNotification(message) {
    const notification = document.createElement('aside');
    notification.className = 'notification-toast';
    notification.textContent = message;
    document.body.appendChild(notification);
    requestAnimationFrame(() => notification.classList.add('visible'));
    setTimeout(() => notification.remove(), 3000);
}
