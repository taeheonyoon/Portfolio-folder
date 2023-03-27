from django.shortcuts import render,get_list_or_404
from .models import FoodCategory,FoodMenu
from django.core import serializers
import random
import json
from django.http import JsonResponse


def explore_menu(request):
    FoodCategory_list = FoodCategory.objects.all()
    return render(request, "eat/explore_menu.html",{'FoodCategory_list':FoodCategory_list})


# def foodmenu(request,pk):
#     menu_list = FoodMenu.objects.filter(category=pk)
#     if menu_list:
#         menu_list_serialize= json.loads(serializers.serialize('json', menu_list))
#         return JsonResponse({'data': menu_list_serialize},status=200)
#     else:
#         return JsonResponse({'data': ""},status=404)


def random_menu(request):
    total_menu_num = len(FoodMenu.objects.all())
    random_menu_pk = random.randint(1,total_menu_num)
    random_menu = FoodMenu.objects.filter(id=random_menu_pk)
    return render(request,"eat/eat_random.html",{'random_menu':random_menu})

def index3(request):
    FoodCategory_list = FoodCategory.objects.all()
    return render(request, "eat//index3.html",{'FoodCategory_list':FoodCategory_list})
def listing(request):
    menu_list = FoodMenu.objects.all()
    context = {'menu_list': menu_list}
    return render(request, 'eat/listing.html', context)