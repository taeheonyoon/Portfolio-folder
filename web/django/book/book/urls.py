from django.urls import path, include
from . import views, forms

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.update, name='update'),
    path('<int:pk>/remove/', views.remove, name='remove'),
    path('create/', views.create, name='create')
]
