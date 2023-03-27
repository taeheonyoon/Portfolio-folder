from django.shortcuts import render, redirect,get_object_or_404
from .models import Review, Store
from django.http import HttpResponse

def storelist(request):
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'review/storelist.html', context)


def review(request, pk):
    store = get_object_or_404(Store, id=pk)
    context = {'store': store}
    
    return render(request, 'review/review.html', context)

