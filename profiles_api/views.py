from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)'
            'Is similar to traditional Django View',
            'Gives the most control over the application logic',
            'Is mapped manually to URLs',
        ]

        data = {'message': 'Hello!', 'an_apiview': an_apiview}

        return Response(data=data)

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello { name }'

            data = {'message': message, }

            return Response(data=data)
        else:
            # serializer.errors will return a dictionary of errors
            data = serializer.errors
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handle updating an object """
        data = {'method': 'PUT', }
        return Response(data=data)

    def patch(self, request, pk=None):
        """ Handle a partial updating an object """
        data = {'method': 'PATCH', }
        return Response(data=data)

    def delete(self, request, pk=None):
        """ Delete an object """
        data = {'method': 'DELETE', }
        return Response(data=data)