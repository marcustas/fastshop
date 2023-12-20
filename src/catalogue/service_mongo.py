from datetime import datetime

from src.catalogue.models.mongo import ProductAnalytics, BaseProductAnalytics
from src.catalogue.repository_mongo import ProductAnalyticsRepository
from src.common.service import BaseService


class ProductAnalyticsService(BaseService):

    def __init__(self, repository: ProductAnalyticsRepository):
        super().__init__(repository)
    async def record_product_visit(self, product_id: int):
        timestamp = datetime.now()
        analytics_data = BaseProductAnalytics(product_id=product_id, timestamp=timestamp)

        await self.repository.create(analytics_data)