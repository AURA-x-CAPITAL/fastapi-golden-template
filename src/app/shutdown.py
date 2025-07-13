from contextlib import asynccontextmanager
from app.core.logging import logger
from app.db.session import engine
from app.utils.redis import get_redis_client


@asynccontextmanager
async def lifespan_manager(app: FastAPI):
    """Manage application lifespan events"""
    logger.info("Application startup initiated")

    # Initialize services
    await init_db()
    await init_redis()

    yield  # Application runs here

    logger.info("Application shutdown initiated")
    # Shutdown services
    await shutdown_db()
    await shutdown_redis()


async def shutdown_db():
    """Release database connections"""
    await engine.dispose()
    logger.info("Database connections released")


async def shutdown_redis():
    """Close Redis connection pool"""
    redis = await get_redis_client()
    await redis.close()
    logger.info("Redis connections closed")
