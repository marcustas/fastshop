from fastapi import Depends

from src.catalogue.models.pydantic import ProductModel, CategoryModel
from src.catalogue.repository import (
    ProductRepository,
    CategoryRepository,
    get_product_repository,
)
from src.common.service import BaseService
from sqlalchemy.orm import Session


class ProductService(BaseService[ProductModel]):
    def __init__(self, repository: ProductRepository):
        super().__init__(repository)


def get_product_service(repo: ProductRepository = Depends(get_product_repository)) -> ProductService:
    return ProductService(repository=repo)


class CategoryService(BaseService[CategoryModel]):
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def create_category(self, db: Session, category: CategoryModel):
        return self.category_repository.create_category(db, category)

    def get_categories(self, db: Session, skip: int = 0, limit: int = 10):
        return self.category_repository.get_categories(db, skip=skip, limit=limit)

    def get_category(self, db: Session, category_id: int):
        return self.category_repository.get_category(db, category_id)

    def update_category(self, db: Session, category_id: int, updated_category: CategoryModel):
        return self.category_repository.update_category(db, category_id, updated_category)

    def delete_category(self, db: Session, category_id: int):
        return self.category_repository.delete_category(db, category_id)
