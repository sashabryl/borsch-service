# Generated by Django 5.0 on 2023-12-12 09:15

import dish.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dish", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dish",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
                (
                    "icon",
                    models.ImageField(
                        upload_to=dish.models.dish_icon_file_path
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DishImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=dish.models.dish_image_file_path
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="region",
            options={"ordering": ["name"]},
        ),
        migrations.RemoveConstraint(
            model_name="region",
            name="unique_region_constraint",
        ),
        migrations.RemoveField(
            model_name="region",
            name="country",
        ),
        migrations.RemoveField(
            model_name="region",
            name="region",
        ),
        migrations.RemoveField(
            model_name="region",
            name="world_part",
        ),
        migrations.AddField(
            model_name="region",
            name="description",
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="region",
            name="image",
            field=models.ImageField(
                default=None, upload_to=dish.models.region_image_file_path
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="region",
            name="name",
            field=models.CharField(default=None, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="dish",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dishes",
                to="dish.region",
            ),
        ),
        migrations.AddField(
            model_name="dishimage",
            name="dish",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="dish.dish",
            ),
        ),
    ]
