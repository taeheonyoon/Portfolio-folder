from django.urls import path
from . import views

urlpatterns = [
    path("eat/", views.foodcategory, name="foodcategory"),
    # path("<int:pk>/", views.foodmenu, name="foodmenu"),

]

