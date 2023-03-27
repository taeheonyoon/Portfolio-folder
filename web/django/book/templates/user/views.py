from django.shortcuts import render

def register(request):
    """
    회원가입
    """
    return render(request, "user/register.html")