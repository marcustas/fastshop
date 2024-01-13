from sqlalchemy import (
    DECIMAL,
    Column,
    Enum,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import relationship

from src.general.databases.postgres import Base


class Basket(Base):
    __tablename__ = "basket"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(DECIMAL(precision=10, scale=2))
    status = Column(Enum("Open", "Closed", "Cancelled"))

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="baskets")

    # Correcting the property name to match BasketLine class
    basket_lines = relationship("BasketLine", back_populates="basket")


class BasketLine(Base):
    __tablename__ = "basket_line"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    basket_id = Column(Integer, ForeignKey("basket.id"))
    quantity = Column(Integer)
    price = Column(DECIMAL(precision=10, scale=2))

    # Correcting the property name to match Basket class
    basket = relationship("Basket", back_populates="basket_lines")
