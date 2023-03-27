from django.shortcuts import render,get_list_or_404
from .models import FoodCategory,FoodMenu

def foodcategory(request):
    FoodCategory_list = FoodCategory.objects.all()
    return render(request, "where/eat.html",{'FoodCategory_list':FoodCategory_list})


