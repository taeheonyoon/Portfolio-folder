from django.shortcuts import render, redirect

from .forms import RegisterForm

def register(request):
    """
    get - 비어 있는 폼
    post - 바인딩 폼
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form': form})
