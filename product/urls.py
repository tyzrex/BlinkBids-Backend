from django.urls import path
from .views import ProductList, ProductCreate, ProductUpdate, ProductDelete, CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete


urlpatterns = [
    path("all/", ProductList.as_view(), name="product-list"),
    path("create/", ProductCreate.as_view(), name="product-create"),
    path("update/<str:pk>/", ProductUpdate.as_view(), name="product-update"),
    path("delete/<str:pk>/", ProductDelete.as_view(), name="product-delete"),

    path("category/all/", CategoryList.as_view(), name="category-list"),
    path("category/create/", CategoryCreate.as_view(), name="category-create"),
    path("category/update/<str:pk>/", CategoryUpdate.as_view(), name="category-update"),
    path("category/delete/<str:pk>/", CategoryDelete.as_view(), name="category-delete"),
]
