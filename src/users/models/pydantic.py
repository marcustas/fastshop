from typing import Union, Optional

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


class UserAddressModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    title: str


class UserAddressModelDetail(UserAddressModel):
    id: Optional[int] = None
    title: str
    city: str
    street: str
    house: str
    apartment: str
    post_code: str
    floor: str
    additional_info: str
