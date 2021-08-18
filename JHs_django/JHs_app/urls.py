from django.urls import include, path

from rest_framework import routers

from JHs_app.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'User', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]