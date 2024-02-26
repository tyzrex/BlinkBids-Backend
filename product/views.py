from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer,

)


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
