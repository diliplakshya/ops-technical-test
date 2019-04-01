"""
This module contains the unit tests for application_response.py module.
"""


from django.test import TestCase
from django.urls import reverse
from technicaltest.helper.application_response import ApplicationResponse


class ApplicationResponseTests(TestCase):
    """
    Unit tests for ApplicationResponse class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.application_response = ApplicationResponse(200, 'Error Message')

    def test_code_setter_getter(self):
        ApplicationResponseTests.application_response.code = 404                                # Property setter method is called
        self.assertEquals(ApplicationResponseTests.application_response.code, 404)              # Property getter method is called

    def test_message_setter_getter(self):
        ApplicationResponseTests.application_response.message = "404 Error"                      # Property setter method is called
        self.assertEquals(ApplicationResponseTests.application_response.message, "404 Error")    # Property getter method is called
