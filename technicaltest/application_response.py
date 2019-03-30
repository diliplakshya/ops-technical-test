class ApplicationResponse(object):
    """Custom Application Response Code And Messages"""

    def __init__(self, code, message):
        super(ApplicationResponse, self).__init__()
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, code):
        self._message = message
