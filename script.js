let apps = [];

const appContainer = document.getElementById("appContainer");
const search = document.getElementById("search");
const categoryBox = document.getElementById("categories");
const appShell = document.getElementById("appShell");

function safeRender(message) {
    if (appContainer) {
        appContainer.innerHTML = message;
    }
}

function showApp() {
    if (!apps.length) {
        loadApps();
    } else {
        createCategories();
        renderApps(apps);
    }
}

async function loadApps() {
    try {
        const response = await fetch("apps.json");
        if (!response.ok) throw new Error("Failed to load apps.json");

        apps = await response.json();
        createCategories();
        renderApps(apps);
    } catch (e) {
        safeRender("<h3 style='text-align:center;padding:30px'>Apps Load Failed</h3>");
    }
}

                                                            function createCategories() {
    if (!categoryBox) return;

    const categories = ["All", ...new Set(apps.map(app => app.category))];
    categoryBox.innerHTML = "";

    categories.forEach(category => {
        const btn = document.createElement("div");
        btn.className = "category";

        if (category === "All") {
            btn.classList.add("active");
        }

        btn.textContent = category;
        btn.onclick = () => {
            document.querySelectorAll(".category").forEach(x => x.classList.remove("active"));
            btn.classList.add("active");

            if (category === "All") {
                renderApps(apps);
            } else {
                renderApps(apps.filter(app => app.category === category));
            }
        };

        categoryBox.appendChild(btn);
    });
}

                                                                                                                                                                                                                                                                                                                function renderApps(data) {
    if (!appContainer) return;

    appContainer.innerHTML = "";

    data.forEach(app => {
        appContainer.innerHTML += `
            <a class="card" href="${app.url}" target="_blank" rel="noopener noreferrer">
                <div class="icon">${app.icon}</div>
                <h3>${app.name}</h3>
                <p>${app.category}</p>
            </a>
        `;
    });
}

if (search) {
    search.addEventListener("input", () => {
        const text = search.value.toLowerCase();
        const active = document.querySelector(".category.active")?.textContent || "All";

        let filtered = apps.filter(app => app.name.toLowerCase().includes(text));

        if (active !== "All") {
            filtered = filtered.filter(app => app.category === active);
        }

        renderApps(filtered);
    });
}

// Auto-load app on page load
window.addEventListener('DOMContentLoaded', () => {
    showApp();
});