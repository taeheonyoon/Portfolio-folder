from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'review'

urlpatterns = [
    path('', views.storelist, name='storelist'),
    path('<int:pk>/', views.review, name='review'),
]

