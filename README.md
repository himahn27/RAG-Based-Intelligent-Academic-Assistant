# 📘 RAG-Based Intelligent Academic Assistant

## 📌 Overview

The **RAG-Based Intelligent Academic Assistant** is a hybrid AI system that provides accurate and reliable academic support by combining:

- 📄 Document-based Retrieval (Vector Database)
- 🌐 Real-time Web Search Fallback
- 🤖 Large Language Model reasoning (Groq LLM)

The system prioritizes answers from uploaded academic documents.  
If the information is not found locally, it automatically retrieves relevant information from the web while minimizing hallucinations using controlled prompting strategies.

---

## 🚀 Key Features

- Hybrid RAG architecture (Documents + Web)
- Multi-format document upload support
- Vector-based semantic search using embeddings
- Automatic fallback to web search
- Hallucination-aware response generation
- Secure API key handling using environment variables
- Clean Streamlit-based user interface

---
## 📂 Supported Document Formats

The assistant supports ingestion of both structured and unstructured academic content:

📄 PDF

📝 DOCX (Word Documents)

📃 TXT (Plain Text Files)

📊 CSV (Comma-Separated Values)

📈 Excel (.xlsx, .xls) — including multi-sheet support

Structured data (CSV & Excel) is automatically converted into natural language format for improved semantic retrieval

---
## 🏗 System Architecture

User Query  
⬇  
Vector Database Search (ChromaDB)  
⬇  
If found → Answer from Documents  
⬇  
If not found → Web Search (DDGS)  
⬇  
LLM generates response using verified context 

---
## 📂 Project Structure
```
rag-based-intelligent-academic-assistant/
│
├── app.py                  # Streamlit UI
├── rag_pipeline.py         # Core query processing logic
├── vector_db.py            # Vector database setup & retrieval
├── document_loader.py      # Multi-format document loading & chunking
├── web_search.py           # Web search integration
├── config.py               # Configuration settings
├── requirements.txt        # Dependencies
├── .gitignore              # Ignored files
└── README.md
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-based-intelligent-academic-assistant.git
cd rag-based-intelligent-academic-assistant
```
### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Set Environment Variables
Create a .env file:
```
GROQ_API_KEY=your_groq_api_key
```
### 5️⃣ Run the Application
```
streamlit run app.py
```
---

## 🔐 Security & Best Practices

- API keys stored securely in `.env`
- `.env`, `venv`, and vector database excluded using `.gitignore`
- No hardcoded secrets in the repository
- Controlled prompting to reduce hallucinations
- Metadata tagging for document traceability

---

## 📌 Example Use Cases

- Academic concept clarification
- Course material understanding
- Research assistance
- Document-based Q&A
- Real-time factual verification using web fallback

---

## 🛠 Technologies Used

- Python
- Streamlit
- ChromaDB
- HuggingFace Embeddings
- Groq LLM API
- DDGS Web Search
- Pandas
- python-docx
- openpyxl

---
Created by Hima 

Developed as part of an academic AI project focused on building a hybrid Retrieval-Augmented Generation (RAG) system.



