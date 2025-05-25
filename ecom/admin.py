from unfold.admin import ModelAdmin
from django.contrib import admin
from django.db.models import TextChoices
from unfold.decorators import action
from django.contrib.admin import TabularInline
from .models import Category, SubCategory
from django.utils.translation import gettext_lazy as _

from unfold.decorators import display

# admin.site.register(Category)
# admin.site.register(SubCategory)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    icon = 'box'


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
    icon = 'layers'
    
    
# @admin.register(Product)
# class ProductAdmin(ModelAdmin):
#     list_display = ('name', 'price', 'category')
#     search_fields = ['name']
    
# @admin.register(Storage)
# class StorageAdmin(ModelAdmin):
#     list_display = ('product', 'type_of_storage', 'total_quantity') 

# class UserStatus(TextChoices):
#     ACTIVE = "ACTIVE", _("Active")
#     PENDING = "PENDING", _("Pending")
#     INACTIVE = "INACTIVE", _("Inactive")
#     CANCELLED = "CANCELLED", _("Cancelled")


# class UserAdmin(ModelAdmin):
#     list_display = [
#         "display_as_two_line_heading",
#         "show_status",
#         "show_status_with_custom_label",
#     ]

#     @display(
#         description=_("Status"),
#         ordering="status",
#         label=True
#     )
#     def show_status_default_color(self, obj):
#         return obj.status

#     @display(
#         description=_("Status"),
#         ordering="status",
#         label={
#             UserStatus.ACTIVE: "success",  # green
#             UserStatus.PENDING: "info",  # blue
#             UserStatus.INACTIVE: "warning",  # orange
#             UserStatus.CANCELLED: "danger",  # red
#         },
#     )
#     def show_status_customized_color(self, obj):
#         return obj.status

#     @display(description=_("Status with label"), ordering="status", label=True)
#     def show_status_with_custom_label(self, obj):
#         return obj.status, obj.get_status_display()

#     @display(header=True)
#     def display_as_two_line_heading(self, obj):
#         """
#         Third argument is short text which will appear as prefix in circle
#         """
#         return [
#             "First main heading",
#             "Smaller additional description",  # Use None in case you don't need it
#             "AB",  # Short text which will appear in front of
#             # Image instead of initials. Initials are ignored if image is available
#             {
#                 "path": "some/path/picture.jpg",
#                 "squared": True, # Picture is displayed in square format, if empty circle
#                 "borderless": True,  # Picture will be displayed without border
#                 "width": 64, # Removes default width. Use together with height
#                 "height": 48, # Removes default height. Use together with width
#             }
#         ]