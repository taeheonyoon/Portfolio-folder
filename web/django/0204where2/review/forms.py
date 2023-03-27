from django import forms
from .models import Review
from .widget import StarWidget


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['store', 'user', 'title', 'content', 'photo','grade']
        exclude = ['store', 'user','title']
        widgets = {
            'grade': StarWidget,
        }
