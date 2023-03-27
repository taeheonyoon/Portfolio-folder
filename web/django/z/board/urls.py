from django.urls import path

from . import views


urlpatterns = [
    # path('', views.board, name='board'),
    
    path('', views.board_list, name='board'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('post/create/', views.create, name='create'),
    path('post/modify/<int:post_id>/', views.modify, name='modify'),
    path('post/delete/<int:post_id>/', views.delete, name='delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('post/vote/<int:post_id>/', views.vote, name='vote'),
]