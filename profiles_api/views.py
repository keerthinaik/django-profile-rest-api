from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        data = {'message': 'Hello!', 'a_viewset': a_viewset, }

        return Response(data=data)

    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello { name }'

            data = {'message': message, }

            return Response(data=data)

        else:
            data = serializer.errors
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID """
        data = {'http_method': 'GET', }
        return Response(data=data)

    def update(self, request, pk=None):
        """ Handle updating an object by its ID """
        data = {'http_method': 'PUT', }
        return Response(data=data)

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object by its ID """
        data = {'http_method': 'PATCH', }
        return Response(data=data)

    def destroy(self, request, pk=None):
        """ Handle removing an object by its ID """
        data = {'http_method': 'DELETE', }
        return Response(data=data)


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )