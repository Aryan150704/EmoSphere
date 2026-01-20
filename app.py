from flask import Flask, request, jsonify
from utils.lexicon import nrc_score

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "EmoSphere backend running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    # Emotion analysis (lexicon-based)
    emotions = nrc_score(text)

    # Simple summary (first 3 sentences or first 200 chars)
    summary = text[:200] + ("..." if len(text) > 200 else "")

    return jsonify({
        "summary": summary,
        "emotions": emotions
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
