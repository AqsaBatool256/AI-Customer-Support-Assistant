from app.services.llm_service import generate_answer
from app.services.vector_store import search_documents


def generate_response(question: str):
    """Retrieve relevant documents and generate an AI answer."""

    results = search_documents(question, limit=3)

    if not results:
        return {
            "answer": "I'm sorry, I couldn't find an answer in the knowledge base.",
            "sources": [],
        }

    answer = generate_answer(question, results)

    return {
        "answer": answer,
        "sources": results,
    }
