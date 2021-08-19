from rest_framework import viewsets
from rest_framework.decorators import api_view
from JHs_rest.serializers import UserSerializer
from JHs_rest.models import User


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer