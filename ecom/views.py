from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer


class CategoryListAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

    
class SubCategoryListAPI(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
    

