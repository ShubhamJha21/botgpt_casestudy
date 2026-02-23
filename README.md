# 🚀 BOT GPT – Conversational AI Backend

Production-grade conversational AI backend built with **FastAPI**, **SQLite**, and **Open-Source LLM integration (Ollama)**.

This project demonstrates:

- Clean backend architecture
- REST API design maturity
- Conversation persistence
- LLM integration
- Basic Retrieval-Augmented Generation (RAG)
- Cost-aware context management
- Docker

---

# 📌 Overview

BOT GPT is a scalable conversational backend that supports:

## 1️⃣ Open Chat Mode
- General LLM conversation
- Multi-turn chat
- Persistent conversation history
- Context window management

## 2️⃣ Grounded Chat (RAG Mode)
- Chat over uploaded documents
- Text chunking
- Embedding generation
- FAISS vector retrieval
- Context injection into LLM prompt

---

# 🏗 Architecture

```
Client (Postman / Swagger)
        |
        v
FastAPI (API Layer)
        |
        v
Service Layer
 - Conversation Service
 - LLM Service
 - RAG Service
        |
        v
Persistence Layer
 - SQLite (Users, Conversations, Messages)
 - FAISS (Vector Index)
        |
        v
Ollama (Llama3 - Local LLM)
```

---

# 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| LLM | Ollama (Llama3) |
| Embeddings | sentence-transformers |
| Vector Search | FAISS |
| Testing | Pytest |
| Containerization | Docker |

---

# 📂 Project Structure

```
bot-gpt/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── config.py
│   ├── routes/
│   │     └── conversations.py
│   ├── services/
│   │     ├── conversation_service.py
│   │     ├── llm_service.py
│   │     └── rag_service.py
│   └── utils/
│         └── context_manager.py
│
├── tests/
│   └── test_conversations.py
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# 🗄 Data Model

## User
- id (UUID)
- email
- created_at

## Conversation
- id (UUID)
- user_id (FK)
- mode (open / rag)
- summary (optional)
- created_at

## Message
- id (UUID)
- conversation_id (FK)
- role (user / assistant / system)
- content
- created_at

Message ordering is maintained using timestamps.

---

# 🔗 API Endpoints

## Create Conversation

**POST** `/conversations`

Request:
```json
{
  "user_id": "123",
  "mode": "open",
  "first_message": "Hello AI"
}
```

Response:
```json
{
  "conversation_id": "uuid",
  "assistant_reply": "Hello! How can I help?"
}
```

---

## Continue Conversation

**POST** `/conversations/{id}/messages`

Request:
```json
{
  "message": "Explain transformers"
}
```

---

## Get Conversation Details

**GET** `/conversations/{id}`

---

## Delete Conversation

**DELETE** `/conversations/{id}`

---

# 🧠 Context Management Strategy

To prevent token overflow and reduce LLM cost:

- Sliding window (last N messages retained)
- Truncation before LLM call
- Optional summarization capability

This ensures scalability and cost efficiency.

---

# 📚 RAG Flow

1. Document text is chunked.
2. Embeddings generated using sentence-transformers.
3. Stored in FAISS vector index.
4. On each user query:
   - Query embedding generated
   - Top-K relevant chunks retrieved
   - Context injected into LLM prompt

Prompt structure:

```
System: Use the provided context to answer the question.

Context:
<retrieved chunks>

User:
<question>
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd bot-gpt
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Install Ollama

Download and install from:

https://ollama.com/

Pull the model:

```bash
ollama pull llama3
```

Run once (to initialize):

```bash
ollama run llama3
```

---

## 4️⃣ Run Backend

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://localhost:8000/docs
```

---

# 🐳 Docker Setup

Build Docker image:

```bash
docker build -t bot-gpt .
```

Run container:

```bash
docker run -p 8000:8000 bot-gpt
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# ⚠️ Error Handling

Handled scenarios:

- Invalid conversation ID → 404 response
- Context truncation before token overflow

---
# 👨‍💻 Author

**Shubham Jha**  
AI Engineer | Data Scientist  
India
