from src.common.routes import BaseCrudPrefixes


class ReviewsRoutesPrefixes:
    product_reviews: str = '/product-reviews'


class ProductReviewRoutesPrefixes(BaseCrudPrefixes):
    add_reply: str = '/{pk}/reply'


class ProductDetailRoutes(BaseCrudPrefixes):
    product_detail: str = '/product-detail'
