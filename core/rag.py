from core.llm_router import route_intent
from core.embedder import embed
from core.llm import generate_answer
from core.templates import TEMPLATES
from core.reranker import rerank

from core.socratic import should_use_socratic_mode
from core.reasoning_planner import build_reasoning_prompt

from core.memory import update_learning_state
from core.session_memory import add_turn, load_session

import chromadb
from config import DB_PATH, COLLECTION_NAME

db = chromadb.PersistentClient(path=DB_PATH)
collection = db.get_collection(COLLECTION_NAME)


# -----------------------------
# LIGHT TOPIC DETECTION
# -----------------------------
def detect_topic(question: str):
    q = question.lower()

    if "supervised" in q:
        return "supervised learning"
    if "unsupervised" in q:
        return "unsupervised learning"
    if "overfitting" in q:
        return "overfitting"
    if "gradient descent" in q:
        return "gradient descent"

    return None


# -----------------------------
# MAIN RAG TUTOR ENGINE
# -----------------------------
def ask(question: str):

    # 1. Intent classification (LLM router)
    intent = route_intent(question)

    valid_intents = [
        "definition",
        "intuition",
        "mechanism",
        "comparison",
        "exam",
        "quiz_request"
    ]

    if intent not in valid_intents:
        intent = "definition"

    # 2. Retrieve from vector DB
    results = collection.query(
        query_embeddings=[embed(question)],
        n_results=12,
        include=["documents", "metadatas"]
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    docs_with_meta = list(zip(docs, metas))

    # 3. Topic detection
    topic = detect_topic(question)

    # 4. Light filtering (keep fallback safe)
    if topic:
        filtered_docs = [
            d for d in docs_with_meta
            if topic.lower() in d[0].lower()
        ]
    else:
        filtered_docs = docs_with_meta

    if len(filtered_docs) == 0:
        filtered_docs = docs_with_meta

    # 5. Rerank
    top_docs = rerank(question, filtered_docs)

    # 6. Build context
    context = "\n\n".join([
        f"{doc}\n(Source: {meta.get('source', 'unknown')})"
        for doc, meta in top_docs
    ])

    # 7. Socratic mode detection
    socratic = should_use_socratic_mode(question, intent)

    # 8. Reasoning planner (for deep mechanism questions)
    if intent == "mechanism":
        instruction = build_reasoning_prompt(question, context)
    else:
        instruction = TEMPLATES.get(intent, TEMPLATES["definition"])

    # 9. Generate main answer
    answer = generate_answer(context, question, instruction)

    # -----------------------------
    # 10. SOCrATIC FOLLOW-UP
    # -----------------------------
    if socratic:
        history = load_session()
        last_q = history["history"][-1]["question"] if history["history"] else ""

        socratic_prompt = f"""
You are a Socratic Machine Learning tutor.

Ask ONE follow-up question that:
- tests understanding
- is specific to the concept
- is slightly harder than before
- is NOT generic

Student question: {question}
Previous question: {last_q}
Answer given: {answer}

Return ONLY the question.
"""

        follow_up = generate_answer(context, question, socratic_prompt)
        answer += f"\n\n🤔 Think about this:\n{follow_up.strip()}"

    # -----------------------------
    # 11. MEMORY UPDATES
    # -----------------------------

    if topic:
        is_confused = any(x in question.lower() for x in [
            "not sure", "don't understand", "confused", "what?"
        ])

        update_learning_state(topic, is_confused=is_confused)

    # -----------------------------
    # 12. SESSION MEMORY (conversation tracking)
    # -----------------------------
    add_turn(question, answer)

    return answer