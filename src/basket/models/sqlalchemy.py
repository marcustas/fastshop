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

    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    user_id = Column(Integer, ForeignKey("user.id"))
    price = Column(DECIMAL(precision=10, scale=2))
    status = Column(Enum("Open", "Closed", "Cancelled"))

    # Assuming there is a User table with an 'id' column
    user = relationship("User", back_populates="basket")


class BasketLine(Base):
    __tablename__ = "basket_line"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    basket_id = Column(Integer, ForeignKey("basket"))
    quantity = Column(Integer)
    price = Column(DECIMAL(precision=10, scale=2))

    product = relationship("Product", backref="basket_line")
