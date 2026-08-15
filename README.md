<div align="center">
 LexiAI

### AI-Powered Legal Document Intelligence

Transform complex legal documents into clear, structured insights with AI-powered summarization, clause extraction, and entity recognition — all processed locally for enhanced privacy.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gemma%202B-LLM-orange?style=for-the-badge" alt="Gemma 2B">
  <img src="https://img.shields.io/badge/Ollama-Local%20AI-black?style=for-the-badge" alt="Ollama">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

</div>
---

## Overview

**LexiAI** is a privacy-focused legal document intelligence system that uses local large language models to analyze complex legal text and transform it into structured, understandable information.

Legal documents often contain lengthy clauses, complex terminology, multiple parties, dates, jurisdictions, and financial terms. LexiAI simplifies this process by automatically identifying the most important information and presenting it in a clear format.

The system combines **Gemma 2B**, **Ollama**, **FastAPI**, and **Streamlit** to provide an end-to-end AI workflow for legal document analysis.

Instead of sending confidential documents to external AI services, LexiAI uses locally hosted inference through Ollama, making privacy a core part of the architecture.

---

## What LexiAI Does

LexiAI transforms unstructured legal text into actionable insights through three primary analysis capabilities:

### Document Summarization

Generates a concise, plain-language summary of the provided legal document, helping users quickly understand its purpose and overall content.

### Key Clause Extraction

Identifies important legal and contractual provisions such as:

* Termination clauses
* Liability provisions
* Confidentiality clauses
* Payment terms
* Jurisdiction clauses
* Indemnification provisions

### Named Entity Extraction

Identifies relevant entities and information within legal documents, including:

* Parties
* Organizations
* Dates
* Locations
* Laws
* Jurisdictions
* Monetary amounts

---

## Key Features

* **AI-Powered Analysis** — Uses a local LLM to understand and analyze legal text.
* **Document Summarization** — Converts lengthy legal documents into concise summaries.
* **Clause Intelligence** — Extracts important contractual and legal clauses.
* **Entity Recognition** — Identifies parties, organizations, dates, locations, laws, and financial information.
* **Local LLM Processing** — Runs inference locally through Ollama.
* **Privacy-Focused** — Legal document content can remain within the local environment.
* **FastAPI Backend** — Provides a clean API layer for document analysis.
* **Streamlit Interface** — Provides an accessible interface for interacting with the system.

---

## Architecture

```text
                         ┌─────────────────────┐
                         │        User         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         │      Frontend       │
                         └──────────┬──────────┘
                                    │
                                    │ HTTP Request
                                    ▼
                         ┌─────────────────────┐
                         │      FastAPI        │
                         │       Backend       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       Ollama        │
                         │    Local Runtime    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Gemma 2B       │
                         │     Local LLM       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                 ┌────────────────────────────────────┐
                 │          Legal Intelligence         │
                 │                                    │
                 │  • Document Summary                │
                 │  • Key Clauses                     │
                 │  • Named Entities                  │
                 └────────────────────────────────────┘
```

---

## How It Works

LexiAI follows a straightforward document intelligence pipeline:

```text
Legal Document
      │
      ▼
Text Input
      │
      ▼
FastAPI Backend
      │
      ▼
Local LLM Inference
      │
      ▼
Legal Text Analysis
      │
      ├───────────────┬────────────────┐
      ▼               ▼                ▼
   Summary      Key Clauses       Entities
      │               │                │
      └───────────────┴────────────────┘
                      │
                      ▼
                Structured Results
```

### Processing Flow

1. The user provides legal document text through the Streamlit interface.
2. The frontend sends the document to the FastAPI backend.
3. The backend prepares the content for analysis.
4. Ollama sends the request to the locally hosted Gemma 2B model.
5. The model analyzes the legal content.
6. LexiAI extracts summaries, key clauses, and relevant entities.
7. The structured results are returned to the Streamlit interface.

---

## Technology Stack

| Technology | Role                         |
| ---------- | ---------------------------- |
| Python     | Core application development |
| Gemma 2B   | Local language model         |
| Ollama     | Local LLM inference          |
| FastAPI    | Backend API                  |
| Uvicorn    | ASGI server                  |
| Streamlit  | Interactive frontend         |
| Requests   | HTTP communication           |
| Pydantic   | Data validation              |

