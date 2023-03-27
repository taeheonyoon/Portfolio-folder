from django.db import models

class FoodCategory(models.Model):
    category = models.CharField(max_length=50, verbose_name="뭐먹지 카테고리")
    
class FoodMenu(models.Model):
    category = models.ForeignKey(FoodCategory, verbose_name="뭐먹지 카테고리", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="뭐먹지 메뉴이름")
    image = models.ImageField(upload_to="eatmenu/", default="eatmenu/pizza.png", verbose_name="뭐먹지 이미지")
    click_count = models.PositiveIntegerField(default=0, verbose_name="뭐먹지 클릭수")
