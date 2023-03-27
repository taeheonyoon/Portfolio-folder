from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from users.forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class BaseView(View):
    """
    클라이언트로부터 요청을 받아 JsonResponse로 응답하는 View
    """
    
    @staticmethod
    def response(result={}, status=200):
        return JsonResponse(result, status=status)


@method_decorator(login_required, name='dispatch')
class ContentCreate(BaseView):
    """
    이미지와 텍스트 가져온 후 입력
    """
    def post(self, request):
        text = request.POST.get('text').strip()
        content = Content.objects.create(user=request.user, text=text)

        for idx, file in enumerate(request.FILES.values()):
            Image.objects.create(content=content, image=file, order=idx)
            
        return self.response({"error":False, "message":"Successfully"},status=200)

class UserCreateView(BaseView):
    
    # get/post 방식인지 판별
    @csrf_exempt # csrftoken 검증하지 말 것
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView,self).dispatch(request, *args, **kwargs)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            # 비밀번호 암호화
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # 로그인 처리 : authenticate() - db 확인, login() - 세션에 정보 담기
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            
            if new_user is not None:
                login(request, new_user)
            
            return self.response({"error":False, "message":"Successfully"},status=200)
        else:
            return self.response({"error":True, "message":form.errors},status=400)