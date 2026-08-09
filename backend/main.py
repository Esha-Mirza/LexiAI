from fastapi import FastAPI, Form
from tinydb import TinyDB, Query
import requests
import time
import datetime
import os

app = FastAPI(title="Legal Document Analyzer")

MODEL = "tinyllama"
OLLAMA_URL = "http://localhost:11434/api/generate"

# TinyDB setup
os.makedirs("memory", exist_ok=True)
db = TinyDB("memory/legal_analysis_db.json")


def call_llm(prompt: str) -> str:
    try:
        start = time.time()
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "max_tokens": 300
            },
            timeout=90
        )
        print(f"⏱️ Response time: {time.time() - start:.2f}s")
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"


@app.get("/")
def root():
    return {"message": "Legal Document Analyzer API"}


@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    prompt = f"""Analyze this contract. Return exactly these five lines, each starting with the label shown:
Summary:
Termination:
Liability:
Jurisdiction:
Entities:

Contract: {text}"""

    result = call_llm(prompt)

    summary = "N/A"
    termination = "N/A"
    liability = "N/A"
    jurisdiction = "N/A"
    entities = "N/A"

    for line in result.split('\n'):
        line = line.strip()
        if line.lower().startswith("summary:"):
            summary = line.split(":", 1)[1].strip()
        elif line.lower().startswith("termination:"):
            termination = line.split(":", 1)[1].strip()
        elif line.lower().startswith("liability:"):
            liability = line.split(":", 1)[1].strip()
        elif line.lower().startswith("jurisdiction:"):
            jurisdiction = line.split(":", 1)[1].strip()
        elif line.lower().startswith("entities:"):
            entities = line.split(":", 1)[1].strip()

    if summary == "N/A" and termination == "N/A" and entities == "N/A":
        response_data = {"result": result}
    else:
        clauses = f"Termination: {termination}\nLiability: {liability}\nJurisdiction: {jurisdiction}"
        response_data = {
            "summary": summary,
            "clauses": clauses,
            "entities": entities
        }

    # Save to TinyDB
    db.insert({
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
        "input_text": text,
        "result": response_data
    })

    return response_data


@app.get("/history/")
def get_history():
    records = db.all()
    # Attach TinyDB's internal doc_id so the frontend can reference specific entries
    for i, record in enumerate(records):
        record["id"] = db.all()[i].doc_id if False else None
    # Simpler: rebuild with real doc_ids
    all_docs = db.all()
    out = []
    for doc in all_docs:
        out.append({"id": doc.doc_id, **doc})
    return list(reversed(out))  # most recent first


@app.delete("/history/{doc_id}")
def delete_history_item(doc_id: int):
    Doc = Query()
    db.remove(doc_ids=[doc_id])
    return {"status": "deleted", "id": doc_id}


@app.delete("/history/")
def clear_history():
    db.truncate()
    return {"status": "cleared"}