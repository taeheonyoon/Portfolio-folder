from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'eat'

urlpatterns = [
    path("explore_menu/", views.explore_menu, name="explore_menu"),
    path("explore_menu/click/<int:pk>/", views.click_count, name="click_count"),
    # path("random_menu/", views.random_menu, name="random_menu"),
    # path("<int:pk>/", views.foodmenu, name="foodmenu"),
   

]

