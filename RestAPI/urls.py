from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import productList, productDetails, orderDetails, RegisterView, userList, LoginView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("product/", productList.as_view()),
    path("product/<int:id>/", productDetails.as_view()),
    path("order/", orderDetails.as_view()),
    path("registers/", RegisterView.as_view()),
    path("loginapi/", LoginView.as_view()),
    path("users/", userList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)