from django.db import models

# 모델 생성
# 클래스로 작성
# 사용할 필드에 적절한 타입을 부여
# CharField() : max_length 필수
# TextField() : 긴 문자열
class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()