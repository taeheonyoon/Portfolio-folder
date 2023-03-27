#장고 폼
#1) 폼 생성에 필요한 데이터를 폼 클래스로 구조화
#2) 폼 클래스의 데이터를 렌더링하여 HTML 폼 작성
#3) 사용자로부터 제출된 폼과 데이터를 수신하고 처리

#바인딩 폼 - 아래코드처럼 데이터랑 폼이랑 연결된 상태
#form = NameForm(request.POST)

from django import forms
from .models import Musician

class NameForm(forms.Form):
    """
    일반 폼
    """


    # input type="text" 생성
    name = forms.CharField(max_length=20, label='Your Name')
    
    # 추가 검증 시 메소드 이름은 반드시 clean이 들어가도록 해야 함(clean_필드명)
    #def clean(self):
    #    cleaned_data = super().clean()
    #    name = cleaned_data.get('name')
    #    if name != '홍길동':
    #        raise forms.ValidationError("이름을 확인해 주세요")
    
    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name != '홍길동':
            raise forms.ValidationError("이름을 확인해 주세요")
        
class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__' # fields = [필요한 필드] or (필요한 필드)
        # exclude = [제외할 필드]