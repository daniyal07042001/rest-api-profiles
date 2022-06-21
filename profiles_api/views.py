from rest_framework import ApiView
from rest_framework.response import response


class HelloApiView(ApiView):
    """Test Api View"""
    def get(self, request, format=None):
        """Returns a List of Api Views Features"""

        an_apiview = [
        'Use HTTP method as function(get, post, put, patch, delete )',
        'Is similar to a traditional Django View',
        'Gives you the most control of your Logics',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
