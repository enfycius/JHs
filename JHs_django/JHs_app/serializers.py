from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    Email = serializers.EmailField()
    Password = serializers.CharField()