from sqladmin import ModelView

from src.orders.models.sqlalchemy import Order, OrderLine

ADMIN_CATEGORY = 'Orders'


class OrderAdmin(ModelView, model=Order):
    display_name = 'Order'
    column_list = [Order.id, Order.number, Order.basket_id, Order.user_id, Order.total_price, Order.status]
    column_searchable_list = [Order.number, Order.basket_id, Order.user_id]
    form_columns = ['number', 'basket', 'user', 'total_price', 'status']
    icon = "fa-solid fa-store"
    category = ADMIN_CATEGORY


class OrderLineAdmin(ModelView, model=OrderLine):
    display_name = 'Order Line'
    column_list = [OrderLine.id, OrderLine.product_id, OrderLine.order_id, OrderLine.quantity, OrderLine.price]
    column_searchable_list = [OrderLine.product_id, OrderLine.order_id]
    form_columns = ['product', 'order', 'quantity', 'price']
    icon = "fa-thin fa-store"
    category = 'Order Lines'


def register_order_admin_views(admin):
    admin.add_view(OrderAdmin)
    admin.add_view(OrderLineAdmin)