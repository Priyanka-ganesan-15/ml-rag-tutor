import chromadb
from core.loaders import load_pdf
from core.chunker import chunk_text
from core.embedder import embed
from config import DB_PATH, COLLECTION_NAME
import os

db = chromadb.PersistentClient(path=DB_PATH)
collection = db.get_or_create_collection(COLLECTION_NAME)

PDF_FOLDER = "data/raw/pdfs"

doc_id = 0

for file in os.listdir(PDF_FOLDER):
    if not file.endswith(".pdf"):
        continue

    path = os.path.join(PDF_FOLDER, file)
    pages = load_pdf(path)

    for page in pages:
        chunks = chunk_text(page["text"])

        for chunk in chunks:
            collection.add(
                ids=[str(doc_id)],
                documents=[chunk],
                embeddings=[embed(chunk)],
                metadatas=[{
                    "source": page["source"],
                    "page": page["page"]
                }]
            )
            doc_id += 1

print("PDF ingestion complete")