from django.test import TestCase
from django.urls import reverse
from django.test import Client
from technicaltest.helper.application_response import ApplicationResponse
from technicaltest.helper.application_response_handler import ApplicationResponseHandler
from django.http.response import Http404


class ApplicationResponseHandlerTests(TestCase):
    # application_response = ApplicationResponse(404, "Test Error Message")

    @classmethod
    def setUpTestData(cls):
        Client().post('/invalid/url')

    def test_application_response_ok_response(self):
        self.assertRaises(Http404)

    def test_application_response_uses_correct_template(self):
        self.assertTemplateUsed(Client().get('/invalid/url'), 'technicaltest/response/response.html')

    def test_application_response_contains_response(self):
        self.assertContains(Client().get('/invalid/url'), "MYOB Application Error. Resource Not Found.", status_code = 404)

    def test_application_response_200_uses_correct_template(self):
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/header.html')
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/footer.html')
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/base.html')
        self.assertTemplateUsed(Client().get('//'), 'technicaltest/home.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/header.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/footer.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/base.html')
        self.assertTemplateUsed(Client().get('/metadata/'), 'technicaltest/about.html')
