from django.shortcuts import render,get_object_or_404,redirect
from .models import FoodMenu
from django.core import serializers
import random
import json
from django.http import JsonResponse


def explore_menu(request):
    
    menu_list = FoodMenu.objects.all()
    
    total_menu_num = len(FoodMenu.objects.all())
    random_menu_pk = random.randint(1,total_menu_num)
    random_menu_queryset = FoodMenu.objects.filter(id=random_menu_pk).values()
    random_menu = random_menu_queryset[0]
    
    top4_menu = FoodMenu.objects.order_by('-click_count')[0:4]
    
    return render(request, "eat/explore_menu.html",{'menu_list':menu_list,'random_menu':random_menu,'top4_menu':top4_menu})


def click_count(request,pk):
    menu = get_object_or_404(FoodMenu,pk=pk)
    menu.click_count = menu.click_count + 1
    
    menu.save()
    
    return redirect("eat:explore_menu")
    
    
    

# def foodmenu(request,pk):
#     menu_list = FoodMenu.objects.filter(category=pk)
#     if menu_list:
#         menu_list_serialize= json.loads(serializers.serialize('json', menu_list))
#         return JsonResponse({'data': menu_list_serialize},status=200)
#     else:
#         return JsonResponse({'data': ""},status=404)


# def random_menu(request):
#     total_menu_num = len(FoodMenu.objects.all())
#     random_menu_pk = random.randint(1,total_menu_num)
#     random_menu_queryset = FoodMenu.objects.filter(id=random_menu_pk).values()
#     random_menu = random_menu_queryset[0]
#     return render(request,"eat/random_menu.html",{'random_menu':random_menu})