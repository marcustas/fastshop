from typing import Optional

from pydantic import (
    BaseModel,
    constr,
)


class ProductModel(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str]
    short_description: Optional[constr(max_length=20)]
    is_active: bool

    class Config:
        from_attributes = True


class CategoryModel(BaseModel):
    name: str


class Category(CategoryModel):
    id: int

    class Config:
        orm_mode = True
