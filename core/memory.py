import json
import os

MEMORY_FILE = "student_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def update_learning_state(topic: str, is_confused: bool = False):
    memory = load_memory()

    if topic not in memory:
        memory[topic] = {
            "attempts": 0,
            "confused": 0,
            "mastery": 0.0
        }

    memory[topic]["attempts"] += 1

    if is_confused:
        memory[topic]["confused"] += 1

    # simple adaptive scoring
    a = memory[topic]["attempts"]
    c = memory[topic]["confused"]

    memory[topic]["mastery"] = max(0, 1 - (c / a))

    save_memory(memory)


def get_mastery(topic: str):
    memory = load_memory()
    return memory.get(topic, {}).get("mastery", 0.0)