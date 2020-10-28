from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles import serializers


class HelloApiView(APIView):
    """ to test the API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradiational Django View',
            'Gives you the most control over your application',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ handles updating an item"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ handles partial updaes of an item"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ deletes an item"""
        return Response({'method': 'DELETE'})
