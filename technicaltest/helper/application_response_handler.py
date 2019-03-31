from django.shortcuts import render
from technicaltest.helper.application_response import ApplicationResponse


class ApplicationResponseHandler(object):
    """Custom ApplicationResponseHandler"""

    def __init__(self):
        super(ApplicationResponseHandler, self).__init__()

    @classmethod
    def response_handler(cls, request, code, message):
        return render(request, 'technicaltest/response/response.html', {"error":ApplicationResponse(code, message)})

    @classmethod
    def response_handler_404(cls, request, exception=None):
        return cls.response_handler(request, 404, "MYOB Application Error. Resource Not Found")

    @classmethod
    def response_handler_200(cls, request, exception=None):
        return cls.response_handler(request, 200, "MYOB Application. Application Responded")

    @classmethod
    def response_handler_204(cls, request, exception=None):
        return cls.response_handler(request, 204, "MYOB Application. Application Responded Without Any Data")

    @classmethod
    def response_handler_400(cls, request, exception=None):
        return cls.response_handler(request, 400, "MYOB Application Error. Bad Request")

    @classmethod
    def response_handler_403(cls, request, exception=None):
        return cls.response_handler(request, 403, "MYOB Application Error. Forbidden")

    @classmethod
    def response_handler_405(cls, request, exception=None):
        return cls.response_handler(request, 405, "MYOB Application Error. Method Not Allowed")

    @classmethod
    def response_handler_408(cls, request, exception=None):
        return cls.response_handler(request, 408, "MYOB Application Error. Request Timeout")

    @classmethod
    def response_handler_429(cls, request, exception=None):
        return cls.response_handler(request, 429, "MYOB Application Error. Too Many Requests")

    @classmethod
    def response_handler_500(cls, request, exception=None):
        return cls.response_handler(request, 500, "MYOB Application Error. Server Not Available")

    @classmethod
    def response_handler_501(cls, request, exception=None):
        return cls.response_handler(request, 501, "MYOB Application Error. Not Implemented")

    @classmethod
    def response_handler_502(cls, request, exception=None):
        return cls.response_handler(request, 502, "MYOB Application Error. Bad Gateway")

    @classmethod
    def response_handler_503(cls, request, exception=None):
        return cls.response_handler(request, 503, "MYOB Application Error. Service Temporarily Unavailable")

    @classmethod
    def response_handler_504(cls, request, exception=None):
        return cls.response_handler(request, 504, "MYOB Application Error. Gateway Timeout")
