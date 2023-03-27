from django.urls import path, include
#from .views import todo_list
from . import views

urlpatterns = [
    #path('', todo_list ,name = "todo_list"),
    
    path('', views.todo_list, name = "todo_list"),
    path('<int:pk>/', views.todo_detail, name = 'todo_detail'),
    path('new/', views.todo_register, name = 'todo_register'),
    path('<int:pk>/edit/', views.todo_edit, name = 'todo_edit'),
    path('<int:pk>/done/', views.todo_done, name = 'todo_done'),
    path('done/', views.done_list, name = 'done_list'),
]
