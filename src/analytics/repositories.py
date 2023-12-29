from src.analytics.models.mongo import ProductAnalytics
from src.common.repository.beanie import BaseMongoRepository


class ProductAnalyticsRepository(BaseMongoRepository[ProductAnalytics]):
    __model__ = ProductAnalytics
