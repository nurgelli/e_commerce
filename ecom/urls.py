from django.urls import path
from .views import CategoryListAPI, SubCategoryListAPI, ProductListAPI, ProductDetailAPI


urlpatterns = [
    path('api/categories/', CategoryListAPI.as_view(), name='api-category-lst'),
    path('api/subcategories/', SubCategoryListAPI.as_view(), name='api-SubCategory-lst'),
    path('api/products/', ProductListAPI.as_view(), name='api-product-lst'),
    path('api/products/<slug:slug>', ProductDetailAPI.as_view(), name='api-product-detail-lst')
]
