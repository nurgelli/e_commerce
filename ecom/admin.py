from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Category, SubCategory

# admin.site.register(Category)
# admin.site.register(SubCategory)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
    
    
# @admin.register(Product)
# class ProductAdmin(ModelAdmin):
#     list_display = ('name', 'price', 'category')
#     search_fields = ['name']
    
# @admin.register(Storage)
# class StorageAdmin(ModelAdmin):
#     list_display = ('product', 'type_of_storage', 'total_quantity') 