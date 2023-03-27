from django.db import models

#title (제목) 단문
#description(상세내용) 장문
#created(작성날짜) 날짜/시간
#complete(완료여부) True/False
#important(중요여부) True/False

class Todo(models.Model):
    # 필드 정의(필드 타입)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    
    def __str__(self)->str:
        return self.title