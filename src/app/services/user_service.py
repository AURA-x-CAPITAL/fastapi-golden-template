from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, data: UserCreate) -> User:
        user = User(**data.model_dump())
        return await self.repo.create(user)
