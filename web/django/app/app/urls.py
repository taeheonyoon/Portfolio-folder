from django.urls import path
from .views import HomeView, OffersView, ListingView, MainView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('offers/', HomeView.as_view(), name='offers'),
    path('listings/', HomeView.as_view(), name='listings'),
]
