from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import UserForm

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
