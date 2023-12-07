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
    __tablename__ = 'baskets'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    price = Column(DECIMAL)
    status = Column(Enum('Open', 'Closed', 'Cancelled'))

    orders = relationship("Order", backref="basket")


class BasketLine(Base):
    __tablename__ = 'basket_line'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    basket_id = Column(Integer, ForeignKey('basket.id'))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    product = relationship("Product", backref="baskets")