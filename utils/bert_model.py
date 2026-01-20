from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/bert-base-go-emotions",
    top_k=None
)

mapping = {
    "anger": ["anger", "annoyance"],
    "anticipation": ["anticipation"],
    "disgust": ["disgust"],
    "fear": ["fear"],
    "joy": ["joy", "amusement"],
    "sadness": ["sadness"],
    "surprise": ["surprise"],
    "trust": ["approval", "pride"]
}

def bert_emotions(text):
    outputs = classifier(text)
    scores = {e: 0 for e in mapping}

    label_scores = {i['label']: i['score'] for i in outputs}

    for emo, labels in mapping.items():
        scores[emo] = sum(label_scores.get(l, 0) for l in labels)

    return scores
