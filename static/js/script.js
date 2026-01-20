const analyzeBtn = document.getElementById("analyzeBtn");
const userText = document.getElementById("userText");
const domainSelect = document.getElementById("domain");
const loader = document.getElementById("loader");

// ✅ LIVE BACKEND URL
const API_URL = "https://emosphere-production.up.railway.app/analyze";

analyzeBtn.addEventListener("click", async () => {
    const text = userText.value.trim();
    const domain = domainSelect.value;

    if (!text) {
        alert("⚠️ Please enter some text before analyzing!");
        return;
    }

    loader.classList.remove("hidden");

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                domain: domain
            })
        });

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();

        localStorage.setItem("emotionData", JSON.stringify(data));

        loader.classList.add("hidden");
        window.location.href = "result.html";

    } catch (error) {
        loader.classList.add("hidden");
        alert("❌ Backend error. Please try again.");
        console.error(error);
    }
});
