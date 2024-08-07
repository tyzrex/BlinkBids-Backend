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
    total_price = serializers.SerializerMethodField()
    items_list = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.total_price
    
    def get_items_list(self, obj):
        return [item.product.title for item in obj.order_items.all()]