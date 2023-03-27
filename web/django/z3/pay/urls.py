from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'pay'

urlpatterns = [
    path("roulette/", TemplateView.as_view(template_name="pay/roulette.html"), name="roulette"),
    path("tic", TemplateView.as_view(template_name="pay/tic.html"), name="tic"),

]

