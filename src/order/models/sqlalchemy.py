from sqlalchemy import (
    DECIMAL,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.general.databases.postgres import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=10000)
    basket_id = Column(Integer, ForeignKey("basket.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    address_id = Column(Integer, ForeignKey("address.id"))
    total_price = Column(DECIMAL)
    shipping_price = Column(DECIMAL)
    shipping_method = Column(String, nullable=True)
    status = Column(Enum("Open", "Paid", "Sent", "Received", "Cancelled", "Returned"))
    additional_info = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())

    basket = relationship("Basket", backref="orders")


class OrderLine(Base):
    __tablename__ = "order_lines"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    order_id = Column(Integer, ForeignKey("order.id"))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    order = relationship("Order", backref="order_lines")
