from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from . import Base
from .country import Country


class City(Base):
    __tablename__ = "city"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"))
    country: Mapped[Country] = relationship(back_populates="cities", lazy="joined")

    def __repr__(self) -> str:
        return f"(id={self.id!r}, name={self.name!r}, country={self.country.name})"
