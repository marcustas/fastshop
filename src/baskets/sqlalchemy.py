from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    DECIMAL,

)
from sqlalchemy.orm import relationship
from src.general.databases.postgres import Base


class Basket(Base):
    __tablename__ = 'baskets'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(DECIMAL)

    orders = relationship("Order", back_populates="basket")
    basket_lines = relationship('BasketLine', back_populates='basket')


class BasketLine(Base):
    __tablename__ = 'basket_lines'

    id = Column(Integer, primary_key=True, index=True)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    basket = relationship('Basket', back_populates='basket_lines')
