from django.db import transaction
from rest_framework import serializers

from .models import Region, Category, Dish, DishImage


class EmptySerializer(serializers.Serializer):
    pass


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name", "description", "image")


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name", "image")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class DishListSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    region = serializers.StringRelatedField()

    class Meta:
        model = Dish
        fields = ("id", "name", "icon", "categories", "region")


class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = ("image",)


class DishCreateSerializer(serializers.ModelSerializer):
    upload_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=100000000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "description",
            "icon",
            "region",
            "images",
            "categories",
            "upload_images",
        )
        read_only_fields = ("id", "images")

    def create(self, validated_data):
        images_data = validated_data.pop("upload_images", None)
        dish = super().create(validated_data)
        if images_data:
            for image in images_data:
                DishImage.objects.create(dish=dish, image=image)

        return dish


class DishDetailSerializer(DishCreateSerializer):
    categories = serializers.StringRelatedField(many=True)
    region = serializers.StringRelatedField()
    images = DishImageSerializer(read_only=True, many=True)


class DishUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "description", "region", "categories")


class DishUpdateIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("icon",)


class DishUpdateImagesSerializer(DishCreateSerializer):
    upload_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=100000000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Dish
        fields = ("upload_images",)

    def update(self, instance, validated_data):
        with transaction.atomic():
            DishImage.objects.filter(dish=instance).delete()
            for image in validated_data.get("upload_images", []):
                DishImage.objects.create(dish=instance, image=image)
        return instance
