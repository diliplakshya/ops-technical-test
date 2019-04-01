from django.shortcuts import render
from technicaltest.helper.application_response import ApplicationResponse


class ApplicationResponseHandler(object):
    """Custom ApplicationResponseHandler"""

    application_response = ApplicationResponse()

    def __init__(self):
        super(ApplicationResponseHandler, self).__init__()

    @classmethod
    def response_handler(cls, request):
        return render(request, 'technicaltest/response/response.html', {"error":cls.application_response}, status = cls.application_response.code)

    @classmethod
    def response_handler_200(cls, request, exception=None):
        cls.application_response.code = 200
        cls.application_response.message = "MYOB Application. Application Responded."
        return cls.response_handler(request)

    @classmethod
    def response_handler_204(cls, request, exception=None):
        cls.application_response.code = 204
        cls.application_response.message = "MYOB Application Error. Application Responded Without Any Data."
        return cls.response_handler(request)

    @classmethod
    def response_handler_400(cls, request, exception=None):
        cls.application_response.code = 400
        cls.application_response.message = "MYOB Application Error. Bad Request."
        return cls.response_handler(request)

    @classmethod
    def response_handler_403(cls, request, exception=None):
        cls.application_response.code = 403
        cls.application_response.message = "MYOB Application Error. Forbidden."
        return cls.response_handler(request)

    @classmethod
    def response_handler_404(cls, request, exception=None):
        cls.application_response.code = 404
        cls.application_response.message = "MYOB Application Error. Resource Not Found."
        return cls.response_handler(request)

    @classmethod
    def response_handler_405(cls, request, exception=None):
        cls.application_response.code = 405
        cls.application_response.message = "MYOB Application Error. Method Not Allowed."
        return cls.response_handler(request)

    @classmethod
    def response_handler_408(cls, request, exception=None):
        cls.application_response.code = 408
        cls.application_response.message = "MYOB Application Error. Request Timeout."
        return cls.response_handler(request)

    @classmethod
    def response_handler_429(cls, request, exception=None):
        cls.application_response.code = 429
        cls.application_response.message = "MYOB Application Error. Too Many Requests."
        return cls.response_handler(request)

    @classmethod
    def response_handler_500(cls, request, exception=None):
        cls.application_response.code = 500
        cls.application_response.message = "MYOB Application Error. Server Not Available."
        return cls.response_handler(request)

    @classmethod
    def response_handler_501(cls, request, exception=None):
        cls.application_response.code = 501
        cls.application_response.message = "MYOB Application Error. Not Implemented."
        return cls.response_handler(request)

    @classmethod
    def response_handler_502(cls, request, exception=None):
        cls.application_response.code = 502
        cls.application_response.message = "MYOB Application Error. Bad Gateway."
        return cls.response_handler(request)

    @classmethod
    def response_handler_503(cls, request, exception=None):
        cls.application_response.code = 503
        cls.application_response.message = "MYOB Application Error. Service Temporarily Unavailable."
        return cls.response_handler(request)

    @classmethod
    def response_handler_504(cls, request, exception=None):
        cls.application_response.code = 504
        cls.application_response.message = "MYOB Application Error. Gateway Timeout."
        return cls.response_handler(request)
