from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a List of Api Views Features"""

        an_apiview = [
        'Use HTTP method as function(get, post, put, patch, delete )',
        'Is similar to a traditional Django View',
        'Gives you the most control of your Logics',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Using Post method to show Hello with the name input"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle the updation of object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updation of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete the object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provide more Functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create an object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """For getting an Object by its ID"""
        return Response({'http_method': 'GET' })

    def update(self, request, pk=None):
        """For Updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self,  request, pk=None):
        """For updating a part of an Object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """For Deleting an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle Creating user authentication Tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
