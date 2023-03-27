# forms.py
from django import forms
from .models import Photo # 현재경로에 models.py 모듈에 잇는 Photo 클래스를 import

# 클래스 파일은 대문자로 시작
# 두개의 단어가 연결되어 있으면 두번째 단어의 첫글자도 대문자로 시작 : 카멜케이스

class PhotoForm(forms.ModelForm):
    # Meta 내부 클래스 반드시 필요
    class Meta:
        model = Photo
        # 모델에서 사용할 필드들을 나열(튜플, 리스트)
        fields = ["title", "author", "image", "description", "price"]

