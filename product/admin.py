from django.contrib import admin
from unfold.decorators import action
from unfold.decorators import display
from django.contrib.admin import TabularInline
from product.models import Product, Storage
from unfold.admin import ModelAdmin


# admin.site.register(Product)
# admin.site.register(Storage)

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ['name']
    icon = "box"  # Unfold icon name from lucide.dev
    fieldsets = (
        ("Basic Info", {"fields": ("name", "slug", "description")}),
        ("Pricing", {"fields": ("price",)}),
        ("Categorization", {"fields": ("category", "subcategory")}),
        ("Image", {"fields": ("image",)}),
        # ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    
@admin.register(Storage)
class StorageAdmin(ModelAdmin):
    list_display = ('product', 'type_of_storage', 'total_quantity') 
    icon = "database"

