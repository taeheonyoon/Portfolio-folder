# form 을 생성
# 일반 폼, 모델 폼 상속
# Userform 생성 => User 모델
# UserCreationForm : User 모델 + form 기능
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"] #password는 필수로 추가됨