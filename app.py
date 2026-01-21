from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.lexicon import nrc_score

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "EmoSphere backend running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    text = data.get("text", "")
    domain = data.get("domain", "General")

    if not text:
        return jsonify({
            "error": "No text provided",
            "main_emotion": None,
            "scores": {},
            "summary": "",
            "domain": domain
        })

    # Run NRC lexicon analysis
    emotion_scores = nrc_score(text)

    # Detect top emotion
    main_emotion = max(emotion_scores, key=emotion_scores.get)

    # Generate summary (simple placeholder)
    summary = f"This text expresses mostly '{main_emotion}' emotions."

    return jsonify({
        "main_emotion": main_emotion,
        "scores": emotion_scores,
        "summary": summary,
        "domain": domain
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
