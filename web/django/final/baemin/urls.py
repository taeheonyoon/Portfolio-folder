from django.urls import path, include
from . import views

app_name = 'baemin'
urlpatterns = [
    path('' , views.index, name='index'),
    path('new/<int:shop_id>/', views.order_new, name='order_new'),
]
