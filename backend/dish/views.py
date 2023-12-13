from rest_framework import viewsets

from .models import Region, Category
from .serializers import (
    RegionListSerializer,
    RegionSerializer, CategorySerializer,
)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return RegionListSerializer

        return RegionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

