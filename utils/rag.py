import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve(query_embedding, doc_embeddings, texts, top_k=3, threshold=0.5):
    scores = []

    for i, emb in enumerate(doc_embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, texts[i]))

    # sort by highest score
    scores.sort(reverse=True, key=lambda x: x[0])

    # 🔥 FILTER based on threshold
    filtered = [text for score, text in scores if score > threshold]

    # 🚨 If nothing relevant
    if not filtered:
        return ["Sorry, no relevant information found."]

    return filtered[:top_k]