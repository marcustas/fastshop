from typing import Optional, List

from fastapi import Depends
from sqlalchemy.exc import (
    MultipleResultsFound,
    NoResultFound,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.common.databases.postgres import get_session
from src.common.exceptions.base import (
    ObjectAlreadyExistException,
    ObjectDoesNotExistException,
)
from src.common.repository.sqlalchemy import BaseSQLAlchemyRepository
from src.users.models.database import User, UserAddress


class UserRepository(BaseSQLAlchemyRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    async def create(self, *args, **kwargs):
        raise NotImplementedError

    async def delete(self, *args, **kwargs):
        raise NotImplementedError

    async def get_by_email(self, email: str) -> Optional[User]:
        statement = select(self.model).where(self.model.email == email)
        result = await self.session.exec(statement)
        try:
            instance = result.one()
        except NoResultFound:
            raise ObjectDoesNotExistException()
        except MultipleResultsFound:
            raise ObjectAlreadyExistException()

        return instance


def get_user_repository(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session=session)


class UserAddressRepository(BaseSQLAlchemyRepository[UserAddress]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    async def create(self, *args, **kwargs):
        raise NotImplementedError

    async def delete(self, *args, **kwargs):
        raise NotImplementedError


    async def get_user_addresses(self, user_id: int) -> List[UserAddress]:
        stmt = select(self.model).filter_by(user_id=user_id)
        result_obj = await self.session.execute(stmt)
        result = result_obj.scalars().all()
        return [self.pydantic_model.model_validate(instance) for instance in result]

    async def get_address_detail(self, address_id: int, user_id: int) -> Optional[UserAddress]:
        stmt = select(self.model).filter_by(id=address_id, user_id=user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            return None

        return UserAddress.model_validate(user)

def get_adress_user_repository(session: AsyncSession = Depends(get_session)) -> UserAddressRepository:
    return UserAddressRepository(session=session)
