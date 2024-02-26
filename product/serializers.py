from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['images']

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
