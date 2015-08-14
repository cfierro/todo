def buildResponse(result, info, statusMsg, statusDetails,
                  statusCode):
    """Function creates and returns a standard HTTP response.

    Args:
        result - Dict of single result or array of dicts for multiple results.
        info - String with extra infromation.
        statusMsg - String with a status message (e.g. Ok).
        statusDetails - String with extra status details.
        statusCode - String with status code.
    """
    return {
        'info': info,
        'status': {
            'statusMsg': statusMsg,
            'statusDetails': statusDetails,
            'statusCode': statusCode
        },
        'result': result
    }


def buildOkResponse(result, info=None, statusMsg='Ok', statusDetails=None,
                    statusCode='HTTPOK'):
    """Function creates a successful HTTP response.

    Args:
        result - Dict of single result or array of dicts for multiple results.
        info - String with extra infromation.
        statusMsg - String with a status message (e.g. Ok).
        statusDetails - String with extra status details.
        statusCode - String with status code.
    """

    info = info or {}
    statusDetails = statusDetails or {}

    return buildResponse(result,info, statusMsg, statusDetails, statusCode)


def buildErrorResponse(result, info=None, statusMsg='buildErrorResponse',
                       statusDetails=None, statusCode='HTTPError'):
    """Function creates a unsuccessful HTTP response.

    Args:
        result - Dict of single result or array of dicts for multiple results.
        info - String with extra infromation.
        statusMsg - String with a status message (e.g. Error).
        statusDetails - String with extra status details.
        statusCode - String with status code.
    """
    info = info or {}
    statusDetails = statusDetails or {}

    return buildResponse(result, info, statusMsg, statusDetails, statusCode)
