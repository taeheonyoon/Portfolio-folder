from django.shortcuts import render
from django.core.mail import EmailMessage

from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from users.models import User








def send_email(request):
    if request.method == 'POST': 
        total_money = request.POST.get('total_money')
        total_people = request.POST.get('total_people')
        deposit_account = request.POST.get('deposit_account')
        t_bilge= request.POST.get('t_bilge')
        t_name = request.POST.get('t_name')
        result = request.POST.get('result')

        
        t_name = t_name.split(', ')
        
        email_list = []    
        
        for name in t_name:
            email = User.objects.filter(name=name).values('email')
            email = str(email).split("'")[3]
            email_list.append(email)

        email = EmailMessage(
            '더치페이', 
            t_bilge, 
            to= email_list, 
            )
        email.send()

    return render(request, 'pay/dutchpay.html')