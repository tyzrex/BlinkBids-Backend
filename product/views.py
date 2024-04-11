from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer,
    CategorySerializer

)
import os
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


def upload_images(images,product_id):
    if not os.path.exists(f"media/{product_id}"):
        os.makedirs(f"media/{product_id}")
    image_names = []
    for image in images:
        image_name = image.name
        image_names.append(image_name)
        with open(os.path.join(f"media/{product_id}", image_name), "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)
    return image_names

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# Product CRUD
class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        category_name = self.request.query_params.get("category")
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            return Product.objects.filter(category=category)
        return Product.objects.all()


class ProductCreate(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        images = request.FILES.getlist("new_images", [])
        serializer = ProductCreateSerializer(data=data)
        if serializer.is_valid():
            product = Product(**serializer.validated_data)
            
            image_names = upload_images(images,product.id)
            product.images = image_names
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()

#Category CRUD
class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdate(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDelete(DestroyAPIView):
    queryset = Category.objects.all()

# Product filter

# class ProductFilter(APIView):
#     def get(self, request):
#         category = self.request.query_params.get("name", None)
#         if category:
#             queryset = Product.objects.filter(category__name=category)
#         else:
#             queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
            
#         return Response({"count": len(serializer.data), 'data': serializer.data})  