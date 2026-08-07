"""URL Shortener API (FastAPI).

Endpoint'ler:
  POST /shorten   -> {"url": "..."} : kısa kod üretir, DB'ye yazar
  GET  /{code}    -> 301 redirect (yoksa 404)
  GET  /health    -> liveness (süreç ayakta mı)
  GET  /ready     -> readiness (DB'ye bağlanabiliyor mu)
  GET  /metrics   -> Prometheus metrikleri
  GET  /          -> basit web arayüzü
"""
import secrets
import string
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, HttpUrl
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from sqlalchemy import text

from pathlib import Path

from .db import engine, get_session, init_db
from .models import Link

# ---- Prometheus metrikleri ----
REQUESTS = Counter(
    "http_requests_total", "Toplam HTTP istekleri", ["method", "path", "status"]
)
LATENCY = Histogram(
    "http_request_duration_seconds", "İstek süresi (sn)", ["method", "path"]
)
LINKS_CREATED = Counter(
    "shortener_links_created_total", "Oluşturulan toplam kısa link sayısı"
)

_ALPHABET = string.ascii_letters + string.digits
_TEMPLATES = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


def _make_code(n: int = 6) -> str:
    return "".join(secrets.choice(_ALPHABET) for _ in range(n))


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="URL Shortener", version="1.0.0", lifespan=lifespan)


@app.middleware("http")
async def _metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    # Rota şablonunu kullan (ör. "/{code}") -> düşük kardinalite
    route = request.scope.get("route")
    path = getattr(route, "path", request.url.path)
    REQUESTS.labels(request.method, path, response.status_code).inc()
    LATENCY.labels(request.method, path).observe(elapsed)
    return response


class ShortenIn(BaseModel):
    url: HttpUrl


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    # Starlette yeni imza: ilk argüman request, sonra template adı.
    return _TEMPLATES.TemplateResponse(request, "index.html")


@app.post("/shorten")
def shorten(body: ShortenIn):
    with get_session() as session:
        code = _make_code()
        while session.get(Link, code) is not None:  # çakışma olmasın
            code = _make_code()
        session.add(Link(code=code, url=str(body.url)))
        session.commit()
    LINKS_CREATED.inc()
    return {"code": code, "short_url": f"/{code}"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception:  # noqa: BLE001
        raise HTTPException(status_code=503, detail="database not ready")
    return {"status": "ready"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


# NOT: parametreli rota EN SONDA tanımlanır ki /health, /metrics vb. ile çakışmasın.
@app.get("/{code}")
def redirect(code: str):
    with get_session() as session:
        link = session.get(Link, code)
        if link is None:
            raise HTTPException(status_code=404, detail="short link not found")
        return RedirectResponse(url=link.url, status_code=301)
