from sqladmin import ModelView

from src.orders.models.sqlalchemy import (
    Order,
)


ADMIN_CATEGORY = 'Orders'


class OrderAdmin(ModelView, model=Order):
    column_list = [Order.id, Order.number, Order.status, Order.created_at]
    column_searchable_list = [Order.nomber, Order.status, Order.created_at]
    icon = 'fa-solid fa-clipboard'
    category = ADMIN_CATEGORY


def register_hr_admin_views(admin):
    admin.add_view(OrderAdmin)
