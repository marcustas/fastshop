from sqladmin import ModelView

from src.baskets.models.sqlalchemy import Basket, BasketLine

ADMIN_CATEGORY = 'Baskets'


class BasketAdmin(ModelView, model=Basket):
    display_name = "Basket"
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.user_id]
    form_columns = ['user', 'status', 'price', 'orders']
    icon = "fa-solid fa-basket-shopping"
    category = ADMIN_CATEGORY


class BasketLineAdmin(ModelView, model=BasketLine):
    display_name = 'Basket Line'
    column_list = [BasketLine.id, BasketLine.basket_id, BasketLine.quantity, BasketLine.price]
    column_searchable_list = [BasketLine.basket_id]
    form_columns = ['product', 'basket', 'quantity', 'price']
    icon = "fa-duotone fa-basket-shopping"
    category = ADMIN_CATEGORY


def register_basket_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketLineAdmin)
