from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, SubCategory, Product
from .serializers import CategorySerializer, ProductSerializer, SubCategorySerializer


class CategoryListAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class SubCategoryListAPI(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
    
class ProductDetailAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
