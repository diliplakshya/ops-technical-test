"""
This module contains the unit tests for application_response_handler.py module.
"""


from django.test import TestCase
from django.urls import reverse
from django.test import Client
from technicaltest.helper.application_response import ApplicationResponse
from technicaltest.helper.application_response_handler import ApplicationResponseHandler
from django.http.response import Http404


class ApplicationResponseHandlerTests(TestCase):
    """
    Unit tests for ApplicationResponseHandler class.
    """
    @classmethod
    def setUpTestData(cls):
        Client().post('/invalid/url')

    def test_application_response_200_returns_correct_http_code(self):
        self.assertEquals(Client().get('//').status_code, ApplicationResponseHandler.HTTP_200)
        self.assertEquals(Client().get('/api/').status_code, ApplicationResponseHandler.HTTP_200)
        self.assertEquals(Client().get('/metadata/').status_code, ApplicationResponseHandler.HTTP_200)
        self.assertEquals(Client().get('/api/metadata/').status_code, ApplicationResponseHandler.HTTP_200)

    def test_application_response_200_uses_correct_template(self):
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/header.html')
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/footer.html')
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/base.html')
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/home.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/header.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/footer.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/base.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/about.html')

    def test_application_response_contains_response(self):
        self.assertContains(Client().get('/invalid/url'), ApplicationResponseHandler.http404.message, status_code = ApplicationResponseHandler.HTTP_404)

    def test_application_response_uses_correct_template(self):
        self.assertTemplateUsed(Client().get('/invalid/url'), 'technicaltest/response/response.html')

    def test_application_response_404(self):
        self.assertRaises(Http404)
