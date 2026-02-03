from fastapi import FastAPI
from rag_pipeline.rag_engine import rag_answer

app = FastAPI()

@app.post("/query")
def query(q: dict):
    return {"answer": rag_answer(q["question"])}
