from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItems
from .serializers import CartItemsSerializer
from product.models import Product
from account.models import User


class AddToCartView(APIView):
    def patch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return Response("You are not logged in", status=status.HTTP_403_FORBIDDEN)

        product_id = request.data.get("product_id")
        if not product_id:
            return Response(
                "Product ID is required", status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItems.objects.get_or_create(
            cart=cart, product=product, user=user
        )

        if item_created:
            return Response("Product added to cart", status=status.HTTP_200_OK)
        else:
            return Response("Product already exists in cart", status=status.HTTP_200_OK)
