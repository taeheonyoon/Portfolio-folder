from django.db import models
from django.contrib.auth.models import User

# 질문 모델
# 제목(Char-200), 내용(TextField), 작성날짜, 수정날짜 - DateTimeField
class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="작성자",related_name="author_question")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")
    voter = models.ManyToManyField(User, related_name="voter_question",verbose_name="추천수")
    view_cnt = models.BigIntegerField(default=0) # 조회수


class QuestionCount(models.Model):
    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.ip



# 답변 모델
# 질문(어떤 질문에 대한 답변인지 파악), 답변내용, 작성날짜, 수정날짜
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="작성자",related_name="author_answer")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")
    voter = models.ManyToManyField(User, related_name="voter_answer",verbose_name="추천수")



# 댓글 모델(작성자, 작성날짜, 수정날짜, 댓글내용, 질문에 대한 댓글, 답변에 대한 댓글)
# 질문, 답변 모두 댓글 기능 사용
# 모델 정의 1. 따로 처리(질문_댓글, 답변_댓글)
#           2. 같이 사용(필드로 구별)
class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True,blank=True) # 답변에 대한 댓글일 경우 이 부분은 입력 안됨
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,null=True,blank=True) # 질문에 대한 댓글일 경우 이 부분은 입력 안됨