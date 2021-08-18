from rest_framework import serializers

from JHs_app.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Email', 'Password')