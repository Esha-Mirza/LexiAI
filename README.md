# Legal Document Analyzer

An AI-powered legal document analyzer that extracts summaries, key clauses, and named entities from legal texts for LexPro Law Firm.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Sample Legal Document](#sample-legal-document)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Sample Input](#sample-input)
- [Sample Output](#sample-output)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application helps legal professionals quickly analyze contracts, case files, and court rulings. It automatically extracts key information — document summaries, critical clauses (Termination, Liability, Jurisdiction, etc.), and named entities (parties, dates, locations, laws) — from unstructured legal text.

The application runs entirely locally, ensuring client confidentiality and eliminating API costs. It uses Ollama to host the LLaMA 2 model, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Document Summarization** — Generates plain-language summaries of legal documents
- **Key Clause Extraction** — Identifies and extracts critical clauses:
  - Termination
  - Liability
  - Jurisdiction
  - Payment Terms
  - Confidentiality
  - Indemnification
- **Named Entity Recognition** — Extracts:
  - Parties involved
  - Dates
  - Locations/Addresses
  - Laws and jurisdictions
  - Monetary amounts
- **Export Ready** — Download results for legal workflows
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for legal text analysis |
| **Ollama** | Local LLM hosting and inference |
| **FastAPI** | Backend API framework |
| **Streamlit** | Frontend user interface |
| **Requests** | HTTP client for API communication |
| **Uvicorn** | ASGI server for FastAPI |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | Version 3.8 or higher |
| **Ollama** | Installed and running |
| **LLaMA 2 Model** | Downloaded via Ollama |
| **RAM** | 8GB+ recommended |
| **Storage** | 4GB+ free space for model |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship/"Project-8 Legal Doc Summarizer"
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull LLaMA 2 Model via Ollama

```bash
ollama pull llama2
```

This downloads the LLaMA 2 model (~3.8 GB). Alternatively, you can use a smaller model:

```bash
ollama pull phi3        # 2.2 GB, faster inference
ollama pull gemma:2b    # 1.4 GB, lightest option
```

---

## Sample Legal Document

The project includes a sample contract in `data/example_contract.txt`:

```text
MASTER SERVICES AGREEMENT

This Master Services Agreement (the "Agreement") is entered into as of January 15, 2024, by and between LexPro Law Firm, with its principal place of business at 123 Legal Street, New York, NY 10001 ("LexPro"), and TechCorp Inc., with its principal place of business at 456 Innovation Drive, San Francisco, CA 94105 ("Client").

1. TERM AND TERMINATION
This Agreement shall commence on the Effective Date and continue for a period of two (2) years. Either party may terminate this Agreement with thirty (30) days written notice.

2. LIMITATION OF LIABILITY
In no event shall LexPro be liable for any indirect, incidental, special, consequential, or punitive damages. LexPro's total liability shall not exceed the total fees paid by Client.

3. JURISDICTION AND GOVERNING LAW
This Agreement shall be governed by and construed in accordance with the laws of the State of New York.

4. CONFIDENTIALITY
LexPro agrees to hold in confidence all confidential information received from Client.

5. PAYMENT TERMS
Client shall pay LexPro the sum of $10,000 USD per month for legal services rendered.
```

---

## Running the Application

**Terminal 1: Start Ollama Service**

```bash
ollama serve
```

**Terminal 2: Start Backend (FastAPI)**

```bash
uvicorn backend.main:app --reload
```

The backend will be available at: `http://localhost:8000`

**Terminal 3: Start Frontend (Streamlit)**

```bash
streamlit run frontend/app.py
```

The frontend will open at: `http://localhost:8501`

---

## Usage

1. Open your browser and navigate to `http://localhost:8501`
2. Paste a legal document in the text area or load the sample
3. Click the **Analyze** button
4. View the results in three tabs:
   - **Summary** — Plain-language document summary
   - **Key Clauses** — Extracted clauses with details
   - **Named Entities** — Parties, dates, locations, laws, amounts

---

## Sample Input

```text
This Agreement is entered into by Party A and Party B. Either party may terminate this agreement with thirty (30) days written notice. Liability shall be limited to direct damages only. This agreement shall be governed by the laws of the State of California.
```

---

## Sample Output

**Summary:**

```text
This is a simple agreement between Party A and Party B that allows either party to terminate with 30 days' notice, limits liability to direct damages, and is governed by California law.
```

**Key Clauses:**

```text
Termination: Either party may terminate with 30 days written notice.
Liability: Limited to direct damages only.
Jurisdiction: Governed by the laws of the State of California.
```

**Named Entities:**

```text
Parties: Party A, Party B
Locations: State of California
Laws: California law
```

---

## API Endpoints

### `POST /analyze/`

**Request:**

```json
{
  "text": "Your legal document text..."
}
```

**Response:**

```json
{
  "summary": "Document summary...",
  "clauses": "Extracted clauses...",
  "entities": "Named entities..."
}
```

---

## Project Structure

```
Project-8 Legal Doc Summarizer/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── data/
│   └── example_contract.txt
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Configuration

### Changing the Model

To use a different model, modify `backend/main.py`:

```python
MODEL = "phi3"           # Change from "llama2" to your preferred model
```

### Changing the Port

**Backend Port** (default: 8000):

```bash
uvicorn backend.main:app --reload --port 8001
```

**Frontend Port** (default: 8501):

```bash
streamlit run frontend/app.py --server.port 8502
```

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Model not found | Run `ollama pull llama2` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |
| No results | Ensure the document is not empty and contains legal text |

---

## Roadmap

- [ ] Add clause-risk flagging (highlight unusually one-sided or non-standard clauses)
- [ ] Add support for multi-document comparison (redlining between contract versions)
- [ ] Add PDF/DOCX direct upload instead of pasted text only

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Disclaimer

**Educational/Prototype Use Only** — This is NOT certified legal advice. Always review AI-generated analysis with a qualified attorney.

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- Meta - LLaMA 2 model
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
