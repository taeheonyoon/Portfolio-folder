from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list,name="post_list"),

    # http://127.0.0.1:8000/blogs/write/ 
    path('write/', views.post_write,name="post_write"),

    # http://127.0.0.1:8000/blogs/1/
    path('<int:pk>/', views.post_detail,name="post_detail"),
]
