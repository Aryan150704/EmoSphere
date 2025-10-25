// Get references to HTML elements
const analyzeBtn = document.getElementById("analyzeBtn");
const userText = document.getElementById("userText");
const domainSelect = document.getElementById("domain");
const loader = document.getElementById("loader");

// Add click event to Analyze button
analyzeBtn.addEventListener("click", async () => {
    const text = userText.value.trim(); // Get text input
    const domain = domainSelect.value;  // Get selected domain

    // If no text entered, show alert
    if (!text) {
        alert("⚠️ Please enter some text before analyzing!");
        return;
    }

    // Show loading message
    loader.classList.remove("hidden");

    try {
        // ---- (Mock response for testing before backend) ----
        // In final version, this will call Flask API: "/analyze"
        const mockResponse = {
            summary: "This is a summarized version of your input text.",
            emotions: { Joy: 0.45, Sadness: 0.25, Anger: 0.15, Fear: 0.15 },
            chart: "" // Will hold Matplotlib chart in base64 later
        };

        // Simulate delay to mimic backend processing
        await new Promise(res => setTimeout(res, 2000));

        // Save data locally (so result page can read it)
        localStorage.setItem("emotionData", JSON.stringify(mockResponse));

        // Hide loader and redirect to result page
        loader.classList.add("hidden");
        window.location.href = "/result.html";
    } 
    catch (err) {
        loader.classList.add("hidden");
        alert("❌ Error occurred while analyzing text. Please try again!");
        console.error(err);
    }
});
