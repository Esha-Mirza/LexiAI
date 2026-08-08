from fastapi import FastAPI, Form
import sys
import os
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.base import call_llm

app = FastAPI(title="Legal Document Analyzer", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Legal Document Analyzer API"}

@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    # 1. Summary
    summary_prompt = f"""
Summarize this legal document in 2-3 sentences:
{text}

Summary:
"""
    summary = call_llm(summary_prompt)
    
    # 2. Key Clauses
    clauses_prompt = f"""
Extract these key clauses from this legal document:
1. Termination
2. Liability
3. Jurisdiction
4. Confidentiality

Format:
Termination: [details]
Liability: [details]
Jurisdiction: [details]
Confidentiality: [details]

Document:
{text}

Clauses:
"""
    clauses = call_llm(clauses_prompt)
    
    # 3. Named Entities
    entities_prompt = f"""
Extract named entities from this legal document:
1. Parties (names)
2. Dates
3. Locations/Addresses
4. Monetary amounts

Format:
Parties: [list]
Dates: [list]
Locations: [list]
Monetary: [list]

Document:
{text}

Entities:
"""
    entities = call_llm(entities_prompt)
    
    return {
        "summary": summary,
        "clauses": clauses,
        "entities": entities
    }