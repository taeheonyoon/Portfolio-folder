from django.contrib import admin
from .models import DrinkMenu


class DrinkMenuAdmin(admin.ModelAdmin):
    list_display = ["name","image","click_count" ]

admin.site.register(DrinkMenu)
