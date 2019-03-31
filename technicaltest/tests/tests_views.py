from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from rest_framework.test import APITestCase, APIClient
from technicaltest.views import ViewHome
from rest_framework.views import status
from technicaltest.models import Home, MetaData
from technicaltest.serializers import HomeSerializer, MetaDataSerializer


class HomeViewTests(TestCase):
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


'''
    def test_get_home(self):
        home = Home(display_text = 'MYOB Display Text Testing')
        request = HomeTests.factory.get('/some-fake/url/', data={"home":home})
        view = views.as_view()
        response = view(request)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_home(display_text=""):
        if display_text != "":
            Home.objects.create(display_text=display_text)

    def setUp(self):
        # add test data
        self.create_home("like glue")
        self.create_home("simple song")
        self.create_home("love is wicked")
        self.create_home("jam rock")

class GetAllHomeTest(BaseViewTest):
    def test_home_response(self):
        """
        This test ensures that all homes added in the setUp method
        exist when we make a GET request to the home/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("Home View")
        )
        # fetch the data from db
        expected = Home.objects.all()
        serialized = HomeSerializer(expected, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
'''
