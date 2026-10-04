from fastapi import APIRouter

from app.services.rag_service import generate_response


router = APIRouter()


@router.get("/ask")
def ask_support(question: str):
    """Answer a customer question using the knowledge base."""
    response = generate_response(question)

    return {
        "question": question,
        "answer": response["answer"],
        "sources": response["sources"],
    }
