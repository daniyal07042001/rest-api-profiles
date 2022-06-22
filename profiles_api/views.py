from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
