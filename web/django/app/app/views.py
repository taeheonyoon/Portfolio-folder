from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'index.html'
    
class OffersView(TemplateView):
    template_name = 'offers.html'
    
def index(request):
    return render(request, 'index.html')

def offers(request):
    return render(request, 'offers.html')

class ListingView(TemplateView):
    template_name = 'listing.html'
    
    def listing(request):
        return render(request, 'listing.html')
    
class MainView(TemplateView):
    template_name = 'home.html'
    
    def main(request):
        return render(request, 'home.html')
    