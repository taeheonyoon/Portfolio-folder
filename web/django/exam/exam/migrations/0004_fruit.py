# Generated by Django 4.1.4 on 2022-12-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_musician_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
