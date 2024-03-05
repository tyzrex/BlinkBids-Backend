from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    images = ArrayField(models.ImageField(null=True, blank=True, upload_to= "images/"), null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return self.title

