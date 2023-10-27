from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from models import Base


class Country(Base):
    __tablename__ = "country"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    cities: Mapped[List["City"]] = relationship(
        "City", back_populates="country", lazy="joined"
    )

    def __repr__(self) -> str:
        return f"(id={self.id!r}, name={self.name!r})"
