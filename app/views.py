from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from typing import List, Tuple, Dict
from .utils import send_gmail, book
    

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def contact(request):
    if request.method == 'POST':
        data = request.POST

        user_name = data.get('name')
        user_email = data.get('email')
        subject = data.get('subject')
        phone = data.get('phone')
        message_body = data.get('message')
        mail = send_gmail(subject, message_body, user_email, user_name, phone  )

        send_mail(subject=subject, message=mail, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=settings.ADMIN_EMAIL.split('_'), fail_silently=False)

        context = {
            'user_name': user_name,   
        }
        return render(request, 'app/contact.html', context)
    return render(request, 'app/contact.html')

def book(request):
    if request.method == 'POST':
        data = request.POST
        user_name = data.get('name')
        user_email = data.get('email')
        subject = data.get('subject')
        date = data.get('date')
        message_body = data.get('message')
        mail = send_gmail(subject, message_body, user_email, user_name, date  )

        #send_mail(subject=subject, message=mail, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=settings.ADMIN_EMAIL.split('_'), fail_silently=False)
        context = {
            'user_name': user_name,
        }
        return render(request,'app/book.html', context)
    return render(request, 'app/book.html')