from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Shop
from .forms import OrderForm

def index(request):
    return render(request, 'baemin/index.html', {
        'shop_list': Shop.objects.all(),
    })

@login_required
def order_new(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
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
        form = OrderForm(shop)
    return render(request, 'baemin/order_new.html', {
        'form': form,
        'shop': shop,
    })
