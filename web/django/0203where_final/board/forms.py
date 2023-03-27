from django import forms
from board.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }  
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }