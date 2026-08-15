# LexiAI

> Legal Document Analysis 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LLM-Gemma%202B-orange?style=for-the-badge" alt="Gemma 2B">
  <img src="https://img.shields.io/badge/Local%20AI-Ollama-black?style=for-the-badge" alt="Ollama">
  <img src="https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</p>

<p align="center">
  Analyze legal documents locally with AI-powered summarization, clause extraction, and named-entity recognition.
</p>

---

## Overview

**Legal Document Intelligence** is an AI-powered application designed to simplify the analysis of contracts, agreements, case files, and other legal documents.

The system uses a locally hosted large language model through **Ollama** to analyze legal text and extract meaningful information, including:

* Plain-language document summaries
* Important legal clauses
* Parties and organizations
* Dates and locations
* Laws and jurisdictions
* Monetary amounts
* Other relevant legal entities

The application combines a **FastAPI backend** with a **Streamlit interface**, providing a simple workflow for submitting legal text and reviewing structured AI-generated results.

Because the language model runs locally, sensitive legal content can be processed without sending document data to external AI APIs.

---

## Why Legal Document Intelligence?

Legal documents are often lengthy, complex, and difficult to review quickly.

This project uses local AI to reduce the time required to understand unstructured legal text by transforming documents into structured insights.

Instead of manually searching through pages of text, users can submit a document and receive:

**Document → AI Analysis → Summary + Key Clauses + Entities**

This makes the project useful as a foundation for legal research, contract review, document intelligence, and privacy-focused AI workflows.

---

## Key Features

### AI-Powered Document Summarization

Generates concise, plain-language summaries of legal documents to help users understand the overall purpose and content of a document more quickly.

### Key Clause Extraction

Identifies important contractual clauses, including:

* Termination
* Liability
* Jurisdiction
* Payment Terms
* Confidentiality
* Indemnification

### Named Entity Extraction

Extracts important entities and information such as:

* Parties
* Organizations
* Dates
* Locations
* Laws
* Jurisdictions
* Monetary amounts

### Local LLM Processing

Uses **Ollama** to run the language model locally, reducing reliance on external AI APIs and keeping document processing within the local environment.

### Privacy-Focused Architecture

Legal documents can contain confidential information. The application is designed around local processing so document content does not need to be sent to third-party AI services.

### Simple Web Interface

The Streamlit interface provides an accessible workflow for submitting legal text and reviewing the generated analysis.

### API-Based Architecture

The FastAPI backend exposes an analysis endpoint that separates the AI processing layer from the user interface.

---

## Technology Stack

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Core programming language                  |
| Gemma 2B   | Large language model for document analysis |
| Ollama     | Local LLM runtime                          |
| FastAPI    | Backend API                                |
| Uvicorn    | ASGI server                                |
| Streamlit  | Interactive web interface                  |
| Requests   | Backend/frontend HTTP communication        |
| Pydantic   | Data validation                            |

---

## Architecture

The application follows a simple client-server architecture:

```text
                    ┌──────────────────────┐
                    │     User / Browser   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Streamlit UI     │
                    │      Frontend        │
                    └──────────┬───────────┘
                               │
                               │ HTTP Request
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Ollama         │
                    │     Local LLM        │
                    │      Gemma 2B        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Structured Analysis │
                    │                      │
                    │  • Summary           │
                    │  • Key Clauses       │
                    │  • Named Entities    │
                    └──────────────────────┘
```

---

## How It Works

1. The user provides legal document text through the Streamlit interface.
2. The frontend sends the document to the FastAPI backend.
3. FastAPI processes the request and communicates with the locally hosted Ollama model.
4. Gemma 2B analyzes the legal content.
5. The system extracts:

   * A document summary
   * Important legal clauses
   * Relevant named entities
6. The results are returned to the frontend.
7. The user can review the structured analysis through the web interface.

---

## Project Structure

```text
legal-document-analyzer-ai/
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

## Prerequisites

Before running the application, make sure you have:

* Python 3.8 or higher
* Ollama
* Gemma 2B model
* At least 8 GB RAM recommended
* Sufficient storage for the local model

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/legal-document-analyzer-ai.git
cd legal-document-analyzer-ai
```

