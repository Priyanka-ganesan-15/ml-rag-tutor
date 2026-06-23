from pypdf import PdfReader


def load_pdf(path: str):
    reader = PdfReader(path)
    docs = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            docs.append({
                "text": text,
                "source": path.split("/")[-1],
                "page": i + 1
            })

    return docs