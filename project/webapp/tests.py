from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Subcategory, Ads


class GetCategoriesListTest(APITestCase):
    def setUp(self):
        Category.objects.create(title='cars')
        Category.objects.create(title='other')

    def test_get_categories_list(self):
        response = self.client.get(reverse('webapp:category'))
        expected_data = {"count": 1, "next": None, "previous": None,
                         "results": [{
                             "id": 1, "title": "cars"},
                             {"id": 2, "title": "other"}
                                     ]}
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSubcategoriesListTest(APITestCase):
    def setUp(self):
        Subcategory.objects.create(title='bmw')
        Subcategory.objects.create(title='audi')

    def test_get_categories_list(self):
        response = self.client.get(reverse('webapp:subcategory'))
        expected_data = {"count": 2, "next": None, "previous": None,
                         "results": [
                             {"id": 1, "title": "bmw"},
                             {"id": 2, "title": "audi"}
                         ]}
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAdsListTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='other')
        Ads.objects.create(
            title='bmw', added_at="2022-04-16", price='111', description='eeee',
            category=self.category
        )
        Ads.objects.create(
            title='bb', added_at="2022-04-16", price='5000', description='eeee',
            category=self.category
        )

    def test_get_list_of_products(self):
        response = self.client.get(reverse('webapp:ads'))
        expected_data = {"count": 2, "next": None, "previous": None,
                         "results": [
                             {"id": 1, "main_image": None,
                             "title": "bmw",
                             "price": "111",
                             "added_at": "2022-04-16",
                             "category": {"id": 1, "title": "cars"},
                              },
                             {"id": 2, "main_image": None,
                             "title": "bb",
                             "price": "5000",
                             "added_at": "2022-04-16",
                             "category": {"id": 2, "title": "other"},
                              }]}
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)