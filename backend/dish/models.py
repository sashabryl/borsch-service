from django.db import models
from django.db.models import UniqueConstraint


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Region(models.Model):
    world_part = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=("world_part", "country", "region"),
                name="unique_region_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.world_part}, {self.country}, {self.region}"
