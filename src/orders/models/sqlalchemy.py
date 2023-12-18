from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    Sequence,
    Enum,
)
from sqlalchemy.orm import relationship

from src.general.databases.postgres import Base


class OrderLine(Base):
    __tablename__ = 'order_line'

    id = Column(Integer, primary_key=True, index=True)
    # product_id = Column(Integer, ForeignKey('products.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    # product = relationship('products', back_populates='order_line')
    order = relationship('Order', back_populates='order_line')


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, Sequence('number_seq', start=10000, increment=1), nullable=False)
    basket_id = Column(Integer, ForeignKey('basket.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    address_id = Column(Integer, ForeignKey('user_addresses.id'))
    total_price = Column(DECIMAL)
    shipping_price = Column(DECIMAL)
    shipping_method = Column(String, nullable=True)
    status = Column(Enum('Open', 'Paid', 'Sent', 'Received', 'Cancelled', 'Returned', name='order_status', nullable=False))
    additional_info = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    basket = relationship('Basket', back_populates='order')
    order_line = relationship('OrderLine', back_populates='order')
