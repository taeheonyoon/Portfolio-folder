from django.db import models
from user.models import User

# 글 등록,수정,삭제,조회
# 글번호(자동생성), 작성자, 제목, 내용, 작성날짜, 수정날짜
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="작성자")
    title = models.CharField(verbose_name="제목" ,max_length=255, blank=False)
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(blank=True, null=True, verbose_name="이미지") # Pillow 라이브러리 필요
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜") # auto_now_add=True 글이 처음 등록될 때 자동으로 입력
    modified_at = models.DateTimeField(auto_now=True,verbose_name="수정날짜") # auto_now=True 글을 수정할 때마다 자동으로 입력


    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="작성자")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,verbose_name="원본글")
    content = models.TextField(verbose_name="내용")    
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜") 
    modified_at = models.DateTimeField(auto_now=True,verbose_name="수정날짜")

    def __str__(self) -> str:
        return "%s-%s" % (self.id, self.user)