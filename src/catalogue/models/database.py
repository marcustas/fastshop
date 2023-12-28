from datetime import datetime
from typing import (
    List,
    Optional,
)

from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
    ForeignKey,
)


class Product(SQLModel, table=True):
    __tablename__ = 'products'

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    short_description: Optional[str] = None
    is_active: bool

    categories: List["ProductCategory"] = Relationship(back_populates="product")
    images: List["ProductImage"] = Relationship(back_populates="product")
    stock_records: List["StockRecord"] = Relationship(back_populates="product")
    discounts: List["ProductDiscount"] = Relationship(back_populates="product")
    additional_products: List["AdditionalProducts"] = Relationship(back_populates="product")
    recommended_products: List["RecommendedProducts"] = Relationship(back_populates="product")


class ProductCategory(SQLModel, table=True):
    __tablename__ = 'product_categories'

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="products.id")
    category_id: int = Field(foreign_key="categories.id")

    product: Product = Relationship(back_populates="categories")
    category: "Category" = Relationship(back_populates="products")


class Category(SQLModel, table=True):
    __tablename__ = 'categories'

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    image: Optional[str] = None
    is_active: bool
    parent_id: Optional[int] = Field(default=None, foreign_key="categories.id")

    products: List["ProductCategory"] = Relationship(back_populates="category")
    parent: Optional["Category"] = Relationship(
        back_populates="subcategories",
        sa_relationship_kwargs={"remote_side": "Category.id"},
    )
    subcategories: List["Category"] = Relationship(back_populates="parent")


class ProductImage(SQLModel, table=True):
    __tablename__ = 'product_images'

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="products.id")
    original: str
    thumbnail: Optional[str] = None
    caption: Optional[str] = None

    product: Product = Relationship(back_populates="images")


class StockRecord(SQLModel, table=True):
    __tablename__ = 'stock_records'

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="products.id")
    price: float
    quantity: int
    date_created: datetime
    additional_info: Optional[str] = None

    product: Product = Relationship(back_populates="stock_records")


class ProductDiscount(SQLModel, table=True):
    __tablename__ = 'product_discounts'

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="products.id")
    discount_percent: Optional[int] = None
    discount_amount: Optional[float] = None
    valid_from: datetime
    valid_to: datetime

    product: Product = Relationship(back_populates="discounts")

class AdditionalProducts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    additional_id: int = Field(foreign_key="products.id")

    product: Optional["Product"] = Relationship(back_populates="additional_products")

class RecommendedProducts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    recommended_id: int = Field(foreign_key="products.id")

    product: Optional["Product"] = Relationship(back_populates="recommended_products")
