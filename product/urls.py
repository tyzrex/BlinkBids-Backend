from django.urls import path
from .views import ProductList, ProductCreate


urlpatterns = [
    path("all/", ProductList.as_view(), name="product-list"),
    path("create/", ProductCreate.as_view(), name="product-create"),
]
