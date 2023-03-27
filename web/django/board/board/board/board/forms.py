from .models import Question,Answer,Comment
from django import forms

# QuestionForm 작성 - subject, content
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject','content']

# AnswerForm - content
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']