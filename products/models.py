from django.db import models
from catergories.models import Category

class Product(models.Model):
    name=models.CharField(max_length=100)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

# Create your models here.
