from sqladmin import ModelView

from src.baskets.models.sqlalchemy import Basket, BasketLine

ADMIN_CATEGORY = 'Baskets'


class BasketAdmin(ModelView, model=Basket):
    display_name = "Basket"
    column_list = [Basket.id, Basket.price]
    column_searchable_list = [Basket.price]
    icon = "fa-solid fa-basket-shopping"
    category = ADMIN_CATEGORY


class BasketLineAdmin(ModelView, model=BasketLine):
    display_name = 'Basket Line'
    column_list = [BasketLine.id, BasketLine.quantity]
    column_searchable_list = [BasketLine.id, BasketLine.quantity]
    icon = "fa-duotone fa-basket-shopping"
    category = ADMIN_CATEGORY


def register_basket_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketLineAdmin)
