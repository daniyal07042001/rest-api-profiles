from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name fiels for texting out APIView"""
    name = serializers.CharField(max_length=10)
