from django.urls import path, include

from . import views

app_name = 'board'

urlpatterns = [
    path('post/list/', views.index, name='index'),
    path('post/list/<str:category_name>/', views.index, name='index'),
    path('post/detail/<int:post_id>/', views.detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('post/create/<str:category_name>/', views.create, name='create'),
    path('post/modify/<int:post_id>/', views.modify, name='modify'),
    path('post/delete/<int:post_id>/', views.delete, name='delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('post/vote/<int:post_id>/', views.vote, name='vote'),
    path('review/', include('review.urls'))
]
