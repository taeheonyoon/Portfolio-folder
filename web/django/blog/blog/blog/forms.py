from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # 모델 연결
        model = Post
        # fields(title,content,image)
        fields = ['title','content','image']