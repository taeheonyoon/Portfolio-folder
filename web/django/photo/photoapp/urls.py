"""config URL Configuration

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from . import views
from django.urls import path

urlpatterns = [
    #http://127.0.0.1:8000/photo/ ==> views.py 에 home 함수가 응답
    path('', views.home, name='home'),
    #http://127.0.0.1:8000/photo/view + get, post
    path('new/', views.post, name='post'),
    
    #http://127.0.0.1:8000/photo/2
    path("<int:pk>/", views.detail, name="detail"),
    
    #http://127.0.0.1:8000/photo/2/remove
    path("<int:pk>/remove/", views.remove, name="remove"),
    
    #http://127.0.0.1:8000/photo/2/edit
    path("<int:pk>/edit/", views.edit, name="edit"),
]
