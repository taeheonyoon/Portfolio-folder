from django.db import models

class FoodCategory(models.Model):
    category = models.CharField(max_length=50, verbose_name="음식카테고리")
    
class FoodMenu(models.Model):
    category = models.ForeignKey(FoodCategory, verbose_name="음식카테고리", on_delete=models.CASCADE)
    menu = models.CharField(max_length=50, verbose_name="음식메뉴")
