from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@192.168.100.71:5432/countries"


bind = create_async_engine(DATABASE_URL)
_sessionmaker = sessionmaker(bind, expire_on_commit=False, class_=AsyncSession)
