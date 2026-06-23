import json
import os

SESSION_FILE = "session_memory.json"


def load_session():
    if not os.path.exists(SESSION_FILE):
        return {"history": []}
    with open(SESSION_FILE, "r") as f:
        return json.load(f)


def save_session(data):
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_turn(question, answer):
    session = load_session()

    session["history"].append({
        "question": question,
        "answer": answer
    })

    # keep last 10 turns only
    session["history"] = session["history"][-10:]

    save_session(session)