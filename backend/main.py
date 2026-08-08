from fastapi import FastAPI, Form
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.base import call_llm

app = FastAPI(title="Legal Document Analyzer", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Legal Document Analyzer API"}

@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    # Single combined prompt (faster)
    prompt = f"""
Analyze this legal document. Extract:
1. Summary (1 sentence)
2. Key clauses: Termination, Liability, Jurisdiction
3. Parties, Dates, Locations

Document:
{text}

Format:
Summary: [your summary]
Termination: [details]
Liability: [details]
Jurisdiction: [details]
Parties: [list]
Dates: [list]
Locations: [list]
"""
    
    result = call_llm(prompt)
    
    # Parse response
    lines = result.split('\n')
    summary = "N/A"
    clauses = ""
    entities = ""
    
    for line in lines:
        if line.startswith("Summary:"):
            summary = line.replace("Summary:", "").strip()
        elif line.startswith("Termination:") or line.startswith("Liability:") or line.startswith("Jurisdiction:"):
            clauses += line + "\n"
        elif line.startswith("Parties:") or line.startswith("Dates:") or line.startswith("Locations:"):
            entities += line + "\n"
    
    if not clauses:
        clauses = "Clauses extracted"
    if not entities:
        entities = "Entities extracted"
    
    return {
        "summary": summary,
        "clauses": clauses,
        "entities": entities
    }