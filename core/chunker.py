def chunk_text(text: str, chunk_size=800, overlap=150):
    """
    Better chunking strategy:
    - keeps semantic flow
    - adds overlap to avoid losing context
    """

    words = text.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]

        chunks.append(" ".join(chunk))

        start = end - overlap  # overlap for continuity

    return chunks