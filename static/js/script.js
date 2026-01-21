// ======================================
// 2️⃣ RESULT PAGE
// ======================================
if (page.endsWith("result.html")) {
    (function() {
        console.log("Result Page Loaded");
        const data = JSON.parse(localStorage.getItem("analysisResult"));
        
        if (!data) {
            alert("No result found. Please analyze again.");
            window.location.href = "index.html";
            return; // ✅ Now return works because we're inside a function
        }
        
        const mainEmotion = data.main_emotion || "Not detected";
        const summary = data.summary || "No summary available.";
        const domainUsed = data.domain || "General";
        const scores = data.scores || {};
        
        document.getElementById("mainEmotion").textContent = mainEmotion;
        document.getElementById("summary").textContent = summary;
        document.getElementById("domainUsed").textContent = domainUsed;
        
        const ul = document.getElementById("emotionScores");
        ul.innerHTML = "";
        for (let [emotion, score] of Object.entries(scores)) {
            const li = document.createElement("li");
            li.textContent = `${emotion}: ${score}`;
            ul.appendChild(li);
        }
        
        document.getElementById("backBtn").addEventListener("click", () => {
            window.location.href = "index.html";
        });
    })();
}
