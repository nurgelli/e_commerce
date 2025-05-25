from django.contrib import admin
from product.models import Product, Storage
from unfold.admin import ModelAdmin

# admin.site.register(Product)
# admin.site.register(Storage)

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ['name']
    
@admin.register(Storage)
class StorageAdmin(ModelAdmin):
    list_display = ('product', 'type_of_storage', 'total_quantity') 

