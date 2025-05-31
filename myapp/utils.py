from rest_framework.response import Response

def standard_response(data=None, message=None, error=None, status=True, status_code=200):
    return Response({
        'status': status,
        'data': data,
        'message': message,
        'error': error
    }, status=status_code)
