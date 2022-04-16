from rest_framework import serializers

from project.webapp.models import AdsImages, Ads, Subcategory, Category


class AdsImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdsImages
        fields = ('images',)


class AdsListSerializer(serializers.ModelSerializer):
    new_price = serializers.SerializerMethodField()

    class Meta:
        model = Ads
        fields = ('id', 'main_image', 'title', 'price', 'added_at ',)


class AdsDetailSerializer(serializers.ModelSerializer):
    coupon_images = AdsImagesSerializers(
        read_only=True,
        allow_null=True,
        many=True
    )

    class Meta:
        model = Ads
        fields = ('id', 'main_image', 'title',  'description','price',
                  'ads_images', 'added_at',)


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')
