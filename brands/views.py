from django.shortcuts import render
from rest_framework import generics

from brands.models import Brand
from brands.serializers import BrandSerializer

# Create your views here.


class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serialized_class = BrandSerializer


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serialized_class = BrandSerializer
