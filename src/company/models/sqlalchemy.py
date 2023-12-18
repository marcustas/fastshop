from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    ForeignKey,
    Enum,
    DateTime,
    Float,
)

from src.general.databases.postgres import Base
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    first_name = Column(String)
    last_name = Column(String)


class BasketLine(Base):
    __tablename__ = 'basket_line'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    basket_id = Column(Integer, ForeignKey('basket.id'))
    quantity = Column(Integer)
    price = Column(Float)

    basket = relationship("Basket", back_populates="basket_lines")


class Basket(Base):
    __tablename__ = 'basket'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    price = Column(Float)
    status = Column(Enum('Open', 'Closed', 'Cancelled'))

    user = relationship("User", back_populates="baskets")


class OrderLine(Base):
    __tablename__ = 'order_line'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    quantity = Column(Integer)
    price = Column(Float)

    order = relationship("Order", back_populates="order_lines")


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=10000)
    basket_id = Column(Integer, ForeignKey('basket.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    address_id = Column(Integer, ForeignKey('address.id'))
    total_price = Column(Float)
    shipping_price = Column(Float)
    shipping_method = Column(String, nullable=True)
    status = Column(Enum('Open', 'Paid', 'Sent', 'Received', 'Cancelled', 'Returned'))
    additional_info = Column(String, nullable=True)
    created_at = Column(DateTime, server_default='CURRENT_TIMESTAMP')

    user = relationship("User", back_populates="orders")
    basket = relationship("Basket", back_populates="order")
    order_lines = relationship("OrderLine", back_populates="order")
