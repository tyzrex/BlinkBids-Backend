from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer,

)
import os

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


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
