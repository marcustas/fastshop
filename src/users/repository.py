from typing import (
    Optional,
    List,
)

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.common.databases.postgres import get_session
from src.common.repository.sqlalchemy import BaseSQLAlchemyRepository
from src.users.models.pydantic import (
    UserModel,
    UserWithPassword,
    UserAddressModel,
    UserAddressDetailModel,
)
from src.users.models.sqlalchemy import (
    User,
    UserAddress,
)


class UserRepository(BaseSQLAlchemyRepository[User, UserModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, pydantic_model=UserModel, session=session)

    async def create(self, *args, **kwargs):
        raise NotImplementedError

    async def delete(self, *args, **kwargs):
        raise NotImplementedError

    async def get_by_email(self, email: str) -> Optional[UserWithPassword]:
        stmt = select(self.model).where(self.model.email == email)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            return None

        return UserWithPassword.model_validate(user)


def get_user_repository(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session=session)


class UserAddressRepository(BaseSQLAlchemyRepository[UserAddress, UserAddressModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=UserAddress, pydantic_model=UserAddressModel, session=session)

    async def get_user_addresses(self, user_id: int) -> List[UserAddressModel]:
        stmt = select(self.model).filter_by(user_id=user_id)
        result_obj = await self.session.execute(stmt)
        result = result_obj.scalars().all()
        return [self.pydantic_model.model_validate(instance) for instance in result]

    async def get_address_detail(self, address_id: int, user_id: int) -> Optional[UserAddressDetailModel]:
        stmt = select(self.model).filter_by(id=address_id, user_id=user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            return None

        return UserAddressDetailModel.model_validate(user)


def get_users_addresses_repository(session: AsyncSession = Depends(get_session)) -> UserAddressModel:
    return UserAddressRepository(session=session)
