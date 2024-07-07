from django.contrib import admin
from .models import  Cart, CartItems, Order, OrderItem
# Register your models here.


admin.site.register(CartItems)
admin.site.register(OrderItem)
admin.site.register(Cart)

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['user', 'total_price']  # Add 'total_price' to list display

#     def display_total_price(self, obj):
#         return obj.total_price
    
#     display_total_price.short_description = 'Total Price'  
#     display_total_price.admin_order_field = 'total_price'  

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['total_price', 'get_order_items'	]

    def get_order_items(self, obj):
        order_items = obj.order_items.all()
        return "\n".join([f"{item.product.title} - Quantity: {item.quantity}" for item in order_items])
    get_order_items.short_description = 'Order Items'

admin.site.register(Order,OrderAdmin)