from rest_framework import viewsets

from .models import Region
from .serializers import RegionListSerializer, RegionSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return RegionListSerializer

        return RegionSerializer

