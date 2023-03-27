from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile, Content, Image
from board.models import Post
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_POST
from .forms import CheckPasswordForm
##로그아웃
from django.contrib.auth import logout
##auth_logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import logout as user_logout



def register(request):
    """ 
    get = 비어있는 폼
    post = 바인딩 폼
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})

def profile(request):
    return render (request, 'users/profile.html')

def index(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post':post}
    return render (request, 'users/profile.html', context)

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


@method_decorator(login_required, name='dispatch')

class UserProfileImageUpdate(BaseView):
    """
    사용자 프로필 사진을 사용자가 선택한 사진으로 변경
    """
    def post(self, request):
        
        # 사용자가 선택한 이미지를 가져오기
        image = request.FILES['file']
        
        
        profile = get_object_or_404(Profile, user=request.user)
        profile.image = image
        profile.save()
        
        return self.response({"error":False, "message":"Successfully"},status=200)

class UserProfileImageDelete(BaseView):
    """
    사용자 프로필 사진을 default.pnp 변경
    """
    def get(self, request):
        """
        현재 로그인 사용자의 이미지 porfile/default.png로 변경
        """
        profile = get_object_or_404(Profile, user=request.user)
        profile.image = 'profile/default.png'
        profile.save()
        
        return self.response({"error":False, "message":"Successfully"},status=200)


@method_decorator(login_required, name='dispatch')
class ProfileEdit(TemplateView):
    template_name = 'porfile.html'
    
    def get_context_data(self, **kwargs):
        """
        로그인 사용자의 작성글 갯수
        """
        context = super().get_context_data(**kwargs)
        context['contents'] = Content.objects.filter(user=self.request.user)
        return context
    
@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            auth_logout(request)
            user_logout(request)
            return render(request, 'index/index.html')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'users/profile_delete.html', {'password_form':password_form})