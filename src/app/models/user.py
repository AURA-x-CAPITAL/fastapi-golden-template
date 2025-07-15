from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.db.base import Base, TableNameMixin, TimestampMixin


class User(Base, TableNameMixin, TimestampMixin):
    username: Mapped[str | None] = mapped_column(String, unique=True, index=True)
