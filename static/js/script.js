// Your backend API
const API_URL = "https://emosphere-production.up.railway.app";

document.getElementById("analyzeBtn").addEventListener("click", async () => {
    
    const text = document.getElementById("userText").value.trim();
    const domain = document.getElementById("domain").value;
    const loading = document.getElementById("loading");

    if (!text) {
        alert("⚠️ Please enter some text.");
        return;
    }

    loading.style.display = "block";

    try {
        const res = await fetch(`${API_URL}/analyze`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text, domain })
        });

        if (!res.ok) throw new Error("Backend error");

        const result = await res.json();

        // Save to local storage
        localStorage.setItem("analysisResult", JSON.stringify(result));

        // Redirect to result page
        window.location.href = "result.html";

    } catch (error) {
        alert("❌ Backend error. Please try again.");
    }

    loading.style.display = "none";
});
