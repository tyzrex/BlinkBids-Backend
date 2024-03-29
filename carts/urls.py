from django.urls import path, include
from carts.views import AddToCartView

urlpatterns = [
    path("add/", AddToCartView.as_view(), name="add_to_cart"),
]
