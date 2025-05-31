from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            'status': False,
            'data': None,
            'message': None,
            'error': response.data
        }, status=response.status_code)

    # fallback untuk error fatal yang tidak tertangani
    return Response({
        'status': False,
        'data': None,
        'message': 'Unexpected error occurred',
        'error': str(exc)
    }, status=500)
