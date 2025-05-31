from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .utils import standard_response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    # GET /api/users/
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return standard_response(data=serializer.data, message="List retrieved")

    # GET /api/users/<id>/
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return standard_response(data=serializer.data, message="Detail retrieved")
    
    # POST /api/users/
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return standard_response(data=serializer.data, message="Created", status_code=status.HTTP_201_CREATED)
        return standard_response(error=serializer.errors, message="Validation failed", status=False, status_code=status.HTTP_400_BAD_REQUEST)

    # PUT /api/users/<id>/
    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return standard_response(data=serializer.data, message="Updated successfully")
        return standard_response(error=serializer.errors, message="Update failed", status=False, status_code=status.HTTP_400_BAD_REQUEST)

    # DELETE /api/users/<id>/
    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return standard_response(message="Deleted successfully", data=None, status=True, status_code=status.HTTP_204_NO_CONTENT)

    # GET /api/users/getactive/
    @action(detail=False, methods=['get'], url_path='getactive')
    def get_active_users(self, request):
        active_users = User.objects.filter(is_active=True)
        serializer = self.get_serializer(active_users, many=True)
        return standard_response(data=serializer.data, message="Detail retrieved")