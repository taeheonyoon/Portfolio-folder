from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'baemin/index.html', {'shop_list': Shop.objects.all(),})    

@login_required
def order_new(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if request.method == 'POST':
        form = OrderForm(shop, request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.shop = shop
            order.save()
            form.save_m2m()
            return redirect('profile')
    else: 
        form = OrderForm(shop=shop)
    return render(request, 'baemin/order_form.html', {'form': form, 'shop': shop,})