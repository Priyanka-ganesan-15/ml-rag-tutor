def should_use_socratic_mode(question: str, intent: str) -> bool:
    q = question.lower()

    triggers = [
        "why",
        "how",
        "explain",
        "what happens",
        "difference",
        "vs"
    ]

    return any(t in q for t in triggers) or intent in ["intuition", "comparison"]