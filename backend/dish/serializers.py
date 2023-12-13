from rest_framework import serializers

from .models import Region, Category


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            "id", "name", "description", "image"
        )


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name", "image")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")

