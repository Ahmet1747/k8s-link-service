"""Veritabanı bağlantısı.

DATABASE_URL ortam değişkeninden okunur (koda gömülü değil):
- Yerel/test: varsayılan SQLite (kurulum gerektirmez)
- Prod: Postgres (ör. RDS)  ->  postgresql+psycopg2://user:pass@host:5432/urls
"""
import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./urls.db")

# SQLite tek dosya + çok thread için özel ayar; Postgres'te gerekmez.
_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=_connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def init_db() -> None:
    """Tabloları oluştur (yoksa). Basit lab; migration aracı kullanılmıyor."""
    # models import edilmeli ki tablolar Base.metadata'ya kaydolsun
    from . import models  # noqa: F401

    Base.metadata.create_all(engine)


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
