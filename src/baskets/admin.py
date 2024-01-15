from sqladmin import ModelView

from src.baskets.models.sqlalchemy import Basket, BasketLine

admin_category = 'Baskets'


class BasketAdmin(ModelView, model=Basket):
    display_name = "Basket"
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.user_id]
    form_columns = ['user', 'status', 'price', 'orders']
    icon = "fa-solid fa-basket-shopping"
    category = admin_category


class BasketLineAdmin(ModelView, model=BasketLine):
    display_name = 'Basket Line'
    column_list = [BasketLine.id, BasketLine.basket_id, BasketLine.quantity, BasketLine.price]
    column_searchable_list = [BasketLine.basket_id]
    form_columns = ['product', 'basket', 'quantity', 'price']
    icon = "fa-duotone fa-cart-plus"
    category = admin_category


def register_basket_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketLineAdmin)
