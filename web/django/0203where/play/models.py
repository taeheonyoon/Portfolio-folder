from django.db import models


class PlayMenu(models.Model):
    name = models.CharField(max_length=50, verbose_name="뭐하지 메뉴이름")
    image = models.ImageField(upload_to="playmenu/", default="playmenu/play_default.png", verbose_name="뭐하지 이미지")
    click_count = models.PositiveIntegerField(default=0, verbose_name="뭐하지 클릭수")