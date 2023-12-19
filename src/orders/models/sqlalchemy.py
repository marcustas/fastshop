from src.general.databases.postgres import Base

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    Enum,
)


class OrderLine(Base):
    __tablename__ = 'order_line'

    id = Column(primary_key=True)
    product_id=Column(Integer,ForeignKey('produkt.id'))
    order_id= Column(Integer,ForeignKey('order.id'))
    quantity = Column(Integer)
    price = Column (DECIMAL)

    order = relationship("Order", back_populates="order_lines")


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=10000)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    address_id = Column(Integer, ForeignKey('user_addresses.id'))
    total_price = Column(DECIMAL)
    shipping_price = Column(DECIMAL)
    shipping_method = Column(String, nullable=True)
    additional_info = Column(String, nullable=True)
    created_at = Column(DateTime, server_default='now')

    order_lines = relationship('OrderLine', back_populates='order')
    basket = relationship("Basket", back_populates="orders")