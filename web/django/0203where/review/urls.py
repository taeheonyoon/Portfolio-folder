from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'review'

urlpatterns = [
    path('', views.storelist, name='storelist'),
    path('<int:pk>/', views.review, name='review'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

