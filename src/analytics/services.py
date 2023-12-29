from typing import Annotated

from datetime import datetime

from fastapi import Depends

from src.common.exceptions.base import ObjectDoesNotExistException
from src.common.service import BaseService
from src.analytics.models.mongo import (
    ProductAnalytics,

)
from src.analytics.repositories import ProductAnalyticsRepository

class ProductAnalyticsService(BaseService):
    def __init__(
            self,
            repository: Annotated[ProductAnalyticsRepository, Depends(ProductAnalyticsRepository)],
    ):
        super().__init__(repository=repository)

    async def record_visit(product_id: int):
        analytics_data = ProductAnalytics(product_id=product_id, timestamp=datetime.utcnow())
        document = await ProductAnalytics.insert_one(analytics_data)
        return str(document.inserted_id)