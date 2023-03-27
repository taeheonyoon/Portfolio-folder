from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    """
    회원가입
    get - 비어있는 폼, post - 바인딩 폼
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserForm()
        
    
    return render(request, "user/register.html", {"form":form})
