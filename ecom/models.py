from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to="products/", blank=True, null=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    stock = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name

