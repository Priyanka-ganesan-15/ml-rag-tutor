# 🧠 ML Tutor RAG System

An AI-powered **Machine Learning Tutor** built using Retrieval-Augmented Generation (RAG), local LLMs (Ollama), and Streamlit.

It transforms ML textbooks (PDFs) into an interactive tutor that:
- explains concepts
- compares ideas
- answers exam-style questions
- adapts responses based on intent

---

# 🚀 What This Project Does

This system simulates a **personal ML tutor** that:

✔ Learns from your PDF textbooks  
✔ Retrieves relevant knowledge before answering (RAG)  
✔ Uses a local LLM (Mistral via Ollama)  
✔ Detects question intent (definition, intuition, mechanism, etc.)  
✔ Generates structured, tutor-style responses  
✔ Provides a chat-based learning experience  

---

# 🏗️ System Architecture
**User Question
↓
Intent Classifier (LLM Router)
↓
Embedding Search (ChromaDB)
↓
Reranking Layer
↓
Context Injection
↓
Prompt Engineering Layer
↓
Ollama LLM (Mistral)
↓
Structured Tutor Response
↓
Streamlit UI**


---

# ✨ Key Features

## 📚 1. PDF-Based Knowledge System (RAG)
- Loads ML textbooks (PDFs)
- Splits into chunks
- Converts into embeddings
- Stores in ChromaDB vector database

---

## 🤖 2. Local LLM (No API Cost)
- Uses Ollama (Mistral model)
- Fully local inference
- No OpenAI or external API required

---

## 🎯 3. Intent-Aware Tutor
Automatically classifies questions into:
- Definition
- Intuition
- Mechanism (step-by-step reasoning)
- Comparison
- Exam-style answers
- Quiz requests

This allows the tutor to change explanation style dynamically.

---

## 🔍 4. Smart Retrieval Pipeline
- SentenceTransformer embeddings
- ChromaDB vector search
- Lightweight reranking for relevance improvement

---

## 💬 5. Interactive Chat UI (Streamlit)
- Chat-style interface
- Session-based memory
- Clean tutor-style responses
- Table rendering for structured outputs

---

## 🧠 6. Prompt Engineering for Teaching Style
The system is designed to:
- Use ONLY retrieved context
- Avoid hallucinations
- Produce structured, exam-ready answers
- Adapt explanation style based on intent

---

---

# ⚙️ Setup & Run Locally

## 1. Clone repository
```bash
git clone https://github.com/yourusername/ml-rag-tutor.git
cd ml-rag-tutor

