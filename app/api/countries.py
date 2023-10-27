import json

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse


from schemas.country import (
    CountrySchema,
    CreateCountrySchema,
    CountryWithCities,
)
from schemas import OkResponseSchema
from services.country import (
    get_country_by_id,
    get_all_countries,
    create_country,
    delete_country,
    update_country,
)


countries_router = APIRouter()


@countries_router.get("/{country_id}/", response_model=CountryWithCities)
async def get_country_by(country_id: int):
    country = await get_country_by_id(country_id)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@countries_router.get("/", response_model=list[CountrySchema])
async def get_countries():
    countries = await get_all_countries()
    return countries


@countries_router.post("/", response_model=CountrySchema)
async def post_country_api(payload: CreateCountrySchema):
    country = await create_country(payload)
    return JSONResponse(status_code=201, content=json.dumps(country))


@countries_router.delete("/{country_id}/", response_model=OkResponseSchema)
async def delete_country_api(country_id: int):
    await delete_country(country_id=country_id)
    return JSONResponse(status_code=204, content=json.dumps({"ok": True}))


@countries_router.put("/{country_id}", response_model=CountrySchema)
async def put_country(payload: CreateCountrySchema, country_id: int):
    country = await update_country(payload, country_id)
    return JSONResponse(status_code=200, content=json.dumps(country))
