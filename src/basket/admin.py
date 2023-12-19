from sqladmin import ModelView

from src.basket.models.database import (
    Basket,
    BasketLine,
    Order,
    OrderLine,
)

BASKET_CATEGORY = 'Basket'

class BasketAdmin(ModelView, model = Basket):
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.id, Basket.user_id]
    form_columns = ['user', 'status', 'price', 'orders']
    column_sortable_list = ['status', 'price']
    icon = 'fa-solid fa-basket-shopping'
    category = BASKET_CATEGORY


class BasketLineAdmin(ModelView, model = BasketLine):
    display_name = 'Basket Line'
    column_list = [BasketLine.id, BasketLine.basket_id, BasketLine.quantity, BasketLine.price]
    column_searchable_list = [BasketLine.basket_id]
    form_columns = ['product', 'basket', 'quantity', 'price']
    column_sortable_list = ['price']
    icon = "fa-solid fa-basket-shopping"
    category = BASKET_CATEGORY



class OrderAdmin(ModelView, model=Order):
    display_name = 'Order'
    column_list = [Order.id, Order.number, Order.basket_id, Order.user_id, Order.total_price, Order.status]
    column_searchable_list = [Order.number, Order.basket_id, Order.user_id]
    form_columns = ['number', 'basket', 'user', 'total_price', 'status']
    column_sortable_list = ['status', 'total_price']
    icon = "fa-regular fa-clipboard"
    category = BASKET_CATEGORY

class OrderLineAdmin(ModelView, model=OrderLine):
    display_name = 'Order Line'
    column_list = [OrderLine.id, OrderLine.order_id, OrderLine.quantity, OrderLine.price]
    column_searchable_list = [OrderLine.order_id]
    form_columns = ['product', 'order', 'quantity', 'price']
    column_sortable_list = ['quantity', 'price']
    icon = "fa-regular fa-clipboard"
    category = BASKET_CATEGORY

def register_products_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketLineAdmin)
    admin.add_view(OrderAdmin)
    admin.add_view(OrderLineAdmin)

