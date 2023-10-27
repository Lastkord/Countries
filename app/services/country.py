from repositories.countries import (
    get_country_by_pk,
    get_all_countries_asy,
    insert_country,
    del_country,
    update_country as put_country,
    select_city_by_id,
    delete_city,
    insert_city,
    get_cities,
    update_city,
)
from schemas.country import CreateCountrySchema, CountrySchema, CreateCitySchema
from models.country import Country
from models.city import City


async def get_country_by_id(country_id: int):
    country = await get_country_by_pk(country_id=country_id)
    if country:
        return {
            "id": country.id,
            "name": country.name,
            "cities": [{"id": city.id, "name": city.name} for city in country.cities],
        }


async def get_all_countries():
    countries = await get_all_countries_asy()
    return [{"id": country.id, "name": country.name} for country in countries]


async def create_country(payload: CreateCountrySchema) -> dict:
    country = await insert_country(Country(name=payload.name))
    return {"id": country.id, "name": country.name}


async def create_city(payload: CreateCitySchema):
    city = await insert_city(City(name=payload.name, country_id=payload.country_id))
    return {"id": city.id, "name": city.name, "country_id": city.country_id}


async def delete_country(country_id: int):
    await del_country(country_id=country_id)


async def update_country(payload: CreateCountrySchema, country_id) -> dict:
    country = await put_country(Country(id=country_id, name=payload.name))
    return {"id": country.id, "name": country.name}


async def get_city_by_pk(country_id: int, citi_id: int):
    city = await select_city_by_id(country_id, citi_id)
    if city:
        return {"id": city.id, "name": city.name}
    return None


async def delete_city_by_id(city_id: int):
    await delete_city(city_id)


async def get_all_cities():
    cities = await get_cities()
    return [
        {"id": city.id, "name": city.name, "country_id": city.country_id}
        for city in cities
    ]


async def update_city_async(payload: CreateCitySchema, city_id: int):
    city = await update_city(
        City(id=city_id, name=payload.name, country_id=payload.country_id)
    )
    return {"id": city.id, "name": city.name, "country_id": city.country_id}
