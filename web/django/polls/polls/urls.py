from django.urls import path
from django.views.generic import TemplateView
from .import views

urlpatterns = [
    #html 페이지만 띄우면 될 때    
    #path('', TemplateView.as_view(template_name="polls/index.html"), name="index"),
    
    path('', views.index, name="index"),
    
    # /polls/1/
    path('<int:pk>/', views.detail, name="detail"),
    
    # /polls/1/votes/
    path('<int:pk>/votes/', views.votes, name="vote"),
] 
