from django.shortcuts import render
from technicaltest.helper.application_response import ApplicationResponse
from collections import namedtuple


class ApplicationResponseHandler(object):
    """Custom ApplicationResponseHandler"""

    HTTP_200 = 200
    HTTP_204 = 204
    HTTP_400 = 400
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_405 = 405
    HTTP_408 = 408
    HTTP_429 = 429
    HTTP_500 = 500
    HTTP_501 = 501
    HTTP_502 = 502
    HTTP_503 = 503
    HTTP_504 = 504

    http200 = ApplicationResponse(HTTP_200, "MYOB Application. Application Responded.")
    http204 = ApplicationResponse(HTTP_204, "MYOB Application Error. Application Responded Without Any Data.")
    http400 = ApplicationResponse(HTTP_400, "MYOB Application Error. Bad Request.")
    http403 = ApplicationResponse(HTTP_403, "MYOB Application Error. Forbidden.")
    http404 = ApplicationResponse(HTTP_404, "MYOB Application Error. Resource Not Found.")
    http405 = ApplicationResponse(HTTP_405, "MYOB Application Error. Method Not Allowed.")
    http408 = ApplicationResponse(HTTP_408, "MYOB Application Error. Request Timeout.")
    http429 = ApplicationResponse(HTTP_429, "MYOB Application Error. Too Many Requests.")
    http500 = ApplicationResponse(HTTP_500, "MYOB Application Error. Server Not Available.")
    http501 = ApplicationResponse(HTTP_501, "MYOB Application Error. Not Implemented.")
    http502 = ApplicationResponse(HTTP_502, "MYOB Application Error. Bad Gateway.")
    http503 = ApplicationResponse(HTTP_503, "MYOB Application Error. Service Temporarily Unavailable.")
    http504 = ApplicationResponse(HTTP_504, "MYOB Application Error. Gateway Timeout.")

    response_codes = namedtuple('ResponseCodes',
                                'http200 http204 http400 http403 http404 http405 http408 http429 http500 http501 http502 http503 http504')(*[
                                    http200, http204, http400, http403, http404, http405, http408, http429,
                                    http500, http501, http502, http503, http504])

    def __init__(self):
        super(ApplicationResponseHandler, self).__init__()

    @classmethod
    def response_handler(cls, request, application_response):
        return render(request, 'technicaltest/response/response.html', {"error" : application_response}, status = application_response.code)

    @classmethod
    def response_handler_200(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http200)

    @classmethod
    def response_handler_204(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http204)

    @classmethod
    def response_handler_400(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http400)

    @classmethod
    def response_handler_403(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http403)

    @classmethod
    def response_handler_404(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http404)

    @classmethod
    def response_handler_405(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http405)

    @classmethod
    def response_handler_408(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http408)

    @classmethod
    def response_handler_429(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http429)

    @classmethod
    def response_handler_500(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http500)

    @classmethod
    def response_handler_501(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http501)

    @classmethod
    def response_handler_502(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http502)

    @classmethod
    def response_handler_503(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http503)

    @classmethod
    def response_handler_504(cls, request, exception=None):
        return cls.response_handler(request, cls.response_codes.http504)
