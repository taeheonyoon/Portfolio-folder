from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy

urlpatterns = [
    # 로그인 http://127.0.0.1:8000/user/login/
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),

    # PasswordChangeView : 비밀번호 변경, 바뀐 비밀번호로 업데이트 하고, 세션도 계속 유지
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name="user/password_change.html", 
                                                                  success_url = reverse_lazy("index")),name="password_change"),

    # 비밀번호 변경이 완료되었습니다와 같은 템플릿 페이지를 보여주고 싶다면
    # path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"), name="password_change_done")

    
    
# 장고에서 제공하는 로그인,로그아웃,비밀번호변경 및 비밀번호 초기화 작업 예시
#   path("",include("django.contrib.auth.urls")),

#   user/ login/ [name='login']
#   user/ logout/ [name='logout']
#   user/ password_change/ [name='password_change']
#   user/ password_change/done/ [name='password_change_done']

#   비밀번호 reset 시 이메일로 링크 전송하고 그 링크를 통해 비밀번호를 재지정하도록 되어 있음
#   user/ password_reset/ [name='password_reset']
#   user/ password_reset/done/ [name='password_reset_done']
#   user/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
#   user/ reset/done/ [name='password_reset_complete']

    # 클래스 뷰
    path("password_reset/", views.UserPasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]