import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load saved data
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

index = faiss.read_index("faiss_index.bin")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def search_similar_chunks(question, top_k=5):
    question_vector = embedder.encode([question])[0].astype("float32").reshape(1, -1)
    _, indices = index.search(question_vector, top_k)
    return "\n".join([chunks[i] for i in indices[0]])
