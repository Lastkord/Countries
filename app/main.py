from typing import Any

from schemas.country import (
    CountrySchema,
    CreateCountrySchema,
    CountryWithCities,
    CitySchema,
    CreateCitySchema,
)
from schemas import OkResponseSchema
import uvicorn
from fastapi import FastAPI, HTTPException, Response
from services.country import (
    get_country_by_id,
    get_all_countries,
    create_country,
    delete_country,
    update_country,
    get_city_by_pk,
    delete_city_by_id,
    create_city,
    get_all_cities,
    update_city_async,
)
import json

app = FastAPI()


@app.get("/countries/{country_id}/", response_model=CountryWithCities)
async def get_country_by(country_id: int):
    country = await get_country_by_id(country_id)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@app.get("/countries/", response_model=list[CountrySchema])
async def get_countries():
    countries = await get_all_countries()
    return countries


@app.post("/countries/", response_model=CountrySchema)
async def post_country_api(payload: CreateCountrySchema):
    country = await create_country(payload)
    return Response(status_code=201, content=json.dumps(country))


@app.post("/countries/{country_id}/cities/", response_model=CitySchema)
async def post_city(payload: CreateCitySchema):
    city = await create_city(payload)
    return Response(status_code=201, content=json.dumps(city))


@app.delete("/countries/{country_id}/", response_model=OkResponseSchema)
async def delete_country_api(country_id: int):
    await delete_country(country_id=country_id)
    return Response(status_code=204, content=json.dumps({"ok": True}))


@app.put("/countries/{country_id}", response_model=CountrySchema)
async def put_country(payload: CreateCountrySchema, country_id: int):
    country = await update_country(payload, country_id)
    return Response(status_code=200, content=json.dumps(country))


@app.get("/countries/{country_id}/cities/{city_id}/", response_model=CitySchema)
async def get_city_by_id(country_id: int, city_id: int):
    city = await get_city_by_pk(country_id, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@app.delete(
    "/countries/{country_id}/cities/{city_id}/", response_model=OkResponseSchema
)
async def del_city(city_id: int):
    await delete_city_by_id(city_id)
    return Response(status_code=204, content=json.dumps({"ok": True}))


@app.get("/countries/{country_id}/cities/", response_model=list[CitySchema])
async def get_cities():
    cities = await get_all_cities()
    return cities


@app.put("/countries/{country_id}/cities/{city_id}/", response_model=CitySchema)
async def put_city(payload: CreateCitySchema, city_id: int):
    city = await update_city_async(payload, city_id)
    return Response(status_code=200, content=json.dumps(city))


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0")
