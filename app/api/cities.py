import json

from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse

from schemas.country import (
    CitySchema,
    CreateCitySchema,
)
from schemas import OkResponseSchema
from services.cities import (
    get_city_by_pk,
    delete_city_by_id,
    create_city,
    get_all_cities,
    update_city_async,
)


cities_router = APIRouter()


@cities_router.post("/countries/{country_id}/cities/", response_model=CitySchema)
async def post_city(payload: CreateCitySchema):
    city = await create_city(payload)
    return JSONResponse(status_code=201, content=json.dumps(city))


@cities_router.get(
    "/countries/{country_id}/cities/{city_id}/", response_model=CitySchema
)
async def get_city_by_id(country_id: int, city_id: int):
    city = await get_city_by_pk(country_id, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@cities_router.delete(
    "/countries/{country_id}/cities/{city_id}/", response_model=OkResponseSchema
)
async def del_city(city_id: int):
    await delete_city_by_id(city_id)
    return JSONResponse(status_code=204, content=json.dumps({"ok": True}))


@cities_router.get("/countries/{country_id}/cities/", response_model=list[CitySchema])
async def get_cities():
    cities = await get_all_cities()
    return cities


@cities_router.put(
    "/countries/{country_id}/cities/{city_id}/", response_model=CitySchema
)
async def put_city(payload: CreateCitySchema, city_id: int):
    city = await update_city_async(payload, city_id)
    return JSONResponse(status_code=200, content=json.dumps(city))
