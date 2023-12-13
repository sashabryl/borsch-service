import os.path
import uuid

from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint


def file_path(instance, filename, suffix, folder) -> str:
    _, ext = os.path.splitext(filename)
    filename = f"{suffix}-{uuid.uuid4()}{ext}"
    return os.path.join(f"uploads/images/{folder}", filename)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


def region_image_file_path(instance, filename) -> str:
    return file_path(instance, filename, instance.name, "regions")


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=region_image_file_path, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


def dish_image_file_path(instance, filename) -> str:
    return file_path(instance, filename, instance.dish.name, "dishes")


class DishImage(models.Model):
    image = models.ImageField(upload_to=dish_image_file_path)
    dish = models.ForeignKey("Dish", on_delete=models.CASCADE, related_name="images")


def dish_icon_file_path(instance, filename) -> str:
    return file_path(instance, filename, f"{instance.name}-icon-", "dishes")


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to=dish_icon_file_path, null=True, blank=True)
    region = models.ForeignKey(
        "Region", on_delete=models.CASCADE, related_name="dishes"
    )
    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_dishes"
    )
    categories = models.ManyToManyField("Category", related_name="dishes")

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        return self.name
