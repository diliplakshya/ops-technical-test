from django.shortcuts import render
from technicaltest.errors import ApplicationError


class ErrorViews(object):
    """Custom ErrorViews"""

    def __init__(self):
        super(ErrorViews, self).__init__()

    @classmethod
    def error_handler(cls, request, code, message):
        error = ApplicationError(code, message)
        return render(request, 'technicaltest/errors/error.html', {"error":error})

    @classmethod
    def error_handler_400(cls, request):
        return cls.error_handler(request, 400, "MYOB Error. Bad Request")

    @classmethod
    def error_handler_404(cls, request):
        return cls.error_handler(request, 404, "MYOB Error. Resource Not Found")

    @classmethod
    def error_handler_405(cls, request):
        return cls.error_handler(request, 405, "MYOB Error. Method Not Allowed")

    @classmethod
    def error_handler_500(cls, request):
        return cls.error_handler(request, 500, "MYOB Error. server not available, please come back later")

    @classmethod
    def error_handler_503(cls, request):
        return cls.error_handler(request, 503, "MYOB Error. Service temporarily unavailable, try again later")
