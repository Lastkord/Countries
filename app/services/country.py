from repositories.countries import (
    get_country_by_pk,
    get_all_countries_asy,
    insert_country,
    del_country,
    update_country as put_country,
)
from schemas.country import CreateCountrySchema
from models.country import Country
from services.cities import map_city


def map_country(country: Country) -> dict:
    return {"id": country.id, "name": country.name}


def map_country_with_cities(country: Country) -> dict:
    return {
        "id": country.id,
        "name": country.name,
        "cities": [map_city(city=city) for city in country.cities],
    }


async def get_country_by_id(country_id: int):
    country = await get_country_by_pk(country_id=country_id)
    if country:
        return map_country_with_cities(country)


async def get_all_countries():
    countries = await get_all_countries_asy()
    return [map_country(country) for country in countries]


async def create_country(payload: CreateCountrySchema) -> dict:
    country = await insert_country(Country(name=payload.name))
    return map_country(country)


async def delete_country(country_id: int):
    await del_country(country_id=country_id)


async def update_country(payload: CreateCountrySchema, country_id) -> dict:
    country = await put_country(Country(id=country_id, name=payload.name))
    return map_country(country)
