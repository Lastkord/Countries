from pydantic import BaseModel


class CountrySchema(BaseModel):
    id: int
    name: str


class CreateCountrySchema(BaseModel):
    name: str


class CitySchema(BaseModel):
    id: int
    name: str


class CreateCitySchema(BaseModel):
    name: str
    country_id: int


class CountryWithCities(CountrySchema):
    cities: list[CitySchema]
