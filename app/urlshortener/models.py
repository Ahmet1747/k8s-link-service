"""Veritabanı modelleri."""
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class Link(Base):
    __tablename__ = "links"

    code: Mapped[str] = mapped_column(String(16), primary_key=True, index=True)
    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
