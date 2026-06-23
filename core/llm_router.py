import requests
from config import OLLAMA_URL, OLLAMA_MODEL


def route_intent(question: str) -> str:
    prompt = f"""
You are an intent classifier for a Machine Learning tutor system.

Classify the user question into ONE category:

Categories:
- definition
- intuition
- mechanism
- comparison
- exam
- quiz_request

Rules:
- Return ONLY the category name.
- No explanation.
- No extra text.

Question:
{question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip().lower()