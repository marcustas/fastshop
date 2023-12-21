from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    DECIMAL,
    Enum,
)
from sqlalchemy.orm import relationship

from src.general.databases.postgres import Base


class BasketLine(Base):
    __tablename__ = 'basket_line'

    id = Column(Integer, primary_key=True, index=True)
    # product_id = Column(Integer, ForeignKey('products.id'))
    basket_id = Column(Integer, ForeignKey('basket.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    # product = relationship('products', back_populates='basket_line')
    basket = relationship('Basket', back_populates='basket_line')


class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(DECIMAL)
    status = Column(Enum('Open', 'Closed', 'Cancelled', name='basket_status', nullable=False))

    basket_line = relationship('BasketLine', back_populates='basket')
    order = relationship('Order', back_populates='basket')
