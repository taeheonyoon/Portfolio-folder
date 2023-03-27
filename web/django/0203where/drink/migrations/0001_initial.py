# Generated by Django 4.1.4 on 2023-01-31 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DrinkMenu",
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
                ("name", models.CharField(max_length=50, verbose_name="뭐마시지 메뉴이름")),
                (
                    "image",
                    models.ImageField(
                        default="drinkmenu/drink_default.png",
                        upload_to="drinkmenu/",
                        verbose_name="뭐마시지 이미지",
                    ),
                ),
                (
                    "click_count",
                    models.PositiveIntegerField(default=0, verbose_name="뭐마시지 클릭수"),
                ),
            ],
        ),
    ]