from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegionViewSet, CategoryViewSet, DishViewSet

app_name = "dish"

router = DefaultRouter()
router.register("regions", RegionViewSet)
router.register("categories", CategoryViewSet)
router.register("dishes", DishViewSet, basename="dish")

urlpatterns = [
    path("", include(router.urls))
]
