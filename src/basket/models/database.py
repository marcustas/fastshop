from datetime import datetime
from src.basket.enums import BasketStatus, OrderStatus
from src.catalogue.models.database import *
from typing import (
    List,
    Optional,
)

from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
)


class BasketLine(SQLModel, table=True):
    __tablename__ = 'basket_line'

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key='product.id')
    basket_id: int = Field(foreign_key='basket.id')
    quantity: int
    price: float

    product: Product = Relationship(back_populates="basket_lines")


class Basket(SQLModel, table=True):
    __tablename__ = 'basket'

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id')
    price: float
    status: BasketStatus

    basket_lines: BasketLine = Relationship(back_populates="basket")

class OrderLine(SQLModel, table = True):
    __tablename__ = 'order_line'

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key='products.id')
    order_id: int = Field(foreign_key='order.id')
    quantity: int
    price: float

    product: Product = Relationship(back_populates="order_lines")


class Order(SQLModel, table=True):
    __tablename__ = 'orders'

    id: Optional[int] = Field(default=None, primary_key=True)
    number:int = Field(min_length=10000)
    basket_id:int = Field(foreign_key='basket.id')
    user_id:int = Field(foreign_key='user.id')
    address_id:int = Field(foreign_key='address.id')
    total_price: float
    shipping_price: float
    shipping_method: str = Field(nullable=True)
    status: OrderStatus
    additional_info: str = Field(nullable=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    basket: Basket = Relationship(back_populates="orders")
    order_lines: OrderLine = Relationship(back_populates="order")
