from django.urls import path
from . import views
from django.urls import reverse_lazy

from . import views

urlpatterns = [
    
    # http://127.0.0.1:8000/contnts/
    
    # 컨텐츠 홈
    path('', views.ContentsView.as_view(), name='contents'),
    path('index/', views.indexView.as_view(), name='index'),
    path('index/offers/', views.offersView.as_view(), name='offers'),
]