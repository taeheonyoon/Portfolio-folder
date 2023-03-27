from django import forms
from .models import User, TestModel2

class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'name', 'nickname']
        
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = TestModel2
        fields = "__all__"