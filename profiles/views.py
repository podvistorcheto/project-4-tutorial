from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ to test the API view"""

    def get(self, request, format=None):
        """ returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a tradiational Django View',
            'Gives you the most control over your application',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
