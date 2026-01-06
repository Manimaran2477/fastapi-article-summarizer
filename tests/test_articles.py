import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_article(monkeypatch):
    # mock external API response
    async def mock_fetch_article(url: str):
        return {
            "title": "Test Article",
            "body": "This is a test article body"
        }

    monkeypatch.setattr(
        "app.services.external_api.fetch_article",
        mock_fetch_article
    )

    response = client.post(
        "/articles",
        json={"source_url": "https://example.com/test"}
    )

    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Article"
    assert data["summary"] == "This is a test article body"[:100]


def test_get_article_not_found():
    response = client.get("/articles/invalid-id")
    assert response.status_code == 404
