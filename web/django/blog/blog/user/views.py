from django.shortcuts import render,redirect
from .forms import UserForm

def sign_up(request):
    """
    회원가입
    get - 비어 있는 UserForm
    post - 바인딩 된 UserForm
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserForm()
    return render(request,"user/signup.html",{"form":form})

