# Milestone 1 — Verilen Uygulamayı Anla & Containerize Et 🐳

**Süre:** ~yarım–1 gün · **Amaç:** **Dev ekibinden gelen** uygulamayı incelemek, **Dockerfile +
docker-compose yazmak** (containerization = DevOps işi) ve local'de uçtan uca çalıştırmak.

> 🧑‍💻 **Senaryo:** Uygulamayı **dev ekibi yazdı ve teslim etti** (`app/` klasörü). **Siz
> uygulama koduna DOKUNMAZSINIZ** — işiniz onu paketleyip çalıştırmak, sonra pipeline'a ve
> AWS'e taşımak.

Branch: `git checkout -b milestone/01-docker`

## Önce: verilen uygulamayı tanıyın
`app/README-DEV.md`'yi okuyun. Kısaca (URL kısaltıcı, Python/FastAPI + Postgres):
- Endpoint'ler: `POST /shorten`, `GET /{code}` (301), `GET /health`, `GET /ready`, `GET /metrics`, `GET /`
- Config: **`DATABASE_URL`** ortam değişkeninden (koda gömülü değil)
- Port: **8000** · Testler: `pytest` (SQLite ile, DB gerektirmez)

## Yapılacaklar (uygulama koduna dokunmadan)
1. **Testleri çalıştırın** (dev ekibinin işini doğrulayın):
   ```bash
   cd app && pip install -r requirements.txt && pytest -q
   ```
2. **`app/Dockerfile` yazın:** slim Python base, bağımlılıkları kur, `urlshortener` paketini
   kopyala, **non-root** kullanıcı, `EXPOSE 8000`, `uvicorn urlshortener.main:app` ile başlat.
   Bir **`.dockerignore`** ekleyin.
3. **`app/docker-compose.yml` yazın:** iki servis — **app** (build: .) + **postgres**.
   - `DATABASE_URL=postgresql+psycopg2://appuser:changeme@db:5432/urls` (dummy şifre).
   - Postgres için healthcheck; app `depends_on: db (healthy)`.
4. **Çalıştırın ve doğrulayın:**
   ```bash
   docker compose up --build      # http://localhost:8000
   # UI'dan bir URL kısaltın; kısa linkin yönlendirdiğini görün.
   curl localhost:8000/health ; curl localhost:8000/ready ; curl -s localhost:8000/metrics | head
   ```

## Definition of Done ✅
- [ ] Dev ekibinin testleri yeşil (`pytest`)
- [ ] Kendi yazdığınız Dockerfile ile image build oluyor (non-root, slim)
- [ ] `docker compose up` ile app + Postgres birlikte çalışıyor; UI + redirect + `/metrics` OK
- [ ] Uygulama koduna **dokunulmadı** · Secret dummy · PR (mentor review) → merge

## Neden önemli? 🎯
Gerçek DevOps'ta uygulamayı çoğu zaman **başka bir ekip** yazar; sizin işiniz onu güvenilir,
tekrar üretilebilir şekilde **paketleyip çalıştırmaktır**. Doğru bir Dockerfile, tüm hattın temelidir.
