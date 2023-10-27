from sqlalchemy import select, delete, update, and_

from models.city import City
from client.db import _sessionmaker


async def select_city_by_id(country_id: int, city_id: int) -> City | None:
    session = _sessionmaker()
    async with session.begin():
        query = select(City).where(
            and_(City.id == city_id, City.country_id == country_id)
        )
        data = await session.scalar(query)
    await session.close()
    if data:
        return data
    return


async def delete_city(city_id: int):
    session = _sessionmaker()
    async with session.begin():
        query = delete(City).where(City.id == city_id)
        session.execute(query)
    await session.close()


async def insert_city(city: City) -> City:
    session = _sessionmaker()
    session.add(city)
    await session.commit()
    await session.refresh(city)
    await session.close()
    return city


async def get_cities() -> list[City]:
    session = _sessionmaker()
    async with session.begin():
        query = select(City).order_by(City.id)
        data = await session.scalars(query)
        result = data.unique()
    await session.close()
    return result


async def update_city(city: City) -> City:
    session = _sessionmaker()
    async with session.begin():
        query = (
            update(City)
            .where(City.id == city.id)
            .values(name=city.name, country_id=city.country_id)
        )
        await session.execute(query)
    await session.close()
    return city
