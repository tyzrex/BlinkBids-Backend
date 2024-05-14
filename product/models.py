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
    images = models.ManyToManyField("ProductImage", related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images"
    )
    image = models.ImageField(upload_to='products/image')

    def __str__(self):
        return self.product.title

