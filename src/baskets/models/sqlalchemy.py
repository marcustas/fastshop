from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Enum,
    DECIMAL,
)

from sqlalchemy.orm import relationship
from src.general.databases.postgres import Base

class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(DECIMAL)
    status = Column(Enum('Open', 'Closed', 'Cancelled', name='basket_status'))
    orders = relationship("Order", back_populates="basket")
    user = relationship('User', back_populates='basket')
    basket_line = relationship('BasketLine', back_populates='basket')


class BasketLine(Base):
    __tablename__ = 'basket_line'

    id = Column(Integer, primary_key=True, index=True)
    basket_id = Column(Integer, ForeignKey('basket.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)
    basket = relationship('Basket', back_populates='basket_line')
