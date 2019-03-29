class ApplicationError(object):
    """Custom Error Messages"""

    def __init__(self, code, message):
        super(ApplicationError, self).__init__()
        self._code = code
        self._message = message
