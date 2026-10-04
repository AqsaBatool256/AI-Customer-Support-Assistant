import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"


def generate_answer(question: str, context: list[str]) -> str:
    """Generate an answer using the retrieved context."""

    context_text = "\n\n".join(context)

    prompt = f"""
You are NovaTech's customer support assistant.

Answer the customer's question using ONLY the information provided in the context.

If the answer cannot be found in the context, say:
"I'm sorry, I couldn't find that information in the knowledge base."

Do not invent information.

Context:
{context_text}

Customer question:
{question}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )

    response.raise_for_status()

    return response.json()["response"].strip()
