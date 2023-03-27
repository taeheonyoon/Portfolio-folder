from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("explore_menu/", views.explore_menu, name="explore_menu"),
    path("random_menu/", views.random_menu, name="random_menu"),
    path("index3/", views.index3, name="index3"),
    path("listing/", views.listing, name="listing"),
    # path("<int:pk>/", views.foodmenu, name="foodmenu"),

]

