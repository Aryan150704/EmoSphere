def fuse_scores(lex, bert, alpha=0.4):
    final = {}
    for e in lex:
        final[e] = alpha * lex[e] + (1 - alpha) * bert[e]
    return final
