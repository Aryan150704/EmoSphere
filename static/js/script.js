// Backend URL
const API_URL = "https://emosphere-production.up.railway.app";

// Detect current page
const page = window.location.pathname;

// ---------------------------------------
// 1️⃣ INDEX PAGE
// ---------------------------------------
if (page.endsWith("index.html") || page === "/" || page === "/EmoSphere/") {

    document.getElementById("analyzeBtn").addEventListener("click", async () => {

        const text = document.getElementById("userText").value.trim();
        const domain = document.getElementById("domain").value;
        const loading = document.getElementById("loading");

        if (!text) {
            alert("Please enter some text.");
            return;
        }

        loading.style.display = "block";

        try {
            const response = await fetch(`${API_URL}/analyze`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text, domain })
            });

            const data = await response.json();

            localStorage.setItem("analysisResult", JSON.stringify(data));

            window.location.href = "result.html";

        } catch (err) {
            alert("❌ Backend error. Please try again.");
        }

        loading.style.display = "none";
    });
}



// ---------------------------------------
// 2️⃣ RESULT PAGE
// ---------------------------------------
if (page.endsWith("result.html")) {

    const data = JSON.parse(localStorage.getItem("analysisResult"));

    if (!data) {
        alert("No result found. Please analyze again.");
        window.location.href = "index.html";
    }

    // Fill result values
    document.getElementById("mainEmotion").textContent = data.main_emotion || "Not detected";
    document.getElementById("summary").textContent = data.summary || "No summary available.";
    document.getElementById("domainUsed").textContent = data.domain || "General";

    const ul = document.getElementById("emotionScores");
    ul.innerHTML = "";

    for (let [emotion, score] of Object.entries(data.scores)) {
        const li = document.createElement("li");
        li.textContent = `${emotion}: ${score}`;
        ul.appendChild(li);
    }

    document.getElementById("backBtn").addEventListener("click", () => {
        window.location.href = "index.html";
    });
}
