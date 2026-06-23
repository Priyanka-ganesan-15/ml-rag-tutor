from sentence_transformers import CrossEncoder

model = CrossEncoder("BAAI/bge-reranker-base")


def rerank(question, docs_with_meta, top_k=5):
    docs = [d[0] for d in docs_with_meta]

    pairs = [(question, doc) for doc in docs]
    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, docs_with_meta),
        reverse=True,
        key=lambda x: x[0]
    )

    return [doc for _, doc in ranked[:top_k]]