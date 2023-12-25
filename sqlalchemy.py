from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    Enum,
)

from sqlalchemy.orm import relationship

from src.general.databases.postgres import Base


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
    status = Column(Enum('Open', 'Paid', 'Sent', 'Received', 'Cancelled', 'Returned', name='order_status'))
    additional_info = Column(String, nullable=True)
    created_at = Column(DateTime, server_default='now')

    basket = relationship("Basket", back_populates="orders")
    user = relationship('User', back_populates='orders')
    order_lines = relationship('OrderLine', back_populates='order')


class OrderLine(Base):
    __tablename__ = 'order_lines'

    product_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    order = relationship("Order", back_populates="order_lines")