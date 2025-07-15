from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")

class AbstractRepository(ABC, Generic[ModelType]):
    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def get(self, id: int) -> ModelType: ...
