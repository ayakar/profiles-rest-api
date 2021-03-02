# importing APIView object in views module of Django Rest Framework
from rest_framework.views import APIView
# importing Response object in response module of Django Rest Framework
from rest_framework.response import Response 


class HelloApiView(APIView):
    """Test API View"""

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