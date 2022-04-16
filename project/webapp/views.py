from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny

from project.webapp.models import Ads, Category, Subcategory
from project.webapp.serializers import AdsListSerializer, CategorySerializer, \
    SubcategorySerializer


class AdsListView(generics.ListAPIView):
    serializer_class = AdsListSerializer
    queryset = Ads.objects.all()
    permission_classes = (AllowAny,)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class SubcategoryListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (AllowAny,)