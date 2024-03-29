from rest_framework import serializers
from .models import Cart, CartItems


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
