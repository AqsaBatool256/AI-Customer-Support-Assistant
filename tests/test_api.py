from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_support_question():
    response = client.get(
        "/support/ask",
        params={"question": "What is the refund policy?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert "14 days" in data["answer"]
    assert len(data["sources"]) > 0


def test_unknown_question():
    response = client.get(
        "/support/ask",
        params={"question": "What is NovaTech mobile phone price?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert "couldn't find" in data["answer"].lower()
