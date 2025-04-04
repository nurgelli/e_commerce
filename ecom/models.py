from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"