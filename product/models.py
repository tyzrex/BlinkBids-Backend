from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    images = models.ManyToManyField("ProductImage", related_name="product_images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False,related_name="category_products")

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    
    image = models.ImageField(upload_to='products/image')

    def __str__(self):
        return self.name

