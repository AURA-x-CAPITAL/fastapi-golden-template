from typing import AsyncGenerator

from redis.asyncio import Redis
from sqlalchemy import create_engine, Engine, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from infrastructure.database.requests import RequestsRepo
from settings import logger
from settings.app_settings import AppSettings
from settings.db_settings import DatabaseSettings

async_session: async_sessionmaker | None = None
redis: None | Redis = None


def get_engine(uri: str, echo=False, async_engine=True) -> AsyncEngine | Engine:
    if async_engine:
        engine = create_async_engine(
            uri,
            query_cache_size=1200,
            pool_size=20,
            max_overflow=200,
            future=True,
            echo=echo,
            pool_recycle=1800,
        )
    else:
        engine = create_engine(
            uri,
            query_cache_size=1200,
            pool_size=20,
            pool_recycle=1800,
            max_overflow=200,
            echo=echo,
        )

    return engine


def create_session_pool(engine, async_engine=True) -> async_sessionmaker | sessionmaker:
    if async_engine:
        session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)
    else:
        session_pool = sessionmaker(bind=engine, expire_on_commit=False)
    return session_pool


def init_db(uri: str) -> None:
    global async_session

    engine = get_engine(uri)
    async_session = create_session_pool(engine)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    global async_session

    if async_session is None:
        return

    async with async_session() as db:
        yield db


async def check_database_connection() -> bool:
    if async_session is None:
        return False

    async with async_session() as session:
        try:
            result = await session.execute(select(1))
            return result.scalar() == 1

        except Exception as e:
            logger.error(f"Database connection error: {str(e)}")
            return False
