import requests
import sqlite3
from retriever.retriever import retrieve_docs

def query_sql():
    conn = sqlite3.connect("data/sql/assets.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM asset_usage WHERE status='abnormal'")
    rows = cur.fetchall()
    conn.close()
    return str(rows)

def call_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

def rag_answer(question):
    docs = retrieve_docs(question)
    sql_data = query_sql()

    prompt = f"""
You are an assistant answering questions using enterprise data.

SQL DATA:
{sql_data}

DOCUMENTS:
{docs}

QUESTION:
{question}
"""

    return call_ollama(prompt)
