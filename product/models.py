from django.db import models
from ecom.models import Category, SubCategory

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name


    
class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    type_of_storage = models.CharField(max_length=32)
    total_quantity = models.IntegerField(default= 0)
    booked_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.product.name}'
    
    
