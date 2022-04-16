from django.urls import path

from .views import (
    AdsListView,
    CategoryListView,
    SubcategoryListView
)

app_name = 'webapp'

urlpatterns = [
    path('', AdsListView.as_view(), name='ads'),
    path('category/', CategoryListView.as_view(), name='ads-category'),
    path('category/subcategory/', SubcategoryListView.as_view(), name='ads-subcategory'),

]