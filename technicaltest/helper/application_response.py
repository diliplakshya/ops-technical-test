"""
This module holds http error code and message.
This module is called by ApplicationResponseHandler class to store and
retrieve https response error code and message.
"""


class ApplicationResponse(object):
    """
    This class stores http error code and message.
    @code: HTTP Error code, e.g. HTTP_404_NOT_FOUND
    @message: Response message, e.g. 'MYOB Application Error. Resource Not Found.''
    """

    def __init__(self, code = None, message = None):
        super(ApplicationResponse, self).__init__()
        self._code = code
        self._message = message

    @property
    def code(self):
        """
        Getter method for self._code
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Setter method for self._code
        """
        self._code = code

    @property
    def message(self):
        """
        Getter method for self._message
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Setter method for self._message
        """
        self._message = message
