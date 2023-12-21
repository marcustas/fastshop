from sqladmin import ModelView

from src.orders.models.sqlalchemy import (
    Order,
    OrderLine
)


ADMIN_CATEGORY = 'Orders'


class OrderAdmin(ModelView, model=Order):
    column_list = [Order.id, Order.number, Order.basket_id, Order.user_id, Order.address_id, Order.total_price, Order.shipping_price, Order.shipping_method, Order.status]
    column_searchable_list = [Order.number, Order.shipping_method]
    icon = 'fa-solid fa-book'
    category = ADMIN_CATEGORY


class OrderLineAdmin(ModelView, model=OrderLine):
    column_list = [OrderLine.id, OrderLine.order_id, OrderLine.quantity, OrderLine.price]
    column_searchable_list = [OrderLine.price]
    icon = 'fa-solid fa-pallet'
    category = ADMIN_CATEGORY


def register_order_admin_views(admin):
    admin.add_view(OrderAdmin)
    admin.add_view(OrderLineAdmin)
