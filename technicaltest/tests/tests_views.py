"""
This module contains the unit tests for views.
"""


from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from technicaltest.views import ViewHome
from rest_framework.views import status
from technicaltest.models import Home, MetaData


class HomeViewTests(TestCase):
    """
    Unit tests for home view.
    """
    def setUp(self):
        Home.objects.create(display_text = 'abcd')

    def test_home_view_ok_response(self):
        self.assertEquals(self.client.get(reverse('Home View')).status_code, status.HTTP_200_OK)

    def test_home_view_uses_correct_template(self):
        self.assertTemplateUsed(self.client.get(reverse('Home View')), 'technicaltest/home.html')

    def test_home_view_contains_response(self):
        self.assertContains(self.client.get(reverse('Home View')), Home.objects.last().display_text)

    def tearDown(self):
        MetaData.objects.all().delete()

class MetaDataViewTests(TestCase):
    """
    This module contains the unit tests for Meta Data view.
    """
    def setUp(self):
        MetaData.objects.create(version = '0.0', description = 'MYOB Web App',
            last_commit_sha = 'abcd4312', commit_message = 'Source code changed')

    def test_meta_data_view_ok_response(self):
        self.assertEquals(self.client.get(reverse('Meta Data View')).status_code, status.HTTP_200_OK)

    def test_meta_data_view_uses_correct_template(self):
        self.assertTemplateUsed(self.client.get(reverse('Meta Data View')), 'technicaltest/about.html')

    def test_meta_data_view_contains_response(self):
        self.assertContains(self.client.get(reverse('Meta Data View')), MetaData.objects.last().version)
        self.assertContains(self.client.get(reverse('Meta Data View')), MetaData.objects.last().description)
        self.assertContains(self.client.get(reverse('Meta Data View')), MetaData.objects.last().last_commit_sha)
        self.assertContains(self.client.get(reverse('Meta Data View')), MetaData.objects.last().commit_message)

    def tearDown(self):
        MetaData.objects.all().delete()
