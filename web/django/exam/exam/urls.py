from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('custom_form/', views.custom_form, name='custom_form'),
    path('django_form/', views.django_form, name='django_form'),
    
    # 함수형 뷰
    path('musician_function_create/', views.musician_create, name='musician_function_create'),
    path('musician_function_list/', views.musician_list, name='musician_function_list'),
    #http://127.0.0.1:8000/exam/musician_detail/1/
    path('musician_function_detail/<int:pk>/', views.musician_detail, name='musician_function_detail'),
    path('musician_function_edit/<int:pk>/', views.musician_edit, name='musician_function_edit'),
    path('musician_function_remove/<int:pk>/', views.musician_remove, name='musician_function_remove'),
    
    # 클래스 뷰
    # view.py 사용하지 않고 url 만 사용해서 템플릿 띠우기
    #path('sample/', TemplateView.as_view(template_name='exam/sample.html')),
    path('sample/', views.SampleView.as_view()),
    path('musician_class_list/', views.MusicianListView.as_view(), name='musician_class_list'),
    path('musician_class_detail/<int:pk>/', views.MusicianDetailView.as_view(), name='musician_class_detail'),
    path('musician_class_create/', views.MusicianCreateView.as_view(), name='musician_class_create'),
    path('musician_class_edit/<int:pk>/', views.MusicianUpdateView.as_view(), name='musician_class_edit'),
    path('musician_class_remove/<int:pk>/', views.MusicianDeleteView.as_view(), name='musician_class_remove'),
]