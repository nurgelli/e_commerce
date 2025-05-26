from django.shortcuts import render
from ecom.serializers import ProductSerializer, StorageSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product, Storage


class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductDetailAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

class StorageListAPI(ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    
