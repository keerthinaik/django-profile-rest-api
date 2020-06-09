from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name fiels for testing the ApiView """
    name = serializers.CharField(max_length=10)