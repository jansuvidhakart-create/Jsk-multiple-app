let apps = [];

const appContainer = document.getElementById("appContainer");
const search = document.getElementById("search");
const categoryBox = document.getElementById("categories");
const appShell = document.getElementById("appShell");
const loginScreen = document.getElementById("loginScreen");
const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const loginError = document.getElementById("loginError");
const registerMessage = document.getElementById("registerMessage");
const logoutBtn = document.getElementById("logoutBtn");

const STORAGE_KEY = "jsk-users";
const AUTH_KEY = "jsk-auth";
const ONE_YEAR_MS = 365 * 24 * 60 * 60 * 1000;

function getUsers() {
    try {
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    } catch {
        return [];
    }
}

function saveUsers(users) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(users));
}

function createUser(id, password, name) {
    return {
        id,
        password,
        name,
        createdAt: Date.now(),
        expiresAt: Date.now() + ONE_YEAR_MS,
    };
}

function isUserValid(user) {
    return user && user.expiresAt > Date.now();
}

function safeRender(message) {
    if (appContainer) {
        appContainer.innerHTML = message;
    }
}

function showApp() {
    loginScreen?.classList.add("hidden");
    appShell?.classList.remove("hidden");

    if (!apps.length) {
        loadApps();
    } else {
        createCategories();
        renderApps(apps);
    }
}

function showLogin() {
    appShell?.classList.add("hidden");
    loginScreen?.classList.remove("hidden");
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

if (loginForm) {
    loginForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const userId = document.getElementById("loginId")?.value.trim() || "";
        const password = document.getElementById("loginPassword")?.value || "";
        const users = getUsers();
        const user = users.find(u => u.id === userId);

        if (user && user.password === password && isUserValid(user)) {
            sessionStorage.setItem(AUTH_KEY, JSON.stringify({ id: user.id, name: user.name, expiresAt: user.expiresAt }));
            loginError.textContent = "";
            showApp();
        } else {
            loginError.textContent = "Incorrect ID or password or access expired";
        }
    });
}

if (registerForm) {
    registerForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const name = document.getElementById("registerName")?.value.trim() || "";
        const userId = document.getElementById("registerId")?.value.trim() || "";
        const password = document.getElementById("registerPassword")?.value || "";

        if (!name || !userId || !password) {
            registerMessage.textContent = "Please fill all fields";
            return;
        }

        const users = getUsers();
        if (users.some(u => u.id === userId)) {
            registerMessage.textContent = "This ID is already taken";
            return;
        }

        users.push(createUser(userId, password, name));
        saveUsers(users);
        registerMessage.textContent = "Registration successful! You can now login.";
        registerForm.reset();
    });
}

if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
        sessionStorage.removeItem(AUTH_KEY);
        showLogin();
    });
}

if (sessionStorage.getItem(AUTH_KEY)) {
    const auth = JSON.parse(sessionStorage.getItem(AUTH_KEY) || "{}");
    if (auth.expiresAt && auth.expiresAt > Date.now()) {
        showApp();
    } else {
        sessionStorage.removeItem(AUTH_KEY);
        showLogin();
    }
} else {
    showLogin();
}