from django.urls import path
from . import views

urlpatterns = [
    
    # http://127.0.0.1:8000/apis/
    
    #회원가입
    # users/create/ name='user_create'
    
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/profile/delete/', views.UserProfileImageDelete.as_view(), name='user_profile_delete'),
    path('users/profile/update/', views.UserProfileImageUpdate.as_view(), name='user_profile_update'),
    
    #새로운 글 작성
    path('contents/create/', views.ContentCreate.as_view(), name='contents_create'),
]