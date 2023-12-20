from src.common.repository.beanie import BaseMongoRepository
from src.catalogue.models.mongo import ProductAnalytics

class ProductAnalyticsRepository(BaseMongoRepository[ProductAnalytics]):
    __model__ = ProductAnalytics
        
