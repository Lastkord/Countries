from fastapi import APIRouter

from .countries import countries_router
from .cities import cities_router


router = APIRouter()

router.include_router(countries_router, prefix="/countries", tags=["countries"])
router.include_router(cities_router, prefix="", tags=["cities"])
