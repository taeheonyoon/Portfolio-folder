# 장고 User 객체
# 속성 - username, password, email, first_name, last_name

# 사용자 생성
#from django.contrib.auth.models import User
#user = User.objects.create_user('john', 'john@gmail.com', 'johnpassword')
#user.save()

# 비밀변호 변경
#u = User.objects.get(username='john')
#u.set_password('new password')
#u.save()

# 일반폼 상속, 모델폼 상속

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    
    #email = forms.EmailField(label="이메일", blank=True 부모가 정의한 상태)
    
    # 상속시 email 은 필수요소가 아니기 때문에 재정의를 통해 필수요소로 변경
    email = forms.EmailField(label="이메일")
    
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'email'] # 비밀번호는 무조건 포함됨