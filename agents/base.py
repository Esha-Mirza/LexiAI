import requests
import json

MODEL = "gemma:2b"  # Using faster Gemma:2b
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(prompt: str, temperature: float = 0.3) -> str:
    """
    Call Ollama with Gemma:2b model
    """
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": temperature,
                "max_tokens": 500
            }
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"