import chromadb
from core.embedder import embed
from config import DB_PATH, COLLECTION_NAME

db = chromadb.PersistentClient(path=DB_PATH)
collection = db.get_collection(COLLECTION_NAME)

query = "What is overfitting?"

results = collection.query(
    query_embeddings=[embed(query)],
    n_results=3
)

print("\nTOP MATCHES:\n")
for doc in results["documents"][0]:
    print("-", doc)