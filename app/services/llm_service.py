import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.8-flash"

client = None


def generate_answer(question: str, context: list[str]) -> str:
    """Generate an answer using the retrieved context."""

    global client

    if client is None:
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not configured.")

        client = genai.Client(api_key=GEMINI_API_KEY)

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

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text.strip()
