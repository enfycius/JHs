from django.urls import include, path

from rest_framework import routers

from JHs_rest.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'User', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]