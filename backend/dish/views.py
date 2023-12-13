from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Region, Category, Dish
from .permissions import IsAdminOrReadOnly
from .serializers import (
    RegionListSerializer,
    RegionSerializer, CategorySerializer, DishListSerializer, DishDetailSerializer,
    DishUpdateSerializer, DishCreateSerializer, DishUpdateIconSerializer, DishUpdateImagesSerializer
)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return RegionListSerializer

        return RegionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class DishViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Dish.objects.all()

        if self.action == "list":
            queryset = queryset.select_related(
                "region"
            ).prefetch_related("categories")

        name = self.request.query_params.get("name")
        region = self.request.query_params.get("region")
        categories_str = self.request.query_params.get("categories")

        if name:
            queryset = queryset.filter(name__icontains=name)

        if region:
            queryset = queryset.filter(region__name__icontains=region)

        if categories_str:
            categories = categories_str.split(",")
            categories_filter = Q()
            for category in categories:
                categories_filter |= Q(
                    categories__name__icontains=category.strip()
                )
            queryset = queryset.filter(categories_filter)

        if self.action == "retrieve":
            queryset = queryset.select_related(
                "region"
            ).prefetch_related("categories", "images")

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "create":
            return DishCreateSerializer

        if self.action == "list":
            return DishListSerializer

        if self.action == "retrieve":
            return DishDetailSerializer

        if self.action in ["update", "partial_update"]:
            return DishUpdateSerializer

        if self.action == "update_icon":
            return DishUpdateIconSerializer

        if self.action == "update_images":
            return DishUpdateImagesSerializer

    @action(["POST"], detail=True, url_path="update-icon")
    def update_icon(self, request, pk=None):
        """
        Sets the icon field to a new image or, if not given, sets it to null
        """
        dish = self.get_object()
        serializer = self.get_serializer(dish, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(["POST"], detail=True, url_path="update-images")
    def update_images(self, request, pk=None):
        """
        Deletes all the DishImage instances related
        to the Dish and, if given, creates new ones
        """
        dish = self.get_object()
        serializer = self.get_serializer(dish, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
