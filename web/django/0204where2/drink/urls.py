from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'drink'

urlpatterns = [
    path("explore_menu/", views.explore_menu, name="explore_menu"),
    path("explore_menu/click/<int:pk>/", views.click_count, name="click_count"),

]

