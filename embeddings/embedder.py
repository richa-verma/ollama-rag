from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_and_store(texts):
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs("vector_store", exist_ok=True)
    faiss.write_index(index, "vector_store/index.faiss")

    with open("vector_store/texts.pkl", "wb") as f:
        pickle.dump(texts, f)
