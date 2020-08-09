from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_cart_data", views.get_cart_data, name="get_cart_data"),
    path("change_quan", views.change_quan, name="change_quan"),
    path("carts", views.add_to_cart, name="cart"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("process_payment", views.process_payment, name="process_payment"),
    path("payment_done", views.payment_done, name="payment_done"),
    path("payment_cancelled", views.payment_cancelled, name="payment_cancelled"),
    path("order_history", views.order_history, name="order_history"),
]