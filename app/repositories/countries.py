from sqlalchemy import select, delete, update

from models.country import Country
from models.city import City
from client.db import _sessionmaker


async def get_country_by_pk(country_id: int) -> Country:
    session = _sessionmaker()
    async with session.begin():
        query = select(Country, City).where(Country.id == country_id)
        data = await session.scalar(query)
    await session.close()
    if data:
        return data
    return None


async def update_country(country: Country) -> Country:
    session = _sessionmaker()
    async with session.begin():
        query = (
            update(Country).where(Country.id == country.id).values(name=country.name)
        )
        await session.execute(query)
    await session.close()
    return country


async def get_all_countries_asy():
    session = _sessionmaker()
    async with session.begin():
        query = select(Country)
        data = await session.scalars(query)
        result = data.unique()
    await session.close()
    return result


async def insert_country(country: Country) -> Country:
    session = _sessionmaker()
    session.add(country)
    await session.commit()
    await session.refresh(country)
    await session.close()
    return country


async def del_country(country_id: int):
    session = _sessionmaker()
    async with session.begin():
        query = delete(Country).where(Country.id == country_id)
        await session.execute(query)
    await session.close()


async def select_city_by_id(country_id: int, city_id: int) -> City:
    session = _sessionmaker()
    async with session.begin():
        query = select(City).where(City.id == city_id, City.country_id == country_id)
        data = await session.scalar(query)
    await session.close()
    if data:
        return data
    return None


async def delete_city(city_id: int):
    session = _sessionmaker()
    async with session.begin():
        query = delete(City).where(City.id == city_id)
        session.execute(query)
    await session.close()


async def insert_city(city: City):
    session = _sessionmaker()
    session.add(city)
    await session.commit()
    await session.refresh(city)
    await session.close()
    return city


async def get_cities() -> list:
    session = _sessionmaker()
    async with session.begin():
        query = select(City)
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
