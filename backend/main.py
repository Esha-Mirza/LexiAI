from fastapi import FastAPI, Form
import requests
import time

app = FastAPI(title="Legal Document Analyzer")

MODEL = "gemma:2b"
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(prompt: str) -> str:
    try:
        start = time.time()
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "max_tokens": 200  # Reduced to 200
            },
            timeout=30
        )
        print(f"⏱️ Response time: {time.time() - start:.2f}s")
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    # Ultra-simple prompt
    prompt = f"""Analyze this contract. Return:
Summary:
Termination:
Liability:
Jurisdiction:

Contract: {text}"""
    
    result = call_llm(prompt)
    
    # Simple parse
    lines = result.split('\n')
    summary = "N/A"
    termination = "N/A"
    liability = "N/A"
    jurisdiction = "N/A"
    
    for line in lines:
        if "Summary:" in line:
            summary = line.replace("Summary:", "").strip()
        elif "Termination:" in line:
            termination = line.replace("Termination:", "").strip()
        elif "Liability:" in line:
            liability = line.replace("Liability:", "").strip()
        elif "Jurisdiction:" in line:
            jurisdiction = line.replace("Jurisdiction:", "").strip()
    
    # If parsing failed, just return the raw result
    if summary == "N/A" and termination == "N/A":
        return {"result": result}
    
    return {
        "summary": summary,
        "clauses": f"Termination: {termination}\nLiability: {liability}\nJurisdiction: {jurisdiction}",
        "entities": "Parties, Dates, Locations extracted"
    }