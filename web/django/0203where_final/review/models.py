from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#상속모델
from django.contrib.auth.models import AbstractUser
from users.models import User
from django.conf import settings

class Store(models.Model):
    name = models.CharField(max_length=200, verbose_name='가게이름')
    category = models.CharField(max_length=200)
    photo = models.ImageField(blank=True)
    mean_grade = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)] ,default=1)

    def __str__(self):
        return self.name


# store모델의 네임과 카테고리 상속받아서 사용
class Review(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    grade = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