---

## Project Structure

```text
lexiAI/
│
├── agents/
│
├── backend/
│   └── main.py
│
├── data/
│   └── example_contract.txt
│
├── frontend/
│   └── app.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Getting Started

### Prerequisites

Make sure the following are installed on your system:

* Python 3.8+
* Ollama
* Gemma 2B
* Git
* Recommended: 8 GB+ RAM

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/legal-document-analyzer-ai.git
cd legal-document-analyzer-ai
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Set Up Ollama

Install Ollama and download the Gemma 2B model:

```bash
ollama pull gemma:2b
```

Make sure Ollama is running before starting the application.

If required, start the Ollama service with:

```bash
ollama serve
```

---

## Run LexiAI

LexiAI consists of two main components:

* FastAPI backend
* Streamlit frontend

### Start the Backend

Open a terminal and run:

```bash
uvicorn backend.main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

### Start the Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

The interface will be available at:

```text
http://localhost:8501
```

Open the Streamlit URL in your browser to begin analyzing legal documents.

---

## Example

### Input

```text
This Agreement is entered into by Party A and Party B.

Either party may terminate this agreement with thirty (30) days written notice.

Liability shall be limited to direct damages only.

This agreement shall be governed by the laws of the State of California.
```

### Generated Analysis

#### Summary

The agreement is between Party A and Party B. Either party can terminate the agreement with 30 days' written notice. Liability is limited to direct damages, and California law governs the agreement.

#### Key Clauses

```text
Termination:
Either party may terminate with 30 days written notice.

Liability:
Liability is limited to direct damages only.

Jurisdiction:
The agreement is governed by California law.
```

#### Named Entities

```text
Parties:
Party A
Party B

Location:
State of California

Law:
California law
```

---

## API

LexiAI exposes its analysis functionality through a FastAPI backend.

### Analyze Document

```http
POST /analyze/
```

### Request

```json
{
  "text": "Your legal document text..."
}
```

### Response

```json
{
  "summary": "Document summary...",
  "clauses": "Extracted clauses...",
  "entities": "Named entities..."
}
```

The API-based architecture also allows the analysis engine to be integrated into other applications or interfaces.

---

## Privacy-First AI

Privacy is an important consideration when working with legal documents.

LexiAI uses **local LLM inference through Ollama**, allowing document analysis to take place on the user's own machine.

This approach provides several advantages:

* No external AI API is required for inference.
* Legal document content can remain local.
* Sensitive documents do not need to be uploaded to a third-party AI provider.
* The application can operate without depending on cloud-based LLM services.

> Local processing does not automatically guarantee complete security. Users should still follow appropriate security practices when handling confidential legal information.

---

## Use Cases

LexiAI can serve as a foundation for a variety of legal-document workflows, including:

* Contract review
* Legal document summarization
* Preliminary clause analysis
* Legal research assistance
* Document intelligence
* Contract information extraction
* Privacy-focused legal AI applications
* Legal-tech experimentation and prototyping

---

## Roadmap

* [ ] PDF document upload
* [ ] DOCX document support
* [ ] Multi-document comparison
* [ ] Contract risk detection
* [ ] Clause-level risk scoring
* [ ] Automatic identification of unusual clauses
* [ ] Document version comparison
* [ ] PDF/DOCX analysis export
* [ ] Advanced legal entity recognition
* [ ] Persistent document history
* [ ] User authentication
* [ ] Support for additional local LLMs
* [ ] Specialized legal-domain models

---

## Disclaimer

LexiAI is intended for **educational, research, and prototype purposes**.

AI-generated analysis should not be considered legal advice. Legal documents and AI-generated interpretations should be reviewed by a qualified legal professional before being used for legal, financial, or business decisions.

---

## License

This project is licensed under the **MIT License**.

---

## Author

**Esha Mirza**

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)


---

<p align="center">
  <strong>LexiAI</strong> — Making legal documents easier to understand with local AI.
</p>
