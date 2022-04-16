from rest_framework import serializers

from .models import AdsImages, Ads, Subcategory, Category


class AdsImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdsImages
        fields = ('images',)


class AdsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('id', 'main_image', 'title', 'price',)


class AdsDetailSerializer(serializers.ModelSerializer):
    coupon_images = AdsImagesSerializers(
        read_only=True,
        allow_null=True,
        many=True
    )

    class Meta:
        model = Ads
        fields = ('id', 'main_image', 'title',  'description', 'price',
                  'ads_images',)


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')
