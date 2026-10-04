# 🤖 AI Customer Support Assistant

An AI-powered customer support application that uses **Retrieval-Augmented Generation (RAG)** to answer customer questions from a trusted knowledge base.

The system combines **FastAPI, ChromaDB, Ollama, Gemma 3, and Streamlit** to provide relevant answers while reducing the risk of AI hallucinations.

---

## 📌 Project Overview

The AI Customer Support Assistant is designed to simulate a real-world customer support system.

Instead of allowing the AI to generate answers from general knowledge, the application first retrieves relevant information from a company knowledge base and then uses a local Large Language Model (LLM) to generate an answer based only on that information.

### Main workflow

```text
User Question
      ↓
Streamlit Web Interface
      ↓
FastAPI Backend
      ↓
RAG Pipeline
      ↓
ChromaDB Vector Search
      ↓
Relevant Knowledge
      ↓
Ollama + Gemma 3
      ↓
AI-Generated Answer
      ↓
Answer + Sources
```

---

## ✨ Features

* 🤖 AI-powered customer support
* 🔎 Retrieval-Augmented Generation (RAG)
* 📚 Knowledge-base question answering
* 🧠 Local AI using Ollama and Gemma 3
* 🗃️ ChromaDB vector database
* ⚡ FastAPI REST API
* 🖥️ Streamlit web interface
* 📖 Source information displayed with answers
* 🛡️ Context-restricted responses to reduce hallucinations
* ❌ Graceful response when information is unavailable
* 🧪 Automated API tests with Pytest
* 🔐 Environment-based configuration support

---

## 🏗️ Technology Stack

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| Python        | Core programming language              |
| FastAPI       | Backend REST API                       |
| ChromaDB      | Vector database and document retrieval |
| Ollama        | Local LLM runtime                      |
| Gemma 3       | Local language model                   |
| Streamlit     | Web interface                          |
| Requests      | API communication                      |
| Pytest        | Automated testing                      |
| Pydantic      | Data validation                        |
| python-dotenv | Environment configuration              |

---

## 📂 Project Structure

```text
AI-Customer-Support-Assistant/
│
├── app/
│   ├── api/
│   │   └── support.py
│   │
│   ├── core/
│   │
│   ├── services/
│   │   ├── index_knowledge.py
│   │   ├── llm_service.py
│   │   ├── rag_service.py
│   │   └── vector_store.py
│   │
│   ├── frontend/
│   │   └── streamlit_app.py
│   │
│   └── main.py
│
├── data/
│   └── knowledge_base.txt
│
├── tests/
│   └── test_api.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

> `.env`, `.venv/`, Python cache files, and other sensitive/local files are excluded from Git using `.gitignore`.

---

## 🔄 How the RAG System Works

The application follows a Retrieval-Augmented Generation pipeline.

### 1. Knowledge Base

Company information is stored in:

```text
data/knowledge_base.txt
```

The knowledge base contains information about:

* Products
* Pricing
* Refund policy
* Cancellation policy
* Customer support
* Data security
* Contact information

### 2. Document Indexing

The knowledge base is divided into smaller sections and stored in ChromaDB.

Run:

```powershell
python -m app.services.index_knowledge
```

The application currently indexes **27 knowledge documents**.

### 3. Retrieval

When a user asks a question, ChromaDB searches for the most relevant information.

For example:

```text
How much does NovaDesk Professional cost?
```

The system retrieves relevant pricing information.

### 4. AI Generation

The retrieved information is passed to the local Gemma 3 model through Ollama.

The model is instructed to answer using only the retrieved context.

### 5. Response

The API returns:

* User question
* Generated answer
* Retrieved sources

This makes the response more transparent and helps reduce hallucination.

---

## 🛡️ Hallucination Control

The assistant is instructed not to invent information.

For example, if the user asks:

```text
What is NovaTech mobile phone price?
```

and the knowledge base does not contain this information, the assistant responds:

```text
I'm sorry, I couldn't find that information in the knowledge base.
```

This behavior was tested successfully.

---

## 🖥️ Running the Project Locally

### 1. Clone the repository

```powershell
git clone https://github.com/AqsaBatool256/AI-Customer-Support-Assistant.git
```

```powershell
cd AI-Customer-Support-Assistant
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Install and run Ollama

Install Ollama and download the required model:

```powershell
ollama pull gemma3:4b
```

Make sure Ollama is running locally.

### 6. Build the knowledge index

```powershell
python -m app.services.index_knowledge
```

### 7. Start the FastAPI backend

```powershell
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 8. Start the Streamlit frontend

Open another terminal and activate the virtual environment.

Then run:

```powershell
python -m streamlit run app/frontend/streamlit_app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 🧪 Running Tests

Run the automated tests with:

```powershell
python -m pytest tests/test_api.py -v
```

Current test coverage includes:

* API health check
* Customer support question
* Unknown-question handling

Current result:

```text
3 passed
```

---

## 🔌 API Endpoint

### Ask a Support Question

```http
GET /support/ask
```

Example:

```text
/support/ask?question=What%20is%20the%20refund%20policy?
```

Example response:

```json
{
  "question": "What is the refund policy?",
  "answer": "Customers can request a refund within 14 days of their initial purchase.",
  "sources": [
    "REFUND POLICY",
    "Refund requests must include the customer's account email and order information."
  ]
}
```

---

## 📚 Example Questions

Try asking:

```text
How much does NovaDesk Basic cost?
```

```text
How much does NovaDesk Professional cost?
```

```text
What is the refund policy?
```

```text
Can I cancel my subscription?
```

```text
When is customer support available?
```

```text
How does NovaTech protect customer information?
```

---

## 🎯 Project Goals

This project was built to demonstrate practical experience with:

* Generative AI
* Retrieval-Augmented Generation
* Vector databases
* Large Language Models
* REST APIs
* Backend development
* AI application development
* Automated testing
* Local AI deployment
* Full-stack AI application architecture

---

## 🚀 Future Improvements

Planned improvements include:

* 💬 Chat-style conversation history
* 🎨 Improved Streamlit UI
* 📄 Support for PDF and document knowledge bases
* 🔍 Improved retrieval and source ranking
* ⚙️ Configuration management
* 🧪 Expanded test coverage
* 📊 Monitoring and logging
* 🔐 Production-ready security
* ☁️ Public cloud deployment
* 🌐 Publicly accessible frontend and backend
* 📱 Responsive interface
* 📖 Improved documentation

---

## 👩‍💻 Author

**Aqsa Batool Saqib**

BS Computer Science Student | AI & Machine Learning Enthusiast | Python Developer | Cloud Computing Learner

GitHub: [AqsaBatool256](https://github.com/AqsaBatool256)

LinkedIn: [Aqsa Batool Saqib](https://www.linkedin.com/in/aqsabatoolsaqib/)

---

## 📄 License

This project is intended for educational and portfolio purposes.
