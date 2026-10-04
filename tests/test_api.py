from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def mock_generate_answer(question: str, context: list[str]) -> str:
    """Return deterministic answers for API tests."""

    if "refund" in question.lower():
        return (
            "Customers can request a refund within 14 days of their initial purchase."
        )

    return "I'm sorry, I couldn't find that information in the knowledge base."


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@patch("app.services.rag_service.generate_answer", side_effect=mock_generate_answer)
def test_support_question(mock_generate):
    response = client.get(
        "/support/ask",
        params={"question": "What is the refund policy?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert "14 days" in data["answer"]
    assert len(data["sources"]) > 0


@patch("app.services.rag_service.generate_answer", side_effect=mock_generate_answer)
def test_unknown_question(mock_generate):
    response = client.get(
        "/support/ask",
        params={"question": "What is NovaTech mobile phone price?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert "couldn't find" in data["answer"].lower()
