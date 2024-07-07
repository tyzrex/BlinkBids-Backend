from rest_framework import serializers
from .models import Cart, CartItems, Order, OrderItem


class CartItemsSerializer(serializers.ModelSerializer):
    product = serializers.CharField()
    price = serializers.SerializerMethodField()
    class Meta:
        model = CartItems
        fields = '__all__'

    def get_price(self, obj):
        return obj.product.price

class CartSerializer(serializers.ModelSerializer):
    items = CartItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
