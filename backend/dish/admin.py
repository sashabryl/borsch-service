from django.contrib import admin

from .models import Category, Region


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "world_part", "country", "region")
    list_filter = ("world_part", "country", "region")
    search_fields = ("region",)

