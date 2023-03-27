from django.urls import path
from . import views
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    
    # http://127.0.0.1:8000/apis/
    
    #로그인 / 로그아웃
    # users/login/ name='login'
    
    path('login/', auth_views.LoginView.as_view(template_name="home.html", success_url=reverse_lazy('contents')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileEdit.as_view(), name='profile_edit'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('test_item/', views.Itemtest.as_view(), name='itemtest_index'),
]