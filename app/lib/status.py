
class TodoException(Exception):
    """Base exception that all errors should inherit from.
    """
    statusCode = 500

    def __init__(self, message, details=None, result=None, info=None):
        super(TodoException, self).__init__()
        self.statusMsg = message
        self.statusDetails = details or {}
        self.result = result or {}
        self.info = info or {}

    def toDict(self):
        return {
            'info': self.info,
            'status': {
                'statusCode': self.statusCode,
                'statusMsg': self.statusMsg,
                'statusDetails': self.statusDetails
            },
            'result': self.result
        }


class BadRequest(TodoException):
    """Exception where bad request is made.
    """
    statusCode = 400

    def __init__(self, message='Bad request', details=None, result=None, info=None):
        super(BadRequest, self).__init__(message, details=details, result=result, info=info)


class NotFound(TodoException):
    """Exception where resource does not exist.
    """
    statusCode = 404

    def __init__(self, message='Not found', details=None, result=None, info=None):
        super(NotFound, self).__init__(message, details=details, result=result, info=info)
