from sqladmin import ModelView
from sqladmin import Admin
from src.company.models.sqlalchemy import BasketLine, Basket, OrderLine, Order
# src not found


class BasketLineModelView(ModelView):
    column_list = ['product_id', 'basket_id', 'quantity', 'price']
    column_searchable_list = ['product_id', 'basket_id']
    category = 'Basket'


class BasketModelView(ModelView):
    column_list = ['user_id', 'price', 'status']
    column_searchable_list = ['user_id']
    category = 'Basket'


class OrderLineModelView(ModelView):
    column_list = ['product_id', 'order_id', 'quantity', 'price']
    column_searchable_list = ['product_id', 'order_id']
    category = 'Order'


class OrderModelView(ModelView):
    column_list = ['number', 'basket_id', 'user_id', 'address_id', 'total_price', 'shipping_price',
                   'shipping_method', 'status', 'additional_info', 'created_at']
    column_searchable_list = ['number', 'basket_id', 'user_id']
    category = 'Order'


def register_admin_views(admin: Admin):
    admin.add_view(BasketLineModelView(BasketLine, admin.session))
    admin.add_view(BasketModelView(Basket, admin.session))
    admin.add_view(OrderLineModelView(OrderLine, admin.session))
    admin.add_view(OrderModelView(Order, admin.session))
