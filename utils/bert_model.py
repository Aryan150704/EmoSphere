from transformers import pipeline

# Lightweight, accurate emotion classifier
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

# Emotion groups (use your existing mapping or simplified)
mapping = {
    "anger": ["anger"],
    "joy": ["joy"],
    "sadness": ["sadness"],
    "fear": ["fear"],
    "disgust": ["disgust"],
    "surprise": ["surprise"]
}

def bert_emotions(text):
    outputs = emotion_classifier(text)
    results = {emo: 0 for emo in mapping}

    # Convert list to dict
    label_scores = {i['label'].lower(): i['score'] for i in outputs}

    # Aggregate into 6 universal emotions
    for emo, labels in mapping.items():
        results[emo] = sum(label_scores.get(l, 0) for l in labels)

    return results
