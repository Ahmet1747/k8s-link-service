# 📦 URL Shortener — Dev Ekibi Teslim Notu

> Bu servisi **dev ekibi** yazıp teslim etti. **DevOps ekibi (siz)** bunu deploy edip
> izleyecek. **Uygulama koduna dokunmayın** — işiniz containerize + CI/CD + altyapı + deploy
> + observability. (Dockerfile/compose'u da **siz** yazacaksınız — bkz. Milestone 1.)

## Ne yapar?
Uzun URL'leri kısaltan küçük bir servis (FastAPI + Postgres).

## Endpoint'ler
| Method | Path | Açıklama |
|--------|------|----------|
| POST | `/shorten` | Gövde: `{"url": "https://..."}` → `{"code": "...", "short_url": "/..."}` |
| GET | `/{code}` | Kısa kodu **301** ile uzun URL'ye yönlendirir; yoksa **404** |
| GET | `/health` | **Liveness** — süreç ayakta mı (`{"status":"ok"}`) |
| GET | `/ready` | **Readiness** — DB'ye bağlanabiliyor mu (bağlanamazsa **503**) |
| GET | `/metrics` | **Prometheus** metrikleri |
| GET | `/` | Basit web arayüzü |

> Deploy'da **probe eşlemesi:** liveness → `/health`, readiness → `/ready`.

## Ortam değişkenleri
| Değişken | Açıklama | Örnek |
|----------|----------|-------|
| `DATABASE_URL` | Veritabanı bağlantısı | `postgresql+psycopg2://appuser:***@host:5432/urls` |

- Varsayılan (ayarlanmazsa): **SQLite** (`sqlite:///./urls.db`) — kurulum gerektirmez, **testler bununla çalışır**.
- Prod: **Postgres** (ör. AWS RDS). **Şifreyi koda/rezerve yazmayın** — env/Secret ile verin.

## Metrikler (Prometheus)
- `http_requests_total{method,path,status}` — istek sayısı
- `http_request_duration_seconds{method,path}` — süre histogramı (p95/p99 için)
- `shortener_links_created_total` — oluşturulan kısa link sayısı

## Yerelde nasıl çalışır (dev notu)
```bash
pip install -r requirements.txt
# testler (SQLite ile, DB gerektirmez):
pytest -q
# uygulamayı çalıştır:
uvicorn urlshortener.main:app --reload
# -> http://localhost:8000
```

> 🐳 **Docker ile test (Milestone 1):** `Dockerfile` ve `docker-compose.yml` bu klasörde
> **yoktur** — onları **siz (DevOps ekibi)** yazacaksınız. Hazırladıktan sonra uygulamayı
> + Postgres'i birlikte tek komutla local'de test edebilirsiniz:
> ```bash
> docker compose up --build   # -> http://localhost:8000
> ```

## Proje yapısı
```
app/
├── urlshortener/
│   ├── main.py        # API + metrikler + UI
│   ├── db.py          # DATABASE_URL'den bağlantı (Postgres/SQLite)
│   ├── models.py      # Link tablosu
│   └── templates/     # web arayüzü
├── tests/             # pytest
├── requirements.txt   # bağımlılıklar (runtime + test)
└── .env.example
```

## DevOps ekibine notlar (handoff)
- Uygulama **stateless**; tüm durum **Postgres**'te → deploy'da bir DB (RDS) bağlayın.
- `DATABASE_URL` **dışarıdan** verilir (ConfigMap/Secret). Şifre **Secret**.
- `/ready` DB'ye bağlı olduğu için, DB ayakta değilse pod **Ready olmaz** — bu beklenen davranış.
- Port: **8000**.
