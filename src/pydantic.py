from typing import Union
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
)
class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Union[int, None] = None
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str

class UserWithPassword(UserModel):
    hashed_password: str

class UserAddressBase(BaseModel):
    title: str


class UserAddressResponse(UserAddressBase):
    id: int


class UserAddressCreate(UserAddressBase):
    pass


class UserAddress(UserAddressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True