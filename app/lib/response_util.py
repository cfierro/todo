def buildResponse(result, info, statusMsg, statusDetails,
                  statusCode):

    return {
        'info': info,
        'status': {
            'statusMsg': statusMsg,
            'statusDetails': statusDetails,
            'statusCode': statusCode
        },
        'result': result
    }


def buildOkResponse(result, info=None, statusMsg='Ok', statusDetails={},
                    statusCode='HTTPOK'):

    return buildResponse(result,info, statusMsg, statusDetails, statusCode)


def buildErrorResponse(result, info=None, statusMsg='buildErrorResponse',
                       statusDetails={}, statusCode='HTTPError'):

    return buildResponse(result,info, statusMsg, statusDetails, statusCode)
