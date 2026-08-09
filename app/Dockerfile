
FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt .

# Tüm bağımlılıkları normal şekilde kurar
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


FROM python:3.12-slim

WORKDIR /app

# Non-root kullanıcı oluşturur (güvenlik)
RUN addgroup --system appgroup \
    && adduser --system --ingroup appgroup --no-create-home appuser

# Builder'dan kurulu paketleri ve binary'leri kopyalar
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# Uygulama kodunu kopyalar (templates dahil)
COPY urlshortener/ ./urlshortener/

# Sahipliği non-root kullanıcıya ver
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "urlshortener.main:app", "--host", "0.0.0.0", "--port", "8000"]