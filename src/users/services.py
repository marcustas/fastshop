from typing import List, Optional

from fastapi import Depends

from src.authentication.security import verify_password
from src.common.service import BaseService
from src.users.models.database import User, UserAddress
from src.users.repository import (
    UserAddressRepository,
    UserRepository,
    get_adress_user_repository,
    get_user_repository,
)


class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    async def get_by_email(self, email: str):
        return await self.repository.get_by_email(email=email)

    async def authenticate(self, email: str, password: str) -> Optional[User]:
        user = await self.get_by_email(email=email)

        if user is None or not verify_password(plain_password=password, hashed_password=user.hashed_password):
            return None
        else:
            return user


def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repository=repo)


class UserAdressService(BaseService[UserAddress]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        async def get_user_address_by_id(self, address_id: int, user_id: int) -> Optional[UserAddress]:
            return await self.repository.get_user_address_by_id(address_id, user_id)
        async def get_user_addresses(self, user_id: int) -> List[UserAddress]:
            return await self.repository.get_user_addresses(user_id=user_id)

def get_user_address_service(repo: UserAddressRepository = Depends(get_adress_user_repository())) -> UserAdressService:
    return UserAdressService(repository=repo)

