from src.general.databases.postgres import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Enum,
    DECIMAL,
)


class Basket(Base):

    __tablename__ = 'baskets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    price = Column(DECIMAL)
    status = Column(Enum('Open','Closed','Cancelled'))

    orders = relationship("Order", back_populates="basket")
    user = relationship('User', back_populates='basket')
    basket_lines = relationship('BasketLine', back_populates='basket')


class BasketLine(Base):

    __tablename__ = 'basket_lines'

    id = Column(Integer, primary_key =True)
    produkt_id = Column(Integer,ForeignKey('produkt.id'))
    basket_id = Column(Integer,ForeignKey('basket.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    basket = relationship('Basket', back_populates='basket_lines')
