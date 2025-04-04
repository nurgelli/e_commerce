from django.shortcuts import render
from ecom.serializers import ProductSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product


class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductDetailAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

