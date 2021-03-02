# importing APIView object in views module of Django Rest Framework
from rest_framework.views import APIView
from rest_framework.views import viewsets
# importing Response object in response module of Django Rest Framework
from rest_framework.response import Response 
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class= serializers.HelloSerializer

#class always needs self as first parameter, fromat=None is not nessesary here but it's good practice
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'my first string',
            'second string',
            'third string',
            'forth string',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with name"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
        
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewser"""
    a_viewset=[
        'Uses actions (list, create, retrieve, update, partial_update',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
    ]

    return Response({'message': 'Hello!', 'a_viewset': a_viewset})