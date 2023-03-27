from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="질문")
    pub_date = models.DateTimeField(verbose_name="작성날짜")
    
    def __str__(self)->str:
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="연결된 질문")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, verbose_name="투표")
    
    def __str__(self)->str:
        return self.choice_text