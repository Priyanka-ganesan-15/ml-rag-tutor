def detect_confusion(question: str, answer: str) -> bool:
    weak_signals = [
        "i don't know",
        "not sure",
        "unclear",
        "explain again",
        "confused"
    ]

    q = question.lower()
    a = answer.lower()

    # user confusion signals
    if any(w in q for w in weak_signals):
        return True

    # very short or weak answer signal
    if len(a.split()) < 60:
        return True

    return False