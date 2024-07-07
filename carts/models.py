from django.db import models
from account.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.email
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items.all())

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="cart_items")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.title}[{self.quantity}] - {self.user.email}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.order_items.all())

    def __str__(self):
        return self.user.email
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.title}[{self.quantity}] - {self.order.user.email}"