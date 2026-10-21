"""Tests for the /api/v1/health endpoint."""
from fastapi.testclient import TestClient

from app.core.config import settings

HEALTH_URL = "/api/v1/health"


def test_health_returns_ok(client: TestClient) -> None:
    response = client.get(HEALTH_URL)

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": settings.version}


def test_health_is_only_served_under_v1_prefix(client: TestClient) -> None:
    assert client.get("/health").status_code == 404


def test_health_rejects_post(client: TestClient) -> None:
    assert client.post(HEALTH_URL).status_code == 405


def test_health_is_documented_in_openapi(client: TestClient) -> None:
    paths = client.get("/openapi.json").json()["paths"]

    assert HEALTH_URL in paths
    assert "get" in paths[HEALTH_URL]
