from django.contrib import admin
from .models import *


class AdsImagesAdminInline(admin.TabularInline):
    model = AdsImages
    fields = ('images', 'ads')


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [AdsImagesAdminInline]


class SubcategoryInline(admin.StackedInline):
    model = Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]