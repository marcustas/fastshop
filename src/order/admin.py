from sqladmin import ModelView

from src.order.models.sqlalchemy import (
    Order,
    OrderLine,
)

ADMIN_CATEGORY = "Order"


class OrderAdmin(ModelView, model=Order):
    column_list = [Order.id, Order.total_price, Order.status, Order.created_at]
    column_searchable_list = [Order.user_id, Order.status]
    icon = "fa-solid fa-shop"
    category = ADMIN_CATEGORY


class OrderLineAdmin(ModelView):
    column_list = [
        OrderLine.id,
        OrderLine.product_id,
        OrderLine.Order_id,
        OrderLine.quantity,
        OrderLine.price,
    ]
    column_searchable_list = [OrderLine.id, OrderLine.product_id, OrderLine.Order_id]
    icon = "fa-solid fa-list-check"
    category = ADMIN_CATEGORY


def register_orders_admin_views(admin):
    admin.add_view(OrderAdmin)
    admin.add_view(OrderLineAdmin)
