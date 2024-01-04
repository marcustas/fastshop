from typing import Annotated

from fastapi import Depends

from src.common.exceptions.base import ObjectDoesNotExistException
from src.common.service import BaseService
from src.reviews.models.mongo import (
    ProductReview,
    Reply,
    ProductAnalytics,
)
from src.reviews.repositories import (
    ProductReviewRepository,
    ProductAnalyticsRepository,
)
from datetime import datetime



class ProductReviewService(BaseService):
    def __init__(
        self,
        repository: Annotated[ProductReviewRepository, Depends(ProductReviewRepository)],
    ):
        super().__init__(repository=repository)

    def __build_reply_tree(self, parent_id, replies):
        tree = []
        for reply in replies:
            if reply.to_reply == parent_id:
                reply.replies = self.__build_reply_tree(reply.id, replies)
                tree.append(reply)
        return tree

    async def detail_with_replies(self, pk: str) -> ProductReview:
        review = await self.repository.get(pk=pk)
        if not review:
            raise ObjectDoesNotExistException()

        replies = self.__build_reply_tree(parent_id=None, replies=review.replies)
        review.replies = replies

        return review

    async def add_reply(self, pk: str, reply: Reply) -> ProductReview:
        review = await self.repository.get(pk=pk)
        if not review:
            raise ObjectDoesNotExistException()

        review.replies.append(reply.model_dump())

        return await review.save()


class ProductAnalyticsService(BaseService):
    def __init__(
            self,
            repository: Annotated[ProductAnalyticsRepository, Depends(ProductAnalyticsRepository)],
    ):
        super().__init__(repository=repository)

    async def add_visiting_notes(self, product_id: int):
        try:
            timestamp = datetime.utcnow()
            visit_data = ProductAnalytics(product_id=product_id, timestamp=timestamp)
            await ProductAnalytics.insert_one(visit_data)
        except Exception as e:
            print(f"Error with adding a visiting note: {e}")
