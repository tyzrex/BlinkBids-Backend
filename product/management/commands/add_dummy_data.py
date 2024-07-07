from django.core.management.base import BaseCommand
from product.models import Category,Product

class Command(BaseCommand):
    help = "Add dummy data"

    def handle(self,*args,**options):
        cateogry_counter = 0
        product_counter = 0
        for i in range(10):
            Category.objects.create(name=f"Category {cateogry_counter}")
            cateogry_counter +=1
        
        for cat in Category.objects.all():
            for i in range(10):
                Product.objects.create(title=f"Product {product_counter}",description="This is a dummy product",price=100,category=cat,slug=f"product-{product_counter}")
                product_counter +=1
        
        print("Done")