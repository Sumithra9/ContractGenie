# ContractGenie – AI-Powered Contract Assistant

ContractGenie is an intelligent legal document assistant powered by LLMs. It helps users generate NDAs, summarize complex contracts, and explain specific legal clauses in simple terms using AI — all through a clean Streamlit interface.


## Features

- **Generate NDAs Instantly**  
  Automatically draft basic Non-Disclosure Agreements from simple text prompts using a Groq-powered LLM backend.

- **Upload & Summarize Contracts (PDF)**  
  Upload any contract in PDF format and get a concise summary highlighting its key points and obligations.

- **Clause Explanation**  
  Copy and paste any legal clause from a document, and the app will explain it in layman's terms for easy understanding.

- **Clean & Minimal UI with Streamlit**  
  The app provides an intuitive interface with tabs for NDA drafting, contract summarization, and clause explanations.

---

## Use Cases

- Startups and freelancers generating NDAs on the fly  
- Students or early professionals understanding legal documents  
- Product managers summarizing partner agreements  
- Anyone needing legal assistance without legal jargon

---

## Built With

- **Streamlit** – for building the interactive web UI  
- **Groq API (Mixtral-8x7B)** – for fast and cost-effective LLM responses  
- **pdfplumber** – for extracting contract text from PDF files  
- **Python** – backend logic and data flow  
- **Secrets Manager** – for securely handling API keys

---
## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/multi-pdf-chat.git
cd multi-pdf-chat
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
