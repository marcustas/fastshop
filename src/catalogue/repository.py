from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.catalogue.models.pydantic import ProductModel, CategoryModel
from src.catalogue.models.sqlalchemy import Product
from src.common.databases.postgres import (
    get_session,
)
from src.common.repository.sqlalchemy import BaseSQLAlchemyRepository


class ProductRepository(BaseSQLAlchemyRepository[Product, ProductModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Product, pydantic_model=ProductModel, session=session)


def get_product_repository(session: AsyncSession = Depends(get_session)) -> ProductRepository:
    return ProductRepository(session=session)


class CategoryRepository:
    def create_category(self, db: Session, category: CategoryModel):
        db_category = CategoryModel(**category.dict())
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category

    def get_categories(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(CategoryModel).offset(skip).limit(limit).all()

    def get_category(self, db: Session, category_id: int):
        return db.query(CategoryModel).filter(CategoryModel.id == category_id).first()

    def update_category(self, db: Session, category_id: int, updated_category: CategoryModel):
        db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
        for key, value in updated_category.dict().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
        return db_category

    def delete_category(self, db: Session, category_id: int):
        db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
        db.delete(db_category)
        db.commit()
