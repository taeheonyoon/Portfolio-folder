from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.sign_up,name="signup"),
    # 장고 로그인 이용
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"),name="login"),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
]
