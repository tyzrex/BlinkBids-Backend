from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
