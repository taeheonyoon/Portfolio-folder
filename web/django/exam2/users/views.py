from django.shortcuts import render
from .forms import UserForm

def signup(request):
    """ 
    회원가입
    """
    
    if request.method == "POST":
        # post로 넘어오는 모든 입력값을 form과 연결(바인딩)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
        
    return render(request, 'users/register.html', {'form':form})


def login(request):
    """ 
    로그인
    """
    return render(request, 'users/login.html')