import uuid
from datetime import datetime

from beanie import Document
from pydantic import (
    BaseModel,
    Field,
)


class BaseProductAnalytics(BaseModel):
    product_id: int = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime


class ProductAnalytics(Document, BaseProductAnalytics):
    class Settings:
        name = 'productAnalytics'
