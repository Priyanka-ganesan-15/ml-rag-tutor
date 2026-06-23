def build_reasoning_prompt(question: str, context: str) -> str:
    return f"""
You are an expert Machine Learning tutor.

You MUST solve the problem using structured reasoning.

Follow this format:

1. Understand the question
2. Identify relevant concepts
3. Break solution into steps
4. Explain each step simply
5. Give final answer

IMPORTANT:
- No fluff
- No repetition
- Be structured and logical

Context:
{context}

Question:
{question}

Now solve step-by-step:
"""