from django.urls import path, include
from carts.views import AddToCartView, CheckoutView

urlpatterns = [
    path("add/", AddToCartView.as_view(), name="add_to_cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
