def enrich_instruction(intent: str, question: str) -> str:
    q = question.lower()

    # smarter overrides based on real student behavior
    if intent == "definition" and "why" in q:
        return "intuition"

    if "how" in q:
        return "mechanism"

    if "difference" in q or "vs" in q:
        return "comparison"

    if "exam" in q or "test" in q:
        return "exam"

    if "example" in q:
        return "definition"

    return intent