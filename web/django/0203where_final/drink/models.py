from django.db import models


class DrinkMenu(models.Model):
    name = models.CharField(max_length=50, verbose_name="뭐마시지 메뉴이름")
    image = models.ImageField(upload_to="drinkmenu/", default="drinkmenu/drink_default.png", verbose_name="뭐마시지 이미지")
    click_count = models.PositiveIntegerField(default=0, verbose_name="뭐마시지 클릭수")
