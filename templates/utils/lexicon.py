import json

with open("nrc_lexicon.json") as f:
    lexicon = json.load(f)

emotions = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]

def nrc_score(tokens):
    scores = {e: 0 for e in emotions}
    evidence = {e: [] for e in emotions}

    for t in tokens:
        if t in lexicon:
            for e in lexicon[t]:
                scores[e] += 1
                evidence[e].append(t)

    total = len(tokens)
    if total > 0:
        for e in scores:
            scores[e] = scores[e] / total

    return scores, evidence
