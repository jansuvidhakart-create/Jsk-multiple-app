let apps = [];

const appContainer = document.getElementById("appContainer");
const search = document.getElementById("search");
const categoryBox = document.getElementById("categories");
const appShell = document.getElementById("appShell");
const assistantToggle = document.getElementById("assistantToggle");
const assistantPanel = document.getElementById("assistantPanel");
const assistantClose = document.getElementById("assistantClose");
const assistantForm = document.getElementById("assistantForm");
const assistantInput = document.getElementById("assistantInput");
const assistantMessages = document.getElementById("assistantMessages");

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
        const response = await fetch(`apps.json?t=${Date.now()}`, { cache: "no-store" });
        if (!response.ok) throw new Error("Failed to load apps.json");

        apps = await response.json();
        createCategories();
        renderApps(apps);
        initAssistant();
    } catch (e) {
        safeRender("<h3 style='text-align:center;padding:30px'>Apps Load Failed</h3>");
    }
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/\"/g, "&quot;");
}

function addAssistantMessage(text, type = "bot") {
    if (!assistantMessages) return;

    const bubble = document.createElement("div");
    bubble.className = `assistant-bubble ${type}`;
    bubble.innerHTML = escapeHtml(text).replace(/\n/g, "<br>");
    assistantMessages.appendChild(bubble);
    assistantMessages.scrollTop = assistantMessages.scrollHeight;
}

function getAppMatches(text) {
    if (!apps.length) return [];

    const query = text.toLowerCase();
    const words = query.split(/\s+/).filter(Boolean);

    return apps.filter(app => {
        const haystack = `${app.name} ${app.description} ${app.category}`.toLowerCase();
        return words.every(word => haystack.includes(word));
    }).slice(0, 4);
}

function getAssistantReply(text) {
    const query = text.trim().toLowerCase();

    if (!query) return "Please type a service name.";

    if (["hi", "hello", "hey", "namaste"].some(word => query.includes(word))) {
        return "Namaste! I can help you find government, finance, health, and education services in this app.";
    }

    if (["help", "what can you do", "services"].some(word => query.includes(word))) {
        return "I can help you find services like Aadhaar, PAN, passport, loan, scholarship, doctor booking, and more.";
    }

    const matches = getAppMatches(query);
    if (matches.length) {
        const list = matches.map(app => `• ${app.name}`).join("\n");
        return `I found these options for you:\n${list}\n\nTap any card to open the service.`;
    }

    if (query.includes("aadhaar")) return "Aadhaar Update is available under Government Services.";
    if (query.includes("pan")) return "PAN Card is available under Government Services.";
    if (query.includes("passport")) return "Passport is available under Government Services.";
    if (query.includes("loan")) return "Try Loan Apply from the Financial Services section.";
    if (query.includes("scholarship")) return "Try Scholarship from the Education & Exams section.";
    if (query.includes("doctor")) return "Try Doctor Booking from the Health Services section.";

    return "I did not find an exact match. Try a service name like Aadhaar, PAN, loan, scholarship, or doctor booking.";
}

function initAssistant() {
    if (!assistantToggle || !assistantPanel || !assistantClose || !assistantForm || !assistantInput || !assistantMessages) return;
    if (assistantMessages.dataset.ready === "true") return;

    assistantMessages.dataset.ready = "true";

    assistantToggle.addEventListener("click", () => {
        assistantPanel.classList.toggle("hidden");
        if (!assistantPanel.classList.contains("hidden")) {
            assistantInput.focus();
        }
    });

    assistantPanel.classList.remove("hidden");
    assistantPanel.style.display = "block";
    assistantToggle.style.display = "block";
    assistantInput.focus();

    assistantClose.addEventListener("click", () => {
        assistantPanel.classList.add("hidden");
    });

    assistantForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const query = assistantInput.value.trim();
        if (!query) return;

        addAssistantMessage(query, "user");
        assistantInput.value = "";
        addAssistantMessage(getAssistantReply(query), "bot");
    });

    addAssistantMessage("Hello! I can help you find services in this app. Try asking for Aadhaar, PAN, loan, scholarship, or doctor booking.", "bot");
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