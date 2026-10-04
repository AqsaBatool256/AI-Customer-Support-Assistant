import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# Find the project root:
# AI-Customer-Support-Assistant/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Explicitly load the .env file from the project root.
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=ENV_FILE)


MODEL_NAME = "gemini-3.8-flash"

client = None


def generate_answer(question: str, context: list[str]) -> str:
    """Generate an answer using the retrieved context."""

    global client

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    if client is None:
        client = genai.Client(api_key=api_key)

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
