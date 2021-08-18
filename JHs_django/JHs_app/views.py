from rest_framework import viewsets
from JHs_app.serializers import UserSerializer
from JHs_app.models import User



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

