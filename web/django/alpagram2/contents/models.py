from django.db import models
from users.models import User
import os
import uuid
from django.db.models import UniqueConstraint

# content - 작성자, 짧은 내용, 이미지, 작성날짜, 수정날짜
class BaseModel(models.Model):
    """
    추상클래스 (껍데기-틀)
    """
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    
    class Meta:
        abstract = True

class Content(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='작성자')
    text = models.TextField(default='')
    
    class Meta:
        ordering = ['-created_at']


def image_upload_to(instance, filename):
    """
    flower.jpg => filename.split('.')[-1] => flower ,jpg
    uuid.uuid4() => 16진수 랜덤값 생성
    00000000-0000-0000-0000-000000000000.jpg
    """
    
    ext = filename.split('.')[-1]
    return os.path.join(instance.UPLOAD_PATH, "%s.%s" % (uuid.uuid4(), ext))

class Image(BaseModel):
    UPLOAD_PATH = 'user-upload'
    
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='작성글')
    image = models.ImageField(upload_to=image_upload_to)
    order = models.SmallIntegerField()
    
    class Meta:
        constraints = [UniqueConstraint(name='unique_together', fields=['content', 'order'])]
        ordering = ['order']