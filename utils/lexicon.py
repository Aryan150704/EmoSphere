import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEXICON_PATH = os.path.join(BASE_DIR, "nrc_lexicon.json")

with open(LEXICON_PATH, "r", encoding="utf-8") as f:
    NRC = json.load(f)

def nrc_score(text):
    scores = {e: 0 for e in [
        "joy", "sadness", "anger", "fear",
        "trust", "anticipation", "surprise", "disgust"
    ]}

    words = text.lower().split()
    for w in words:
        if w in NRC:
            for emotion in NRC[w]:
                scores[emotion] += 1

    total = sum(scores.values()) or 1
    return {k: round(v / total, 3) for k, v in scores.items()}
