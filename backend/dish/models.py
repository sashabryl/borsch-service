import os.path
import uuid

from django.db import models
from django.db.models import UniqueConstraint


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


def region_image_file_path(instance, filename) -> str:
    _, ext = os.path.splitext(filename)
    filename = f"{instance.name}-{uuid.uuid4()}{ext}"
    return os.path.join("upload/images/regions", filename)


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=511)
    image = models.ImageField(upload_to=region_image_file_path)


def dish_image_file_path(instance, filename) -> str:
    _, ext = os.path.splitext(filename)
    filename = f"{instance.dish.name}-{uuid.uuid4()}{ext}"
    return os.path.join("uploads/images/dishes", filename)


class DishImage(models.Model):
    image = models.ImageField(upload_to=dish_image_file_path)
    dish = models.ForeignKey(
        "Dish", on_delete=models.CASCADE, related_name="images"
    )


