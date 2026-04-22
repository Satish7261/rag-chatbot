# 🤖 AI RAG Chatbot (TXT/PDF)

A Retrieval-Augmented Generation (RAG) based chatbot that answers questions from custom documents (TXT/PDF).

---

## 📸 Demo

<p align="center">
  <img src="assets/screenshotproject.png" width="800"/>
</p>

---

## 🚀 Features

- 📄 Load custom TXT/PDF files
- ✂️ Text chunking for better context
- 🔎 Semantic search using embeddings
- 🤖 Question answering based on document
- ⚠️ Returns "No information found" for unknown queries

---

## 🧠 How It Works (RAG Pipeline)

1. Load document  
2. Split into chunks  
3. Convert text → embeddings  
4. Store embeddings  
5. Retrieve relevant chunks  
6. Generate answer  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Sentence Transformers  
- NumPy  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
