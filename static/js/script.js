const analyzeBtn = document.getElementById("analyzeBtn");
const userText = document.getElementById("userText");
const domainSelect = document.getElementById("domain");
const loader = document.getElementById("loader");

analyzeBtn.addEventListener("click", async () => {
    const text = userText.value.trim();
    const domain = domainSelect.value;

    if (!text) {
        alert("Please enter some text!");
        return;
    }

    loader.classList.remove("hidden");

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text, domain })
        });

        const data = await response.json();

        localStorage.setItem("emotionData", JSON.stringify(data));

        loader.classList.add("hidden");

        window.location.href = "/result";

    } catch (err) {
        loader.classList.add("hidden");
        alert("Server error");
        console.error(err);
    }
});
