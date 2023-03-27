from .models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone']

#class RegisterForm(forms.ModelForm):

#    password = forms.PasswordInput()
#    confirm_password = forms.PasswordInput()
#    class Meta:
#        model = User
#        fields = ['email', 'name', 'phone']