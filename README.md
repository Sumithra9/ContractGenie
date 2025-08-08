# 🤖 ContractGenie – AI-Powered Legal Assistant

**ContractGenie** is a GenAI-powered legal assistant that helps users quickly draft NDAs, summarize contracts, explain legal clauses, and ask context-aware questions about uploaded agreements — all in one clean Streamlit app.

---

## 🚀 Features

### 📝 Generate NDAs Instantly
Automatically draft simple Non-Disclosure Agreements from natural language inputs like discloser name, receiver, purpose, and duration — powered by Groq's blazing-fast LLaMA 3.

### 📄 Upload & Summarize Contracts (PDF)
Upload any legal contract in PDF format and get a clear, concise bullet-point summary of the document’s key obligations and provisions.

### 📘 Clause Explanation
Paste any complex legal clause and the app will explain it in plain, human-readable terms — perfect for non-lawyers or fast interpretation.

### 🤖 Ask Questions about Contracts (RAG QnA)
Use Retrieval-Augmented Generation (RAG) to ask questions about the uploaded PDF:
- Automatically extracts and embeds document chunks
- Retrieves relevant sections using semantic search (MiniLM + FAISS)
- Generates grounded answers using Groq LLaMA 3

💬 **Examples**:
- "What are the termination conditions?"
- "Is there a confidentiality clause?"
- "When does the agreement expire?"

### 🎯 Clean & Minimal UI with Streamlit
Tabbed interface with intuitive sidebar navigation for each functionality. Built entirely in Python using modular design principles.

---

## ⚙️ Tech Stack

- **Frontend/UI**: Streamlit
- **LLM Backend**: Groq API + LLaMA 3
- **RAG Components**: LangChain, FAISS, HuggingFace Embeddings
- **PDF Parsing**: pdfplumber
- **Deployment**: Streamlit Cloud

---

## 📦 Installation



1. **Clone the repository**

```bash
git clone https://github.com/Sumithra9/ContractGenie.git
cd contractgenie
pip install -r requirements.txt

```
2.**Create and activate a virtual environment**
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3.**Install dependencies**
```bash
pip install -r requirements.txt
```
4.**Set your Groq API key**
```bash
GROQ_API_KEY="your-groq-api-key-here"
```
5. **Run Streamlit App**
```bash
streamlit run app.py
```
