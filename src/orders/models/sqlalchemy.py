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
    user_id = Column(Integer, ForeignKey('users.id'))
    address_id = Column(Integer, ForeignKey('user_addresses.id'))
    total_price = Column(DECIMAL)
    shipping_price = Column(DECIMAL)
    shipping_method = Column(String, nullable=True)
    additional_info = Column(String, nullable=True)
    created_at = Column(DateTime, server_default='now')

    order_lines = relationship('OrderLine', back_populates='order')

    def __str__(self):
        return self.additional_info

class OrderLine(Base):
    __tablename__ = 'order_lines'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    order = relationship("Order", back_populates="order_lines")