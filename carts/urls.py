from django.urls import path
from carts.views import AddToCartView, CheckoutView, UpdateCartItemView, CartDetailView, RemoveFromCartView,GetUserOrders

urlpatterns = [
    path("add/", AddToCartView.as_view(), name="add_to_cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("remove/", RemoveFromCartView.as_view(), name="remove-cart"),
    path("update/", UpdateCartItemView.as_view(), name="update-cart"),
    path("detail/", CartDetailView.as_view(), name="cart-detail"),
    path("user/orders/",GetUserOrders.as_view(),name="user-orders")
    
]
