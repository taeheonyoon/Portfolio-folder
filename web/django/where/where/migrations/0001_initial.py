# Generated by Django 4.1.4 on 2023-01-23 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoodCategory",
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
                ("category", models.CharField(max_length=50, verbose_name="음식메뉴")),
            ],
        ),
        migrations.CreateModel(
            name="FoodMenu",
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
                ("menu", models.CharField(max_length=50, verbose_name="음식메뉴")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="where.foodcategory",
                        verbose_name="음식메뉴",
                    ),
                ),
            ],
        ),
    ]
