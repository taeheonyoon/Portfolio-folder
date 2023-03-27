from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'index'

urlpatterns = [
    path("", TemplateView.as_view(template_name="index/index.html"), name="index"),
]