### 2. Create a Virtual Environment

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

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Start Ollama

Install Ollama for your operating system and make sure the Ollama service is running.

Then pull the Gemma 2B model:

```bash
ollama pull gemma:2b
```

Start the Ollama service if required:

```bash
ollama serve
```

---

## Running the Application

The application consists of a FastAPI backend and a Streamlit frontend.

### Start the Backend

Open a terminal and run:

```bash
uvicorn backend.main:app --reload
```

The FastAPI server will be available at:

```text
http://localhost:8000
```

### Start the Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

The Streamlit application will be available at:

```text
http://localhost:8501
```

Open the frontend URL in your browser to start analyzing documents.

---

## Usage

### Step 1 — Open the Application

Navigate to:

```text
http://localhost:8501
```

### Step 2 — Provide a Legal Document

Paste legal text into the application or use the included example document.

### Step 3 — Analyze

Submit the document for AI-powered analysis.

### Step 4 — Review the Results

The application generates structured insights including:

* **Summary** — A concise overview of the document
* **Key Clauses** — Important contractual provisions
* **Named Entities** — Parties, dates, locations, laws, and monetary values

---

## Example Input

```text
This Agreement is entered into by Party A and Party B.

Either party may terminate this agreement with thirty (30) days written notice.

Liability shall be limited to direct damages only.

This agreement shall be governed by the laws of the State of California.
```

## Example Analysis

### Summary

The agreement is between Party A and Party B. Either party can terminate the agreement with 30 days' written notice. Liability is limited to direct damages, and California law governs the agreement.

### Key Clauses

```text
Termination:
Either party may terminate with 30 days written notice.

Liability:
Liability is limited to direct damages only.

Jurisdiction:
The agreement is governed by California law.
```

### Named Entities

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

The backend exposes an analysis endpoint for programmatic document processing.

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

The API makes it possible to integrate the document analysis engine with other applications or interfaces beyond Streamlit.

---

## Configuration

The application can be configured to use different local language models supported by Ollama.

For example, the model configuration can be changed in the backend:

```python
MODEL = "gemma:2b"
```

Other compatible local models can be used depending on the implementation and available system resources.

---

## Privacy & Security

Legal documents may contain confidential or sensitive information.

This project is designed with a **local-first processing approach**:

* Documents can be processed locally.
* The LLM runs through Ollama.
* No external AI API key is required for the local inference workflow.
* Document content does not need to be uploaded to a third-party AI provider.

However, users should still follow appropriate security practices when processing confidential legal information on their own machines.

---

## Performance Considerations

Local LLM inference performance depends on available hardware.

For better performance:

* Use a machine with sufficient RAM.
* Use GPU acceleration when supported by your Ollama setup.
* Consider a smaller model for faster inference.
* Avoid unnecessarily large document inputs when possible.

---

## Roadmap

Potential future improvements include:

* [ ] PDF document upload
* [ ] DOCX document upload
* [ ] Multi-document comparison
* [ ] Contract risk detection
* [ ] Clause-level risk scoring
* [ ] Highlighting potentially unusual clauses
* [ ] Document version comparison
* [ ] Export analysis as PDF or DOCX
* [ ] Improved legal entity recognition
* [ ] Authentication and user management
* [ ] Persistent document history
* [ ] Advanced legal-domain models

---

## Disclaimer

This project is intended for **educational, research, and prototype purposes**.

AI-generated analysis should not be treated as professional legal advice. Legal documents and AI-generated interpretations should always be reviewed by a qualified legal professional before making legal or business decisions.

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgments

Built using:

* Ollama for local LLM inference
* Gemma 2B for language understanding
* FastAPI for backend API development
* Streamlit for the interactive frontend
* Python for application development

---

## Author

**Esha Mirza**

GitHub: https://github.com/Esha-Mirza

---

<p align="center">
  Built with Python, FastAPI, Streamlit, Ollama, and Gemma 2B.
</p>
