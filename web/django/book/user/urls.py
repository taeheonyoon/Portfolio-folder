from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    #회원가입
    path("register/", views.register, name="register"),
    #로그인 : 직접구현 or 장고 view(template_name wlwjd)
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
