import streamlit as st
import os

from utils.embedder import get_embeddings
from utils.rag import retrieve

st.title("📄 AI TXT Chatbot")

# 🔥 TEXT FILE PATH
file_path = "data/sample.txt"

# ✅ DEBUG
st.write("File exists:", os.path.exists(file_path))

if os.path.exists(file_path):
    st.write("File size:", os.path.getsize(file_path))
else:
    st.error("❌ File not found")
    st.stop()

if os.path.getsize(file_path) == 0:
    st.error("❌ File is empty")
    st.stop()

# ✅ READ TEXT FILE
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

st.success("✅ Text Loaded")

# 🔹 Split into chunks (simple)
texts = text.split("\n")

# 🔹 Create embeddings
doc_embeddings = get_embeddings(texts)
st.success("✅ Embeddings created")

# 🔹 User query
query = st.text_input("Ask something:")

if query:
    query_embedding = get_embeddings([query])[0]
    results = retrieve(query_embedding, doc_embeddings, texts)

    st.write("### 📌 Answer:")
    for r in results:
        st.write(r)