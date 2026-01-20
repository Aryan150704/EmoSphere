from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.lexicon import nrc_score

app = Flask(__name__)
CORS(app)   # Enable CORS for all routes

@app.route("/", methods=["GET"])
def home():
    return "EmoSphere backend running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    domain = data.get("domain", "General")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    # Call NRC lexicon scoring
    result = nrc_score(text)

    return jsonify({
        "domain": domain,
        "input_text": text,
        "analysis": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
