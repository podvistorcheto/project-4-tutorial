from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles import serializers
from rest_framework import viewsets


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


class HelloViewSet(viewsets.ModelViewSet):
    """Testing the API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """returns hello message"""

        a_viewset = [
            'Uses CRUD model actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
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
        """handles getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handles updating an object by"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handles partial updates an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handles removing an object"""
        return Response({'http_method': 'DELETE'})