from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from .country import Country
from .city import City
