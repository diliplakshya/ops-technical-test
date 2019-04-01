"""
This module contains the unit tests for api_views.py module.
"""


from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from rest_framework.test import APITestCase, APIClient
from technicaltest.api_views import HomeApiView, MetaDataApiView
from rest_framework.views import status
from technicaltest.models import Home, MetaData
from technicaltest.serializers import HomeSerializer, MetaDataSerializer


class ApiHomeViewTests(TestCase):
    """
    Unit tests for HomeApiView class.
    """
    def setUp(self):
        Home.objects.create(display_text = 'A B C D')

    def test_home_api_view_ok_response(self):
        self.assertEquals(self.client.get(reverse('Home API View')).status_code, status.HTTP_200_OK)

    def test_home_api_view_contains_response(self):
        self.assertContains(self.client.get(reverse('Home API View')), Home.objects.last().display_text)

    def test_home_api_view_valid(self):
        form = HomeSerializer(data = {'display_text': "MYOB Home"})

        self.assertTrue(form.is_valid())

    def test_home_api_view_object_count(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Home.objects.count(), 1)

    def tearDown(self):
        MetaData.objects.all().delete()


class ApiMetaDataViewTests(TestCase):
    """
    Unit tests for MetaDataApiView class.
    """
    def setUp(self):
        MetaData.objects.create(version = '0.0', description = 'MYOB Web App',
            last_commit_sha = 'abcd4312', commit_message = 'Source code changed')

    def test_meta_data_api_view_ok_response(self):
        self.assertEquals(self.client.get(reverse('Meta Data API View')).status_code, status.HTTP_200_OK)

    def test_meta_data_api_view_contains_response(self):
        response = self.client.get(reverse('Meta Data API View'))
        self.assertContains(response, MetaData.objects.last().version)
        self.assertContains(response, MetaData.objects.last().description)
        self.assertContains(response, MetaData.objects.last().last_commit_sha)
        self.assertContains(response, MetaData.objects.last().commit_message)

    def test_meta_data_api_view_valid(self):
        form = MetaDataSerializer(
            data = {'version': "2.2", 'description': "Meta Data Description", 'last_commit_sha': "a1b2c3d4", 'commit_message': "Source Code Commit"})

        self.assertTrue(form.is_valid())

    def test_meta_data_api_view_object_count(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MetaData.objects.count(), 1)

    def tearDown(self):
        MetaData.objects.all().delete()
