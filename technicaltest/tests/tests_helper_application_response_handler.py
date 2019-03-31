from django.test import TestCase
from django.urls import reverse
from django.test import Client
from technicaltest.helper.application_response import ApplicationResponse
from technicaltest.helper.application_response_handler import ApplicationResponseHandler
from django.http.response import Http404


class ApplicationResponseHandlerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.application_response = ApplicationResponse(404, "Test Error Message")
        cls.client = Client()

    def test_application_response_ok_response(self):
        response = ApplicationResponseHandlerTests.client.post('/invalid/url')
        self.assertRaises(Http404)

    def test_application_response_uses_correct_template(self):
        self.assertTemplateUsed(ApplicationResponseHandlerTests.client.post('/invalid/url'),
                'technicaltest/response/response.html')
                
    '''
    def test_application_response_contains_response(self):
        self.assertContains(ApplicationResponseHandlerTests.client.post('/invalid/url'),
                ApplicationResponseHandlerTests.application_response.message)
    '''
