from django.urls import path
from .views import ProductList, ProductCreate, ProductUpdate, ProductDelete


urlpatterns = [
    path("all/", ProductList.as_view(), name="product-list"),
    path("create/", ProductCreate.as_view(), name="product-create"),
    path("update/<str:pk>/", ProductUpdate.as_view(), name="product-update"),
    path("delete/<str:pk>/", ProductDelete.as_view(), name="product-delete"),
]
