"""Temel testler. Varsayılan SQLite ile çalışır (Postgres gerekmez)."""
import os

os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from urlshortener.main import app  # noqa: E402


@pytest.fixture(scope="module")
def client():
    # Context manager -> lifespan (startup) çalışır ve init_db() tabloları oluşturur.
    with TestClient(app) as c:
        yield c


def test_index_page(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "URL Shortener" in r.text


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_ready(client):
    r = client.get("/ready")
    assert r.status_code == 200
    assert r.json()["status"] == "ready"


def test_shorten_then_redirect(client):
    r = client.post("/shorten", json={"url": "https://example.com/path"})
    assert r.status_code == 200
    code = r.json()["code"]
    assert code and len(code) == 6

    r2 = client.get(f"/{code}", follow_redirects=False)
    assert r2.status_code == 301
    assert r2.headers["location"].startswith("https://example.com")


def test_unknown_code_404(client):
    r = client.get("/thiscodedoesnotexist", follow_redirects=False)
    assert r.status_code == 404


def test_invalid_url_rejected(client):
    r = client.post("/shorten", json={"url": "not-a-url"})
    assert r.status_code == 422  # pydantic doğrulama hatası


def test_metrics_exposed(client):
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_requests_total" in r.text
