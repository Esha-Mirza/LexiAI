"""
LexiAI - Flask front end (UI layer only).

This file does NOT contain any analysis logic. It serves the HTML/CSS/JS
interface and forwards requests, unchanged, to the existing FastAPI backend
(backend/main.py) using exactly the same endpoints and payloads that the
Streamlit app (frontend/app.py) used:

    POST   /analyze/        form field: text
    GET    /history/
    DELETE /history/{id}
    DELETE /history/

Run the backend first, then:   python frontend/flask_app.py
"""
import os

import requests
from flask import Flask, jsonify, render_template, request

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

app = Flask(__name__, template_folder="templates", static_folder="static")


def _forward(method: str, path: str, timeout: int, **kwargs):
    """Send a request to the FastAPI backend and relay its JSON + status code."""
    try:
        resp = requests.request(method, f"{BACKEND_URL}{path}", timeout=timeout, **kwargs)
        try:
            payload = resp.json()
        except ValueError:
            payload = {"error": resp.text}
        return jsonify(payload), resp.status_code
    except Exception as e:  # backend down, timeout, etc.
        return jsonify({"error": str(e)}), 502


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/analyze")
def analyze():
    text = request.form.get("text", "")
    return _forward("POST", "/analyze/", timeout=120, data={"text": text})


@app.get("/api/history")
def history():
    return _forward("GET", "/history/", timeout=10)


@app.delete("/api/history/<int:doc_id>")
def delete_history_item(doc_id: int):
    return _forward("DELETE", f"/history/{doc_id}", timeout=10)


@app.delete("/api/history")
def clear_history():
    return _forward("DELETE", "/history/", timeout=10)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
