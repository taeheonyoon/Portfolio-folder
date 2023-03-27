from django.db import models
from users.models import User
from taggit.managers import TaggableManager

# title, content, writer(User), registed_dttm
class Board(models.Model):
    title = models.CharField(verbose_name='제목', max_length=120)
    contents = models.TextField(verbose_name='내용') # 테이블이 만들어지기는 content 로 만들어졌어요=>이름 변경하고 다시 마이그레이션 하면
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    
    tags = TaggableManager()