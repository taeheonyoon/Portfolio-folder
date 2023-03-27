from django.urls import path
from . import views
from .views import send_email
from django.views.generic import TemplateView

app_name = 'pay'

urlpatterns = [
    path("roulette/", TemplateView.as_view(template_name="pay/roulette.html"), name="roulette"),
    path("tic", TemplateView.as_view(template_name="pay/tic.html"), name="tic"),
    path("dutchpay/", TemplateView.as_view(template_name="pay/dutchpay.html"), name="dutchpay"),
    path("send_email/", views.send_email, name="send_email"),
]

