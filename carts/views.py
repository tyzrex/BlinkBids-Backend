# carts/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart, CartItems
from .serializers import CartItemsSerializer
from product.models import Product
from rest_framework.views import APIView
from account.models import User

class AddToCartView(APIView):
    def patch(self, request, *args, **kwargs):
        user = self.request.user
        print(user)
        product_id = request.data.get("product_id")

        cart, created = Cart.objects.get_or_create(user=User)
        if request.user.is_authenticated:
           cart, created = Cart.objects.get_or_create(user=request.user)

        else:
            return Response("You are not logged in", status.HTTP_403_FORBIDDEN)
        
        cart_items = cart.items.get_or_create(product=Product)

        return Response("Product added to cart", status=status.HTTP_200_OK)