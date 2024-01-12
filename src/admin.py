from src.basket.admin import register_basket_admin_views
from src.order.admin import register_orders_admin_views
from src.users.admin import register_hr_admin_views


def register_admin_views(admin):
    register_hr_admin_views(admin=admin)
    register_orders_admin_views(admin=admin)
    register_basket_admin_views(admin=admin)