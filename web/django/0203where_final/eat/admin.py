from django.contrib import admin
from .models import FoodCategory,FoodMenu


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["category"]

admin.site.register(FoodCategory)

class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ["category",'menu']

admin.site.register(FoodMenu)
