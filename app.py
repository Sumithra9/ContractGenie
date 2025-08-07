import streamlit as st
import pdfplumber
import os
from dotenv import load_dotenv
import requests

# RAG-specific imports
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama3-8b-8192"  # or "llama3-70b-8192"

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 800
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"❌ Groq API Error: {str(e)}\n\nResponse: {response.text if response else 'No response'}"

# PDF Reader
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

# NDA Generator
def draft_nda(discloser, receiver, purpose, duration):
    prompt = f"""
Draft a simple Non-Disclosure Agreement (NDA) between:
- Discloser: {discloser}
- Receiver: {receiver}
- Purpose: {purpose}
- Duration: {duration}
Use plain English and proper formatting.
"""
    return ask_groq(prompt)

# Contract Summarizer
def summarize_contract(text):
    prompt = f"""
Summarize the following contract in 5-7 bullet points with headings:\n\n{text[:2000]}
"""
    return ask_groq(prompt)

# Clause Explainer
def explain_clause(clause):
    prompt = f"Explain the following legal clause in simple terms:\n\n{clause}"
    return ask_groq(prompt)

# RAG Vector Store Builder
def build_vectorstore(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embeddings)

# RAG-based QnA
def query_contract_rag(question, vectorstore):
    docs = vectorstore.similarity_search(question, k=4)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"""
You are a legal assistant. Use the following extracted contract sections to answer the user's question.

Context:
{context}

Question: {question}
Answer:
"""
    return ask_groq(prompt)

# Streamlit UI
st.set_page_config(page_title="ContractGenie", layout="centered")
st.title("🤖 ContractGenie")

option = st.sidebar.selectbox("Choose a Task", [
    "📄 Draft NDA", "📂 Summarize Contract", "🔍 Explain Clause", "💬 Ask Contract Questions (RAG)"
])

if option == "📄 Draft NDA":
    st.header("📄 NDA Generator")
    discloser = st.text_input("Discloser Name")
    receiver = st.text_input("Receiver Name")
    purpose = st.text_area("Purpose of NDA")
    duration = st.text_input("Duration (e.g., 2 years)")
    if st.button("Generate NDA"):
        if all([discloser, receiver, purpose, duration]):
            result = draft_nda(discloser, receiver, purpose, duration)
            st.text_area("Generated NDA", result, height=400)
        else:
            st.warning("Fill in all fields.")

elif option == "📂 Summarize Contract":
    st.header("📂 Contract Summarizer")
    uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"], key="summarizer")
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
        st.success("✅ PDF processed. Click below to summarize.")
        if st.button("Summarize"):
            summary = summarize_contract(text)
            st.text_area("📋 Summary", summary, height=400)

elif option == "🔍 Explain Clause":
    st.header("🔍 Clause Explainer")
    clause = st.text_area("Paste legal clause here")
    if st.button("Explain"):
        explanation = explain_clause(clause)
        st.text_area("📘 Explanation", explanation, height=300)

elif option == "💬 Ask Contract Questions (RAG)":
    st.header("💬 Contract QnA (RAG)")
    uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"], key="rag")

    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
        vectorstore = build_vectorstore(text)
        st.success("✅ Contract uploaded and processed.")

        # Always show input after upload
        user_q = st.text_input("Ask a question about the contract", placeholder="e.g., What is the termination clause?")
        if user_q:
            with st.spinner("🧠 Generating answer..."):
                answer = query_contract_rag(user_q, vectorstore)
            st.markdown("**📘 Answer:**")
            st.write(answer)
    else:
        st.info("📤 Please upload a contract PDF to enable QnA.")
