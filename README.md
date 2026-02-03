
# Enterprise RAG over Structured (SQL) and Unstructured (PDF) Data using Local LLMs

This project demonstrates a **production-style Retrieval Augmented Generation (RAG)** system that allows natural language querying over:

- Structured enterprise data (SQL database)
- Unstructured documents (PDF manuals/reports)

The system uses **local LLMs (Ollama + Mistral)**, embeddings, and vector search to generate grounded, evidence-based answers.

> Example question:  
> “Which assets showed abnormal energy usage and what does the manual recommend?”

---

## 🚀 Key Features

- RAG pipeline for enterprise data
- Integration of SQL + document store
- Embeddings using SentenceTransformers
- Vector search using FAISS
- Local LLM inference using Ollama (no paid APIs)
- REST API using FastAPI
- Docker-ready
- Designed for AWS-style deployment

---

## 🏗️ Architecture

```
User Question
      │
      ▼
 Query Router
      │
 ┌───────────────┬────────────────┐
 │               │                │
SQL Retriever  Doc Retriever   Vector Search (FAISS)
      │               │
      └───────────Context────────┘
                      │
                   Mistral (Ollama)
                      │
                 Grounded Answer
```

---

## 🧰 Tech Stack

| Component | Tool |
|---|---|
| LLM | Ollama (Mistral 7B) |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB | FAISS |
| Structured Data | SQLite |
| API | FastAPI |
| Language | Python |
| Deployment-ready | Docker |

---

## 📁 Project Structure

```
enterprise-rag-aws/
├── data/
│   ├── docs/
│   └── sql/
├── ingestion/
├── embeddings/
├── retriever/
├── rag_pipeline/
├── api/
├── vector_store/
└── README.md
```

---

## ▶️ Running the Project

### 1. Create conda environment

```bash
conda create -n rag_env python=3.10
conda activate rag_env
conda install -c conda-forge faiss-cpu
pip install -r requirements.txt
```

### 2. Start Ollama

```bash
ollama run mistral
```

Exit after it starts.

### 3. Ingest data

```bash
python -m ingestion.sql_ingest
python -m ingestion.pdf_ingest
```

### 4. Start API

```bash
uvicorn api.app:app --reload
```

### 5. Query

```bash
curl -X POST http://127.0.0.1:8000/query \
-H "Content-Type: application/json" \
-d "{\"question\":\"Which assets are abnormal and what should be done?\"}"
```

---

## 🧪 Example Questions

- Which assets show abnormal energy usage?
- What does the manual recommend for overheating equipment?
- List assets with repeated abnormal readings and relevant guidelines.

---

## 🎯 Why This Project

This project demonstrates:

- Practical RAG for enterprise use cases
- Integration of structured and unstructured data
- Local LLM deployment without external APIs
- Production-style API design
- Foundations for AWS/SageMaker deployment

---

## 🧭 Future Improvements

- LangChain/LangGraph orchestration
- MLflow/LangSmith observability
- Role-based access & security
- Deployment on AWS EC2/S3
- Query caching and cost optimization

---

## 👩‍💻 Author

Richa Verma  
Applied AI Scientist | PhD IIT Madras  
Focus: LLM post-training, RAG systems, and ML deployment
