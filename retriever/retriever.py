import faiss, pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector_store/index.faiss")
texts = pickle.load(open("vector_store/texts.pkl", "rb"))

def retrieve_docs(query, k=1):
    q_emb = model.encode([query])
    _, idx = index.search(q_emb, k)
    return [texts[i] for i in idx[0]]
