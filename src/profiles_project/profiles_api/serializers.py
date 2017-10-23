from rest_framework import serializers


# serializers convert python object into json format and vice versa.
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)
