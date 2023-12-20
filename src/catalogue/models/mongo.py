from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class BaseProductAnalytics(BaseModel):
    product_id: int
    timestamp: datetime

class ProductAnalytics(BaseProductAnalytics, Document):
    class Settings:
        name = "product_analytics_collection"
