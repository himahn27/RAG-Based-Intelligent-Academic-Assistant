import streamlit as st
import os
import shutil
from document_loader import load_and_split
from vector_db import create_vector_store
from rag_pipeline import process_query

st.title("🌐 RAG-Based Intelligent Assistant")

# ----------------------------
# Initialize session state
# ----------------------------
if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

# 🔥 Added: Initialize question state
if "question" not in st.session_state:
    st.session_state.question = ""    

# ----------------------------
# Ensure data folder exists
# ----------------------------
if os.path.exists("data"):
    shutil.rmtree("data")
os.makedirs("data")

uploaded_file = st.file_uploader("Upload Document", type=["pdf" , "docx", "txt","xlsx"])

# Handle file upload
if uploaded_file and uploaded_file.name != st.session_state.get("last_uploaded_file"):

    # Store new filename
    st.session_state.last_uploaded_file = uploaded_file.name

    # 🔥 Clear old question when new file is uploaded
    st.session_state.question = ""

    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    chunks = load_and_split(file_path)
    create_vector_store(chunks)

    st.session_state.document_uploaded = True

# ----------------------------
# Question Section
# ----------------------------
question = st.text_input("Ask a question:", key="question")

if question:
    if not st.session_state.document_uploaded:
        st.warning("⚠️ Please upload a document first.")
        st.stop()

    answer = process_query(question)
    st.write("### Answer:")
    st.write(answer)