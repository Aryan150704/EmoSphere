from flask import Flask, request, jsonify, render_template
from utils.preprocess import preprocess_text
from utils.lexicon import nrc_score
from utils.bert_model import bert_emotions
from utils.fusion import fuse_scores
from utils.summarizer import generate_summary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result")
def result_page():
    return render_template("result.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    domain = data.get("domain", "general")

    # Step 1: Preprocess
    tokens = preprocess_text(text)

    # Step 2: NRC scoring
    lex_scores, evidence = nrc_score(tokens)

    # Step 3: BERT scoring
    bert_scores = bert_emotions(text)

    # Step 4: Fusion
    final_scores = fuse_scores(lex_scores, bert_scores)

    # Step 5: BART summary
    summary = generate_summary(final_scores, text)

    return jsonify({
        "lexicon": lex_scores,
        "bert": bert_scores,
        "final": final_scores,
        "evidence": evidence,
        "summary": summary
    })

if __name__ == "__main__":
    app.run(debug=True)
