from sqladmin import ModelView

from src.orders.models.sqlalchemy import Order, OrderLine

admin_category = 'Orders'


class OrderAdmin(ModelView, model=Order):
    display_name = 'Order'
    column_list = [Order.id, Order.number, Order.basket_id, Order.user_id, Order.total_price, Order.status]
    column_searchable_list = [Order.number, Order.basket_id, Order.user_id]
    form_columns = ['number', 'basket', 'user', 'total_price', 'status']
    icon = "fa-regular fa-store"
    category = admin_category


class OrderLineAdmin(ModelView, model=OrderLine):
    display_name = 'Order Line'
    column_list = [OrderLine.product_id, OrderLine.order_id, OrderLine.quantity, OrderLine.price]
    column_searchable_list = [OrderLine.order_id]
    form_columns = ['product', 'order', 'quantity', 'price']
    icon = "fa-duotone fa-store"
    category = admin_category


def register_order_admin_views(admin):
    admin.add_view(OrderAdmin)
    admin.add_view(OrderLineAdmin)
