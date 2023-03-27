from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import UserForm
from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import messages
from django.urls import reverse_lazy

def register(request):
    """
    회원가입 
    get(비어 있는 폼) / post(바인딩 폼)
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # 회원가입 완료 후 로그인 처리도 해주고 싶다면?
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            # db 확인(사용자의 입력값과 데이터베이스 내용과 확인)
            user = authenticate(request, username=username, password=password)
            # 세션에 정보 저장
            if user is not None:
                login(request, user)
                return redirect("index")

    else:
        form = UserForm()

    return render(request, "user/register.html",{"form":form})

# 비밀번호 reset 담당 클래스 뷰
class UserPasswordResetView(PasswordResetView):
    # 이메일을 입력할 수 있는 화면
    template_name = "user/password_reset_form.html"
    # 이메일이 존재하는 경우 그 다음 작업을 진행할 경로 지정
    success_url = reverse_lazy("password_reset_done")
    # 이메일로 전송될 페이지 지정
    email_template_name = "user/password_reset_email.txt"



    def form_valid(self, form):
        # 사용자가 입력한 이메일이 실제 존재하는지 확인 후 없으면 에러 메세지 전송
        # 존재한다면 유효성 검증

        if User.objects.filter(email=self.request.POST.get('email')).exists():
            return super().form_valid(form)
        else:
            messages.info(self.request, "이메일을 확인해 주세요")
            return redirect("password_reset")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "user/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "user/password_reset_confirm.html"


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "user/password_reset_complete.html"