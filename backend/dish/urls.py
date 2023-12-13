from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegionViewSet

app_name = "dish"

router = DefaultRouter()
router.register("regions", RegionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
