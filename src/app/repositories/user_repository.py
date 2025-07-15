from app.models.user import User
from sqlalchemy import select
from app.repositories.base import AbstractRepository


class UserRepository(AbstractRepository[User]):
    async def get(self, id: int) -> User | None:
        stmt = select(User).where(User.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.flush()
        return user
