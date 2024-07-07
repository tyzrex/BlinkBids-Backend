from django.core.management.base import BaseCommand
from product.models import Category,Product
import os
import random
from django.core.files import File
from django.db import transaction
from product.models import ProductImage


class Command(BaseCommand):
    help = "Add dummy data"

    def handle(self,*args,**options):
        ProductImage.objects.all().delete()
        folder_path = '/mnt/c/Users/Acer/Desktop/new-media'

        # List all files in the folder
        image_files = os.listdir(folder_path)

        # Randomly select 200 images (adjust the number as needed)
        selected_images = random.sample(image_files, 200)

        # Function to create ProductImage objects
        @transaction.atomic
        def create_product_images(images):
            for image_name in images:
                # Create ProductImage object
                product_image = ProductImage()
                
                # Set name (you can modify this as per your requirements)
                product_image.name = image_name[:100]
                
                # Open the image file
                with open(os.path.join(folder_path, image_name), 'rb') as f:
                    # Assign the image to the ProductImage object
                    product_image.image.save(image_name, File(f), save=True)
                
                # Save the ProductImage object to the database
                product_image.save()

        # Call the function to create ProductImage objects
        create_product_images(selected_images)
