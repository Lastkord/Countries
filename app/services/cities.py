from repositories.cities import (
    select_city_by_id,
    delete_city,
    insert_city,
    get_cities,
    update_city,
)
from schemas.country import CreateCitySchema
from models.city import City


def map_city(city: City) -> dict:
    return {"id": city.id, "name": city.name}


def map_city_with_country(city: City) -> dict:
    return {"id": city.id, "name": city.name, "country_id": city.country_id}


async def get_all_cities():
    cities = await get_cities()
    return [map_city_with_country(city=city) for city in cities]


async def create_city(payload: CreateCitySchema):
    city = await insert_city(City(name=payload.name, country_id=payload.country_id))
    return map_city_with_country(city=city)


async def get_city_by_pk(country_id: int, citi_id: int):
    city = await select_city_by_id(country_id, citi_id)
    if city:
        return map_city(city=city)
    return


async def delete_city_by_id(city_id: int):
    await delete_city(city_id)


async def update_city_async(payload: CreateCitySchema, city_id: int):
    city = await update_city(
        City(id=city_id, name=payload.name, country_id=payload.country_id)
    )
    return map_city(city=city)
