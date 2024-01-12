from sqladmin import ModelView
from src.basket.models.sqlalchemy import Basket, BasketLine

ADMIN_CATEGORY = 'Basket'


class BasketAdmin(ModelView, model=Basket):
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.user_id, Basket.status]
    icon = 'fa-solid fa-basket-shopping'
    category = ADMIN_CATEGORY


class BasketLineAdmin(ModelView):
    column_list = [BasketLine.id, BasketLine.product_id,
                   BasketLine.basket_id, BasketLine.quantity, BasketLine.price]
    column_searchable_list = [BasketLine.id, BasketLine.product_id,
                              BasketLine.basket_id]
    icon = 'fa-solid fa-list'
    category = ADMIN_CATEGORY


def register_basket_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketLineAdmin)
